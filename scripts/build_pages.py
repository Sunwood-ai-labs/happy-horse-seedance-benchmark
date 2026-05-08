from __future__ import annotations

import html
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
HF = ROOT / "hf-character-reference-comparison"


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def build() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)

    copy_file(HF / "assets" / "background.png", SITE / "assets" / "background.png")
    for name in [
        "review-reflection-check.jpg",
        "frame-alignment-check.jpg",
        "full-analysis-contact-sheet.jpg",
        "qc-contact-sheet.jpg",
        "final-copy-check.jpg",
    ]:
        copy_file(HF / "renders" / name, SITE / "frames" / name)

    prompts = read_json(ROOT / "configs" / "prompts.json")
    models = read_json(ROOT / "configs" / "models.json")

    (SITE / "index.html").write_text(render_index(prompts, models), encoding="utf-8")
    print(f"Built {SITE}")


def render_index(prompts: object, models: object) -> str:
    prompt_cards = "\n".join(
        f"""
        <article class="card">
          <span class="kicker">Scene {idx:02d}</span>
          <h3>{html.escape(prompt["title"])}</h3>
          <p>{html.escape(prompt["category"])} / {prompt["duration_sec"]}s / {html.escape(prompt["aspect_ratio"])}</p>
        </article>
        """
        for idx, prompt in enumerate(prompts, 1)
    )
    model_cards = "\n".join(
        f"""
        <article class="model-card">
          <span>{html.escape(model["track"])}</span>
          <strong>{html.escape(model["display_name"])}</strong>
          <p>{html.escape(model["notes"])}</p>
        </article>
        """
        for model in models
    )
    return f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Happy Horse 1.0 vs Seedance 2.0 Benchmark</title>
  <style>
    :root {{
      color-scheme: light;
      --ink: #073f46;
      --muted: #5f5547;
      --paper: #fff8e8;
      --line: #bf8e58;
      --accent: #cc3434;
      --teal: #004f59;
      --shadow: 0 18px 42px rgba(41, 30, 16, .14);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Yu Gothic", sans-serif;
      color: var(--ink);
      background: #f8efd8 url("assets/background.png") center top / cover fixed;
      line-height: 1.7;
    }}
    body::before {{
      content: "";
      position: fixed;
      inset: 0;
      background: rgba(255, 248, 232, .78);
      pointer-events: none;
    }}
    main {{
      position: relative;
      width: min(1120px, calc(100% - 36px));
      margin: 0 auto;
      padding: 42px 0 64px;
    }}
    .hero {{
      min-height: 72vh;
      display: grid;
      align-content: center;
      gap: 24px;
    }}
    .label {{
      width: fit-content;
      padding: 8px 14px;
      border: 2px dashed var(--line);
      border-radius: 14px;
      background: rgba(255, 248, 232, .88);
      color: var(--accent);
      font-weight: 800;
      letter-spacing: .04em;
    }}
    h1 {{
      max-width: 980px;
      margin: 0;
      font-size: clamp(38px, 7vw, 86px);
      line-height: 1.02;
      letter-spacing: 0;
    }}
    .lead {{
      max-width: 820px;
      margin: 0;
      color: #2c251c;
      font-size: clamp(18px, 2.2vw, 24px);
      font-weight: 700;
    }}
    .actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .button {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 44px;
      padding: 10px 18px;
      border-radius: 999px;
      background: var(--teal);
      color: white;
      text-decoration: none;
      font-weight: 800;
      box-shadow: var(--shadow);
    }}
    section {{
      margin-top: 42px;
      padding: 30px;
      border: 2px dashed rgba(191, 142, 88, .85);
      border-radius: 18px;
      background: rgba(255, 248, 232, .9);
      box-shadow: var(--shadow);
    }}
    h2 {{
      margin: 0 0 18px;
      font-size: clamp(26px, 4vw, 42px);
      line-height: 1.15;
      letter-spacing: 0;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 16px;
    }}
    .scene-grid {{
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }}
    .card, .model-card {{
      min-height: 154px;
      padding: 18px;
      border: 2px solid rgba(0, 79, 89, .16);
      border-radius: 12px;
      background: rgba(255, 255, 255, .66);
    }}
    .kicker, .model-card span {{
      display: block;
      margin-bottom: 8px;
      color: var(--accent);
      font-size: 13px;
      font-weight: 900;
      text-transform: uppercase;
    }}
    h3 {{
      margin: 0 0 10px;
      font-size: 21px;
      line-height: 1.35;
      letter-spacing: 0;
    }}
    .model-card strong {{
      display: block;
      margin-bottom: 10px;
      font-size: 24px;
      line-height: 1.2;
    }}
    .proofs {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 18px;
    }}
    figure {{
      margin: 0;
      padding: 10px;
      border-radius: 14px;
      background: rgba(255, 255, 255, .7);
      border: 1px solid rgba(0, 79, 89, .16);
    }}
    img {{
      display: block;
      width: 100%;
      height: auto;
      border-radius: 10px;
    }}
    figcaption {{
      margin-top: 8px;
      color: var(--muted);
      font-weight: 800;
      font-size: 14px;
    }}
    .note {{
      margin: 0;
      padding: 18px;
      border-left: 6px solid var(--accent);
      background: rgba(255, 255, 255, .62);
      font-weight: 700;
    }}
    footer {{
      position: relative;
      margin: 32px auto 0;
      color: var(--muted);
      font-weight: 700;
      text-align: center;
    }}
    @media (max-width: 760px) {{
      main {{ width: min(100% - 24px, 1120px); padding-top: 24px; }}
      .grid, .scene-grid, .proofs {{ grid-template-columns: 1fr; }}
      section {{ padding: 20px; }}
    }}
  </style>
