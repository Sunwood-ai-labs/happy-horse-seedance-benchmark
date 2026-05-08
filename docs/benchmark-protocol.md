# Benchmark Protocol

**Language:** English | [日本語へ切り替え](ja/benchmark-protocol.md)

## Goal

Compare Happy Horse 1.0, Seedance 2.0, and Seedance 2.0 Fast under the same input conditions, then preserve speed, cost, and output-quality differences in a reproducible format.

## Run Rules

1. Send every prompt in `configs/prompts.json` to every model.
2. Match duration, aspect ratio, seed, negative prompt, and resolution whenever a platform allows it.
3. Record any model-side parameters that cannot be fixed in the run `notes`.
4. Record failures with `status=failed`; do not keep only successful examples.
5. Store generated media in `artifacts/<run-id>/` and reference it from `data/runs/<run-id>.json`.

## Human Scoring

Score each output from 1 to 5.

- 1: clearly broken
- 2: difficult to use, but part of the intent is visible
- 3: meets the goal with noticeable issues
- 4: usable with only small issues
- 5: usable as-is

## Report

```sh
uv run python -m vbench report --run-id <run-id>
```

The report is generated at `reports/<run-id>.md`.
