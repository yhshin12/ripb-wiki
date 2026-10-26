"""Figures: render PNGs from the PDF, replace captions with image embeds, drop vector-figure text debris."""
import os
import re

import fitz
from PIL import Image

from .doc import El

FIG_TXT = re.compile(r"^(?:Kemmerer Unit 1 PSAR\s+)?Figure\s+(\d+(?:\.\d+)*-\d+[A-Z]?)\.?\s+(.*)$")


def odl_to_visible(bbox, page):
    """opendataloader bbox -> PyMuPDF visible rect.

    opendataloader reports boxes in the displayed (already rotated) page with the origin at the bottom-left,
    so only the y axis is flipped (checked on /Rotate 90 pages of PSAR ch7, e.g. p131)."""
    if not bbox:
        return None
    x0, y0, x1, y1 = bbox
    hgt = page.rect.height
    r = fitz.Rect(x0, hgt - y1, x1, hgt - y0)
    r.normalize()
    return r


def render_png(pdf_doc, ref, out_path, dpi=200):
    page = pdf_doc[ref.page - 1]
    pix = page.get_pixmap(dpi=dpi)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    s = dpi / 72.0
    x0, y0, x1, y1 = ref.box
    img = img.crop((int(x0 * s), int(y0 * s), int(x1 * s), int(y1 * s)))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path, optimize=True)
    return img.size


def figures_step(doc, aux, render=True, fig_dir_rel=None, fig_txt=FIG_TXT):
    """Replace each figure's caption with heading + image (or withheld callout); drop debris inside the figure box.
    fig_txt: caption pattern (number, title) for profiles whose captions differ, e.g. "Figure 4-1: Title"."""
    fig_dir_rel = fig_dir_rel or f"figures/{doc.key}"
    pdf = fitz.open(doc.pdf_path)
    by_page = {}
    for ref in aux.figures:
        by_page.setdefault(ref.page, []).append(ref)
    done = set()
    out = []
    for e in doc.els:
        refs = by_page.get(e.page)
        if not refs:
            out.append(e)
            continue
        page = pdf[e.page - 1]
        m = fig_txt.match(" ".join(e.text.split())) if e.kind in ("para", "item", "heading", "caption", "hdr") else None
        ref = next((r for r in refs if m and m.group(1) == r.num), None)
        if ref and ref.num not in done:
            done.add(ref.num)
            caption = " ".join(m.group(2).split()) or ref.caption
            h = El("heading", f"Figure {ref.num} {caption}", e.page, e.bbox, meta={"figure": ref.num})
            out.append(h)
            if ref.withheld:
                doc.meta.setdefault("withheld", []).append(f"Figure {ref.num} {caption}")
                continue  # the withheld callout element follows separately
            fname = f"Fig_{ref.num}.png"
            if render:
                render_png(pdf, ref, os.path.join(doc.out_dir, fig_dir_rel, fname))
            out.append(El("raw_md", f"![Figure {ref.num} {caption}]({fig_dir_rel}/{fname})", e.page,
                          meta={"figure_img": ref.num}))
            continue
        if e.kind in ("raw_md",) or e.meta.get("numbered"):
            out.append(e)
            continue
        # debris: element centre inside a (non-withheld) figure box on this page
        vis = odl_to_visible(e.bbox, page)
        inside = False
        if vis is not None:
            c = fitz.Point((vis.x0 + vis.x1) / 2, (vis.y0 + vis.y1) / 2)
            inside = any(not r.withheld and fitz.Rect(r.box).contains(c) for r in refs)
        if e.kind == "image" or inside:
            continue
        out.append(e)
    pdf.close()
    missing = [r.num for r in aux.figures if r.num not in done]
    doc.meta.setdefault("figures_without_caption_element", []).extend(missing)
    doc.meta["figures"] = [f"{r.num} {r.caption}" for r in aux.figures]
    doc.els = out
