"""Load the opendataloader JSON tree into a flat element stream (Doc.els)."""
import json
import os
import re
from dataclasses import dataclass, field

from . import tables as _tables


@dataclass
class El:
    kind: str                 # 'heading' | 'para' | 'item' | 'table' | 'image' | 'caption' | 'hdr' | 'raw_md'
    text: str = ""
    page: int = 0
    bbox: tuple = ()
    font: str = ""
    size: float = 0.0
    level: int = 0            # heading: Markdown level; item: nesting depth
    list_style: str = ""
    table: object = None
    id: int = 0
    meta: dict = field(default_factory=dict)


@dataclass
class Doc:
    key: str
    stem: str
    raw_dir: str
    out_dir: str
    n_pages: int
    page_labels: dict
    els: list
    meta: dict = field(default_factory=dict)

    @property
    def pdf_path(self):
        return os.path.join(self.raw_dir, self.stem + ".pdf")

    @property
    def json_path(self):
        return os.path.join(self.raw_dir, self.stem + ".json")


LABEL_PATTERNS = [
    re.compile(r"^(\S+)\s+Revision\s+\d+$"),                                   # PSAR: '4.2-7 Revision 1'
    re.compile(r"^Appendix [ABC] to RG 1\.232, Rev\. 0, Page ([A-C]-\d+)$"),   # RG appendices
    re.compile(r"^RG 1\.232, Rev\. 0, Page (\d+)$"),                            # RG body
    re.compile(r"^©\s*NEI 2019\. All rights reserved\. nei\.org\s+(\S+)$"),     # NEI front matter
]
HEADER_PREFIX = re.compile(r"^\s*Kemmerer Unit 1 PSAR\b\s*")


def _text(node):
    return (node.get("content") or "").strip()


def _items(node, depth, out, page_hint, warn=None):
    style = node.get("numbering style", "")
    for it in node.get("list items", []) or []:
        out.append(El("item", _text(it), it.get("page number", page_hint), tuple(it.get("bounding box", ())),
                      it.get("font", ""), it.get("font size", 0.0), depth, style, id=it.get("id", 0)))
        for kid in it.get("kids", []) or []:
            _item_kid(kid, depth, out, it.get("page number", page_hint), warn)


def _item_kid(kid, depth, out, page_hint, warn=None):
    """A child of a list item, emitted in document order with the same kinds as a top-level node.

    Nested lists recurse one level deeper; paragraphs and headings become `para` (a heading inside a list item is
    never a document heading in this corpus); tables, images and captions are carried through as their own elements
    so that a table nested under a list item (NEI Table 5-9, p87) reaches the stream instead of being dropped.
    """
    t = kid.get("type")
    page = kid.get("page number", page_hint)
    bbox = tuple(kid.get("bounding box", ()))
    font, size = kid.get("font", ""), kid.get("font size", 0.0)
    eid = kid.get("id", 0)
    if t == "list":
        _items(kid, depth + 1, out, page_hint, warn)
    elif t in ("paragraph", "heading"):
        out.append(El("para", _text(kid), page, bbox, font, size, id=eid, meta={"in_item": True}))
    elif t == "caption":
        out.append(El("caption", _text(kid), page, bbox, font, size, id=eid,
                      meta={"in_item": True, "linked": kid.get("linked content id")}))
    elif t == "table":
        out.append(El("table", "", page, bbox, table=_tables.from_odl(kid), id=eid, meta={"in_item": True}))
    elif t == "image":
        out.append(El("image", kid.get("source", ""), page, bbox, id=eid, meta={"in_item": True}))
    else:
        txt = _text(kid)
        if txt:
            out.append(El("para", txt, page, bbox, font, size, id=eid, meta={"in_item": True, "odl_type": t}))
        elif warn is not None:
            warn.append(f"dropped empty {t} kid id={eid} on page {page} under a list item")


def _label_from_footer(node):
    for kid in node.get("kids", []) or []:
        t = _text(kid)
        for pat in LABEL_PATTERNS:
            m = pat.match(t)
            if m:
                return next(g for g in m.groups() if g)
    return None


def elements_from_json(tree, warn=None, flatten_text_blocks=False):
    """Return (els, page_labels) from an opendataloader JSON tree; `warn` collects dropped-node messages.

    A 'text block' node groups the text of one drawn box. In the reports and guides its text is diagram labelling
    inside a rendered figure and is skipped; a slide profile sets flatten_text_blocks to read it as body content.
    """
    els, labels = [], {}
    for node in tree.get("kids", []):
        t = node.get("type")
        if t == "text block" and flatten_text_blocks:
            sub_els, sub_labels = elements_from_json(node, warn, flatten_text_blocks)
            els += sub_els
            labels.update(sub_labels)
            continue
        page = node.get("page number", 0)
        bbox = tuple(node.get("bounding box", ()))
        if t == "footer":
            lab = _label_from_footer(node)
            if lab:
                labels[page] = lab
            continue
        if t == "header":
            for kid in node.get("kids", []) or []:
                rest = HEADER_PREFIX.sub("", _text(kid)).strip()
                if rest:
                    els.append(El("hdr", rest, page, tuple(kid.get("bounding box", bbox)), kid.get("font", ""),
                                  kid.get("font size", 0.0), id=kid.get("id", 0)))
            continue
        if t == "heading":
            els.append(El("heading", _text(node), page, bbox, node.get("font", ""), node.get("font size", 0.0),
                          int(node.get("heading level") or 0), id=node.get("id", 0)))
        elif t == "paragraph":
            els.append(El("para", _text(node), page, bbox, node.get("font", ""), node.get("font size", 0.0),
                          id=node.get("id", 0)))
        elif t == "caption":
            els.append(El("caption", _text(node), page, bbox, node.get("font", ""), node.get("font size", 0.0),
                          id=node.get("id", 0), meta={"linked": node.get("linked content id")}))
        elif t == "list":
            _items(node, 0, els, page, warn)
        elif t == "table":
            els.append(El("table", "", page, bbox, table=_tables.from_odl(node), id=node.get("id", 0)))
        elif t == "image":
            els.append(El("image", node.get("source", ""), page, bbox, id=node.get("id", 0)))
        else:
            txt = _text(node)
            if txt:
                els.append(El("para", txt, page, bbox, id=node.get("id", 0), meta={"odl_type": t}))
    return els, labels


def load_doc(key, stem, raw_dir, out_dir, flatten_text_blocks=False):
    with open(os.path.join(raw_dir, stem + ".json"), encoding="utf-8") as f:
        tree = json.load(f)
    warn = []
    els, labels = elements_from_json(tree, warn, flatten_text_blocks)
    meta = {"pdf_title": tree.get("title", ""), "pdf_author": tree.get("author", "")}
    if warn:
        meta["doc_warnings"] = warn
    return Doc(key=key, stem=stem, raw_dir=raw_dir, out_dir=out_dir,
               n_pages=int(tree.get("number of pages", 0)), page_labels=labels, els=els, meta=meta)
