"""ACRS slide-deck profile: unit checks of the layout helpers, and one in-memory build of ACRS_ML25293A458."""
import os
import re
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")
KEY = "ACRS_ML25293A458"


def test_level_from_x():
    from refclean.profiles.acrs_slides import level_from_x
    assert [level_from_x(x) for x in (73, 109, 145, 60)] == [0, 1, 2, 0]


def test_group_rects_merges_overlapping_fragments_only():
    import fitz
    from refclean.profiles.acrs_slides import group_rects
    g = group_rects([(0, 0, 10, 10), (5, 5, 20, 20), (100, 100, 110, 110)])
    assert [tuple(r) for r in g] == [(0, 0, 20, 20), (100, 100, 110, 110)]
    assert all(isinstance(r, fitz.Rect) for r in g)


def test_bullets_become_items_and_labels_level_three():
    from refclean.doc import Doc, El
    from refclean.profiles import acrs_slides as A
    d = Doc(KEY, "x", RAW, VAULT, 1, {}, [
        El("para", "Slide title", 3, (73, 436, 600, 480), size=44.0),
        El("heading", "• Described in PSAR sections", 3, (73, 339, 452, 398), size=28.0, level=1),
        El("para", "• nested point", 3, (109, 300, 400, 330), size=24.0),
        El("heading", "PDC 26", 3, (73, 396, 143, 420), size=24.0, level=2),
    ])
    A.slide_titles(d)
    A.bullets_and_labels(d)
    assert [(e.kind, e.level) for e in d.els] == [("heading", 2), ("item", 0), ("item", 1), ("heading", 3)]


def test_column_order_left_right_then_spanning():
    from refclean.doc import Doc, El
    from refclean.profiles import acrs_slides as A
    d = Doc(KEY, "x", RAW, VAULT, 1, {}, [
        El("para", "Title", 19, (73, 436, 700, 480), size=44.0),
        El("heading", "Left label", 19, (73, 396, 143, 420), level=2),
        El("heading", "Right label", 19, (493, 396, 683, 420), level=2),
        El("item", "R1", 19, (493, 312, 878, 390)),
        El("item", "L1", 19, (73, 287, 456, 350)),
        El("para", "Spanning conclusion", 19, (148, 41, 795, 103)),
    ])
    A.slide_titles(d)
    A.bullets_and_labels(d)
    A.column_order(d)
    assert [e.text for e in d.els] == ["Title", "Left label", "L1", "Right label", "R1", "Spanning conclusion"]


@pytest.fixture(scope="module")
def built():
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import DOCS, acrs_slides
    from refclean.verify import verify
    stem = DOCS[KEY][0]
    if not os.path.exists(os.path.join(RAW, stem + ".json")):
        pytest.skip("ACRS conversion not available")
    doc = load_doc(KEY, stem, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=None, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in acrs_slides.steps():
        step(doc, aux)
    text, failed = CR.apply_patches(KEY, render(doc, acrs_slides.metadata(doc, aux)))
    return text, failed, verify(doc, aux, text)


@pytest.mark.refs
def test_acrs_deck_structure(built):
    text, failed, ver = built
    assert failed == []
    assert 'doc_id: "ML25293A458"' in text and "pdf_pages: 22" in text
    assert text.count("<!-- page ") >= 20
    body = text.split("\n---\n", 1)[1]
    titles = re.findall(r"^## (.+)$", body, re.M)
    assert len(titles) == 21 and "Topics" in titles and "Acronyms" in titles
    assert re.search(r"^# NRC Review of Kemmerer Unit 1 Construction Permit Application$", body, re.M)
    assert not re.search(r"^#+ •", body, re.M)
    assert ver["summary"]["missing_pct"] <= 2.0, ver["summary"]


@pytest.mark.refs
def test_acrs_figures_and_columns(built):
    text, _, _ = built
    body = text.split("\n---\n", 1)[1]
    callouts = re.findall(r"^> \[!figure\] Slide (\d+(?:-\d+)?)$", body, re.M)
    assert {c.split("-")[0] for c in callouts} == {"3", "4", "5", "6", "7", "10", "14", "21"}
    assert body.index("## Reactor core components (RCC)") < body.index("> [!figure] Slide 3")
    assert "> PSAR figure 7.1.1-1" in body
    assert "\nPSAR figure 7.1.1-1\n" not in body
    assert body.index("insert negative reactivity") < body.index("Delatch and gravity scram")
    assert body.index("Delatch and gravity scram") < body.index("Based on the independence")
