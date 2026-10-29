import sys
from pathlib import Path

import pymupdf


def main() -> None:
    if len(sys.argv) not in (4, 6):
        sys.exit(
            "usage: uv run tools/pdf_figure.py <pdf> <caption-prefix> <out.png> [x0 x1]"
        )
    src, needle, out = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
    doc = pymupdf.open(src)
    for page in doc:
        hits = page.search_for(needle)
        if not hits:
            continue
        caption = hits[0]
        page_rect = page.rect
        x0 = float(sys.argv[4]) if len(sys.argv) == 6 else page_rect.x0 + 36
        x1 = float(sys.argv[5]) if len(sys.argv) == 6 else page_rect.x1 - 36
        top = max(page_rect.y0 + 36, caption.y0 - 340)
        clip = pymupdf.Rect(x0, top, x1, caption.y1 + 8)
        out.parent.mkdir(parents=True, exist_ok=True)
        page.get_pixmap(clip=clip, dpi=200).save(out)
        print(f"{out} | page {page.number + 1} | clip {clip}")
        return
    sys.exit(f"caption not found: {needle}")


if __name__ == "__main__":
    main()
