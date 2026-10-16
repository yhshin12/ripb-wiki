"""leak_guard.py — refuse public commits that name internal documents (spec §3.3, §8.2; ruling R14; plan P10).

The name list is built at run time from internal/ (never stored in the public repo):
file stems under internal/references and internal/references/raw; stem, key, title, H1 and aliases of
internal/wiki notes; stem, title and H1 of internal/meetings notes. Names are case-folded with whitespace
collapsed; names shorter than MIN_LEN characters are ignored. internal/leak_allow.txt (private repo) lists
false positives; RIPB_LEAK_EXTRA (';'-separated) adds probe names for smoke tests.

Usage:
  python scripts/leak_guard.py --staged          # pre-commit: added lines and paths of staged files
  python scripts/leak_guard.py --message FILE    # commit-msg
  python scripts/leak_guard.py --files PATH...   # whole files
"""
import argparse
import os
import re
import subprocess
import sys

from notes import NoteError, read_note

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
MIN_LEN = 8


def norm(s):
    return re.sub(r"\s+", " ", str(s)).strip().casefold()


def _h1(body):
    for line in body.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def internal_names(vault):
    base = os.path.join(vault, "internal")
    raw = set()
    for sub in ("references", os.path.join("references", "raw")):
        d = os.path.join(base, sub)
        for fn in (os.listdir(d) if os.path.isdir(d) else []):
            if os.path.isfile(os.path.join(d, fn)) and not fn.startswith("_"):   # _conversion.json etc.
                raw.add(os.path.splitext(fn)[0])
    for sub in ("wiki", "meetings"):
        d = os.path.join(base, sub)
        for fn in (os.listdir(d) if os.path.isdir(d) else []):
            p = os.path.join(d, fn)
            if not (fn.endswith(".md") and os.path.isfile(p)):
                continue
            raw.add(fn[:-3])
            try:
                fm, body = read_note(p)
            except NoteError:
                with open(p, encoding="utf-8", errors="replace") as f:
                    fm, body = {}, f.read()
            raw.update(str(fm[k]) for k in ("key", "title") if fm.get(k))
            raw.update(str(a) for a in (fm.get("aliases") or []))
            if _h1(body):
                raw.add(_h1(body))
    raw.update(x for x in os.environ.get("RIPB_LEAK_EXTRA", "").split(";") if x)
    allow = set()
    allow_path = os.path.join(base, "leak_allow.txt")
    if os.path.isfile(allow_path):
        with open(allow_path, encoding="utf-8") as f:
            allow = {norm(line) for line in f if line.strip()}
    return {n for n in map(norm, raw) if len(n) >= MIN_LEN and n not in allow}


def scan(items, names):
    hits = []
    for where, text in items:
        low = norm(text)
        hits.extend((where, n) for n in sorted(names) if n in low)
    return hits


def staged_added_lines(repo):
    git = ["git", "-C", repo, "-c", "core.quotepath=false"]
    paths = subprocess.run(git + ["diff", "--cached", "--name-only", "-z", "--diff-filter=ACMR"],
                           capture_output=True, check=True).stdout.decode("utf-8").split("\0")
    items = [(p, p) for p in paths if p]
    diff = subprocess.run(git + ["diff", "--cached", "--no-color", "--no-ext-diff", "-U0", "--diff-filter=ACMR"],
                          capture_output=True, check=True).stdout.decode("utf-8", errors="replace")
    path, lineno = None, 0
    for line in diff.split("\n"):
        if line.startswith("+++ "):
            # git appends a TAB to a path that contains a space
            path = line[6:].rstrip("\t") if line.startswith("+++ b/") else None
        elif line.startswith("@@"):
            m = re.search(r"\+(\d+)", line)
            lineno = int(m.group(1)) if m else 0
        elif line.startswith("+") and path:
            items.append((f"{path}:{lineno}", line[1:]))
            lineno += 1
    return items


def main(argv=None):
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--staged", action="store_true")
    g.add_argument("--message")
    g.add_argument("--files", nargs="+")
    a = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    if not os.path.isdir(os.path.join(VAULT, "internal")):
        print("leak_guard: internal/ not present; nothing to check")
        return 0
    names = internal_names(VAULT)
    if a.staged:
        items = staged_added_lines(VAULT)
    elif a.message:
        with open(a.message, encoding="utf-8", errors="replace") as f:
            items = [("commit message", f.read())]
    else:
        items = []
        for p in a.files:
            with open(p, encoding="utf-8", errors="replace") as f:
                items += [(f"{p}:{i}", t) for i, t in enumerate(f.read().split("\n"), 1)]
    hits = scan(items, names)
    for where, n in hits:
        print(f"leak_guard: {where}: internal name \"{n}\"")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
