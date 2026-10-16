"""Generic slide-deck profile for 16:9 decks exported from PowerPoint (one slide per PDF page).

Bibliographic fields come from the internal registry (profiles.INTERNAL_META, read from internal/refclean/docs.json)
or from META below for a public deck. Steps:
- slide title: the first heading of at least TITLE_MIN_SIZE pt on each page (level 1 on page 1, level 2 elsewhere);
  the remaining headings are level 3;
- noise: tables without any cell text (decorative bars and boxes) and all pictures (icons, backgrounds) are dropped;
  their count is recorded as dropped_images;
- reading order: on a slide whose content sits in a left and a right column, the left column is read before the
  right one within each horizontal band; an element crossing the page middle (a full-width box or table) closes a
  band and stays between the bands it separates.
"""
import fitz

from .. import structure as S
from . import INTERNAL_META

META = {}

FLATTEN_TEXT_BLOCKS = True    # slide text boxes are body content (see doc.elements_from_json)
TITLE_MIN_SIZE = 20.0          # slide titles are 22 pt; subtitles 14 pt; body text at most 14 pt
SPAN_TOLERANCE = 10.0          # an element must reach this far past the middle to count as crossing it


def slide_titles(doc, aux=None):
    seen = set()
    for e in doc.els:
        if e.kind not in ("heading", "para") or e.page in seen:
            continue
        if e.size >= TITLE_MIN_SIZE:
            seen.add(e.page)
            e.kind = "heading"
            e.level = 1 if e.page == 1 else 2
            e.meta.update(heading_done=True, slide_title=True)
    for e in doc.els:
        if e.kind == "heading" and not e.meta.get("slide_title"):
            e.level = 3
            e.meta["heading_done"] = True


def drop_noise(doc, aux=None):
    keep, dropped = [], 0
    for e in doc.els:
        if e.kind == "image":
            dropped += 1
            continue
        if e.kind == "table" and not any(c.text.strip() for row in e.table.grid for c in row):
            continue
        keep.append(e)
    doc.els = keep
    doc.meta["dropped_images"] = dropped


def band_column_order(els, mid):
    """Reorder one slide's elements (title first). Elements are ODL boxes (x0, y0, x1, y1) with y upwards."""
    head = [e for e in els if e.meta.get("slide_title")]
    body = [e for e in els if not e.meta.get("slide_title")]
    boxed = [e for e in body if e.bbox]
    left = [e for e in boxed if e.bbox[2] <= mid + SPAN_TOLERANCE]
    right = [e for e in boxed if e.bbox[0] >= mid - SPAN_TOLERANCE and e not in left]
    if not left or not right:
        return els
    spans = sorted((e for e in boxed if e not in left and e not in right), key=lambda e: -e.bbox[3])
    out = list(head) + [e for e in body if not e.bbox]
    placed = set(id(e) for e in out)
    upper = float("inf")
    for cut in spans + [None]:
        lower = cut.bbox[3] if cut else float("-inf")
        for col in (left, right):
            for e in col:
                yc = (e.bbox[1] + e.bbox[3]) / 2
                if id(e) not in placed and lower <= yc < upper:
                    out.append(e)
                    placed.add(id(e))
        if cut:
            out.append(cut)
            placed.add(id(cut))
            upper = cut.bbox[1]
    out += [e for e in body if id(e) not in placed]   # anything between a span's top and bottom edge
    return out


def column_order(doc, aux=None):
    pdf = fitz.open(doc.pdf_path)
    pages, order = {}, []
    for e in doc.els:
        if e.page not in pages:
            pages[e.page] = []
            order.append(e.page)
        pages[e.page].append(e)
    out = []
    for p in order:
        mid = pdf[p - 1].rect.width / 2 if 0 < p <= len(pdf) else 480.0
        out += band_column_order(pages[p], mid)
    pdf.close()
    doc.els = out


def steps():
    return [
        drop_noise,
        slide_titles,
        column_order,
        S.normalise_text,
        S.normalise_item_levels,
    ]


def metadata(doc, aux):
    src = INTERNAL_META.get(doc.key) or META.get(doc.key)
    if src is None:
        raise KeyError(f"slides profile has no metadata for {doc.key!r}; add it to internal/refclean/docs.json "
                       "(internal deck) or META in scripts/refclean/profiles/slides.py (public deck)")
    m = dict(src)
    m.update({
        "source_pdf": f"references/raw/{doc.stem}.pdf",
        "raw_json": f"references/raw/{doc.stem}.json",
        "pdf_pages": doc.n_pages,
        "dropped_images": doc.meta.get("dropped_images", 0),
        "figures": [],
        "withheld": [],
    })
    return m
