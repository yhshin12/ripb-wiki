"""build_index.py — regenerate index.md (public) or internal/index.md from note types and summaries (spec §7.5).

Usage: python scripts/build_index.py [--root internal] [--check]
Writes by default (one generated file); --check exits 1 when the file is missing or stale.
Line per note: `- [[Name]] — <first sentence of the 요약 callout>`; source cards whose summary is still the
template text show their title. disputed notes are flagged; deprecated notes move to a separate section.
"""
import argparse
import os
import re
import sys

import notes as N
import terms as T

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
ORDER = [("source", "원문"), ("regulation", "규제"), ("concept", "개념"), ("natrium", "Natrium"),
         ("synthesis", "종합"), ("map", "지도"), ("hsfr", "H-SFR")]
HEADER = "# index\n\n<!-- build_index.py가 생성한다. 손으로 고치지 않는다. -->\n"
TEMPLATE_SUMMARY = "(인제스트 완료 시 작성)"


def index_path(vault, root=None):
    return os.path.join(vault, root, "index.md") if root else os.path.join(vault, "index.md")


def summary(note):
    lines = note.body.split("\n")
    text = ""
    for i, line in enumerate(lines):
        if line.strip() == "> [!abstract] 요약":
            block = []
            for nxt in lines[i + 1:]:
                if not nxt.startswith(">"):
                    break
                block.append(nxt[1:].strip())
            text = T.MARKER.sub("", " ".join(block)).strip()
            break
    if not text or text == TEMPLATE_SUMMARY:
        return str(note.fm.get("title") or "")
    m = re.match(r"^(.+?[.!?])(?:\s|$)", text)
    return m.group(1) if m else text


def render(vault, root=None):
    groups, deprecated = {t: [] for t, _ in ORDER}, []
    for p in N.wiki_notes(vault, root):
        try:
            note = N.load(p)
        except (N.NoteError, UnicodeDecodeError):
            continue
        typ, status = note.fm.get("type"), note.fm.get("status")
        if typ not in groups:
            continue
        line = f"- [[{note.name}]] — {summary(note)}" + (" (disputed)" if status == "disputed" else "")
        (deprecated if status == "deprecated" else groups[typ]).append(line)
    parts = [HEADER]
    for typ, label in ORDER:
        if groups[typ]:
            parts.append(f"\n## {label} ({typ})\n\n" + "\n".join(groups[typ]) + "\n")
    if deprecated:
        parts.append("\n## 대체됨 (deprecated)\n\n" + "\n".join(deprecated) + "\n")
    return "".join(parts)


def write(vault, root=None):
    path = index_path(vault, root)
    N.write_text(path, render(vault, root))
    return path


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    path, text = index_path(VAULT, a.root), render(VAULT, a.root)
    rel = N.relpath(path, VAULT)
    if a.check:
        have = None
        if os.path.isfile(path):
            with open(path, encoding="utf-8", newline="") as f:
                have = f.read()
        print(f"build_index: {rel} {'up to date' if have == text else 'missing or stale'}")
        return 0 if have == text else 1
    N.write_text(path, text)
    print(f"build_index: wrote {rel} ({text.count(chr(10) + '- [[')} notes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
