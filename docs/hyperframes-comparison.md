# HyperFrames Comparison Artifacts

**Language:** English | [日本語へ切り替え](ja/hyperframes-comparison.md)

This document defines how to handle HyperFrames artifacts for the 4-scene x 3-model comparison video.

## Tracked

Keep these files in Git:

- `hf-character-reference-comparison/index.html`: the comparison composition source
- `hf-character-reference-comparison/DESIGN.md`: layout and review-iteration notes
- `hf-character-reference-comparison/assets/background.png`: background image
- `hf-character-reference-comparison/renders/**/*.jpg`: review frames and contact sheets referenced by the README

## Local Only

Keep these files out of Git:

- `hf-character-reference-comparison/assets/videos/**/*.mp4`: generated source videos
- `hf-character-reference-comparison/renders/*.mp4`: full rendered comparison videos

The final render is stored locally at:

```text
hf-character-reference-comparison/renders/all-scenes-comparison.mp4
```

MP4 files are large, so they should not be committed to GitHub. Promote them to release assets or external storage only when distribution is needed.

## Render

When the HyperFrames CLI is available, use the composition directory as the working directory:

```sh
cd hf-character-reference-comparison
```

For rendered-video review, start with the README review frames and check for overflowing text, tile misalignment, and overlapping analysis notes.
