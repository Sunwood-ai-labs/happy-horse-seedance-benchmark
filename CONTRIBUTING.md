# Contributing

This repository is currently maintained as a controlled benchmark workspace.
External contributions are reviewed case by case.

## Ground Rules

- Keep model IDs and display names stable in `configs/models.json`.
- Add provider/API clarifications to `notes` instead of renaming existing IDs.
- Save run metadata as `data/runs/<run-id>.json`.
- Keep generated media under `artifacts/<run-id>/`.
- Regenerate reports with `python -m vbench report --run-id <run-id>`.
- Do not commit API keys, personal account data, raw provider exports, or large
  generated MP4 files.

## Checks

Run the local checks before proposing changes:

```sh
uv run pytest -q
uv run python scripts/smoke_test.py
uv run python scripts/check_readme_links.py
uv run python scripts/build_pages.py
uv run python scripts/check_pages_site.py
```
