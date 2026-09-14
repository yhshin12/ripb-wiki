"""lint_wiki.py — structure and terminology lint of wiki notes (spec §5.4 items 6-7, §6.4, §4.2; plan P1, P4, P7, P8).

Usage: python scripts/lint_wiki.py PATH... | --all [--root internal]
File checks (L01-L20) run on each PATH; --all adds the vault-wide checks (L30-L36).
Errors exit 1; warnings alone exit 0.
"""
import argparse
import os
import re
import sys

import notes as N
import terms as T

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
TYPES = {"source", "regulation", "concept", "natrium", "synthesis", "map", "hsfr"}
STATUSES = {"draft", "checked", "reviewed", "disputed", "deprecated"}
INGEST = {"pending", "in_progress", "complete"}
NOTE_FIELDS = ("type", "aliases", "sources", "status", "verified", "term", "tags", "terms_pending")
CARD_FIELDS = ("type", "key", "title", "file", "pdf", "sha256_pdf", "sha256_md", "pdf_pages", "build", "ingest", "units")
SECTIONS = {"full": ["원문 사실", "해설", "관련 문서"], "short": ["관련 문서"],
            "source": ["서지", "구조", "알려진 모순", "관련 문서"]}
FILENAME = re.compile(r"^[A-Za-z0-9]+(?:[_.\-][A-Za-z0-9]+)*\.md$")
H1 = re.compile(r"^# \S.* \(.+\)$")
LINK = re.compile(r"(!?)\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
MDLINK = re.compile(r"(?<!!)\[[^\]\n]*\]\([^)\n]*\)")
PLACEHOLDER = re.compile(r"\bTBD\b|\bTODO\b|\(작성 예정\)|\{[^{}\n]{1,40}\}")
CARD_PENDING_TEXT = ("(인제스트 완료 시 작성)", "(sync 전)")
ABBR = re.compile(r"(?<![A-Za-z0-9_\-])([A-Z]{2,6})s?(?![A-Za-z0-9_\-])")
SENTINEL = ""


class Context:
    def __init__(self, vault):
        self.vault = vault
        self.public = {os.path.basename(p)[:-3]: p for p in N.wiki_notes(vault)}
        self.internal = {os.path.basename(p)[:-3]: p for p in N.wiki_notes(vault, "internal")}
        self.cards = N.load_cards(vault)
        self.terms, self.terms_error = {}, None
        tpath = os.path.join(vault, "wiki", "Terminology.md")
        if os.path.isfile(tpath):
            try:
                self.terms = T.load(tpath)
            except T.TermError as exc:
                self.terms_error = str(exc)
        self.assets = set()
        for d in (os.path.join(vault, "wiki", "assets"), os.path.join(vault, "references", "figures"),
                  os.path.join(vault, "internal", "references", "figures")):
            for _, _, files in os.walk(d):
                self.assets.update(files)


def _body_lines(note):
    return list(enumerate(note.body.split("\n"), note.offset + 1))


def _fields(ctx, note, F):
    fm, typ = note.fm, note.fm.get("type")
    for k in (CARD_FIELDS if typ == "source" else NOTE_FIELDS):
        if k not in fm:
            F(2, "L04", f"frontmatter field {k} missing")
    if typ == "source":
        if fm.get("key") != note.name:
            F(2, "L04", f"key {fm.get('key')!r} differs from the file name")
        if fm.get("ingest") not in INGEST:
            F(2, "L04", f"ingest {fm.get('ingest')!r} not in {sorted(INGEST)}")
        for u in fm.get("units") or []:
            if not isinstance(u, dict) or set(u) - {"unit", "status"} or u.get("status") not in INGEST:
                F(2, "L04", f"bad unit {u!r} (fields: unit, status)")
        return
    st = fm.get("status")
    if st not in STATUSES:
        F(2, "L04", f"status {st!r} not in {sorted(STATUSES)}")
    if st in ("checked", "reviewed") and not fm.get("verified"):
        F(2, "L04", f"status {st} needs a verified date")
    for k in ("aliases", "sources", "tags", "terms_pending"):
        if k in fm and not isinstance(fm[k], list):
            F(2, "L04", f"{k} must be a list")
    for key in (fm.get("sources") if isinstance(fm.get("sources"), list) else []):
        if key not in ctx.cards:
            F(2, "L05", f"source key {key} has no source card")


def _structure(note, F):
    typ = note.fm.get("type")
    lines = _body_lines(note)
    nonblank = [(i, l) for i, l in lines if l.strip()]
    first = nonblank[0][0] if nonblank else note.offset + 1
    if not nonblank or not H1.match(nonblank[0][1]):
        F(first, "L06", "first line must be '# 한국어 제목 (English Title)'")
    elif len(nonblank) < 2 or nonblank[1][1].strip() != "> [!abstract] 요약":
        F(first, "L06", "H1 must be followed by '> [!abstract] 요약'")
    if sum(1 for _, l in lines if l.startswith("# ")) > 1:
        F(first, "L06", "more than one H1")
    kind = "source" if typ == "source" else ("short" if typ in ("synthesis", "map") else "full")
    need = SECTIONS[kind]
    got = [t for t, _, _ in N.sections(note) if t in need]
    missing = [s for s in need if s not in got]
    if missing:
        F(first, "L06", "missing sections: " + ", ".join(missing))
    elif got != need:
        F(first, "L06", "sections out of order: " + " → ".join(need))


def _placeholders(note, F):
    pending_card = note.fm.get("type") == "source" and note.fm.get("ingest") != "complete"
    for i, l in _body_lines(note):
        for t in CARD_PENDING_TEXT:
            if t in l:
                if pending_card:
                    l = l.replace(t, "")
                else:
                    F(i, "L07", f"placeholder {t!r}")
        m = PLACEHOLDER.search(l)
        if m:
            F(i, "L07", f"placeholder {m.group(0)!r}")


def _links(ctx, note, is_internal, F):
    for i, l in _body_lines(note):
        for m in LINK.finditer(l):
            embed, target = m.group(1) == "!", m.group(2).strip()
            if embed:
                if os.path.basename(target) not in ctx.assets:
                    F(i, "L08", f"embedded file not found: {target}")
            elif target in ctx.public:
                continue
            elif target in ctx.internal or target.startswith("HSFR_"):
                if not is_internal:
                    F(i, "L10", f"public note links to internal note [[{target}]]")
                elif target not in ctx.internal:
                    F(i, "L08", f"link target does not exist: [[{target}]]")
            else:
                F(i, "L08", f"link target does not exist: [[{target}]]")
        if MDLINK.search(l):
            F(i, "L09", "Markdown link; use [[wikilink]]")


def _scan_text(line):
    s = T.MARKER.sub(SENTINEL, line)
    s = re.sub(r"`[^`]*`", " ", s)
    s = re.sub(r"\[\[[^\]]*\]\]", " ", s)
    return re.sub(r"\[[^\[\]\n]+\]", " ", s)


def _korean_lines(note):
    out = []
    for title, _, lines in N.sections(note):
        if title in ("", "해설"):
            out += [(i, l) for i, l in lines if not l.startswith("# ")]
    return out


def _terms(ctx, note, F):
    seen, pending = set(), set()
    for i, l in _korean_lines(note):
        for m in T.MARKER.finditer(l):
            tid, term = m.group(1), ctx.terms.get(m.group(1))
            if term is None:
                F(i, "L11", f"term marker {tid} is not in Terminology")
                continue
            if term.state == "용어 아님":
                F(i, "L11", f"term {tid} is 용어 아님; remove the marker")
                continue
            if term.state == "미정":
                pending.add(tid)
            want = T.display(term, tid not in seen)
            seen.add(tid)
            if not l[:m.start()].endswith(want):
                F(i, "L11", f"term {tid}: expected '{want}' before the marker")
                continue
            after = l[m.end():]
            fixed = T.retarget(after, T.final(want))
            if fixed != after:
                F(i, "L11", f"term {tid}: particle after '{want}' should start '{fixed[:2]}'")
        s = _scan_text(l)
        for term in ctx.terms.values():
            for bad in term.forbidden:
                if bad in s:
                    F(i, "L12", f"forbidden form '{bad}' (term {term.id})")
            if term.state == "확정" and term.korean and \
                    re.search(re.escape(term.korean) + r"(?:\([^()]*\))?+(?!" + SENTINEL + ")", s):
                F(i, "L13", f"'{term.korean}' without marker %%t:{term.id}%%", "warning")
        for m in ABBR.finditer(s):
            if s[m.end():m.end() + 1] == SENTINEL:
                continue
            base = m.group(1)
            if any(base in (t.abbr, t.id) for t in ctx.terms.values()):
                F(i, "L13", f"'{base}' without term marker", "warning")
            else:
                F(i, "L14", f"abbreviation '{base}' is not in Terminology")
    listed = note.fm.get("terms_pending") or []
    if isinstance(listed, list) and sorted(listed) != sorted(pending):
        F(2, "L15", f"terms_pending {sorted(listed)} differs from markers {sorted(pending)}; run sync_terms.py --apply",
          "warning")


def lint_file(ctx, path):
    rel = N.relpath(path, ctx.vault)
    out = []

    def F(line, code, msg, level="error"):
        out.append(N.Finding(rel, line, code, msg, level))

    with open(path, "rb") as f:
        raw = f.read()
    if raw.startswith(b"\xef\xbb\xbf"):
        F(1, "L01", "BOM")
    if b"\r" in raw:
        F(1, "L01", "CR line endings")
    if "�" in raw.decode("utf-8", errors="replace"):
        F(1, "L01", "invalid UTF-8 or U+FFFD")
    if not FILENAME.match(os.path.basename(path)):
        F(1, "L03", "file name must be ASCII letters, digits, '_', '.', '-'")
    try:
        note = N.load(path)
    except (N.NoteError, UnicodeDecodeError) as exc:
        F(1, "L02", str(exc))
        return out
    if not note.fm:
        F(1, "L02", "frontmatter missing")
        return out
    if note.fm.get("type") not in TYPES:
        F(2, "L04", f"type {note.fm.get('type')!r} not in {sorted(TYPES)}")
        return out
    _fields(ctx, note, F)
    _structure(note, F)
    _placeholders(note, F)
    _links(ctx, note, rel.startswith("internal/"), F)
    if note.name == "Terminology" and ctx.terms_error:
        F(1, "L20", ctx.terms_error)
    if note.fm.get("type") != "source":
        _terms(ctx, note, F)
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
    ctx = Context(VAULT)
    # without PATHs: the public tree, or internal/ with --root internal (each repo's pre-commit lints its own notes)
    paths = [os.path.abspath(p) for p in a.paths] or N.wiki_notes(VAULT, a.root)
    findings = []
    for p in paths:
        findings += lint_file(ctx, p)
    for f in findings:
        print(f)
    errors = sum(1 for f in findings if f.level == "error")
    print(f"lint_wiki: {len(paths)} notes, {errors} errors, {len(findings) - errors} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
