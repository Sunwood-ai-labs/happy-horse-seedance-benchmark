from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_FILES = [
    ROOT / "README.md",
    ROOT / "README.ja.md",
    *sorted((ROOT / "docs").rglob("*.md")),
]
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def strip_anchor(target: str) -> str:
    return target.split("#", 1)[0]


def main() -> int:
    missing: list[str] = []
    for markdown_file in MARKDOWN_FILES:
        text = markdown_file.read_text(encoding="utf-8")
        for raw_target in [*LINK_RE.findall(text), *IMAGE_RE.findall(text)]:
            target = strip_anchor(unquote(raw_target.strip()))
            if not target or is_external(target):
                continue
            candidate = (markdown_file.parent / target).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                missing.append(f"{markdown_file.relative_to(ROOT)}: {raw_target}")
                continue
            if not candidate.exists():
                missing.append(f"{markdown_file.relative_to(ROOT)}: {raw_target}")

    if missing:
        print("Missing README links:")
        for target in missing:
            print(f"- {target}")
        return 1

    print("Markdown links OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
