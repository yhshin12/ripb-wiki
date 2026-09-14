"""Kemmerer Unit 1 PSAR chapters (TerraPower Natrium) — common steps; chapter hooks live in psar_chNN.py."""
import importlib
import re

from .. import structure as S
from ..doc import El
from ..figures import figures_step

CHAPTER_TITLE = re.compile(r"^Chapter\s+(\d+)\s+(.+)$")


def depth(num):
    return len(num.split("."))


def _owner(num_with_dash):
    """'4.2-7' -> '4.2'; '7.2.3-1' -> '7.2.3'."""
    return num_with_dash.rsplit("-", 1)[0]


def assign_levels(doc, aux=None):
    cur = 1
    els = doc.els
    for i, e in enumerate(els):
        if e.kind == "heading":
            m = CHAPTER_TITLE.match(e.text.strip())
            if m and not e.meta.get("numbered"):
                e.level = 1
                e.meta["chapter_title"] = True
                cur = 1
                continue
            if e.meta.get("numbered"):
                e.level = min(depth(e.meta["num"]), 6)
                cur = e.level
                continue
            if e.meta.get("sub"):
                if cur >= 6:
                    e.kind, e.text = "para", f"**{e.text}**"
                else:
                    e.level = cur + 1
                continue
            if e.meta.get("figure"):
                e.level = min(depth(_owner(e.meta["figure"])) + 1, 6)
                continue
            if e.meta.get("keep_heading") and re.fullmatch(r"References?", e.text.strip()):
                owner = None
                for nxt in els[i + 1:i + 4]:
                    mm = re.match(r"^(\d+(?:\.\d+)+)-\d+\s", nxt.text)
                    if mm:
                        owner = mm.group(1)
                        break
                if owner:
                    e.text = f"References ({owner})"
                    e.level = min(depth(owner) + 1, 6)
                else:
                    e.level = min(cur + 1, 6)
                continue
            e.level = e.level or min(cur + 1, 6)
        elif e.kind == "table" and e.table.caption:
            mm = re.match(r"^Table\s+(\d+(?:\.\d+)*)-\d+", e.table.caption)
            e.meta["caption_level"] = min(depth(mm.group(1)) + 1, 6) if mm else min(cur + 1, 6)


def drop_cover(doc, aux=None):
    S.drop_pages(doc, {1})


FOOTER_LABEL = re.compile(r"^([ivx]+|\d+(?:\.\d+)*-\d+)\s+Revision\s+\d+$")
FOOTER_DOE = re.compile(r"^SUBJECT TO DOE COOPERATIVE AGREEMENT", re.I)


def drop_stray_footers(doc, aux=None):
    """Footer lines that opendataloader typed as body text on some landscape pages (ch1 p58-59)."""
    out = []
    for e in doc.els:
        if e.kind in ("para", "item", "heading"):
            t = e.text.strip()
            m = FOOTER_LABEL.match(t)
            if m:
                doc.page_labels.setdefault(e.page, m.group(1))
                continue
            if FOOTER_DOE.match(t):
                continue
        out.append(e)
    doc.els = out


PREFIX = re.compile(r"^\s*Kemmerer Unit 1 PSAR\b\s*")


def strip_running_header(doc, aux=None):
    """'Kemmerer Unit 1 PSAR Table 4.2-5 …' inside body elements -> 'Table 4.2-5 …' (caption); bare header dropped."""
    out = []
    for e in doc.els:
        if e.kind in ("para", "heading", "caption", "item") and PREFIX.match(e.text):
            rest = PREFIX.sub("", e.text).strip()
            if not rest:
                continue
            e.text = rest
            if S.CAPTION_RE.match(S.SHEET_RE.sub("", rest)):
                e.kind = "caption"
        out.append(e)
    doc.els = out


def keep_chapter_title(e):
    return bool(CHAPTER_TITLE.match(e.text.strip()))


def ensure_title(doc, aux=None):
    """Guarantee a level-1 chapter title as the first heading."""
    for e in doc.els:
        if e.kind == "heading" and CHAPTER_TITLE.match(e.text.strip()):
            return
    for e in doc.els:
        if e.kind in ("para", "hdr") and CHAPTER_TITLE.match(e.text.strip()):
            e.kind, e.meta["keep_heading"] = "heading", True
            return


def steps(chapter):
    base = [
        drop_cover,
        drop_stray_footers,
        S.drop_toc,
        strip_running_header,
        S.hdr_to_captions,
        S.withheld_callouts,
        lambda d, a: figures_step(d, a, render=a.meta.get("render_figures", True)),
        ensure_title,
        S.promote_headings,
        S.insert_subheads,
        lambda d, a: S.demote_other_headings(d, a, keep=keep_chapter_title),
        S.fix_false_items,
        S.join_breaks,
        S.attach_captions_and_merge,
        S.attach_table_notes,
        S.normalise_text,
        S.references_as_items,
        S.normalise_item_levels,
    ]
    try:
        hook = importlib.import_module(f"{__package__}.psar_ch{chapter:02d}")
        base += list(getattr(hook, "STEPS", []))
    except ModuleNotFoundError:
        pass
    base.append(assign_levels)
    return base


def metadata(doc, chapter, aux):
    title = ""
    for e in doc.els:
        if e.kind == "heading" and e.meta.get("chapter_title"):
            title = CHAPTER_TITLE.match(e.text.strip()).group(2)
            break
    tables = [e.table.caption for e in doc.els if e.kind == "table" and e.table.caption]
    return {
        "doc_id": f"Kemmerer Unit 1 PSAR, Chapter {chapter}",
        "title": title,
        "doc_type": "PSAR chapter",
        "issuer": "US SFR Owner, LLC (a wholly owned subsidiary of TerraPower, LLC)",
        "facility": "Kemmerer Power Station Unit 1 (Natrium)",
        "revision": "1",
        "date": "2025",
        "source_pdf": f"references/raw/{doc.stem}.pdf",
        "raw_json": f"references/raw/{doc.stem}.json",
        "pdf_pages": doc.n_pages,
        "tables": tables,
        "figures": doc.meta.get("figures", []),
        "withheld": doc.meta.get("withheld", []),
        "tags": ["reference", "natrium", "psar"],
        "aliases": [f"PSAR Ch. {chapter}", f"Kemmerer Unit 1 PSAR Chapter {chapter}"],
    }
