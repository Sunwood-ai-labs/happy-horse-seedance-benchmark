# ドキュメント

このドキュメントは、ベンチマークプロトコル、生成動画の受け取り手順、HyperFrames比較動画の成果物ポリシーをまとめます。

**言語:** 日本語 | [Switch to English](../index.md)

## 日本語

- [ベンチマークプロトコル](benchmark-protocol.md)
- [動画受け取り手順](incoming-video-intake.md)
- [HyperFrames成果物](hyperframes-comparison.md)

## English

- [English Documentation](../index.md)
- [Benchmark Protocol](../benchmark-protocol.md)
- [Incoming Video Intake](../incoming-video-intake.md)
- [HyperFrames Comparison Artifacts](../hyperframes-comparison.md)
- [Repository Polish QA](../repository-polish-qa.md)

## リポジトリ方針

生成メディアは原則ローカル保持です。run JSON は `data/runs/<run-id>.json`、生成物は `artifacts/<run-id>/` に置き、レポートは `uv run python -m vbench report --run-id <run-id>` で再生成できる形を保ちます。
