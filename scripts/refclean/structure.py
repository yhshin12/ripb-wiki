"""Generic structure transforms on Doc.els (each step: f(doc, aux) -> None)."""
import re

from .doc import El
from . import normalize as N
from . import tables as T

TERMINAL = tuple('.:;?!”")')
SUB_TERMINAL = tuple('.?!”")')
LEADER = re.compile(r"(?:\.\s?){4,}")
CAPTION_RE = re.compile(r"^(Table|Figure)\s+(\d+(?:\.\d+)*-\d+[A-Z]?|\d+-\d+)\.?\s+(.*)$")
SHEET_RE = re.compile(r"\s*\((?:Sheet \d+ of \d+|continued)\)\s*$", re.I)
WITHHELD_RE = re.compile(r"\[\[\s*|\s*\]\]\s*SRI|This information is withheld in accordance with 10 CFR 2\.390\.?")
BODY_KINDS = ("para", "item")


def ws(s):
    return " ".join(s.split())


# ---------------------------------------------------------------- noise ----
def drop_pages(doc, pages):
    doc.els = [e for e in doc.els if e.page not in pages]


def drop_toc(doc, aux):
    """Drop TOC/LoT/LoF pages; harvest caption titles."""
    lot, lof = [], []
    keep = []
    for e in doc.els:
        on_toc = e.page in aux.toc_pages
        if on_toc or (e.kind in ("para", "item", "heading") and LEADER.search(e.text)):
            t = LEADER.split(e.text)[0].strip()
            m = CAPTION_RE.match(t)
            if m:
                (lot if m.group(1) == "Table" else lof).append(ws(t))
            continue
        keep.append(e)
    doc.els = keep
    doc.meta["lot"], doc.meta["lof"] = lot, lof


def drop_images(doc, aux=None):
    doc.els = [e for e in doc.els if e.kind != "image"]


# ------------------------------------------------------------- withheld ----
def withheld_callouts(doc, aux=None):
    out, i = [], 0
    els = doc.els
    while i < len(els):
        e = els[i]
        if e.kind in ("para", "item", "heading", "caption", "hdr") and ("[[" in e.text or "This information is withheld" in e.text or re.fullmatch(r"\]\]\s*SRI", e.text.strip())):
            body = WITHHELD_RE.sub(" ", e.text).strip()
            has_sentence = "This information is withheld" in e.text
            if body and not re.fullmatch(r"\]\]\s*SRI", body):
                out.append(El(e.kind, body, e.page, e.bbox, e.font, e.size, e.level, e.list_style, id=e.id, meta=dict(e.meta)))
            if has_sentence:
                sent = re.search(r"This information is withheld in accordance with 10 CFR 2\.390\.?", e.text).group(0)
                out.append(El("raw_md", f"> [!withheld] SRI — {sent}", e.page, meta={"withheld": True}))
            i += 1
            continue
        out.append(e)
        i += 1
    doc.els = out


# ------------------------------------------------------------- headings ----
def _split_at(e, pos, length, new_kind, new_text, meta):
    before = e.text[:pos].strip()
    after = e.text[pos + length:].strip()
    res = []
    if before:
        res.append(El(e.kind, before, e.page, e.bbox, e.font, e.size, e.level, e.list_style, id=e.id, meta=dict(e.meta)))
    res.append(El(new_kind, new_text, e.page, e.bbox, e.font, e.size, 0, id=e.id, meta=meta))
    if after:
        res.append(El("para", after, e.page, e.bbox, e.font, e.size, id=e.id, meta={"split_from": e.id}))
    return res


def _find(text, needle):
    """Find needle in text, whitespace-insensitive. Returns (start, end) in text or None."""
    pat = r"\s+".join(re.escape(tok) for tok in needle.split())
    m = re.search(r"(?<![\w.])" + pat + r"(?![\w])", text)
    return (m.start(), m.end()) if m else None


