"""ACRS slide-deck profile (ACRS_ML25293A458): slide titles as headings, bullets as list items, two-column slides in
column order, and each slide's content pictures rendered from the PDF as `[!figure] Slide N` callouts.

Decision 2026-09-15 (meta/status.md): slide titles `##`, no bullet sentence promoted to a heading, caption-less
pictures included. The converter reports one full-slide template image per page; those are backgrounds and are
dropped. The remaining pictures are fragments that overlap (a figure cut into 2-3 images), so they are grouped by
intersection and each group is rendered from the PDF page as one PNG.
"""
import os
import re

import fitz

from .. import structure as S
from ..doc import El
from ..figures import odl_to_visible

META = {
    "ACRS_ML25293A458": {
        "doc_id": "ML25293A458", "doc_type": "NRC staff presentation (ACRS subcommittee meeting)",
        "issuer": "U.S. Nuclear Regulatory Commission, NRR/DANU/UTB2 (Reed Anzalone)",
        "revision": "", "date": "2025-10-22/2025-10-23",
        "title": "NRC Review of Kemmerer Unit 1 Construction Permit Application, Control of Heat Generation",
        "tags": ["reference", "nrc", "acrs", "natrium"], "aliases": ["ACRS Control of Heat Generation slides"],
    },
}

TITLE_MIN_SIZE = 32.0          # slide titles are 36-48 pt (slide 21: 36 pt); body text is at most 28 pt
BULLET = re.compile(r"^\s*[•●▪■◦]")
MARGIN_X0, INDENT_STEP = 73.0, 36.0
COLUMN_X0 = 400.0              # a label heading starting right of this opens a second column
PSAR_FIG = re.compile(r"^PSAR figure\s+\S+$")


def level_from_x(x0):
    """Bullet depth from the left edge: 73 pt -> 0, 109 pt -> 1, 145 pt -> 2."""
    return max(0, round((x0 - MARGIN_X0) / INDENT_STEP))


def group_rects(rects):
    """Merge intersecting rectangles until no two groups intersect; order by first appearance."""
    groups = [fitz.Rect(r) for r in rects]
    merged = True
    while merged:
        merged = False
        for i in range(len(groups)):
            for j in range(i + 1, len(groups)):
                if groups[i].intersects(groups[j]):
                    groups[i] |= groups[j]
                    del groups[j]
                    merged = True
                    break
            if merged:
                break
    return groups


def slide_titles(doc, aux=None):
    """First large paragraph on each page -> heading (level 1 on the cover slide, level 2 elsewhere)."""
    seen = set()
    for e in doc.els:
        if e.kind != "para" or e.size < TITLE_MIN_SIZE or e.page in seen:
            continue
        seen.add(e.page)
        e.kind = "heading"
        e.level = 1 if e.page == 1 else 2
        e.meta.update(heading_done=True, slide_title=True)


def bullets_and_labels(doc, aux=None):
    """Bullet sentences (tagged heading or paragraph by the converter) become list items at their indent depth;
    remaining non-title headings are column labels one level below the slide title."""
    for e in doc.els:
        if e.meta.get("slide_title"):
            continue
        if e.kind in ("heading", "para", "item") and BULLET.match(e.text):
            e.kind = "item"
            e.level = level_from_x(e.bbox[0]) if e.bbox else 0
        elif e.kind == "heading":
            e.level = 3
            e.meta["heading_done"] = True


