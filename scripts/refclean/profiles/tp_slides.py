"""TerraPower presentation package profile (TP-LIC-LET-0080, public version): the transmittal letter, the withholding
affidavit and enclosure covers (letter-size pages) followed by 16:9 slides of two decks (open meeting, closed meeting).

- Page furniture: the DOE agreement and copyright lines on every slide are dropped. The printed label of a slide is
  its slide number (bottom centre, 12 pt; the numbering restarts in each deck); a letter page keeps "Page N of M".
- Slide titles (32 pt) are headings; other converter headings become level 3 (as in the slides profile).
- Redaction brackets are letter-spaced on the slides ("[ [ ] ] (a)(4 ), E CI"); they are closed up and then handled
  as in the TerraPower report profile (one "> [!withheld]" callout per closing bracket; the letter's sentence that
  explains the marks keeps them as code spans).
- Tables: the converter splits the letter-spaced cells of the slide tables; each slide table is read again with
  PyMuPDF and letter-spaced cell lines ("1 . 0 2 0", "E B R -I I") are closed up.
- Equations: slides set in a math font (Unicode math italic, extracted as doubled glyphs) are rendered as one PNG per
  slide and the garbled equation fragments are dropped. The equations of the hot channel factor slide (PDF p.55) are
  transcribed to LaTeX from the slide image (EQUATIONS), marked with an editorial comment.
"""
import os
import re

import fitz

from .. import structure as S
from ..doc import El
from ..figures import odl_to_visible
from ..tables import Cell, Table
from . import slides, tp_report

META = {
    "TP-LIC-LET-0080": {
        "doc_id": "TP-LIC-LET-0080", "doc_type": "Pre-application meeting presentation package (letter, slides)",
        "issuer": "TerraPower, LLC", "revision": "", "date": "2023-05-25", "adams_accession": "ML23146A113",
        "title": "Core Thermal Hydraulic Methods Presentation Material",
        "tags": ["reference", "natrium", "presentation"],
        "aliases": ["TP-LIC-LET-0080", "Core Thermal Hydraulic Methods slides"],
    },
}

FLATTEN_TEXT_BLOCKS = True
TITLE_MIN_SIZE = 30.0          # slide titles are 32 pt; subtitles 24 pt; body at most 18 pt
SLIDE_NO = re.compile(r"^\d{1,3}$")
MATH = re.compile("[\U0001D400-\U0001D7FF]")
SPACED = [(re.compile(r"\[\s\["), "[["), (re.compile(r"\]\s\]"), "]]"), (re.compile(r"\(a\)\(4\s\)"), "(a)(4)"),
          (re.compile(r"\bE\sCI\b"), "ECI")]
EQUATIONS = {
    55: [
        r"\Delta T^{0\sigma}_{cladID} = F^{coolant}_{direct}\,\Delta T_{coolant} + F^{film}_{direct}\,\Delta T_{film}"
        r" + F^{clad}_{direct}\,\Delta T_{clad}",
        r"\Delta T^{3\sigma}_{j,stat} = \begin{pmatrix} F^{coolant}_{j,stat}-1 \\ F^{film}_{j,stat}-1 \\"
        r" F^{clad}_{j,stat}-1 \end{pmatrix}^{T} \begin{bmatrix} F^{coolant}_{direct} & 0 & 0 \\ 0 & F^{film}_{direct}"
        r" & 0 \\ 0 & 0 & F^{clad}_{direct} \end{bmatrix} \begin{pmatrix} \Delta T_{coolant} \\ \Delta T_{film} \\"
        r" \Delta T_{clad} \end{pmatrix}",
        r"T^{2\sigma}_{cladID} = T_{inlet} + \Delta T^{0\sigma}_{cladID} + \frac{2}{3}\sqrt{\sum_{j}"
        r" \left(\Delta T^{3\sigma}_{j,stat}\right)^{2}}",
    ],
}


