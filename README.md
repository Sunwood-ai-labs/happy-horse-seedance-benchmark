# Happy Horse 1.0 vs Seedance 2.0 Benchmark

ハッピーホース 1.0、シーダンス 2.0、シーダンス 2.0 Fast を同じ条件で比較するためのベンチマーク用リポジトリです。

このリポジトリは、まず「比較条件を固定して記録する」ことを目的にしています。現在のプロンプトセットは、@image の女性キャラクター参照を軸にした 4コンセプト x 15秒 の比較実験です。各モデルのAPI実行部分は `src/vbench/adapters/` に追加する想定で、現時点では生成結果のメタデータをJSONとして登録し、Markdownレポートに集計できます。

## 比較対象

| ID | 表示名 | 用途 |
| --- | --- | --- |
| `happy-horse-1.0` | Happy Horse 1.0 | ベース比較対象 |
| `seedance-2.0` | Seedance 2.0 | 品質重視の比較対象 |
| `seedance-2.0-fast` | Seedance 2.0 Fast | 速度重視の比較対象 |

## セットアップ

```sh
cd /Users/admin/Prj/happy-horse-seedance-benchmark
```

外部依存を増やさないため、CLI本体は標準ライブラリだけで動きます。ローカルではインストールなしで `PYTHONPATH=src` を付けて実行できます。

## 使い方

プロンプト一覧を確認します。

```sh
PYTHONPATH=src python3 -m vbench prompts
```

今回の動画受け取り手順は [docs/incoming-video-intake.md](docs/incoming-video-intake.md) にまとめています。

空のベンチマーク実行ファイルを作ります。

```sh
PYTHONPATH=src python3 -m vbench init-run --run-id smoke-001
```

生成結果を登録します。

```sh
PYTHONPATH=src python3 -m vbench add-result \
  --run-id smoke-001 \
  --prompt-id product-orbit \
  --model-id seedance-2.0-fast \
  --status ok \
  --latency-sec 42.8 \
  --cost-usd 0.12 \
  --artifact artifacts/smoke-001/seedance-fast-product-orbit.mp4 \
  --notes "動きは速いがロゴの安定性は要確認"
```

Markdownレポートを生成します。

```sh
PYTHONPATH=src python3 -m vbench report --run-id smoke-001
```

出力先は `reports/smoke-001.md` です。

## 評価軸

`configs/metrics.json` に定義しています。

- Prompt adherence: 指示への忠実度
- Character identity: @image の女性キャラとして認識できるか
- Character consistency: 15秒間の人物一貫性
- Temporal consistency: フレーム間の一貫性
- Motion quality: 動きの自然さ
- Visual quality: 画質、質感、破綻の少なさ
- Text/logo stability: 文字やロゴの安定性
- Audio quality: 音楽、効果音、セリフ、ナレーション
- Style accuracy: コンセプト別の様式再現性
- Latency: 生成完了までの時間
- Cost: 生成コスト

## ディレクトリ

```text
configs/       モデル、プロンプト、評価軸
data/runs/     実行結果JSON
artifacts/     生成動画や画像などの成果物
reports/       集計レポート
src/vbench/    CLIと集計ロジック
tests/         最低限の検証
```

## 次に足すもの

- 各サービスの実APIアダプタ
- 人手評価フォーム
- 画像・動画の自動メトリクス
- 複数runの横断ランキング

## 検証

```sh
python3 scripts/smoke_test.py
```
