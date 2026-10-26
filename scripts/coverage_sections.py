"""coverage_sections.py — headed sections of a cleaned source that no note cites (skill wiki-ingest §3).

Usage:
  python scripts/coverage_sections.py [--only KEY] [--root internal] [--min-chars 150]
Prints one finding per uncovered section and exits 1 if there is any.

A heading of a cleaned file (`references/<stem>.md`) is covered when a note cites, for the same key,
  - its section number or a descendant (`§3.7.1` covers `3.7.1` and `3.7.1.2`),
  - a table or figure named in the heading (`Table 5.2-1`), or a record ID (`SFR-DC 4`, `DL3-RC1`) in the locator,
  - or a page of the heading when the heading has no section number, or when the citation names an ancestor section.
An unnumbered subheading ("Criterion text", "Application of Loads") takes the number or record of its parent heading.
Headings whose own body is shorter than --min-chars are skipped. Reference lists, acronym lists and contents pages are
skipped everywhere; per-source exclusions (with a reason) are in meta/coverage_exclusions.json:
  {"KEY": [{"heading": "<regex>", "reason": "…"}, {"pages": "30-60", "reason": "…"}]}
Coverage is a lower bound on omissions: a cited section is not checked for completeness.
Sources with `ingest: partial` (on-demand) are skipped unless named with --only.
"""
import argparse
import json
import os
import re
import sys

import citations as C
import notes as N

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
EXCLUSIONS = os.path.join("meta", "coverage_exclusions.json")

HEAD = re.compile(r"^(#{1,6}) (.+?)\s*$")
SECNUM = re.compile(r"^(?:Appendix [A-Z] — )?(\d+(?:\.\d+)+)\b")
TABLE = re.compile(r"\b(Table|Figure) ([0-9A-Z][0-9A-Z.\-]*\d)")
RECORD = re.compile(r"^((?:SFR-DC|ARDC|MHTGR-DC|GDC|PDC) \d+[a-z]?|DL\d-[A-Z]+\d+[a-z]?)\b")
SKIP = re.compile(r"\bReferences\b|\bREFERENCES\b|Acronyms|ACRONYMS|Abbreviations|Table of Contents|"
                  r"TABLE OF CONTENTS|List of (?:Tables|Figures)", re.I)
CITE = re.compile(r"\[([^\[\]\n]+)\]")


def headings(text):
    """[(line, level, title, page, body_chars)] for each Markdown heading; page is the first page of its anchor."""
    out, page = [], None
    for i, line in enumerate(text.split("\n"), 1):
        m = C.ANCHOR.match(line.strip())
        if m:
            page = int(m.group(1))
            continue
        h = HEAD.match(line)
        if h:
            out.append([i, len(h.group(1)), h.group(2).strip(), page, 0])
        elif out and line.strip() and not line.startswith("<!--"):
            out[-1][4] += len(line.strip())
    return [tuple(x) for x in out]


def cited(vault, root=None):
    """{key: [Citation]} over the content notes of the tree (source cards and the terminology map do not count)."""
    out = {}
    for p in N.wiki_notes(vault, root):
        fm, body = N.read_note(p)
        if fm.get("type") in ("source", "map"):
            continue
        for inner in CITE.findall(body):
            c = C.parse_citation(inner)
            if c:
                out.setdefault(c.key, []).append(c)
    return out


def _pages(c):
    return set(range(c.p1, c.p2 + 1)) if c.p1 is not None else set()


def _sec_of(loc):
    m = re.search(r"§(\d+(?:\.\d+)*)", loc)
    return m.group(1) if m else None


def ident(title):
    """(section number or None, [table/figure/record names]) named by a heading."""
    sm = SECNUM.match(title)
    names = [f"{a} {b}" for a, b in TABLE.findall(title)]
    rm = RECORD.match(title)
    if rm:
        names.append(rm.group(1))
    return (sm.group(1) if sm else None), names


def _names_in(names, loc):
    return any(re.search(re.escape(n) + r"(?![\d.\-])", loc) for n in names)


def covered(cites, sec, names, page, ctx=()):
    """ctx: table/record names of enclosing headings; they count only on the heading's own page."""
    for c in cites:
        s = _sec_of(c.locator)
        if sec and s and (s == sec or s.startswith(sec + ".")):
            return True
        if _names_in(names, c.locator):
            return True
        if page is not None and page in _pages(c):
            if ctx and _names_in(ctx, c.locator):
                return True
            if sec is None and not names:
                return True
            if sec and s and sec.startswith(s + "."):
                return True
    return False


def _excluded(rules, title, page):
    for r in rules:
        if "heading" in r and re.search(r["heading"], title):
            return True
        if "pages" in r and page is not None:
            a, _, b = str(r["pages"]).partition("-")
            if int(a) <= page <= int(b or a):
                return True
    return False


def check(vault, root=None, only=None, min_chars=150):
    cards = {k: v for k, v in N.load_cards(vault).items() if v["root"] == root and (only is None or k == only)}
    if only and not cards:
        raise SystemExit(f"coverage_sections: unknown key {only}")
    excl_path = os.path.join(N.tree(vault, root)["root"], EXCLUSIONS)
    excl = {}
    if os.path.isfile(excl_path):
        with open(excl_path, encoding="utf-8") as f:
            excl = json.load(f)
    cites = cited(vault, root)
    findings = []
    for key in sorted(cards):
        if only is None and cards[key]["fm"].get("ingest") == "partial":
            continue    # on-demand source: coverage is reported only when named with --only
        rel = cards[key]["fm"].get("file")
        path = os.path.join(N.tree(vault, root)["root"], rel) if rel else None
        if not path or not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
        stack = []  # [(level, sec, names, ctx)] of enclosing headings; ctx accumulates enclosing names
        for line, level, title, page, chars in headings(text):
            while stack and stack[-1][0] >= level:
                stack.pop()
            sec, names = ident(title)
            ctx = (stack[-1][3] + stack[-1][2]) if stack else []
            if sec is None and not names and stack:   # an unnumbered subheading inherits its parent's identity
                sec, names = stack[-1][1], stack[-1][2]
            stack.append((level, sec, names, ctx))
            if chars < min_chars or SKIP.search(title) or _excluded(excl.get(key, []), title, page):
                continue
            if not covered(cites.get(key, []), sec, names, page, ctx):
                findings.append(N.Finding(f"{rel}", line, "C01",
                                          f"[{key} p.{page}] uncited: {title[:100]} ({chars} chars)", "warning"))
    return findings


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--root")
    ap.add_argument("--min-chars", type=int, default=150)
    a = ap.parse_args(argv)
    findings = check(VAULT, a.root, a.only, a.min_chars)
    for f in findings:
        print(f)
    print(f"coverage_sections: {len(findings)} uncited sections")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