def close_marks(text):
    for pat, rep in SPACED:
        text = pat.sub(rep, text)
    return text


def despace(line):
    """'1 . 0 2 0' -> '1.020', 'E B R -I I' -> 'EBR-II', 'O v erall' -> 'Overall', 'N atrium' -> 'Natrium': a line
    whose tokens are mostly single characters is letter-spaced; a lone capital before a lower-case word is a kerning
    split. 'Type 1' and 'FFTF-SAR *' stay."""
    toks = line.split()
    if not toks:
        return ""
    if sum(len(t) == 1 for t in toks) / len(toks) > 0.6:
        return "".join(toks)
    out = []
    for t in toks:
        if out and len(out[-1]) == 1 and out[-1].isupper() and t[:1].islower():
            out[-1] += t
        else:
            out.append(t)
    return " ".join(out)


def page_labels(doc, aux=None):
    pdf = fitz.open(doc.pdf_path)
    for page in pdf:
        pno = page.number + 1
        if page.rect.width > page.rect.height:      # slide: the slide number, alone at the bottom centre
            for b in page.get_text("dict")["blocks"]:
                for ln in b.get("lines", []):
                    t = "".join(s["text"] for s in ln["spans"]).strip()
                    if SLIDE_NO.match(t) and ln["bbox"][1] > 0.85 * page.rect.height:
                        doc.page_labels[pno] = t
        else:
            m = re.search(r"Page (\d+) of \d+", page.get_text())
            if m:
                doc.page_labels[pno] = m.group(1)
    pdf.close()


def drop_furniture(doc, aux=None):
    out = []
    for e in doc.els:
        t = " ".join(e.text.split()) if e.kind != "table" else ""
        if e.kind != "table" and (re.match(r"^SUBJECT TO DOE COOPERATIVE AGREEMENT|^Copyright ?©", t)
                                  or (SLIDE_NO.match(t) and e.page in doc.page_labels and t == doc.page_labels[e.page])):
            continue
        if e.kind != "table":
            e.text = close_marks(e.text)
        out.append(e)
    doc.els = out
    lone_openers(doc)


def lone_openers(doc):
    """A slide whose withheld block the converter reduced to its opening '[[' (the closing mark sits in a dropped
    text box): the opener becomes a callout with the label read from the slide's PDF text."""
    pdf = fitz.open(doc.pdf_path)
    out = []
    for e in doc.els:
        if e.kind in ("para", "heading", "item") and e.text.strip() == "[[":
            m = re.search(tp_report.CLOSE, close_marks(pdf[e.page - 1].get_text()))
            if m:
                out.append(tp_report.callout(m.group(1), e.page))
                continue
        out.append(e)
    pdf.close()
    doc.els = out


def slide_titles(doc, aux=None):
    seen = set()
    for e in doc.els:
        if e.kind in ("heading", "para") and e.page not in seen and e.size >= TITLE_MIN_SIZE:
            seen.add(e.page)
            e.kind, e.level = "heading", 2
            e.meta.update(heading_done=True, slide_title=True)
    for e in doc.els:
        if e.kind == "heading" and not e.meta.get("slide_title"):
            e.level = 3
            e.meta["heading_done"] = True


