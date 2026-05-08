# HyperFrames Comparison Artifacts

このドキュメントは、4シーン x 3モデルの比較動画を作るための HyperFrames 成果物の扱いをまとめます。

## Tracked

Gitに残すもの:

- `hf-character-reference-comparison/index.html`: 比較動画の構成本体
- `hf-character-reference-comparison/DESIGN.md`: レイアウトとレビュー反映メモ
- `hf-character-reference-comparison/assets/background.png`: 背景画像
- `hf-character-reference-comparison/renders/**/*.jpg`: READMEで参照する確認フレームとコンタクトシート

## Local Only

Gitから外すもの:

- `hf-character-reference-comparison/assets/videos/**/*.mp4`: 生成元動画
- `hf-character-reference-comparison/renders/*.mp4`: 完成動画レンダー

完成動画はローカルでは次の場所にあります。

```text
hf-character-reference-comparison/renders/all-scenes-comparison.mp4
```

MP4はサイズが大きいため、GitHubには置かず、必要に応じてRelease assetや外部ストレージに昇格します。

## Render

HyperFrames CLIが使える環境では、次のディレクトリを作業場所にします。

```sh
cd hf-character-reference-comparison
```

レンダー済み動画の確認では、まずREADMEの確認フレームを見て、文字はみ出し、タイルずれ、分析メモの重なりを確認します。
