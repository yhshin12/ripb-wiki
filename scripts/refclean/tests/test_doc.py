import pytest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from refclean.doc import elements_from_json, load_doc  # noqa: E402
from refclean.tables import render_md  # noqa: E402

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")


def _cell(r, c, text, bold=False, rs=1, cs=1):
    return {"type": "table cell", "row number": r, "column number": c, "row span": rs, "column span": cs,
            "page number": 5, "kids": [{"type": "paragraph", "content": text, "font": "Arial,Bold" if bold else "Arial"}]}


SYNTH = {"number of pages": 5, "kids": [
    {"type": "header", "page number": 5, "kids": [
        {"type": "heading", "content": "Kemmerer Unit 1 PSAR Table 6.4-7 X (Sheet 1 of 2)"}]},
    {"type": "list", "page number": 5, "numbering style": "unordered", "list items": [
        {"type": "list item", "content": "● a", "page number": 5, "kids": []},
        {"type": "list item", "content": "● b", "page number": 5, "kids": []}]},
    {"type": "table", "page number": 5, "number of rows": 3, "number of columns": 2, "rows": [
        {"cells": [_cell(1, 1, "K", True), _cell(1, 2, "V", True)]},
        {"cells": [_cell(2, 1, "A", rs=2), _cell(2, 2, "1")]},
        {"cells": [_cell(3, 2, "2")]}]},
    {"type": "footer", "page number": 5, "kids": [
        {"type": "paragraph", "content": "6.4-12 Revision 1"},
        {"type": "paragraph", "content": "SUBJECT TO DOE COOPERATIVE AGREEMENT NO. DE-NE0009054"}]},
]}


def test_synthetic_elements():
    els, labels = elements_from_json(SYNTH)
    assert labels == {5: "6.4-12"}
    assert [e.kind for e in els] == ["hdr", "item", "item", "table"]
    assert els[0].text == "Table 6.4-7 X (Sheet 1 of 2)"
    t = els[3].table
    assert t.header_rows == 1
    assert render_md(t).splitlines()[2:] == ["| A | 1 |", "| A | 2 |"]  # rowspan filled down


@pytest.mark.refs
def test_ch4_smoke():
    d = load_doc("PSAR_ch04", "TP_Natrium_PSAR2025_ch4_integrated evaluations", RAW, os.path.join(VAULT, "references"))
    assert d.n_pages == 16
    assert d.page_labels[4] == "4.1-1" and d.page_labels[16] == "4.2-11"
    assert sum(1 for e in d.els if e.kind == "table") >= 5
    t2 = [e.table for e in d.els if e.kind == "table" and e.page == 13][0]
    assert "Mean Dose Margin[d]" in render_md(t2).splitlines()[0]


# A list item whose kids are a nested list, a table, a caption and an image (NEI Table 5-9, p87, is a table kid of
# the list item that carries its caption): every kid must reach the stream, in document order.
NESTED = {"number of pages": 1, "kids": [
    {"type": "list", "page number": 87, "numbering style": "unordered", "list items": [
        {"type": "list item", "content": "Table 5-9. LBE IE Series", "page number": 87, "kids": [
            {"type": "caption", "content": "Table 5-9. LBE IE Series", "page number": 87, "linked content id": 9},
            {"type": "table", "page number": 87, "id": 2133, "number of rows": 2, "number of columns": 2, "rows": [
                {"cells": [_cell(1, 1, "K", True), _cell(1, 2, "V", True)]},
                {"cells": [_cell(2, 1, "a"), _cell(2, 2, "b")]}]},
            {"type": "image", "source": "img.png", "page number": 87},
            {"type": "paragraph", "content": "trailing text", "page number": 87},
            {"type": "list", "numbering style": "unordered", "list items": [
                {"type": "list item", "content": "sub", "page number": 87, "kids": []}]},
            {"type": "footnote", "content": "", "page number": 87, "id": 77}]}]}]}