def slide_tables(doc, aux=None):
    """Replace each converter table on a slide with the PyMuPDF table of that slide, letter-spacing closed up and the
    redaction brackets kept as code spans (a withheld cell)."""
    pdf = fitz.open(doc.pdf_path)
    out, debris = [], {}
    for e in doc.els:
        if e.kind != "table":
            out.append(e)
            continue
        tabs = pdf[e.page - 1].find_tables().tables
        if not tabs:
            out.append(e)
            continue
        debris.setdefault(e.page, []).append(fitz.Rect(tabs[0].bbox) + (-4, -4, 4, 4))
        grid = []
        for r, row in enumerate(tabs[0].extract()):
            cells = []
            for c, text in enumerate(row):
                t = " ".join(despace(close_marks(ln)) for ln in (text or "").split("\n")).strip()
                t = tp_report.EMPTY_PAIR.sub("`[[ ]]`", re.sub(r"\[\[\s*\]\]", "[[ ]]", t))
                cells.append(Cell(t, r, c))
            grid.append(cells)
        out.append(El("table", "", e.page, e.bbox, table=Table(grid=grid, header_rows=2 if len(grid) > 2 else 1,
                                                                  page=e.page, pages=[e.page]), id=e.id))
        out.append(El("raw_md", "<!-- source: table read with PyMuPDF; letter-spaced cell text closed up -->", e.page))
    keep = []
    for e in out:        # converter fragments of the table cells (outside its table element) on the same slide
        vis = odl_to_visible(e.bbox, pdf[e.page - 1]) if e.kind in ("para", "item", "heading") and e.bbox else None
        if vis is not None and any(r.contains(fitz.Point((vis.x0 + vis.x1) / 2, (vis.y0 + vis.y1) / 2))
                                   for r in debris.get(e.page, [])):
            continue
        keep.append(e)
    pdf.close()
    doc.els = keep


def _fragment(text):
    """An equation fragment: math glyphs with fewer than three ordinary words, or a lone digit or minus sign of a
    fraction or exponent. Sentences that carry inline math stay (with their doubled glyphs)."""
    if re.fullmatch(r"[-–\s\d]{0,4}", text.strip()):
        return True
    words = re.findall(r"[A-Za-z]{2,}", MATH.sub(" ", text))
    return bool(MATH.search(text)) and len(words) < 3


def equation_slides(doc, aux):
    """Render each slide set in a math font as a PNG and drop its garbled equation fragments."""
    pages = {e.page for e in doc.els if e.kind != "table" and MATH.search(e.text)}
    if not pages:
        return
    pdf = fitz.open(doc.pdf_path)
    fig_dir = os.path.join(doc.out_dir, "figures", doc.key)
    os.makedirs(fig_dir, exist_ok=True)
    kept = [e for e in doc.els
            if not (e.page in pages and e.kind != "table" and not e.meta.get("slide_title") and _fragment(e.text))]
    out, done = [], set()
    for i, e in enumerate(kept):
        out.append(e)
        last = i + 1 == len(kept) or kept[i + 1].page != e.page
        if e.page in pages and last and e.page not in done:     # after the slide's text
            done.add(e.page)
            name = f"Slide_p{e.page}.png"
            if aux.meta.get("render_figures", True):
                pdf[e.page - 1].get_pixmap(dpi=150).save(os.path.join(fig_dir, name))
            out.append(El("raw_md", f"![Slide p.{e.page}](figures/{doc.key}/{name})", e.page, meta={"figure_img": e.page}))
            if e.page in EQUATIONS:
                out.append(El("raw_md", "<!-- source: equations transcribed to LaTeX from the slide image -->\n"
                              + "\n\n".join(f"$${q}$$" for q in EQUATIONS[e.page]), e.page))
    pdf.close()
    doc.meta["figures"] = [f"Slide p.{p}" for p in sorted(done)]
    doc.els = out


def steps():
    return [
        slides.drop_noise,
        page_labels,
        drop_furniture,
        slide_titles,
        slide_tables,
        equation_slides,
        tp_report.withheld,
        slides.column_order,
        S.normalise_text,
        S.normalise_item_levels,
    ]


def metadata(doc, aux):
    m = dict(META[doc.key])
    tables = [e.table.caption for e in doc.els if e.kind == "table" and e.table.caption]
    m.update({
        "source_pdf": f"references/raw/{doc.stem}.pdf",
        "raw_json": f"references/raw/{doc.stem}.json",
        "pdf_pages": doc.n_pages,
        "dropped_images": doc.meta.get("dropped_images", 0),
        "tables": tables,
        "figures": doc.meta.get("figures", []),
        "withheld": [],
    })
    return m
