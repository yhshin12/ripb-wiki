"""check_absence.py — absence statements ("vault에 없다", "원문에 없다", …) that newer notes may have made stale.

Usage:
  python scripts/check_absence.py [--root internal]            report, exit 1 on any finding
  python scripts/check_absence.py [--root internal] --accept   record every current statement as reviewed

A statement is a line outside 원문 사실 that matches ABSENCE. The ledger (meta/absence_ledger.json, or
internal/meta/absence_ledger.json) keeps the reviewed statements and a hash of every note at the last --accept.
  A1  statement not in the ledger (new or reworded): review it.
  A2  reviewed statement shares a key token with a note that is new or changed since --accept: re-review it.
Key tokens of a line are its term markers (%%t:ID%%), link targets and English words or abbreviations, minus
citations and minus tokens found in more than COMMON of the notes. A shared token weighs ln(notes / notes with it),
twice when it is in the other note's file name or H1; a note is a hit at score >= THRESHOLD * ln 10.
Matching is lexical: a finding is a candidate for re-review, not a judgment, and new evidence worded differently
(DBEHL vs DBHL) is missed, so the semantic lint still reads the new notes. --accept after the review clears it.
"""
import argparse
import datetime
import hashlib
import json
import math
import os
import re
import sys

import notes as N

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)

ABSENCE = re.compile(r"vault에 없|원문에 없|원문에는 없|서술이 없|설명되어 있지 않|설명하지 않|언급하지 않|"
                     r"나와 있지 않|밝히지 않|밝혀져 있지 않|다루지 않|(?<![가-힣])정하지 않|규정하지 않|제시하지 않")
SKIP_SECTIONS = {"원문 사실", "관련 문서"}
CITE = re.compile(r"\[[A-Za-z][A-Za-z0-9_.\-]* [^\[\]\n]*\]")
TERM = re.compile(r"%%t:([A-Za-z0-9_\-]+)%%")
LINK = re.compile(r"\[\[([^\]|#]+)")
WORD = re.compile(r"(?<![A-Za-z0-9_])([A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])(?![A-Za-z0-9_])")
STOP = {"the", "and", "for", "that", "with", "this", "are", "from", "not", "which", "shall", "will", "have",
        "been", "their", "these", "those", "into", "than", "such", "also", "each", "other", "any", "all",
        "vault", "note", "report", "number", "meta", "contradiction"}
COMMON = 0.35
THRESHOLD = 2.0   # score >= THRESHOLD * ln 10: two tokens each in 10 % of the notes, or one in 1 %


def ledger_path(vault, root=None):
    return os.path.join(vault, root, "meta", "absence_ledger.json") if root else \
        os.path.join(vault, "meta", "absence_ledger.json")


def _hash(text):
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def _words(text):
    out = set()
    found = WORD.findall(text)
    for w in found + [part for w in found if "-" in w for part in w.split("-") if len(part) > 1]:
        if w[:-1].isupper() and w.endswith("s") and len(w) > 2:
            w = w[:-1]                                          # DBHLs -> DBHL
        if w.isupper() or any(c.isdigit() for c in w):
            out.add(w)
        else:
            w = w.lower()
            w = w[:-1] if w.endswith("s") and not w.endswith("ss") else w
            if len(w) >= 4 and w not in STOP:
                out.add(w)
    return out


def note_tokens(body):
    """Tokens a note offers as possible new evidence: term markers, link targets, words."""
    return ({"t:" + t for t in TERM.findall(body)} | {"l:" + l.strip() for l in LINK.findall(body)}
            | _words(TERM.sub(" ", body)))


def line_tokens(line):
    text = CITE.sub(" ", line)
    return ({"t:" + t for t in TERM.findall(text)} | {"l:" + l.strip() for l in LINK.findall(text)}
            | _words(LINK.sub(" ", TERM.sub(" ", text))))


def _h1(body):
    return next((l[2:] for l in body.split("\n") if l.startswith("# ")), "")


def statements(note):
    out = []
    for title, _, lines in N.sections(note):
        if title in SKIP_SECTIONS:
            continue
        for i, line in lines:
            text = line.strip()
            if text and not text.startswith("# ") and ABSENCE.search(text):
                out.append((i, text, _hash(note.name + "\n" + text)))
    return out


def load_vault(vault, root=None):
    loaded = {}
    for p in N.wiki_notes(vault, root):
        try:
            loaded[os.path.basename(p)[:-3]] = N.load(p)
        except (N.NoteError, UnicodeDecodeError):
            continue
    return loaded


def read_ledger(path):
    if not os.path.isfile(path):
        return {"accepted": None, "notes": {}, "statements": {}}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def check(vault, root=None):
    notes = load_vault(vault, root)
    ledger = read_ledger(ledger_path(vault, root))
    tokens = {name: note_tokens(n.body) for name, n in notes.items()}
    titles = {name: _words(name.replace("_", " ") + " " + _h1(n.body)) for name, n in notes.items()}
    df = {}
    for ts in tokens.values():
        for t in ts:
            df[t] = df.get(t, 0) + 1
    total = max(1, len(notes))
    weight = {t: math.log(total / c) for t, c in df.items() if c <= COMMON * total}
    fresh = [name for name, n in notes.items() if ledger["notes"].get(name) != _hash(n.body)]
    findings = []
    for name, n in sorted(notes.items()):
        rel = N.relpath(n.path, vault)
        for line, text, sid in statements(n):
            if sid not in ledger["statements"]:
                findings.append(N.Finding(rel, line, "A1", "absence statement not reviewed"))
                continue
            keys = {t for t in line_tokens(text) if t in weight}
            hits = []
            for other in fresh:
                shared = keys & tokens[other] if other != name else set()
                score = sum(weight[t] * (2 if t in titles[other] else 1) for t in shared)
                if score >= THRESHOLD * math.log(10):
                    hits.append((score, other, sorted(shared, key=lambda t: -weight[t])[:4]))
            if hits:
                hits.sort(reverse=True)
                shown = [f"{o} ({', '.join(ts)})" for _, o, ts in hits[:5]]
                findings.append(N.Finding(rel, line, "A2", "new or changed notes share key tokens: " + "; ".join(shown)
                                          + (f"; +{len(hits) - 5} more" if len(hits) > 5 else "")))
    return findings


def accept(vault, root=None):
    notes = load_vault(vault, root)
    ledger = {"accepted": datetime.date.today().isoformat(),
              "notes": {name: _hash(n.body) for name, n in sorted(notes.items())},
              "statements": {sid: {"note": name, "line": line, "text": text}
                             for name, n in sorted(notes.items()) for line, text, sid in statements(n)}}
    path = ledger_path(vault, root)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    N.write_text(path, json.dumps(ledger, ensure_ascii=False, indent=1))
    return len(ledger["statements"])


def main(argv=None):
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--root")
    ap.add_argument("--accept", action="store_true")
    a = ap.parse_args(argv)
    if a.accept:
        print(f"check_absence: {accept(VAULT, a.root)} statements recorded as reviewed")
        return 0
    findings = check(VAULT, a.root)
    for f in findings:
        print(f)
    print(f"check_absence: {len(findings)} statements to review")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
