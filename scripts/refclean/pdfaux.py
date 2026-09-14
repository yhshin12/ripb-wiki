"""PDF-side auxiliary data extracted with PyMuPDF (visible/rotated page coordinates, y downwards)."""
import collections
import re
from dataclasses import dataclass, field

import fitz

LEADER = re.compile(r"(?:\.\s?){4,}")
NUM_HEAD = re.compile(r"^(\d+(?:\.\d+)+)\s+(\S.*?)\s*$")
FIG_CAP = re.compile(r"^(?:Kemmerer Unit 1 PSAR\s+)?Figure\s+(\d+(?:\.\d+)*-\d+[A-Z]?)\.?\s+(\S.*)$")
WITHHELD = "This information is withheld"


@dataclass
class Line:
    text: str
    x0: float
    y0: float
    x1: float
    y1: float
    size: float
    fonts: tuple
    block: int
    spans: list = field(default_factory=list)   # [(text, rect, size, font, flags, color)]


@dataclass
class HeadingRef:
    num: str
    title: str
    page: int
    level: int = 0


@dataclass
class SubRef:
    text: str
    page: int
    y: float


@dataclass
class SupRef:
    base: str
    sup: str
    before: str


@dataclass
class FigureRef:
    num: str
    caption: str
    page: int
    box: tuple
    withheld: bool = False


@dataclass
class Aux:
    headings: list = field(default_factory=list)
    subheads: list = field(default_factory=list)
    sups: dict = field(default_factory=dict)
    hyphen_map: dict = field(default_factory=dict)
    figures: list = field(default_factory=list)
    toc_pages: set = field(default_factory=set)
    body_x0: dict = field(default_factory=dict)
    meta: dict = field(default_factory=dict)


def page_lines(page):
    """Visual lines in visible coordinates: spans of one block that share a baseline, joined left to right.

    PyMuPDF reports tab-separated parts (e.g. a section number and its title) as separate lines; they are
    merged here when their vertical extents overlap.
    """
    m = page.rotation_matrix
    out = []
    for bi, b in enumerate(page.get_text("dict")["blocks"]):
        spans = []
        for ln in b.get("lines", []):
            for s in ln["spans"]:
                if not s["text"].strip():
                    continue
                r = fitz.Rect(s["bbox"]) * m
                r.normalize()
                spans.append((s["text"], r, s["size"], s["font"], s["flags"], s["color"]))
        rows = []
        for sp in sorted(spans, key=lambda s: (round(s[1].y1, 0), s[1].x0)):
            mid = (sp[1].y0 + sp[1].y1) / 2
            for row in rows:
                if row["y0"] - 1 <= mid <= row["y1"] + 1 and sp[2] > 0.75 * row["size"]:
                    row["spans"].append(sp)
                    row["y0"], row["y1"] = min(row["y0"], sp[1].y0), max(row["y1"], sp[1].y1)
                    break
                if row["y0"] - 1 <= mid <= row["y1"] + 1:   # superscript on the same row
                    row["spans"].append(sp)
                    break
            else:
                rows.append({"y0": sp[1].y0, "y1": sp[1].y1, "size": sp[2], "spans": [sp]})
        for row in sorted(rows, key=lambda r: r["y0"]):
            sps = sorted(row["spans"], key=lambda s: s[1].x0)
            text = ""
            for i, sp in enumerate(sps):
                if i and sp[1].x0 - sps[i - 1][1].x1 > 1.5 and not text.endswith(" "):
                    text += " "
                text += sp[0]
            rect = fitz.Rect(sps[0][1])
            for sp in sps[1:]:
                rect |= sp[1]
            size = collections.Counter(round(sp[2], 1) for sp in sps).most_common(1)[0][0]
            out.append(Line(" ".join(text.split()), rect.x0, rect.y0, rect.x1, rect.y1, size,
                            tuple(sp[3] for sp in sps), bi, sps))
    return out


