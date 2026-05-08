from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.images: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")
        if tag == "img" and values.get("src"):
            self.images.append(values["src"] or "")


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:"))


def check_target(target: str, ids: set[str]) -> str | None:
    if target.startswith("#"):
        return None if target[1:] in ids else target
    if is_external(target):
        return None
    path, _, anchor = unquote(target).partition("#")
    candidate = (SITE / path).resolve()
    try:
        candidate.relative_to(SITE)
    except ValueError:
        return target
    if not candidate.exists():
        return target
    if anchor and candidate == SITE / "index.html":
        return None if anchor in ids else target
    return None


def main() -> int:
    index = SITE / "index.html"
    if not index.exists():
        print("Run scripts/build_pages.py before checking the site.")
        return 1

    parser = SiteParser()
    parser.feed(index.read_text(encoding="utf-8"))

    missing = [target for target in [*parser.links, *parser.images] if check_target(target, parser.ids)]
    if missing:
        print("Broken Pages targets:")
        for target in missing:
            print(f"- {target}")
        return 1

    text = re.sub(r"<[^>]+>", " ", index.read_text(encoding="utf-8"))
    required = ["Happy Horse 1.0", "Seedance 2.0", "確認フレーム", "B級映像"]
    missing_text = [word for word in required if word not in text]
    if missing_text:
        print("Missing required page text:")
        for word in missing_text:
            print(f"- {word}")
        return 1

    print("Pages site OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
