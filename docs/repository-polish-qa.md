# Repository Polish QA

## Requested Deliverables

- Fully polish the repository with the `repository-polish` workflow.
- Preserve model IDs and display names from `configs/models.json`.
- Keep generated run JSON, artifacts, and reports in the expected locations.
- Avoid committing API keys, private account details, and large generated media.
- Keep reports regenerable with `python -m vbench report --run-id <run-id>`.

## User-Facing Artifacts

- `README.md`: English public-facing entrypoint.
- `README.ja.md`: Japanese public-facing entrypoint.
- `docs/index.md`: English documentation home.
- `docs/benchmark-protocol.md`: English benchmark protocol.
- `docs/incoming-video-intake.md`: English intake guide.
- `docs/hyperframes-comparison.md`: English HyperFrames artifact policy.
- `docs/ja/index.md`: Japanese documentation home.
- `docs/ja/benchmark-protocol.md`: Japanese benchmark protocol.
- `docs/ja/incoming-video-intake.md`: Japanese intake guide.
- `docs/ja/hyperframes-comparison.md`: Japanese HyperFrames artifact policy.
- `LICENSE`: explicit proprietary license notice.
- `SECURITY.md`: sensitive-data and reporting guidance.
- `CONTRIBUTING.md`: contribution and benchmark workflow rules.
- `.github/workflows/ci.yml`: Python CI and repository checks.
- `.github/workflows/pages.yml`: static Pages build/check workflow.
- `scripts/check_readme_links.py`: bilingual README and docs link validation.
- `scripts/build_pages.py`: static Pages source.
- `scripts/check_pages_site.py`: static Pages structural validation.

## Final-Response Claims To Verify

- README surfaces are bilingual and link to each other.
- English and Japanese docs exist with parallel protocol, intake, and HyperFrames pages.
- The repository has explicit license, security, and contribution guidance.
- Generated media remains ignored by Git unless intentionally promoted.
- CI, smoke test, README link check, static site build, and static site check pass locally.
- GitHub repository metadata is set.
- GitHub Pages is enabled for the public repository and the live site returns HTTP 200.

## Structural QA Checklist

- README badge rows and language switch are separated.
- README links and image targets resolve locally.
- Japanese and English README structures are parallel.
- Japanese and English docs are reachable from README and `docs/index.md`.
- Verification commands use `uv run` for local Python execution.
- Static site paths point at files included in `_site`.
- Pages workflow builds `_site` and deploys after the repository is public.
- Staged payload excludes local MP4s, raw artifacts, report outputs, `.venv`, and `_site`.