def promote_headings(doc, aux, refs=None, kinds=("para", "item", "heading", "caption", "hdr")):
    """Turn whitelisted numbered headings into heading elements (split glued text)."""
    refs = aux.headings if refs is None else refs
    els = doc.els
    cursor, unmatched = 0, []
    for ref in refs:
        full = f"{ref.num} {ref.title}"
        found = None
        for i in range(cursor, len(els)):
            e = els[i]
            if e.kind not in kinds or e.meta.get("heading_done"):
                continue
            if abs(e.page - ref.page) > 1 and e.page > ref.page:
                break
            span = _find(e.text, full)
            if span:
                found = (i, span, None)
                break
            # wrapped title continued in the next element
            head = f"{ref.num} " + " ".join(ref.title.split()[:4])
            span = _find(e.text, head)
            if span and i + 1 < len(els):
                rest_needed = ws(full)[len(ws(e.text[span[0]:])) :].strip()
                nxt = els[i + 1]
                if rest_needed and nxt.kind in kinds and ws(nxt.text).startswith(rest_needed[:25]):
                    found = (i, (span[0], len(e.text)), (i + 1, len(rest_needed)))
                    break
        if not found:
            # out-of-order heading (reading-order defect): look back a little on the same page
            for i in range(max(0, cursor - 40), cursor):
                e = els[i]
                if e.kind in kinds and not e.meta.get("heading_done") and e.page == ref.page:
                    span = _find(e.text, full)
                    if span:
                        found = (i, span, None)
                        doc.meta.setdefault("out_of_order_headings", []).append(full)
                        break
        if not found:
            unmatched.append(ref)
            continue
        i, (s, t), cont = found
        e = els[i]
        meta = {"num": ref.num, "heading_done": True, "numbered": True}
        new = _split_at(e, s, t - s, "heading", full, meta)
        for n in new:
            if n.kind == "heading":
                n.level = min(ref.level or len(ref.num.split(".")), 6)
        if cont:
            j, n_chars = cont
            nxt = els[j]
            rest = ws(nxt.text)[n_chars:].strip()
            els[j] = El("para", rest, nxt.page, nxt.bbox, id=nxt.id) if rest else El("drop", "", nxt.page)
        els[i:i + 1] = new
        cursor = max(cursor, i + [k for k, n in enumerate(new) if n.kind == "heading"][0] + 1)
    doc.els = [e for e in els if e.kind != "drop"]
    doc.meta.setdefault("unmatched_headings", []).extend(f"{r.num} {r.title} (p{r.page})" for r in unmatched)


def demote_other_headings(doc, aux=None, keep=None):
    """ODL headings that are not whitelisted sections/captions/References/doc title become paragraphs."""
    keep = keep or (lambda e: False)
    for e in doc.els:
        if e.kind == "heading" and not e.meta.get("numbered") and not e.meta.get("sub") and not e.meta.get("figure"):
            t = e.text.strip()
            if CAPTION_RE.match(t):
                e.kind = "caption"
            elif re.fullmatch(r"References?", t) or keep(e):
                e.meta["keep_heading"] = True
            else:
                e.kind = "para"


def insert_subheads(doc, aux, subs=None):
    """Split unnumbered subheadings (PDF underline / bold-italic) out of glued text, in order."""
    subs = aux.subheads if subs is None else subs
    els = doc.els
    cursor, unmatched = 0, []
    for sub in subs:
        found = None
        for i in range(cursor, len(els)):
            e = els[i]
            if e.page < sub.page - 1:
                continue
            if e.page > sub.page + 1:
                break
            if e.kind not in ("para", "item", "hdr", "heading") or e.meta.get("numbered") or e.meta.get("sub"):
                continue
            span = _find(e.text, sub.text)
            if not span and "(" in sub.text:
                # subscripts inside a parenthesis are extracted differently: match the prefix + its '(...)'
                pre = sub.text.split("(")[0].strip()
                m = re.search(r"(?<![\w.])" + r"\s+".join(map(re.escape, pre.split())) + r"\s*\([^)]{0,20}\)", e.text) if pre else None
                span = (m.start(), m.end()) if m else None
            if span:
                before = e.text[: span[0]].rstrip()
                after = e.text[span[1]:].lstrip()
                # a subheading stands at a line/paragraph boundary: nothing before, or before ends a sentence
                # (a colon/semicolon before it means a run-in list: '… four subsystems: Spent Fuel Pool (SFP), …')
                if before and not before.endswith(SUB_TERMINAL):
                    continue
                if after and not (after[:1].isupper() or after[:1].isdigit() or after[:1] in "“\""):
                    continue
                found = (i, span)
                break
        if not found:
            unmatched.append(sub)
            continue
        i, (s, t) = found
        new = _split_at(els[i], s, t - s, "heading", ws(els[i].text[s:t]), {"sub": True, "heading_done": True})
        els[i:i + 1] = new
        cursor = i + [k for k, n in enumerate(new) if n.kind == "heading"][0] + 1
    doc.meta.setdefault("unmatched_subheads", []).extend(f"{s.text} (p{s.page})" for s in unmatched)


