# ベンチマークプロトコル

## 目的

Happy Horse 1.0、Seedance 2.0、Seedance 2.0 Fast を同じ入力条件で比較し、速度・コスト・生成品質の違いを再現可能な形で残します。

## 実行ルール

1. `configs/prompts.json` の全プロンプトを全モデルに投げる。
2. 同じ duration、aspect ratio、seed、negative prompt、解像度を使える場合は揃える。
3. モデル側で固定できないパラメータは、run の `notes` に残す。
4. 失敗も `status=failed` として記録し、成功例だけを残さない。
5. 生成物は `artifacts/<run-id>/` に置き、`data/runs/<run-id>.json` から参照する。

## 人手評価

各成果物を 1 から 5 で評価します。

- 1: 明確に破綻している
- 2: 使いにくいが意図は一部見える
- 3: 目的は満たすが気になる破綻がある
- 4: 実用可能で小さな問題だけがある
- 5: そのまま使える

## レポート

```sh
uv run python -m vbench report --run-id <run-id>
```

レポートは `reports/<run-id>.md` に生成されます。
