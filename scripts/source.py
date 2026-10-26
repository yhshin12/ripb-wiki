"""source.py — register source documents and maintain their source cards (spec §4.2, appendix B).

Usage (run from the vault root with the pykaeri venv python):
  python scripts/source.py register <pdf in inbox/> --key KEY --title "Title" [--root internal]
  python scripts/source.py adopt KEY [--root internal]        # card for a PDF already in references/raw (DOCS entry)
  python scripts/source.py sync KEY [--root internal] | sync --all   # build fields + structure block from the cleaned file
  python scripts/source.py finish KEY [--root internal]       # sync, then ingest: complete
  python scripts/source.py finish KEY --partial               # on-demand source: ingest: partial
  python scripts/source.py status [--root internal]

Rules: the PDF is only moved, never modified; nothing under references/raw is written except the PDF itself.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sys

from notes import NoteError as SourceError, read_note, write_note  # noqa: F401  (SourceError kept as the CLI name)

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
FORBIDDEN = re.compile(r'[\\/:*?"<>|]')


def dirs(root=None):
    base = VAULT if not root else os.path.join(VAULT, root)
    return {
        "root": base,
        "raw": os.path.join(base, "references", "raw"),
        "refs": os.path.join(base, "references"),
        "wiki": os.path.join(base, "wiki"),
        "inbox": os.path.join(VAULT, "inbox", root) if root else os.path.join(VAULT, "inbox"),
    }


def load_docs():
    if SCRIPTS not in sys.path:
        sys.path.insert(0, SCRIPTS)
    from refclean.profiles import DOCS
    return DOCS


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def safe_stem(key, title):
    t = FORBIDDEN.sub(" ", title)
    t = re.sub(r"\s+", " ", t).strip()
    return f"{key}_{t}"[:150].rstrip()


def rel(path):
    return os.path.relpath(path, VAULT).replace(os.sep, "/")


def card_path(key, root=None):
    return os.path.join(dirs(root)["wiki"], f"{key}.md")


def _existing_card(key):
    for r in (None, "internal"):
        if os.path.exists(card_path(key, r)):
            return card_path(key, r)
    return None


def _all_cards():
    for r in (None, "internal"):
        w = dirs(r)["wiki"]
        if not os.path.isdir(w):
            continue
        for fn in os.listdir(w):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(w, fn)
            try:
                fm, _ = read_note(path)
            except SourceError as exc:
                print(f"warning: skipped {rel(path)}: {exc}", file=sys.stderr)
                continue
            if fm.get("type") == "source":
                yield r, fm


def _new_card(key, title, pdf_path, root):
    path = card_path(key, root)
    taken = _existing_card(key)
    if taken:
        raise SourceError(f"card exists: {rel(taken)}")
    with open(os.path.join(VAULT, "templates", "source_card.md"), encoding="utf-8") as f:
        body = f.read().format(title=title, key=key, pdf=rel(pdf_path))
    fm = {"type": "source", "key": key, "title": title, "file": "", "pdf": rel(pdf_path),
          "sha256_pdf": sha256(pdf_path), "sha256_md": "", "pdf_pages": 0, "build": {},
          "ingest": "pending", "units": []}
    os.makedirs(os.path.dirname(path), exist_ok=True)
    write_note(path, fm, body)
    return path


def register(pdf, key, title, root=None):
    d = dirs(root)
    pdf = os.path.abspath(pdf)
    if not os.path.isfile(pdf):
        raise SourceError(f"not a file: {pdf}")
    digest = sha256(pdf)
    for r in (None, "internal"):
        raw = dirs(r)["raw"]
        for fn in (sorted(os.listdir(raw)) if os.path.isdir(raw) else []):
            p = os.path.join(raw, fn)
            if fn.lower().endswith(".pdf") and os.path.isfile(p) and sha256(p) == digest:
                raise SourceError(f"duplicate of {rel(p)}; left in inbox")
    for _, fm in _all_cards():
        if fm.get("sha256_pdf") == digest:
            raise SourceError(f"duplicate of {fm['key']} ({fm['pdf']}); left in inbox")
    taken = _existing_card(key)
    if taken:
        raise SourceError(f"card exists: {rel(taken)}")
    dest = os.path.join(d["raw"], safe_stem(key, title) + ".pdf")
    if os.path.exists(dest):
        raise SourceError(f"target exists: {rel(dest)}")
    os.makedirs(d["raw"], exist_ok=True)
    shutil.move(pdf, dest)
    try:
        path = _new_card(key, title, dest, root)
    except Exception:
        shutil.move(dest, pdf)
        raise
    print(f"registered {key}: {rel(dest)}\n  card: {rel(path)}\n  next: convert_references.py"
          f"{' --root ' + root if root else ''} --only \"{os.path.basename(dest)[:20]}\" ; add DOCS['{key}'] ; "
          f"clean_references.py --only {key} --verify ; source.py sync {key}")
    return path


def _stem(key, root):
    docs = load_docs()
    if key in docs:
        return docs[key][0]
    fm, _ = read_note(card_path(key, root))
    return os.path.splitext(os.path.basename(fm["pdf"]))[0]


def adopt(key, root=None):
    docs = load_docs()
    if key not in docs:
        raise SourceError(f"{key} is not in DOCS")
    stem = docs[key][0]
    pdf = os.path.join(dirs(root)["raw"], stem + ".pdf")
    if not os.path.isfile(pdf):
        raise SourceError(f"missing PDF: {rel(pdf)}")
    title = stem[len(key) + 1:] if stem.startswith(key + "_") else stem
    path = _new_card(key, title, pdf, root)
    sync(key, root)
    return path


def _sync_block(fm_clean):
    lines = [f"- PDF 쪽 수: {fm_clean.get('pdf_pages', '')}", f"- 인쇄 쪽: {fm_clean.get('page_labels', '')}"]
    for label, k in (("표", "tables"), ("그림", "figures"), ("비공개", "withheld")):
        items = fm_clean.get(k) or []
        lines.append(f"- {label} ({len(items)}):")
        lines += [f"  - {x}" for x in items]
    return "\n".join(lines)


def sync(key, root=None):
    d = dirs(root)
    path = card_path(key, root)
    if not os.path.exists(path):
        raise SourceError(f"no card for {key}")
    fm, body = read_note(path)
    cleaned = os.path.join(d["refs"], _stem(key, root) + ".md")
    if os.path.isfile(cleaned):
        fmc, _ = read_note(cleaned)
        fm["file"] = rel(cleaned)
        fm["sha256_md"] = sha256(cleaned)
        fm["pdf_pages"] = int(fmc.get("pdf_pages") or 0)
        build = {"converter": fmc.get("converter", ""), "cleaned": fmc.get("cleaned", "")}
        vpath = os.path.join(d["raw"], "_verify", f"{key}.json")
        if os.path.isfile(vpath):
            with open(vpath, encoding="utf-8") as f:
                build["missing_pct"] = json.load(f).get("verify", {}).get("summary", {}).get("missing_pct")
        fm["build"] = build
        if "<!-- sync:begin -->" not in body or "<!-- sync:end -->" not in body:
            raise SourceError(f"{rel(path)}: sync markers missing")
        block = _sync_block(fmc)
        body = re.sub(r"<!-- sync:begin -->.*?<!-- sync:end -->",
                      lambda m: "<!-- sync:begin -->\n" + block + "\n<!-- sync:end -->", body, flags=re.S)
    else:
        print(f"{key}: no cleaned file yet ({rel(cleaned)})")
    write_note(path, fm, body)
    return path


def finish(key, root=None, partial=False):
    """Close a source: complete, or partial for an on-demand source whose listed units are all ingested."""
    sync(key, root)
    path = card_path(key, root)
    fm, body = read_note(path)
    if not fm["file"]:
        raise SourceError(f"{key}: no cleaned file; cannot finish")
    if partial and not fm.get("units"):
        raise SourceError(f"{key}: no completed unit; cannot mark partial")
    if any(u.get("status") != "complete" for u in fm.get("units", [])):
        raise SourceError(f"{key}: units not complete")
    fm["ingest"] = "partial" if partial else "complete"
    write_note(path, fm, body)
    print(f"{key}: ingest {fm['ingest']}")
    return path


def status(root=None):
    d = dirs(root)
    rows = []
    wiki = d["wiki"]
    entries = sorted(os.listdir(wiki)) if os.path.isdir(wiki) else []
    for fn in entries:
        path = os.path.join(wiki, fn)
        if not (fn.endswith(".md") and os.path.isfile(path)):
            continue
        try:
            fm, _ = read_note(path)
        except SourceError as exc:
            print(f"warning: skipped {rel(path)}: {exc}", file=sys.stderr)
            continue
        if fm.get("type") != "source":
            continue
        units = fm.get("units", [])
        done = sum(1 for u in units if u.get("status") == "complete")
        cleaned = os.path.join(VAULT, fm["file"]) if fm.get("file") else ""
        if not cleaned:
            sha = "-"
        elif not os.path.isfile(cleaned):
            sha = "MISSING"
        else:
            sha = "ok" if sha256(cleaned) == fm.get("sha256_md") else "CHANGED"
        rows.append((fm["key"], fm.get("ingest", "?"), f"{done}/{len(units)}",
                     "yes" if fm.get("file") else "no", sha))
    inbox = d["inbox"]
    waiting = [f for f in os.listdir(inbox) if f.lower().endswith(".pdf")] if os.path.isdir(inbox) else []
    print(f"{'key':<22}{'ingest':<12}{'units':<8}{'cleaned':<9}sha")
    for r in rows:
        print(f"{r[0]:<22}{r[1]:<12}{r[2]:<8}{r[3]:<9}{r[4]}")
    print(f"inbox waiting: {len(waiting)}" + (": " + ", ".join(waiting) if waiting else ""))
    return rows


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("register"); p.add_argument("pdf"); p.add_argument("--key", required=True); p.add_argument("--title", required=True); p.add_argument("--root")
    p = sub.add_parser("adopt"); p.add_argument("key"); p.add_argument("--root")
    p = sub.add_parser("sync"); p.add_argument("key", nargs="?"); p.add_argument("--all", action="store_true"); p.add_argument("--root")
    p = sub.add_parser("finish"); p.add_argument("key"); p.add_argument("--root"); p.add_argument("--partial", action="store_true")
    p = sub.add_parser("status"); p.add_argument("--root")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        if a.cmd == "register":
            register(a.pdf, a.key, a.title, a.root)
        elif a.cmd == "adopt":
            adopt(a.key, a.root)
        elif a.cmd == "sync":
            if a.key:
                sync(a.key, a.root)
            elif a.all:
                for k, r in [(fm["key"], r) for r, fm in _all_cards()]:
                    sync(k, r)
            else:
                raise SourceError("sync: give KEY or --all")
        elif a.cmd == "finish":
            finish(a.key, a.root, a.partial)
        elif a.cmd == "status":
            status(a.root)
    except SourceError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
