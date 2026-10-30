"""Regression checks: cleaned Markdown vs PDF text (bag of words), residue patterns, heading coverage.

What the numbers mean: `missing_tokens` / `missing_pct` are the PDF-side tokens (lower-cased alphanumeric runs,
inner `.`/`-` kept) that the whole output does not contain, counted as a document-level multiset. The metric is a
regression detector with a known floor (0.0-1.7 % in this corpus, pinned per document in
scripts/refclean/tests/test_*.py), not a proof of completeness. Its blind spots:

1. Header/footer band. `pdf_page_text` keeps only the words between the two rules that `pdfaux.header_footer_band`
   finds, so the PSAR running sheet captions and the 106 ch5 subheading labels printed in the header band are not
   on the PDF side at all: losing them cannot raise `missing` (only the ch5 tests catch that).
2. Table borders near a page edge. A table rule inside the top/bottom 14 % of the page is taken for the band
   boundary (`pdfaux.header_footer_band`), so the first or last row of such a table is cut from the PDF side
   (e.g. the ch1 p17 acronym row).
3. Global sheet credit. `_sheet_credit` adds the repeated header row and running caption of every merged
   multi-page table to the output side once per extra sheet. The credit is document-wide, so it can mask an equal
   number of tokens genuinely lost somewhere else. A profile may add strings to `doc.meta["sheet_credit"]` for page
   furniture it drops on purpose (RG 1.247: the per-page column header row and the repeated caption of the Appendix A
   tables); the same masking caveat applies.
4. Bag of words, not order or attribution. A token moved to the wrong section, a duplicated sentence, a wrong
   number pairing or a scrambled table row is invisible; only the profile tests check placement.
5. Tokenisation. A line-end hyphen split (`risk-` + `significant` vs `risk-significant`) and `<sub>`/`<sup>`
   markup each count as a miss; these inflate `missing` by roughly 100 tokens in RG 1.232 and NEI 18-04.
6. `pages_with_missing_gt3` uses a +-1 page window and is unreliable for profile-rendered `raw_md` tables, whose
   text is credited to the anchor page only (RG Table 1: 52 pages flagged, 116-278 tokens each) and for RG's
   non-monotonic page anchors (30 duplicate anchor lines).
7. `headings_whitelist` / `headings_emitted` are counts, not a set comparison, and are 0/0 for the two documents
   whose profile builds its own heading list (RG 1.232, NEI 18-04).
8. Page 1 and the TOC/LoT/LoF pages are skipped entirely (`skip`), as are pages the caller passes in `skip_pages`.
"""
import collections
import re

import fitz

from . import normalize as N
from .pdfaux import header_footer_band

TOKEN = re.compile(r"[A-Za-z0-9]+(?:[.\-][A-Za-z0-9]+)*")
ANCHOR = re.compile(r"^<!-- page (\d+)(?:-(\d+))?(?: \| [^>]*)? -->$")
RESIDUE = {
    "dot_leader": re.compile(r"(?:\.\s){4,}"),
    "html_entity": re.compile(r"&(?:amp|lt|gt|quot);"),
    "wikilink_open": re.compile(r"(?<!`)\[\["),        # a code span (`[[ ]]`) is not an Obsidian link
    "running_header": re.compile(r"^Kemmerer Unit 1 PSAR\s*$", re.M),
    "doe_footer": re.compile(r"SUBJECT TO DOE COOPERATIVE"),
    "sheet_heading": re.compile(r"^#+ \(Sheet \d+ of \d+\)", re.M),
    "x10_exponent": re.compile(r"\d\s?[x×]\s?10-\d"),
    "br_tag": re.compile(r"<br\s*/?>"),
}


def _tokens(s):
    return [t.lower() for t in TOKEN.findall(s)]


def md_pages(text):
    """{page: text} split on page anchors (text before the first anchor is ignored = frontmatter).

    A range anchor `<!-- page a-b | … -->` (a table merged from several PDF pages) credits every page it spans.
    """
    pages, cur, buf = {}, None, []

    def flush():
        if cur is not None:
            for p in cur:
                pages[p] = pages.get(p, "") + "\n" + "\n".join(buf)

    for line in text.split("\n"):
        m = ANCHOR.match(line.strip())
        if m:
            flush()
            a, b = int(m.group(1)), int(m.group(2) or m.group(1))
            cur, buf = list(range(a, b + 1)), []
            continue
        buf.append(line)
    flush()
    return pages


def pdf_page_text(page):
    top, bot = header_footer_band(page)
    m = page.rotation_matrix
    words = []
    for w in page.get_text("words"):
        r = fitz.Rect(w[:4]) * m
        r.normalize()
        if top <= (r.y0 + r.y1) / 2 <= bot:
            words.append(w[4])
    return " ".join(words)


def _sheet_credit(doc):
    """Tokens the PDF repeats on every sheet of a merged multi-page table (header row, running caption) but the
    cleaned output prints once: credited to the output side so they do not show up as missing."""
    credit = collections.Counter()
    for e in doc.els:
        t = getattr(e, "table", None)
        if e.kind == "table" and t is not None and len(t.pages) > 1:
            rep = len(t.pages) - 1
            hdr = " ".join(" ".join(t.texts(r)) for r in range(min(t.header_rows, t.n_rows)))
            for _ in range(rep):
                credit.update(_tokens(hdr))
                credit.update(_tokens(t.caption))
    for text in doc.meta.get("sheet_credit", []):   # repeated page furniture a profile drops on purpose (RG 1.247)
        credit.update(_tokens(text))
    return credit


def verify(doc, aux, text, skip_pages=None):
    skip = set(skip_pages or []) | set(aux.toc_pages) | {1}
    pdf = fitz.open(doc.pdf_path)
    out_pages = md_pages(text)
    body = text.split("\n---\n", 1)[1] if text.startswith("---\n") and "\n---\n" in text else text
    out_all = collections.Counter(_tokens(body))
    out_all.update(_sheet_credit(doc))
    pdf_all = collections.Counter()
    per_page = {}
    for page in pdf:
        pno = page.number + 1
        if pno in skip:
            continue
        sups = [s.sup for s in aux.sups.get(pno, [])]
        t = N.text_pipeline(pdf_page_text(page), sups, aux.hyphen_map)
        toks = collections.Counter(_tokens(t))
        pdf_all.update(toks)
        win = collections.Counter()
        for q in (pno - 1, pno, pno + 1):
            win.update(_tokens(out_pages.get(q, "")))
        miss = toks - win
        if sum(miss.values()) > 3:
            per_page[pno] = sum(miss.values())
    pdf.close()
    missing = pdf_all - out_all
    extra = out_all - pdf_all
    res = {k: len(p.findall(text)) for k, p in RESIDUE.items()}
    numbered = sum(1 for e in doc.els if e.kind == "heading" and e.meta.get("numbered"))
    summary = {
        "pdf_tokens": sum(pdf_all.values()),
        "missing_tokens": sum(missing.values()),
        "missing_pct": round(100 * sum(missing.values()) / max(1, sum(pdf_all.values())), 2),
        "pages_with_missing_gt3": len(per_page),
        "residue": {k: v for k, v in res.items() if v},
        "headings_whitelist": len(aux.headings),
        "headings_emitted": numbered,
    }
    return {
        "summary": summary,
        "top_missing": missing.most_common(40),
        "top_extra": extra.most_common(20),
        "pages_missing": dict(sorted(per_page.items(), key=lambda kv: -kv[1])[:30]),
    }