TOC_TITLES = ("TABLE OF CONTENTS", "LIST OF TABLES", "LIST OF FIGURES")


def is_toc_page(lines):
    n = sum(1 for ln in lines if LEADER.search(ln.text))
    titled = any(ln.text.strip().upper() in TOC_TITLES for ln in lines)
    return n >= 5 or (n >= 2 and titled)


def header_footer_band(page):
    """(top, bottom) of the body band in visible coordinates, from page-wide rules if present."""
    m = page.rotation_matrix
    w, h = page.rect.width, page.rect.height
    top, bot = h * 0.085, h * 0.925
    for d in page.get_drawings():
        r = fitz.Rect(d["rect"]) * m
        r.normalize()
        if r.height < 2 and r.width > w * 0.6:
            if r.y0 < h * 0.14:          # running-header rule (PSAR: 8-10 % of the page height)
                top = max(top, r.y1 + 1)
            elif r.y0 > h * 0.86:        # footer rule; table borders sit inside the body band
                bot = min(bot, r.y0 - 1)
    return top, bot


def _inside(ln, boxes):
    c = fitz.Point((ln.x0 + ln.x1) / 2, (ln.y0 + ln.y1) / 2)
    return any(fitz.Rect(b).contains(c) for b in boxes)


def numbered_headings(doc_pdf, chapter, lines_by_page, toc_pages, body_x0, exclude=None, doc_margin=None):
    """PSAR-style numbered section headings: lines at the body margin (page or document margin), outside
    tables/figures. A heading may share a PyMuPDF block with preceding list/reference lines."""
    exclude = exclude or {}
    refs, seen = [], set()
    for pno, lines in lines_by_page.items():
        if pno in toc_pages:
            continue
        by_block = collections.defaultdict(list)
        for ln in lines:
            by_block[ln.block].append(ln)
        margins = {mg for mg in (body_x0.get(pno), doc_margin) if mg is not None}
        for bl in by_block.values():
            for li, first in enumerate(bl):
                m = NUM_HEAD.match(first.text)
                if not m or LEADER.search(first.text):
                    continue
                num, title = m.group(1), m.group(2)
                if num.split(".")[0] != str(chapter):
                    continue
                if any(int(x) > 40 or int(x) == 0 for x in num.split(".")[1:]):
                    continue   # e.g. 'RG 1.233' rows in conformance tables; 'Section 7.0 of …' wrapped body text
                if not (title[:1].isupper() or title[:1].isdigit()):
                    continue   # a wrapped body line such as '7.0 of the Safety Evaluation …'
                if _inside(first, exclude.get(pno, ())):
                    continue
                if margins and all(abs(first.x0 - mg) > 3 for mg in margins):
                    continue
                if re.match(r"^\d+\.\d+-\d+", first.text):
                    continue
                # wrapped titles: short heading blocks whose following lines do not end a sentence
                if li == 0 and len(bl) <= 3:
                    for nxt in bl[1:]:
                        if title.endswith((".", ":")) or NUM_HEAD.match(nxt.text):
                            break
                        title = title + " " + nxt.text
                if title.endswith(".") and len(title) > 120:
                    continue
                key = (num, title)
                if key in seen:
                    continue
                seen.add(key)
                refs.append(HeadingRef(num, " ".join(title.split()), pno, len(num.split("."))))
    return refs


