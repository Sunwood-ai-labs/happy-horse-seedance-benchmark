from pathlib import Path

from vbench.cli import CONFIG_DIR, load_json, parse_scores


def test_configs_have_three_models() -> None:
    models = load_json(CONFIG_DIR / "models.json")
    assert {model["id"] for model in models} == {
        "happy-horse-1.0",
        "seedance-2.0",
        "seedance-2.0-fast",
    }


def test_prompts_have_unique_ids() -> None:
    prompts = load_json(CONFIG_DIR / "prompts.json")
    ids = [prompt["id"] for prompt in prompts]
    assert len(ids) == len(set(ids))
    assert {prompt["duration_sec"] for prompt in prompts} == {15}
    assert all("@image" in prompt["prompt"] for prompt in prompts)


def test_parse_scores() -> None:
    assert parse_scores(["visual_quality=4", "motion_quality=3.5"]) == {
        "visual_quality": 4.0,
        "motion_quality": 3.5,
    }


def test_project_root_resolution() -> None:
    assert (Path(__file__).resolve().parents[1] / "configs" / "models.json").exists()
