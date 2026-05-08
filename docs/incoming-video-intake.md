# Incoming Video Intake

Place completed videos under the same `run-id`, grouped by model and prompt.

## Recommended Run

```sh
RUN_ID=character-reference-15s-001
mkdir -p artifacts/$RUN_ID/{happy-horse-1.0,seedance-2.0,seedance-2.0-fast}
uv run python -m vbench init-run --run-id $RUN_ID
```

## File Naming

```text
artifacts/character-reference-15s-001/
  happy-horse-1.0/
    vhs-convenience-horse-shadow.mp4
    showa-tokusatsu-horse-monster.mp4
    late-night-uma-talk-3000.mp4
    ova-ramen-delivery-robot.mp4
  seedance-2.0/
    ...
  seedance-2.0-fast/
    ...
```

## Register Results

When registering a result, include at least `--artifact` and `--notes`. Add `--latency-sec` and `--cost-usd` when generation time or cost is known.

```sh
uv run python -m vbench add-result \
  --run-id character-reference-15s-001 \
  --prompt-id vhs-convenience-horse-shadow \
  --model-id seedance-2.0-fast \
  --status ok \
  --artifact artifacts/character-reference-15s-001/seedance-2.0-fast/vhs-convenience-horse-shadow.mp4 \
  --score character_identity=4 \
  --score prompt_adherence=4 \
  --score audio_quality=3 \
  --notes "女性キャラは維持。馬の影はやや弱い。"
```

## Scoring Checklist

Score each video from 1 to 5.

- `character_identity`: whether the output is recognizable as the referenced female character from `@image`
- `character_consistency`: whether face, hair, and overall vibe stay stable for 15 seconds
- `prompt_adherence`: whether the requested scene, role, and direction are satisfied
- `motion_quality`: movement, camera behavior, and action quality
- `visual_quality`: image quality, texture, and absence of distracting artifacts
- `audio_quality`: sound effects, music, dialogue, and narration
- `style_accuracy`: fidelity to VHS horror, Showa tokusatsu, late-night shopping TV, or 80s OVA style

## Generate Report

```sh
uv run python -m vbench report --run-id character-reference-15s-001
```

The report is written to `reports/character-reference-15s-001.md`.
