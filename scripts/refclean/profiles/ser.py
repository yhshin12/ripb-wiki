"""NRC safety evaluation profile (SER_KU1_CP): the generic pipeline with SER-specific structure.

- Numbered section headings ("3.2.1 Mechanistic Source Term") are set in the body font, so they are found from the
  PDF lines with pdfaux.numbered_headings for every chapter number (the PSAR profiles do this for one chapter).
- Proprietary text is withheld inline as "[[ ]]" (the redacted public version keeps the brackets and drops the
  text). A bracket closer at the start of a converter paragraph ("]] and more detailed models") is body text, not a
  heading.
- Printed page labels ("3-43", roman numerals in the front matter) sit alone on the bottom line of each page; they
  become the second part of the page anchors.
"""
import re

import fitz

from .. import structure as S
from ..figures import figures_step
from ..levels import assign_levels
from ..pdfaux import numbered_headings
from . import generic

META = {"SER_KU1_CP": generic.META["SER_KU1_CP"]}

MAX_CHAPTER = 25
LABEL = re.compile(r"^(?:\d{1,2}-\d{1,3}|[ivxl]{1,6})$")
BRACKET_START = re.compile(r"^\s*\]\]")


def page_labels(doc, aux):
    pdf = fitz.open(doc.pdf_path)
    labels = {}
    for page in pdf:
        h = page.rect.height
        bottom = [b for b in page.get_text("blocks") if b[1] > 0.85 * h]
        for b in sorted(bottom, key=lambda b: b[1]):
            for line in b[4].splitlines():
                if LABEL.match(line.strip()):
                    labels[page.number + 1] = line.strip()
    pdf.close()
    doc.page_labels.update(labels)


def headings_all_chapters(doc, aux):
    lines = aux.meta.get("lines_by_page", {})
    pdf = fitz.open(doc.pdf_path)
    refs = []
    for ch in range(1, MAX_CHAPTER + 1):
        refs += numbered_headings(pdf, ch, lines, aux.toc_pages, aux.body_x0, None,
                                  doc_margin=aux.meta.get("body_x0_doc"))
    pdf.close()
    aux.headings = sorted(refs, key=lambda r: r.page)


def bracket_closers_are_body(doc, aux=None):
    for e in doc.els:
        if e.kind == "heading" and BRACKET_START.match(e.text):
            e.kind, e.level = "para", 0


def steps():
    return [
        page_labels,
        headings_all_chapters,
        bracket_closers_are_body,
        S.drop_toc,
        S.withheld_callouts,
        lambda d, a: figures_step(d, a, render=a.meta.get("render_figures", True)),
        S.promote_headings,
        S.insert_subheads,
        S.fix_false_items,
        S.join_breaks,
        S.attach_captions_and_merge,
        S.attach_table_notes,
        S.normalise_text,
        S.references_as_items,
        S.normalise_item_levels,
        assign_levels,
    ]


def metadata(doc, aux):
    m = generic.metadata(doc, aux) if doc.key in generic.META else {}
    m.update(META[doc.key])
    m.update({
        "source_pdf": f"references/raw/{doc.stem}.pdf",
        "raw_json": f"references/raw/{doc.stem}.json",
        "pdf_pages": doc.n_pages,
        "headings_found": len(aux.headings),
    })
    return m
