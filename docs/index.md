# Documentation

This documentation describes the benchmark protocol, incoming video intake, and HyperFrames comparison artifact policy.

**Language:** English | [日本語へ切り替え](ja/index.md)

## English

- [Benchmark Protocol](benchmark-protocol.md)
- [Incoming Video Intake](incoming-video-intake.md)
- [HyperFrames Comparison Artifacts](hyperframes-comparison.md)
- [Repository Polish QA](repository-polish-qa.md)

## Japanese

- [日本語ドキュメント](ja/index.md)
- [ベンチマークプロトコル](ja/benchmark-protocol.md)
- [動画受け取り手順](ja/incoming-video-intake.md)
- [HyperFrames成果物](ja/hyperframes-comparison.md)

## Repository Policy

Generated media stays local by default. Keep run JSON files under `data/runs/<run-id>.json`, generated media under `artifacts/<run-id>/`, and regenerate reports with `uv run python -m vbench report --run-id <run-id>`.
