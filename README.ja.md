<p align="center">
  <img src="hf-character-reference-comparison/renders/review-reflection-check/t3.jpg" alt="Happy Horse 1.0 vs Seedance 2.0 Benchmark title frame" width="100%">
</p>

<h1 align="center">Happy Horse 1.0 vs Seedance 2.0 Benchmark</h1>

<p align="center">
  Happy Horse 1.0、Seedance 2.0、Seedance 2.0 Fast を同じ女性キャラクター参照で比較する動画生成ベンチマークです。
</p>

<p align="center">
  <strong>日本語</strong> | <a href="README.md">English</a>
</p>

<p align="center">
  <a href="https://github.com/Sunwood-ai-labs/happy-horse-seedance-benchmark/actions/workflows/ci.yml"><img src="https://github.com/Sunwood-ai-labs/happy-horse-seedance-benchmark/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/Sunwood-ai-labs/happy-horse-seedance-benchmark/actions/workflows/pages.yml"><img src="https://github.com/Sunwood-ai-labs/happy-horse-seedance-benchmark/actions/workflows/pages.yml/badge.svg" alt="Pages"></a>
</p>

このリポジトリは、4コンセプト x 15秒 の同条件比較を再現可能に残すための作業場です。動画生成そのものは各モデル/各プラットフォーム上で行い、このリポジトリでは生成済み動画の受け取り、メタデータ登録、確認フレーム管理、Markdownレポート化、HyperFrames比較動画化を扱います。

今回の見方は、綺麗にまとまるかだけではありません。Happy Horse 1.0 が出す粗い実写感、物理の変さ、B級映像としての味も比較対象に含めます。