def column_order(doc, aux=None):
    """On a slide with a label heading right of COLUMN_X0, emit the left column, then the right column, then the
    elements that span both columns (x0 left of the column, x1 right of it)."""
    pages = {}
    for i, e in enumerate(doc.els):
        pages.setdefault(e.page, []).append(i)
    order = list(range(len(doc.els)))
    for page, idx in pages.items():
        cols = [doc.els[i].bbox[0] for i in idx if doc.els[i].kind == "heading"
                and not doc.els[i].meta.get("slide_title") and doc.els[i].bbox and doc.els[i].bbox[0] >= COLUMN_X0]
        if not cols:
            continue
        colx = min(cols)
        head, left, right, span = [], [], [], []
        for i in idx:
            e = doc.els[i]
            if e.meta.get("slide_title") or not e.bbox or e.kind == "image":
                head.append(i)
            elif e.bbox[0] >= colx:
                right.append(i)
            elif e.bbox[2] < colx:
                left.append(i)
            else:
                span.append(i)
        new = head + left + right + span
        for pos, i in zip(sorted(idx), new):
            order[pos] = i
    doc.els = [doc.els[i] for i in order]


def slide_figures(doc, aux, render=True, fig_dir_rel=None):
    """Drop full-slide background images; render each group of overlapping content images as one PNG callout.
    'PSAR figure x' captions on the same slide are moved into the slide's (last) callout."""
    fig_dir_rel = fig_dir_rel or f"figures/{doc.key}"
    pdf = fitz.open(doc.pdf_path)
    by_page = {}
    for e in doc.els:
        by_page.setdefault(e.page, []).append(e)
    names, out = [], []
    for page_no in sorted(by_page):
        els = by_page[page_no]
        page = pdf[page_no - 1]
        pr = page.rect
        rects, first_img = [], None
        for e in els:
            if e.kind != "image" or not e.bbox:
                continue
            x0, y0, x1, y1 = e.bbox
            if x0 <= 1 and y0 <= 1 and x1 >= pr.width - 1 and y1 >= pr.height - 1:
                continue                                    # slide template background
            vis = odl_to_visible(e.bbox, page) & pr
            if vis.is_empty:
                continue
            rects.append(vis)
            first_img = first_img or e
        groups = group_rects(rects)
        captions = [e for e in els if e.kind in ("caption", "para") and PSAR_FIG.match(" ".join(e.text.split()))]
        callouts = []
        for k, g in enumerate(groups, 1):
            suffix = "" if len(groups) == 1 else f"-{k}"
            fname = f"Slide_{page_no}{suffix}.png"
            if render:
                path = os.path.join(doc.out_dir, fig_dir_rel, fname)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                page.get_pixmap(dpi=200, clip=g).save(path)
            names.append(f"Slide {page_no}{suffix}")
            callouts.append([f"> [!figure] Slide {page_no}{suffix}", f"> ![Slide {page_no}{suffix}]({fig_dir_rel}/{fname})"])
        if callouts and captions:
            callouts[-1] += [">"] + [f"> {' '.join(c.text.split())}" for c in captions]
        blocks = [El("raw_md", "\n".join(c), page_no, meta={"slide_figure": True}) for c in callouts]
        has_title = any(e.meta.get("slide_title") for e in els)
        placed = not blocks
        for e in els:
            if e.kind == "image":
                if e is first_img and not placed and not has_title:
                    out += blocks        # no title on this slide: the pictures stand where the first one was
                    placed = True
                continue
            if callouts and e in captions:
                continue
            out.append(e)
            if e.meta.get("slide_title") and not placed:
                out += blocks            # pictures follow the slide title
                placed = True
        if not placed:
            out += blocks
    pdf.close()
    doc.meta["figures"] = names
    doc.els = out


def steps():
    return [
        S.withheld_callouts,
        slide_titles,
        bullets_and_labels,
        column_order,
        lambda d, a: slide_figures(d, a, render=a.meta.get("render_figures", True)),
        S.normalise_text,
        S.normalise_item_levels,
    ]


def metadata(doc, aux):
    if doc.key not in META:
        raise KeyError(f"acrs_slides profile has no META entry for {doc.key!r}")
    m = dict(META[doc.key])
    m.update({
        "source_pdf": f"references/raw/{doc.stem}.pdf",
        "raw_json": f"references/raw/{doc.stem}.json",
        "pdf_pages": doc.n_pages,
        "figures": doc.meta.get("figures", []),
        "withheld": doc.meta.get("withheld", []),
    })
    return m
