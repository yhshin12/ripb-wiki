"""Generic slide profile and the opt-in text-block flattening (synthetic input; no source document is read)."""
from refclean.doc import El, elements_from_json
from refclean.profiles.slides import band_column_order


def el(name, x0, y0, x1, y1, title=False):
    return El("para", name, 1, (x0, y0, x1, y1), meta={"slide_title": True} if title else {})


def names(els):
    return [e.text for e in els]


def test_two_columns_read_left_then_right():
    els = [el("T", 40, 480, 500, 505, title=True), el("L1", 50, 400, 400, 420), el("R1", 500, 400, 900, 420),
           el("L2", 50, 300, 400, 320), el("R2", 500, 300, 900, 320)]
    assert names(band_column_order(els, 480)) == ["T", "L1", "L2", "R1", "R2"]


def test_full_width_box_separates_bands():
    els = [el("T", 40, 480, 500, 505, title=True), el("L1", 50, 400, 400, 420), el("R1", 500, 400, 900, 420),
           el("WIDE", 50, 250, 900, 280), el("L2", 50, 100, 400, 120), el("R2", 500, 100, 900, 120)]
    assert names(band_column_order(els, 480)) == ["T", "L1", "R1", "WIDE", "L2", "R2"]


def test_single_column_slide_keeps_order():
    els = [el("T", 40, 480, 500, 505, title=True), el("A", 50, 400, 900, 420), el("B", 50, 300, 900, 320)]
    assert names(band_column_order(els, 480)) == ["T", "A", "B"]


def test_text_block_is_opt_in():
    tree = {"kids": [{"type": "text block", "page number": 2, "kids": [
        {"type": "paragraph", "content": "boxed text", "page number": 2, "bounding box": [1, 2, 3, 4]}]}]}
    assert elements_from_json(tree)[0] == []
    els, _ = elements_from_json(tree, flatten_text_blocks=True)
    assert [(e.kind, e.text, e.page) for e in els] == [("para", "boxed text", 2)]
