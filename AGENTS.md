# AGENTS.md

このリポジトリは動画生成モデル比較ベンチマークの作業場です。

- モデル名やAPI仕様が曖昧な場合は、`configs/models.json` の表示名とIDを壊さず、追加情報を `notes` として追記してください。
- 実行結果は `data/runs/<run-id>.json` に保存し、生成物本体は `artifacts/<run-id>/` に置いてください。
- レポートは `python -m vbench report --run-id <run-id>` で再生成できる形を保ってください。
- APIキーや個人アカウント情報はコミットしないでください。
- 依存関係を増やす場合は、まず標準ライブラリで足りない理由をREADMEに残してください。