def underlined_subheads(page, lines, table_boxes=()):
    """Unnumbered subheadings drawn with an underline rule (PSAR)."""
    m = page.rotation_matrix
    marks = []
    for d in page.get_drawings():
        for it in d["items"]:
            if it[0] == "re":
                r = fitz.Rect(it[1]) * m
            elif it[0] == "l":
                r = fitz.Rect(it[1], it[2]) * m
            else:
                continue
            r.normalize()
            if r.height < 1.6 and r.width > 3:
                marks.append(r)
    out = []
    for ln in lines:
        covered = []
        for (t, sr, *_rest) in ln.spans:
            rs = [r for r in marks
                  if sr.x1 > r.x0 + 1 and sr.x0 < r.x1 - 1 and -3.0 <= r.y0 - sr.y1 <= 3.0 and r.y0 > sr.y0 + 0.6 * sr.height]
            if rs:
                covered.append((t, sr, rs))   # an underline may be drawn as several abutting rectangles
        if not covered:
            continue
        x0 = min(sr.x0 for _, sr, _ in covered)
        x1 = max(sr.x1 for _, sr, _ in covered)
        if any(r.width > (x1 - x0) + 40 or r.width > 450 for _, _, rs in covered for r in rs):
            continue
        # a heading is underlined over (nearly) its whole line; run-in underlined phrases are not headings
        ul = fitz.Rect()
        for _, _, rs in covered:
            for r in rs:
                ul |= r
        if ul.width < 0.85 * (ln.x1 - ln.x0):
            continue
        if _inside(ln, table_boxes):
            continue
        text = " ".join(" ".join(t.split()) for t, _, _ in covered).strip()
        if len(text) >= 3 and not text.startswith("Function ID"):
            out.append((text, ln.y0))
    return out


def superscripts(lines, body_size):
    out = []
    for ln in lines:
        prev = None
        for (t, r, size, font, flags, color) in ln.spans:
            if prev is not None and size <= 0.8 * body_size and r.y1 < prev[1].y1 - 1.0:
                out.append(SupRef(prev[0].split()[-1] if prev[0].split() else "", t.strip(), prev[0][-12:]))
            prev = (t, r, size)
    return out


def _line_below(a, page_lines_sorted):
    """Nearest line below `a` on the same page whose x-range overlaps it (same column of a table)."""
    best = None
    for b in page_lines_sorted:
        if b.y0 > a.y0 + 2 and b.x0 < a.x1 and b.x1 > a.x0 and (best is None or b.y0 < best.y0):
            best = b
    return best


def hyphen_map(lines_by_page):
    full_inline = collections.Counter()
    cands = {}
    pages = sorted(lines_by_page)
    all_lines = [ln for p in pages for ln in lines_by_page[p]]
    for ln in all_lines:
        for w in re.findall(r"[A-Za-z][\w/.-]*", ln.text):
            full_inline[w.strip(".")] += 1
    pairs = []
    for pi, p in enumerate(pages):
        page_sorted = sorted(lines_by_page[p], key=lambda l: (l.y0, l.x0))
        for a in page_sorted:
            if not re.search(r"[-—]$", a.text):
                continue
            b = _line_below(a, page_sorted)
            if b is None and pi + 1 < len(pages):
                nxt = sorted(lines_by_page[pages[pi + 1]], key=lambda l: (l.y0, l.x0))
                b = next((l for l in nxt if len(l.text) > 3), None)
            if b is not None:
                pairs.append((a, b))
    for a, b in pairs:
        ma = re.search(r"([A-Za-z][\w/.-]*?)([-—])$", a.text)
        mb = re.match(r"([A-Za-z0-9][\w/.-]*)", b.text)
        if not ma or not mb:
            continue
        left, dash, right = ma.group(1), ma.group(2), mb.group(1).rstrip(".,;:)")
        joined = left + right
        if full_inline.get(joined, 0) == 0:
            cands[joined] = left + dash + right
    return cands


def figure_refs(doc_pdf, lines_by_page, toc_pages):
    refs, seen = [], set()
    for pno, lines in lines_by_page.items():
        if pno in toc_pages:
            continue
        page_text = " ".join(ln.text for ln in lines)
        for ln in lines:
            m = FIG_CAP.match(ln.text)
            if not m or m.group(1) in seen:
                continue
            if not all("Bold" in f or "bold" in f for f in ln.fonts):
                continue   # body sentences that merely start with "Figure x-y"
            seen.add(m.group(1))
            page = doc_pdf[pno - 1]
            cap = fitz.Rect(ln.x0, ln.y0, ln.x1, ln.y1)
            refs.append(FigureRef(m.group(1), " ".join(m.group(2).split()), pno, figure_box(page, cap),
                                  withheld=WITHHELD in page_text))
    return refs


