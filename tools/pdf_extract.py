import sys
from pathlib import Path

import pymupdf


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: uv run tools/pdf_extract.py papers/<paper-id>/paper.pdf")
    src = Path(sys.argv[1])
    doc = pymupdf.open(src)
    target = src.with_suffix(".txt")
    target.write_text(
        "\n\n".join(page.get_text("text") for page in doc), encoding="utf-8"
    )
    print(f"{target} | {doc.page_count} pages")


if __name__ == "__main__":
    main()