# ----------------------------------------------------- paragraphs/lists ----
CONT_WORDS = {"in", "of", "to", "and", "or", "the", "a", "an", "see", "per", "with", "by", "from", "as", "within",
               "under", "for", "on", "at", "into", "than", "that", "which", "is", "are", "be", "been", "Section",
               "Sections", "Table", "Figure", "Chapter", "Reference"}
CONT_START = re.compile(r"^(?:Section|Sections|Chapter|Chapters|Table|Figure|Reference|\(Reference|\d)")


def _is_continuation(prev_text, next_text, prev_kind):
    p = prev_text.rstrip()
    t = N.strip_bullet(next_text).lstrip()
    if not p or not t or p.endswith(TERMINAL):
        return False
    if t[0].islower():
        return True
    last = re.findall(r"[A-Za-z]+$", p)
    return bool(CONT_START.match(t)) and bool(last) and last[0] in CONT_WORDS


def join_breaks(doc, aux=None):
    """Merge paragraph fragments split by page or column breaks."""
    out = []
    for e in doc.els:
        if e.kind in BODY_KINDS and out:
            j = len(out) - 1
            while j >= 0 and out[j].kind in ("hdr", "image"):
                j -= 1
            prev = out[j] if j >= 0 else None
            bulleted = e.kind == "item" and bool(re.match(r"^\s*[•●▪■◦]", e.text))
            if (prev is not None and prev.kind in BODY_KINDS and not bulleted
                    and _is_continuation(prev.text, e.text, prev.kind)
                    and not (e.kind == "item" and prev.kind == "item" and e.level > prev.level)):
                prev.text = prev.text.rstrip() + " " + N.strip_bullet(e.text).lstrip()
                continue
        out.append(e)
    doc.els = out


def normalise_item_levels(doc, aux=None):
    """List depth relative to the run: first item after a non-item is depth 0; depth grows by at most 1."""
    prev_item = None
    base = 0
    for e in doc.els:
        if e.kind != "item":
            if e.kind not in ("raw_md",) or not e.meta.get("anchor"):
                prev_item = None
            continue
        if prev_item is None:
            base = e.level
            e.level = 0
        else:
            e.level = max(0, min(e.level - base, prev_item.level + 1))
        prev_item = e


NOTE_START = re.compile(r"^(?:Notes?:|\[[a-z0-9]{1,2}\]\s|\*{1,3}\s?\S|\(\d{1,2}\)\s|[a-z]\.\s|Note \d+:|Source:)")


def attach_table_notes(doc, aux=None):
    """Paragraphs/captions right after a table that look like notes become the table's notes."""
    out = []
    for e in doc.els:
        last_tab = out[-1] if out and out[-1].kind == "table" else None
        if last_tab is not None and e.kind in ("para", "caption", "item") and NOTE_START.match(e.text.strip()):
            last_tab.table.notes.append(e.text.strip())
            continue
        out.append(e)
    doc.els = out


def split_notes(t):
    """'Notes: [a] x [b] y' -> ['Notes:', '[a] x', '[b] y']."""
    res = []
    for n in t.notes:
        parts = re.split(r"\s(?=\[[a-z0-9]{1,2}\]\s+[A-Z])", n)
        for p in parts:
            m = re.match(r"^(Notes?:)\s+(\S.*)$", p)
            if m:
                res.extend([m.group(1), m.group(2)])
            else:
                res.append(p)
    t.notes = res


def references_as_items(doc, aux=None):
    """Entries under a References heading ('4.1-1 NEI, …') become list items."""
    in_refs = False
    for e in doc.els:
        if e.kind == "heading":
            in_refs = bool(re.fullmatch(r"References?(?: \(.*\))?", e.text.strip()))
            continue
        if in_refs and e.kind in ("para", "item") and re.match(r"^\d+(?:\.\d+)*-\d+\s", e.text.strip()):
            e.kind, e.level = "item", 0


LIST_LABEL = re.compile(r"^(?:[•●▪■◦o]\s|\(?\d{1,2}[.)]\s|\(?[a-z][.)]\s|\([ivx]+\)\s|[A-Z]\.\s|-\s)")


def fix_false_items(doc, aux, body_x0=None):
    """List items without a printed label that sit at the body margin are paragraphs."""
    for e in doc.els:
        if e.kind != "item":
            continue
        if LIST_LABEL.match(e.text):
            continue
        x0 = e.bbox[0] if e.bbox else None
        margins = {m for m in ((aux.body_x0.get(e.page) if aux and aux.body_x0 else None),
                               (aux.meta.get("body_x0_doc") if aux else None)) if m is not None} or {72}
        if x0 is not None and any(abs(x0 - m) <= 3 for m in margins):
            e.kind = "para"