def figure_box(page, caption_rect=None):
    """Figure region in visible coordinates: drawings and images inside the header-footer band, grown by the
    text blocks that overlap them (labels) and by the caption line."""
    m = page.rotation_matrix
    w, h = page.rect.width, page.rect.height
    top, bot = header_footer_band(page)
    band = fitz.Rect(0, top, w, bot)
    acc = fitz.Rect()
    graphics = [fitz.Rect(d["rect"]) for d in page.get_drawings()]
    graphics += [fitz.Rect(img["bbox"]) for img in page.get_image_info()]
    for r in graphics:
        rv = r * m
        rv.normalize()
        if rv.width > w * 0.9 and rv.height < 3:
            continue  # page-wide rules
        if (rv & band).get_area() >= 0.8 * max(rv.get_area(), 1e-6) or (rv.height < 1 and band.contains(rv.tl)):
            acc |= rv
    if not acc.is_empty:
        for b in page.get_text("dict")["blocks"]:
            rv = fitz.Rect(b["bbox"]) * m
            rv.normalize()
            if rv.intersects(acc) and band.contains(rv):
                acc |= rv
    if caption_rect is not None:
        acc |= caption_rect
    if acc.is_empty:
        acc = band
    acc = (acc + (-6, -6, 6, 6)) & fitz.Rect(0, 0, w, h)
    return tuple(acc)


def build_aux(pdf_path, chapter=None, want=("headings", "subheads", "sups", "hyphens", "figures"), exclude=None):
    """exclude: {page: [visible rects]} of table regions (from the ODL tables) to keep out of heading search."""
    exclude = dict(exclude or {})
    doc_pdf = fitz.open(pdf_path)
    aux = Aux()
    lines_by_page = {}
    sizes = collections.Counter()
    for page in doc_pdf:
        lines = page_lines(page)
        pno = page.number + 1
        lines_by_page[pno] = lines
        if is_toc_page(lines):
            aux.toc_pages.add(pno)
        xs = collections.Counter(round(ln.x0) for ln in lines if len(ln.text) > 40)
        if xs:
            aux.body_x0[pno] = xs.most_common(1)[0][0]
        for ln in lines:
            sizes[ln.size] += len(ln.text)
    body_size = sizes.most_common(1)[0][0] if sizes else 11.0
    aux.meta["body_size"] = body_size
    if aux.body_x0:
        aux.meta["body_x0_doc"] = collections.Counter(aux.body_x0.values()).most_common(1)[0][0]
    if "figures" in want:
        aux.figures = figure_refs(doc_pdf, lines_by_page, aux.toc_pages)
        for f in aux.figures:
            if not f.withheld:
                exclude.setdefault(f.page, []).append(f.box)
    if "headings" in want and chapter is not None:
        aux.headings = numbered_headings(doc_pdf, chapter, lines_by_page, aux.toc_pages, aux.body_x0, exclude,
                                         doc_margin=aux.meta.get("body_x0_doc"))
    if "subheads" in want:
        for pno, lines in lines_by_page.items():
            if pno in aux.toc_pages:
                continue
            for text, y in underlined_subheads(doc_pdf[pno - 1], lines, exclude.get(pno, ())):
                aux.subheads.append(SubRef(text, pno, y))
    if "sups" in want:
        for pno, lines in lines_by_page.items():
            s = superscripts(lines, body_size)
            if s:
                aux.sups[pno] = s
    if "hyphens" in want:
        aux.hyphen_map = hyphen_map(lines_by_page)
    aux.meta["lines_by_page"] = lines_by_page
    doc_pdf.close()
    return aux
