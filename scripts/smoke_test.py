from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENV = {**os.environ, "PYTHONPATH": str(ROOT / "src")}


def run(args: list[str]) -> None:
    print("+", " ".join(args))
    subprocess.run(args, cwd=ROOT, env=ENV, check=True)


def main() -> None:
    run([sys.executable, "-m", "py_compile", "src/vbench/cli.py", "src/vbench/__init__.py"])
    run([sys.executable, "-m", "vbench", "models"])
    run([sys.executable, "-m", "vbench", "prompts"])
    run([sys.executable, "-m", "vbench", "init-run", "--run-id", "smoke-001", "--force"])
    run(
        [
            sys.executable,
            "-m",
            "vbench",
            "add-result",
            "--run-id",
            "smoke-001",
            "--prompt-id",
            "vhs-convenience-horse-shadow",
            "--model-id",
            "seedance-2.0-fast",
            "--status",
            "ok",
            "--latency-sec",
            "42.8",
            "--cost-usd",
            "0.12",
            "--artifact",
            "artifacts/smoke-001/seedance-2.0-fast/vhs-convenience-horse-shadow.mp4",
            "--score",
            "character_identity=4",
            "--score",
            "visual_quality=4",
            "--score",
            "motion_quality=3.5",
            "--notes",
            "smoke test result",
        ]
    )
    run([sys.executable, "-m", "vbench", "report", "--run-id", "smoke-001"])


if __name__ == "__main__":
    main()