</head>
<body>
  <main>
    <header class="hero">
      <div class="label">Character Reference Video Benchmark</div>
      <h1>Happy Horse 1.0 vs Seedance 2.0 Benchmark</h1>
      <p class="lead">ハッピーホース1.0とシーダンス2.0とシーダンス2.0 Fastを、同じ女性キャラクター参照と4つのB級映像コンセプトで比較します。</p>
      <div class="actions">
        <a class="button" href="https://github.com/Sunwood-ai-labs/happy-horse-seedance-benchmark">GitHub</a>
        <a class="button" href="#proof">確認フレーム</a>
      </div>
    </header>

    <section>
      <h2>比較対象</h2>
      <div class="grid">{model_cards}</div>
    </section>

    <section>
      <h2>4つのコンセプト</h2>
      <div class="grid scene-grid">{prompt_cards}</div>
    </section>

    <section>
      <h2>今回の見方</h2>
      <p class="note">今回は、綺麗にまとまるかだけではなく、B級映像でHappy Horse 1.0が出す「実写の説得力」「制御不能な異物感」「破綻込みの作家性」を評価対象にしています。</p>
    </section>

    <section id="proof">
      <h2>確認フレーム</h2>
      <div class="proofs">
        <figure>
          <img src="frames/review-reflection-check.jpg" alt="レビュー反映確認のコンタクトシート">
          <figcaption>レビュー反映確認</figcaption>
        </figure>
        <figure>
          <img src="frames/frame-alignment-check.jpg" alt="タイル配置とフレーム位置の確認">
          <figcaption>タイル配置 / フレーム確認</figcaption>
        </figure>
        <figure>
          <img src="frames/full-analysis-contact-sheet.jpg" alt="個別分析メモの確認">
          <figcaption>個別分析メモ</figcaption>
        </figure>
        <figure>
          <img src="frames/final-copy-check.jpg" alt="最終文言確認">
          <figcaption>最終文言確認</figcaption>
        </figure>
      </div>
    </section>

    <section>
      <h2>成果物ポリシー</h2>
      <p>GitHub Pagesには軽量な確認フレームと概要を載せます。完成MP4と生成元動画はサイズが大きいため、Gitには含めずローカル成果物またはRelease assetとして扱います。</p>
    </section>

    <footer>Built by GitHub Actions from repository sources.</footer>
  </main>
</body>
</html>
"""


if __name__ == "__main__":
    build()