# ------------------------------------------------------------- captions ----
def hdr_to_captions(doc, aux=None):
    """Header-band texts: 'Table …'/'Figure …' become captions; repeats of the same caption are dropped."""
    out, last, last_hdr = [], None, None
    sub_texts = {ws(s.text) for s in aux.subheads} if aux is not None and getattr(aux, "subheads", None) else set()
    for e in doc.els:
        if e.kind == "hdr":
            base = SHEET_RE.sub("", ws(e.text))
            if base in sub_texts:
                out.append(e)      # a subheading printed in the header band (ch5 PDC labels): keep every one
                continue
            if CAPTION_RE.match(base):
                if last == base:
                    continue
                last = base
                out.append(El("caption", ws(e.text), e.page, e.bbox, id=e.id, meta={"from_hdr": True}))
                continue
            if re.fullmatch(r"\(Sheet \d+ of \d+\)", ws(e.text)):
                continue
            if base == last_hdr and "withheld" not in base.lower():
                continue        # the same running title repeated on every page of a multi-page table
            last_hdr = base     # (withheld markers repeat per figure/page and are collapsed by withheld_callouts)
            out.append(e)
            continue
        if e.kind == "caption" or (e.kind == "heading" and CAPTION_RE.match(SHEET_RE.sub("", ws(e.text)))):
            base = SHEET_RE.sub("", ws(e.text))
            if last == base:
                continue
            last = base
        out.append(e)
    doc.els = out


def attach_captions_and_merge(doc, aux=None):
    """Caption -> following table; consecutive sheets of one table merged; 'Notes' captions -> table notes."""
    out = []
    pending = None
    els = doc.els
    for idx, e in enumerate(els):
        txt = ws(e.text)
        cm = CAPTION_RE.match(SHEET_RE.sub("", txt)) if e.kind in ("caption", "heading", "hdr", "para", "item") else None
        if cm and cm.group(1) == "Table":
            nxt = next((x for x in els[idx + 1:idx + 4] if x.kind not in ("hdr",)), None)
            standalone = e.kind in ("caption", "heading", "hdr") or (
                nxt is not None and nxt.kind == "table" and not txt.endswith(".") and len(txt) < 250)
            if standalone:
                pending = SHEET_RE.sub("", txt)
                continue
        if e.kind in ("caption", "heading", "hdr", "para", "item") and re.fullmatch(r"\(?Sheet \d+ of \d+\)?", txt):
            continue
        if e.kind == "table":
            t = e.table
            cap = pending
            pending = None
            prev_tab = None
            for k in range(len(out) - 1, -1, -1):
                if out[k].kind == "table":
                    prev_tab = out[k]
                    break
                if out[k].kind in ("raw_md",) and out[k].meta.get("anchor"):
                    continue
                break
            later_page = (not prev_tab.table.pages or not t.pages or t.pages[0] > prev_tab.table.pages[-1]) if prev_tab else False
            if prev_tab is not None and ((cap and cap == prev_tab.table.caption)
                                         or (not cap and later_page and T.same_header(prev_tab.table, t))):
                T.append_rows(prev_tab.table, t, drop_header=T.same_header(prev_tab.table, t))
                continue
            t.caption = cap or ""
            out.append(e)
            continue
        if e.kind == "caption" and txt.startswith("Notes") and out and out[-1].kind == "table":
            out[-1].table.notes.append(txt)
            continue
        out.append(e)
    if pending:
        doc.meta.setdefault("orphan_captions", []).append(pending)
    doc.els = out


# ----------------------------------------------------------------- text ----
def normalise_text(doc, aux):
    hmap = aux.hyphen_map if aux else {}
    for e in doc.els:
        sups = [s.sup for s in aux.sups.get(e.page, [])] if aux else None
        if e.kind in ("para", "item", "heading", "caption", "hdr"):
            e.text = N.text_pipeline(e.text, sups, hmap)
            if e.kind == "item":
                e.text = N.strip_bullet(e.text)
        elif e.kind == "table":
            for row in e.table.grid:
                for c in row:
                    if c.text:
                        c.text = "\n".join(N.text_pipeline(x, sups, hmap) for x in c.text.split("\n"))
            e.table.caption = N.text_pipeline(e.table.caption, sups, hmap) if e.table.caption else ""
            e.table.notes = [N.text_pipeline(x, sups, hmap) for x in e.table.notes]