def test_nested_item_kids_are_kept_in_order():
    warn = []
    els, _ = elements_from_json(NESTED, warn)
    assert [e.kind for e in els] == ["item", "caption", "table", "image", "para", "item"]
    assert all(e.meta.get("in_item") for e in els[1:5])
    assert els[2].id == 2133 and els[2].table.n_rows == 2 and els[2].table.grid[1][1].text == "b"
    assert els[5].level == 1 and els[5].text == "sub"                      # nested list one level deeper
    assert warn == ["dropped empty footnote kid id=77 on page 87 under a list item"]


def test_overlapping_cells_keep_the_first_and_are_recorded():
    """Two ODL cells claiming the same grid position (PSAR ch7 table 8849, p334): the first wins, the loss is
    recorded in Table.meta['overlaps'] so clean_references can report it."""
    from refclean.tables import from_odl
    node = {"page number": 334, "id": 8849, "number of rows": 2, "number of columns": 2, "rows": [
        {"cells": [_cell(1, 1, "MTS", cs=2), _cell(1, 2, "AC PANELBOARD")]},
        {"cells": [_cell(2, 1, "x"), _cell(2, 2, "y")]}]}
    t = from_odl(node)
    assert t.grid[0][1].text == "MTS"                                      # the second cell did not overwrite it
    assert t.meta["overlaps"] == [{"row": 1, "col": 2, "kept": "MTS", "dropped": "AC PANELBOARD"}]
    assert from_odl({"page number": 1, "number of rows": 1, "number of columns": 1,
                     "rows": [{"cells": [_cell(1, 1, "a")]}]}).meta == {}   # no key when nothing overlaps


def test_overlap_warnings_reach_the_report():
    from refclean.doc import Doc, El
    from refclean.tables import Cell, Table, overlap_warnings
    t = Table(grid=[[Cell("MTS", 0, 0)]], page=334, id=8849)
    t.meta["overlaps"] = [{"row": 1, "col": 2, "kept": "MTS", "dropped": "AC PANELBOARD"}]
    doc = Doc("k", "s", "", "", 1, {}, [El("table", "", 334, table=t)])
    assert len(overlap_warnings(doc)) == 1
    assert doc.meta["table_warnings"][0].startswith("table id=8849 p334 r1c2: kept 'MTS', dropped 'AC PANELBOARD'")


def test_text_after_a_multipage_table_reannounces_the_last_page():
    """A range anchor p a-b covers the table only; text after it gets its own page-b anchor so that the first-number
    citation rule does not date it back to page a."""
    from refclean.doc import Doc, El
    from refclean.emit import render
    from refclean.tables import Cell, Table
    t = Table(grid=[[Cell("K", 0, 0)], [Cell("A", 1, 0)]], page=138, pages=[138, 139])
    doc = Doc("k", "s", "", "", 140, {138: "7.2-46", 139: "7.2-47"},
              [El("para", "before", 138), El("table", "", 138, table=t), El("para", "after", 139),
               El("para", "next", 140)])
    body = render(doc, {}).split("\n")
    assert [x for x in body if x.startswith("<!-- page")] == [
        "<!-- page 138 | 7.2-46 -->", "<!-- page 138-139 | 7.2-46..7.2-47 -->", "<!-- page 139 | 7.2-47 -->",
        "<!-- page 140 -->"]
    assert body.index("<!-- page 139 | 7.2-47 -->") < body.index("after")


def test_text_block_of_lists_is_body_but_other_text_blocks_are_figure_labels():
    tree = {"kids": [
        {"type": "text block", "page number": 18, "kids": [
            {"type": "list", "page number": 18, "list items": [
                {"type": "list item", "content": "• seismic PRA", "page number": 18, "kids": []}]}]},
        {"type": "text block", "page number": 19, "kids": [
            {"type": "paragraph", "page number": 19, "content": "diagram label"}]}]}
    els, _ = elements_from_json(tree)
    assert [(e.kind, e.text, e.page) for e in els] == [("item", "• seismic PRA", 18)]
