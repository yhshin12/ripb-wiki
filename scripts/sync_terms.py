"""sync_terms.py — propagate wiki/Terminology.md to the term markers of every note (spec §6.2, §6.4; plan P2, P3, P5).

Usage: python scripts/sync_terms.py [--apply]
Dry-run by default. --apply writes the notes and, when there is no conflict, meta/terms_state.json.
Exit 1 on a table error or a conflict (display text before a marker matches neither the previous nor the current
table; left unchanged for the user).
"""
import argparse
import json
import os
import re
import sys

import notes as N
import terms as T

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
STATE = os.path.join("meta", "terms_state.json")
_JOSA_AHEAD = re.compile(r"^(으로|로|은|는|이|가|을|를|과|와)(?![가-힣])")


def load_state(vault):
    p = os.path.join(vault, STATE)
    if not os.path.isfile(p):
        return {}
    with open(p, encoding="utf-8") as f:
        data = json.load(f)["terms"]
    return {tid: T.Term(tid, d["english"], d["abbr"], d["korean"], d["later"], tuple(d["forbidden"]), "", d["state"], "")
            for tid, d in data.items()}


def terms_changed(vault):
    new = T.snapshot(T.load(os.path.join(vault, "wiki", "Terminology.md")))
    p = os.path.join(vault, STATE)
    old = {}
    if os.path.isfile(p):
        with open(p, encoding="utf-8") as f:
            old = json.load(f)["terms"]
    return sorted(k for k in set(new) | set(old) if new.get(k) != old.get(k))


def plan_note(note, terms, old, rel, report):
    lines, seen = note.body.split("\n"), set()
    for ln, _ in N.korean_lines(note):
        idx = ln - note.offset - 1
        line, pos = lines[idx], 0
        while True:
            m = T.MARKER.search(line, pos)
            if not m:
                break
            tid, head, after = m.group(1), line[:m.start()], line[m.end():]
            term = terms.get(tid)
            if term is None:
                report["conflicts"].append(f"conflict {rel}:{ln} {tid}: not in Terminology")
                pos = m.end()
                continue
            if term.state == "용어 아님":
                line, pos = head + after, len(head)
                continue
            first = tid not in seen
            seen.add(tid)
            cands = sorted({d for t in (old.get(tid), term) if t for d in (T.display(t, True), T.display(t, False)) if d},
                           key=len, reverse=True)
            hit = next((c for c in cands if head.endswith(c)), None)
            if hit is None:
                report["conflicts"].append(f"conflict {rel}:{ln} {tid}: text before the marker matches no display form")
                pos = m.end()
                continue
            want = T.display(term, first)
            fin = T.final(want)
            if fin is None and _JOSA_AHEAD.match(after):
                report["particles"].append(f"check particle {rel}:{ln} {tid}: after '{want}'")
            new_head = head[:len(head) - len(hit)] + want
            line = new_head + m.group(0) + T.retarget(after, fin)
            pos = len(new_head) + len(m.group(0))
        lines[idx] = line
    body, fm = "\n".join(lines), dict(note.fm)
    tid = fm.get("term")
    if isinstance(tid, str) and tid in terms and terms[tid].state == "확정":
        t = terms[tid]
        blines = body.split("\n")
        for i, l in enumerate(blines):
            if l.startswith("# "):
                blines[i] = f"# {t.korean} ({t.english})"
                break
        body = "\n".join(blines)
        prev = old.get(tid).korean if old.get(tid) else None
        aliases = [a for a in (fm.get("aliases") or []) if not (prev and a == prev and a != t.korean)]
        if t.korean not in aliases:
            aliases.append(t.korean)
        fm["aliases"] = aliases
    remaining = N.Note(note.path, fm, body, note.offset)
    pending = sorted({m.group(1) for _, l in N.korean_lines(remaining) for m in T.MARKER.finditer(l)
                      if m.group(1) in terms and terms[m.group(1)].state == "미정"})
    if "terms_pending" in fm or pending:
        fm["terms_pending"] = pending
    return fm, body


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        terms = T.load(os.path.join(VAULT, "wiki", "Terminology.md"))
    except (OSError, T.TermError) as exc:
        print(f"sync_terms: error: {exc}")
        return 1
    old, report, updated = load_state(VAULT), {"conflicts": [], "particles": []}, []
    for p in N.wiki_notes(VAULT) + N.wiki_notes(VAULT, "internal"):
        try:
            note = N.load(p)
        except (N.NoteError, UnicodeDecodeError):
            continue
        if note.fm.get("type") == "source":
            continue
        rel = N.relpath(p, VAULT)
        fm, body = plan_note(note, terms, old, rel, report)
        if fm != note.fm or body != note.body:
            updated.append(rel)
            if a.apply:
                N.write_note(p, fm, body)
    for r in updated:
        print(("updated " if a.apply else "would update ") + r)
    for line in report["conflicts"] + report["particles"]:
        print(line)
    if a.apply and not report["conflicts"]:
        N.write_text(os.path.join(VAULT, STATE),
                     json.dumps({"terms": T.snapshot(terms)}, ensure_ascii=False, indent=1, sort_keys=True))
    mode = "" if a.apply else " (dry-run; --apply to write)"
    print(f"sync_terms: {len(updated)} notes, {len(report['conflicts'])} conflicts, "
          f"{len(report['particles'])} particle checks{mode}")
    return 1 if report["conflicts"] else 0


if __name__ == "__main__":
    sys.exit(main())
