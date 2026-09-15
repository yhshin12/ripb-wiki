"""verify_quotes.py — checks of the 원문 사실 section against the cleaned sources (spec §5.4 items 1-5; plan P6).

V1 every list item / table row carries a trailing citation; the section holds only items and rows; tables end in 출처
V2 the source key has a card and a cleaned file; p.N lies in 1..pdf_pages; paged sources need p.N
V3 each quoted fragment (split at ... / …, at least MIN_WORDS words) occurs in the cited pages ±1 after normalisation
V4 each table value occurs in the cited pages ±1
V5 every number in 해설 also occurs in 원문 사실

Usage: python scripts/verify_quotes.py PATH... | --all [--root internal]
"""
import argparse
import os
import re
import sys

import citations as C
import notes as N

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
FACTS, COMMENTARY = "원문 사실", "해설"
MIN_WORDS = 3


class Sources:
    """Cleaned texts per source key, normalised per page, loaded once."""

    def __init__(self, vault, cards):
        self.vault, self.cards, self._cache = vault, cards, {}

    def get(self, key):
        if key not in self._cache:
            card = self.cards.get(key)
            rel = (card or {}).get("fm", {}).get("file") or ""
            path = os.path.join(self.vault, rel)
            if not card or not rel or not os.path.isfile(path):
                self._cache[key] = None
            else:
                with open(path, encoding="utf-8") as f:
                    text = f.read()
                body = text.split("\n---\n", 1)[1] if text.startswith("---\n") and "\n---\n" in text else text
                pages = {p: C.normalize(t) for p, t in C.page_map(text).items()}
                self._cache[key] = {"pages": pages, "all": C.normalize(body), "paged": bool(pages),
                                    "n": int(card["fm"].get("pdf_pages") or 0)}
        return self._cache[key]

    def window(self, cite):
        s = self.get(cite.key)
        if cite.p1 is None:
            return s["all"]
        return " ".join(s["pages"].get(p, "") for p in range(cite.p1 - 1, cite.p2 + 2))


def _cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _check_cites(src, cites, rel, ln):
    out, ok = [], []
    for c in cites:
        s = src.get(c.key)
        if c.key not in src.cards:
            out.append(N.Finding(rel, ln, "V2", f"unknown source key {c.key}"))
        elif s is None:
            out.append(N.Finding(rel, ln, "V2", f"{c.key}: cleaned file missing"))
        elif c.p1 is None and s["paged"]:
            out.append(N.Finding(rel, ln, "V2", f"{c.raw}: page required (source has page anchors)"))
        elif c.p1 is not None and not (1 <= c.p1 <= c.p2 <= s["n"]):
            out.append(N.Finding(rel, ln, "V2", f"{c.raw}: page outside 1-{s['n']}"))
        else:
            ok.append(c)
    return out, ok


def _item(ln, text, src, rel, fact_text):
    body, cites = C.split_trailing(text)
    if not cites:
        return [N.Finding(rel, ln, "V1", "item has no citation")]
    fact_text.append(body)
    out, ok = _check_cites(src, cites, rel, ln)
    if not ok:
        return out
    qs = C.quotes(body)
    if not qs:
        return out + [N.Finding(rel, ln, "V3", "item has no quoted source text")]
    for q in qs:
        for frag in C.fragments(q):
            nf = C.normalize(frag)
            if len(nf.split()) < MIN_WORDS:
                out.append(N.Finding(rel, ln, "V3", f"fragment shorter than {MIN_WORDS} words: \"{frag}\""))
            elif not any(nf in src.window(c) for c in ok):
                out.append(N.Finding(rel, ln, "V3", f"not found at cited pages (±1): \"{frag[:80]}\""))
    return out


def _table(block, src, rel, fact_text):
    head = _cells(block[0][1])
    if head[-1] != "출처":
        return [N.Finding(rel, block[0][0], "V1", "원문 사실 table needs a last column 출처")]
    out = []
    for ln, line in block[2:]:
        cells = _cells(line)
        if len(cells) != len(head):
            out.append(N.Finding(rel, ln, "V1", f"row has {len(cells)} cells, header has {len(head)}"))
            continue
        _, cites = C.split_trailing(cells[-1])
        if not cites:
            out.append(N.Finding(rel, ln, "V1", "row has no citation"))
            continue
        fact_text.extend(cells[:-1])
        errs, ok = _check_cites(src, cites, rel, ln)
        out += errs
        for cell in (cells[:-1] if ok else []):
            nc = C.normalize(cell)
            if nc and not any(nc in src.window(c) for c in ok):
                out.append(N.Finding(rel, ln, "V4", f"table value not found at cited pages (±1): \"{cell[:80]}\""))
    return out


def verify_note(vault, path, src):
    note = N.load(path)
    rel = N.relpath(path, vault)
    secs = {title: lines for title, _, lines in N.sections(note)}
    if FACTS not in secs:
        return []
    out, fact_text, rows, i = [], [], secs[FACTS], 0
    while i < len(rows):
        ln, line = rows[i]
        s = line.strip()
        if not s:
            i += 1
        elif s.startswith("|"):
            block = []
            while i < len(rows) and rows[i][1].strip().startswith("|"):
                block.append(rows[i])
                i += 1
            out += _table(block, src, rel, fact_text)
        else:
            if re.match(r"^\s*- ", line):
                out += _item(ln, s[2:], src, rel, fact_text)
            elif re.match(r"^!\[\[[^\[\]]+\]\]$", s):
                pass  # figure embed from figures/ (CLAUDE.md §4); the caption item above carries the citation
            else:
                out.append(N.Finding(rel, ln, "V1", "원문 사실 holds list items and table rows only"))
            i += 1
    fact_numbers = C.numbers("\n".join(fact_text))
    for ln, line in secs.get(COMMENTARY, []):
        for n in sorted(C.numbers(line) - fact_numbers):
            out.append(N.Finding(rel, ln, "V5", f"number {n} in 해설 is not in 원문 사실"))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--root")
    a = ap.parse_args(argv)
    if not a.paths and not a.all:
        ap.error("give PATH... or --all")
    sys.stdout.reconfigure(encoding="utf-8")
    src = Sources(VAULT, N.load_cards(VAULT))
    paths = [os.path.abspath(p) for p in a.paths] or N.wiki_notes(VAULT, a.root)
    findings = []
    for p in paths:
        try:
            findings += verify_note(VAULT, p, src)
        except (N.NoteError, UnicodeDecodeError) as exc:
            findings.append(N.Finding(N.relpath(p, VAULT), 1, "V0", str(exc)))
    for f in findings:
        print(f)
    errors = sum(1 for f in findings if f.level == "error")
    print(f"verify_quotes: {len(paths)} notes, {errors} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
