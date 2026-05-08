from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any, Optional


ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / "configs"
RUNS_DIR = ROOT / "data" / "runs"
REPORTS_DIR = ROOT / "reports"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        f.write("\n")


def run_path(run_id: str) -> Path:
    return RUNS_DIR / f"{run_id}.json"


def command_prompts(_: argparse.Namespace) -> None:
    for prompt in load_json(CONFIG_DIR / "prompts.json"):
        print(f"{prompt['id']}: {prompt['category']} {prompt['duration_sec']}s {prompt['aspect_ratio']}")
        print(f"  {prompt['prompt']}")


def command_models(_: argparse.Namespace) -> None:
    for model in load_json(CONFIG_DIR / "models.json"):
        print(f"{model['id']}: {model['display_name']} ({model['track']})")


def command_init_run(args: argparse.Namespace) -> None:
    path = run_path(args.run_id)
    if path.exists() and not args.force:
        raise SystemExit(f"Run already exists: {path}")

    payload = {
        "run_id": args.run_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "models": load_json(CONFIG_DIR / "models.json"),
        "prompts": load_json(CONFIG_DIR / "prompts.json"),
        "results": [],
    }
    write_json(path, payload)
    print(f"Created {path}")


def command_add_result(args: argparse.Namespace) -> None:
    path = run_path(args.run_id)
    if not path.exists():
        raise SystemExit(f"Run does not exist. Create it first: python -m vbench init-run --run-id {args.run_id}")

    payload = load_json(path)
    known_models = {model["id"] for model in payload["models"]}
    known_prompts = {prompt["id"] for prompt in payload["prompts"]}
    if args.model_id not in known_models:
        raise SystemExit(f"Unknown model_id: {args.model_id}")
    if args.prompt_id not in known_prompts:
        raise SystemExit(f"Unknown prompt_id: {args.prompt_id}")

    result = {
        "model_id": args.model_id,
        "prompt_id": args.prompt_id,
        "status": args.status,
        "latency_sec": args.latency_sec,
        "cost_usd": args.cost_usd,
        "artifact": args.artifact,
        "scores": parse_scores(args.score),
        "notes": args.notes,
        "recorded_at": datetime.now(timezone.utc).isoformat(),
    }
    payload["results"].append(result)
    write_json(path, payload)
    print(f"Added result to {path}")


def parse_scores(raw_scores: list[str]) -> dict[str, float]:
    scores: dict[str, float] = {}
    for item in raw_scores:
        if "=" not in item:
            raise SystemExit(f"Score must use metric=value format: {item}")
        key, raw_value = item.split("=", 1)
        try:
            scores[key] = float(raw_value)
        except ValueError as exc:
            raise SystemExit(f"Score value must be numeric: {item}") from exc
    return scores


def command_report(args: argparse.Namespace) -> None:
    path = run_path(args.run_id)
    if not path.exists():
        raise SystemExit(f"Run does not exist: {path}")

    payload = load_json(path)
    model_names = {model["id"]: model["display_name"] for model in payload["models"]}
    prompt_names = {prompt["id"]: prompt["prompt"] for prompt in payload["prompts"]}
    metrics = load_json(CONFIG_DIR / "metrics.json")
    metric_names = {metric["id"]: metric["display_name"] for metric in metrics}

    lines = [
        f"# Benchmark Report: {args.run_id}",
        "",
        f"- Created: `{payload.get('created_at', 'unknown')}`",
        f"- Results: `{len(payload['results'])}`",
        "",
        "## Summary",
        "",
        "| Model | OK | Avg latency sec | Avg cost USD | Avg human score |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]

    for model in payload["models"]:
        rows = [r for r in payload["results"] if r["model_id"] == model["id"]]
        ok_rows = [r for r in rows if r["status"] == "ok"]
        latencies = [r["latency_sec"] for r in ok_rows if r.get("latency_sec") is not None]
        costs = [r["cost_usd"] for r in ok_rows if r.get("cost_usd") is not None]
        score_values = [
            value
            for r in ok_rows
            for key, value in r.get("scores", {}).items()
            if key not in {"latency_sec", "cost_usd"}
        ]
        lines.append(
            "| {name} | {ok} | {latency} | {cost} | {score} |".format(
                name=model["display_name"],
                ok=len(ok_rows),
                latency=format_number(mean(latencies)) if latencies else "-",
                cost=format_number(mean(costs)) if costs else "-",
                score=format_number(mean(score_values)) if score_values else "-",
            )
        )

    lines.extend(["", "## Results", ""])
    for result in payload["results"]:
        lines.extend(
            [
                f"### {model_names[result['model_id']]} / {result['prompt_id']}",
                "",
                f"- Status: `{result['status']}`",
                f"- Prompt: {prompt_names[result['prompt_id']]}",
                f"- Latency: `{format_optional(result.get('latency_sec'))}` sec",
                f"- Cost: `${format_optional(result.get('cost_usd'))}`",
                f"- Artifact: `{result.get('artifact') or '-'}`",
                f"- Notes: {result.get('notes') or '-'}",
            ]
        )
        if result.get("scores"):
            lines.append("- Scores:")
            for key, value in sorted(result["scores"].items()):
                lines.append(f"  - {metric_names.get(key, key)}: `{value}`")
        lines.append("")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS_DIR / f"{args.run_id}.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {report_path}")


def format_number(value: float) -> str:
    return f"{value:.3f}".rstrip("0").rstrip(".")


def format_optional(value: Optional[float]) -> str:
    if value is None:
        return "-"
    return format_number(float(value))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Benchmark helper for Happy Horse and Seedance comparison.")
    subparsers = parser.add_subparsers(required=True)

    prompts = subparsers.add_parser("prompts", help="List benchmark prompts.")
    prompts.set_defaults(func=command_prompts)

    models = subparsers.add_parser("models", help="List benchmark models.")
    models.set_defaults(func=command_models)

    init_run = subparsers.add_parser("init-run", help="Create an empty run file.")
    init_run.add_argument("--run-id", required=True)
    init_run.add_argument("--force", action="store_true")
    init_run.set_defaults(func=command_init_run)

    add_result = subparsers.add_parser("add-result", help="Append one benchmark result.")
    add_result.add_argument("--run-id", required=True)
    add_result.add_argument("--prompt-id", required=True)
    add_result.add_argument("--model-id", required=True)
    add_result.add_argument("--status", choices=["ok", "failed", "skipped"], required=True)
    add_result.add_argument("--latency-sec", type=float)
    add_result.add_argument("--cost-usd", type=float)
    add_result.add_argument("--artifact")
    add_result.add_argument("--score", action="append", default=[], help="Human score as metric=value. Can be repeated.")
    add_result.add_argument("--notes", default="")
    add_result.set_defaults(func=command_add_result)

    report = subparsers.add_parser("report", help="Generate a Markdown report for a run.")
    report.add_argument("--run-id", required=True)
    report.set_defaults(func=command_report)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