Planned Pages preview target: [Happy Horse 1.0 vs Seedance 2.0 Benchmark](https://sunwood-ai-labs.github.io/happy-horse-seedance-benchmark/)。Pages workflow は毎回ビルドと検証を行います。リポジトリが private で、private GitHub Pages を使えないプランではデプロイだけスキップします。

## 🧪 比較対象

モデルIDと表示名は [configs/models.json](configs/models.json) が正です。モデル名やAPI仕様が曖昧な場合は、IDや表示名を壊さず `notes` に補足してください。

| ID | 表示名 | 用途 |
| --- | --- | --- |
| `happy-horse-1.0` | Happy Horse 1.0 | ベース比較対象 |
| `seedance-2.0` | Seedance 2.0 | 品質重視の比較対象 |
| `seedance-2.0-fast` | Seedance 2.0 Fast | 速度重視の比較対象 |

## 🎞️ ベンチマークセット

プロンプトは [configs/prompts.json](configs/prompts.json) にあります。現在の共通条件は次の通りです。

- `15s`
- `16:9`
- 音声あり
- 同じ `@image` 女性キャラクター参照
- コンセプト別の評価観点あり

現在の4コンセプトは、VHS都市伝説ホラー、昭和特撮、深夜通販、80年代OVA予告です。

## ⚙️ セットアップ

```sh
cd /Users/admin/Prj/happy-horse-seedance-benchmark
uv run python -m vbench models
```

CLI本体はランタイムでは標準ライブラリだけで動きます。`pytest` は開発時の検証用です。

## ▶️ 使い方

プロンプト一覧を確認します。

```sh
uv run python -m vbench prompts
```

空のベンチマーク実行ファイルを作ります。

```sh
uv run python -m vbench init-run --run-id smoke-001
```

生成結果を登録します。

```sh
uv run python -m vbench add-result \
  --run-id smoke-001 \
  --prompt-id vhs-convenience-horse-shadow \
  --model-id seedance-2.0-fast \
  --status ok \
  --latency-sec 42.8 \
  --cost-usd 0.12 \
  --artifact artifacts/smoke-001/seedance-2.0-fast/vhs-convenience-horse-shadow.mp4 \
  --score character_identity=4 \
  --score visual_quality=4 \
  --score motion_quality=3.5 \
  --notes "女性キャラは維持。馬の影はやや弱い。"
```

Markdownレポートを再生成します。

```sh
uv run python -m vbench report --run-id smoke-001
```

出力先は `reports/<run-id>.md` です。今回の動画受け取り手順は [docs/incoming-video-intake.md](docs/incoming-video-intake.md) にまとめています。

## 🎬 HyperFrames比較動画

HyperFrames で、4シーン x 3モデルを1本にまとめた比較動画を作成しています。

- Composition: [hf-character-reference-comparison/index.html](hf-character-reference-comparison/index.html)
- Visual design notes: [hf-character-reference-comparison/DESIGN.md](hf-character-reference-comparison/DESIGN.md)
- 成果物ポリシー: [docs/hyperframes-comparison.md](docs/hyperframes-comparison.md)
- ローカル最終動画: `hf-character-reference-comparison/renders/all-scenes-comparison.mp4`

MP4はサイズが大きいため、Gitではソース構成と確認フレームを管理し、完成動画本体はローカル成果物またはRelease assetとして扱います。

## 🖼️ 確認フレーム

動画内の文字、タイル配置、分析メモ、まとめスライドを確認するために使った代表フレームです。

| 用途 | 時刻 | 画像 |
| --- | ---: | --- |
| 冒頭タイトル / ベンチマーク意図 | 3s | [t3.jpg](hf-character-reference-comparison/renders/review-reflection-check/t3.jpg) |
| VHS / Happy Horse 1.0分析 | 32s | [t32.jpg](hf-character-reference-comparison/renders/review-reflection-check/t32.jpg) |
| 昭和特撮 / Happy Horse 1.0分析 | 96s | [t96.jpg](hf-character-reference-comparison/renders/review-reflection-check/t96.jpg) |
| 深夜通販 / Happy Horse 1.0分析 | 160s | [t160.jpg](hf-character-reference-comparison/renders/review-reflection-check/t160.jpg) |
| 80年代OVA / Happy Horse 1.0分析 | 224s | [t224.jpg](hf-character-reference-comparison/renders/review-reflection-check/t224.jpg) |
| まとめスライド | 266s | [t266.jpg](hf-character-reference-comparison/renders/review-reflection-check/t266.jpg) |

![レビュー反映確認](hf-character-reference-comparison/renders/review-reflection-check.jpg)

![フレーム位置確認](hf-character-reference-comparison/renders/frame-alignment-check.jpg)

![分析メモQC](hf-character-reference-comparison/renders/full-analysis-contact-sheet.jpg)

![最終文言確認](hf-character-reference-comparison/renders/final-copy-check.jpg)

## 📏 評価軸

評価軸は [configs/metrics.json](configs/metrics.json) に定義しています。

- Prompt adherence: 指示への忠実度
- Character identity: `@image` の女性キャラとして認識できるか
- Character consistency: 15秒間の人物一貫性
- Temporal consistency: フレーム間の一貫性
- Motion quality: 動きの自然さ
- Visual quality: 画質、質感、破綻の少なさ
- Text/logo stability: 文字やロゴの安定性
- Audio quality: 音楽、効果音、セリフ、ナレーション
- Style accuracy: コンセプト別の様式再現性
- Latency: 生成完了までの時間
- Cost: 生成コスト

## 🗂️ ディレクトリ

```text
configs/       モデル、プロンプト、評価軸
data/runs/     実行結果JSON
artifacts/     生成動画や画像などの成果物、原則ローカル保持
reports/       集計レポートとローカルQC出力
docs/          ベンチマーク手順と受け取りメモ
src/vbench/    CLIと集計ロジック
tests/         最低限の検証
```

## 🛡️ データの扱い

APIキー、個人アカウント情報、生成元動画、完成MP4、private な provider export はコミットしないでください。`.gitignore` では `artifacts/**`、`reports/**`、`data/runs/**`、HyperFrames の source videos、完成MP4をローカル保持にし、`.gitkeep` だけを残しています。

## ✅ 検証

```sh
uv run pytest -q
uv run python scripts/smoke_test.py
uv run python scripts/check_readme_links.py
uv run python scripts/build_pages.py
uv run python scripts/check_pages_site.py
```

コミット前には staged payload を確認し、巨大なローカル動画や生成物を Git に入れないでください。
