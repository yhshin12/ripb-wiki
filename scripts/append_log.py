"""append_log.py — append one entry to log.md or internal/log.md (spec §7.5; plan P1).

Usage: python scripts/append_log.py --type ingest --title "NEI 18-04 §3" --item "..." [--item ...]
                                    [--date YYYY-MM-DD] [--root internal]
The file is opened in append mode; earlier bytes are never rewritten. Commit hashes are not recorded.
"""
import argparse
import datetime
import os
import re
import sys

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
TYPES = ("init", "chore", "feat", "fix", "docs", "ingest", "terms", "lint", "audit", "query")


class LogError(Exception):
    pass


def _one_line(value, what):
    if not value or not value.strip():
        raise LogError(f"{what} is empty")
    for bad, name in (("\n", "newline"), ("\r", "CR"), ("﻿", "BOM"), ("�", "U+FFFD")):
        if bad in value:
            raise LogError(f"{what} contains {name}")
    return value.strip()


def entry(date, typ, title, items):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date or ""):
        raise LogError(f"date {date!r} is not YYYY-MM-DD")
    if typ not in TYPES:
        raise LogError(f"type {typ!r} not in {TYPES}")
    if not items:
        raise LogError("at least one --item is required")
    lines = [f"- {_one_line(i, 'item')}\n" for i in items]
    return f"\n## [{date}] {typ} | {_one_line(title, 'title')}\n" + "".join(lines)


def append(vault, root, date, typ, title, items):
    path = os.path.join(vault, root, "log.md") if root else os.path.join(vault, "log.md")
    if not os.path.isfile(path):
        raise LogError(f"{path} does not exist")
    text = entry(date, typ, title, items)
    with open(path, "rb") as f:
        data = f.read()
    with open(path, "a", encoding="utf-8", newline="\n") as f:
        f.write(("" if data.endswith(b"\n") else "\n") + text)
    return path


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--type", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--item", action="append", default=[])
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--root")
    a = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        path = append(VAULT, a.root, a.date, a.type, a.title, a.item)
    except LogError as exc:
        print(f"append_log: error: {exc}", file=sys.stderr)
        return 1
    print(f"append_log: appended to {os.path.relpath(path, VAULT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
