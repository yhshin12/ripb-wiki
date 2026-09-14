"""source.py — register source documents and maintain their source cards (spec §4.2, appendix B).

Usage (run from the vault root with the pykaeri venv python):
  python scripts/source.py register <pdf in inbox/> --key KEY --title "Title" [--root internal]
  python scripts/source.py adopt KEY [--root internal]        # card for a PDF already in references/raw (DOCS entry)
  python scripts/source.py sync  (KEY | --all) [--root internal]   # build fields + structure block from the cleaned file
  python scripts/source.py finish KEY [--root internal]       # sync, then ingest: complete
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

import yaml

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORBIDDEN = re.compile(r'[\\/:*?"<>|]')


class SourceError(Exception):
    pass


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
    sys.path.insert(0, os.path.join(VAULT, "scripts"))
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


def read_note(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---\n"):
        return {}, text
    _, fm, body = text.split("---\n", 2)
    return (yaml.safe_load(fm) or {}), body.lstrip("\n")


def write_note(path, fm, body):
    text = "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---\n\n" + body
    if not text.endswith("\n"):
        text += "\n"
    assert "\r" not in text
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def card_path(key, root=None):
    return os.path.join(dirs(root)["wiki"], f"{key}.md")


def _all_cards():
    for r in (None, "internal"):
        w = dirs(r)["wiki"]
        if not os.path.isdir(w):
            continue
        for fn in os.listdir(w):
            if fn.endswith(".md"):
                fm, _ = read_note(os.path.join(w, fn))
                if fm.get("type") == "source":
                    yield fm


def _new_card(key, title, pdf_path, root):
    path = card_path(key, root)
    if os.path.exists(path):
        raise SourceError(f"card exists: {rel(path)}")
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
    for fm in _all_cards():
        if fm.get("sha256_pdf") == digest:
            raise SourceError(f"duplicate of {fm['key']} ({fm['pdf']}); left in inbox")
    if os.path.exists(card_path(key, root)):
        raise SourceError(f"card exists: {rel(card_path(key, root))}")
    dest = os.path.join(d["raw"], safe_stem(key, title) + ".pdf")
    if os.path.exists(dest):
        raise SourceError(f"target exists: {rel(dest)}")
    os.makedirs(d["raw"], exist_ok=True)
    shutil.move(pdf, dest)
    path = _new_card(key, title, dest, root)
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
        body = re.sub(r"<!-- sync:begin -->.*?<!-- sync:end -->",
                      "<!-- sync:begin -->\n" + _sync_block(fmc) + "\n<!-- sync:end -->", body, flags=re.S)
    else:
        print(f"{key}: no cleaned file yet ({rel(cleaned)})")
    write_note(path, fm, body)
    return path


def finish(key, root=None):
    sync(key, root)
    path = card_path(key, root)
    fm, body = read_note(path)
    if not fm["file"]:
        raise SourceError(f"{key}: no cleaned file; cannot finish")
    if any(u.get("status") != "complete" for u in fm.get("units", [])):
        raise SourceError(f"{key}: units not complete")
    fm["ingest"] = "complete"
    write_note(path, fm, body)
    print(f"{key}: ingest complete")
    return path


def status(root=None):
    d = dirs(root)
    rows = []
    wiki = d["wiki"]
    for fn in sorted(os.listdir(wiki)) if os.path.isdir(wiki) else []:
        fm, _ = read_note(os.path.join(wiki, fn))
        if fm.get("type") != "source":
            continue
        units = fm.get("units", [])
        done = sum(1 for u in units if u.get("status") == "complete")
        cleaned = os.path.join(VAULT, fm["file"]) if fm.get("file") else ""
        sha_ok = bool(cleaned) and os.path.isfile(cleaned) and sha256(cleaned) == fm.get("sha256_md")
        rows.append((fm["key"], fm.get("ingest", "?"), f"{done}/{len(units)}", "yes" if fm.get("file") else "no",
                     "ok" if sha_ok else ("-" if not cleaned else "CHANGED")))
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
    p = sub.add_parser("finish"); p.add_argument("key"); p.add_argument("--root")
    p = sub.add_parser("status"); p.add_argument("--root")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        if a.cmd == "register":
            register(a.pdf, a.key, a.title, a.root)
        elif a.cmd == "adopt":
            adopt(a.key, a.root)
        elif a.cmd == "sync":
            keys = [a.key] if a.key else [fm["key"] for fm in _all_cards()] if a.all else []
            if not keys:
                raise SourceError("sync: give KEY or --all")
            for k in keys:
                sync(k, a.root)
        elif a.cmd == "finish":
            finish(a.key, a.root)
        elif a.cmd == "status":
            status(a.root)
    except SourceError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
