# 動画受け取り手順

**言語:** 日本語 | [Switch to English](../incoming-video-intake.md)

生成が終わった動画は、同じ `run-id` の下にモデル別・プロンプト別で置きます。

## 推奨run

```sh
RUN_ID=character-reference-15s-001
mkdir -p artifacts/$RUN_ID/{happy-horse-1.0,seedance-2.0,seedance-2.0-fast}
uv run python -m vbench init-run --run-id $RUN_ID
```

## ファイル命名

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

## 結果登録

登録時は、少なくとも `--artifact` と `--notes` を入れます。秒数やコストが分かる場合は `--latency-sec` / `--cost-usd` も追加します。

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

## 採点チェックリスト

各動画は 1 から 5 で採点します。

- `character_identity`: `@image` の女性キャラとして認識できるか
- `character_consistency`: 15秒間で顔・髪型・雰囲気が保たれるか
- `prompt_adherence`: 指示された場面・役割・演出を満たすか
- `motion_quality`: 動きの自然さ、カメラ、アクション
- `visual_quality`: 画質、質感、破綻の少なさ
- `audio_quality`: 効果音、音楽、セリフ、ナレーション
- `style_accuracy`: VHS、昭和特撮、深夜通販、80年代OVAの再現性

## レポート生成

```sh
uv run python -m vbench report --run-id character-reference-15s-001
```

レポートは `reports/character-reference-15s-001.md` に出ます。
