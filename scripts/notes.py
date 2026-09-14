"""notes.py — note files shared by the vault scripts: YAML frontmatter + Markdown body (spec §5.1, §8.1).

Every write goes through write_text, which refuses CR, BOM and U+FFFD before touching the file.
"""
import os
from dataclasses import dataclass

import yaml


class NoteError(Exception):
    pass


def read_note(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---\n"):
        return {}, text
    try:
        _, fm_text, body = text.split("---\n", 2)
    except ValueError as exc:
        raise NoteError(f"{path}: bad frontmatter ({type(exc).__name__})") from exc
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as exc:
        raise NoteError(f"{path}: bad frontmatter ({type(exc).__name__})") from exc
    if fm is not None and not isinstance(fm, dict):
        raise NoteError(f"{path}: bad frontmatter (not a mapping)")
    return (fm or {}), body.lstrip("\n")


def dump_note(fm, body):
    return "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---\n\n" + body


def write_text(path, text):
    for bad, name in (("\r", "CR"), ("﻿", "BOM"), ("�", "U+FFFD")):
        if bad in text:
            raise NoteError(f"{path}: {name} in text; not written")
    if not text.endswith("\n"):
        text += "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def write_note(path, fm, body):
    write_text(path, dump_note(fm, body))


@dataclass
class Note:
    path: str
    fm: dict
    body: str
    offset: int

    @property
    def name(self):
        return os.path.splitext(os.path.basename(self.path))[0]


def load(path):
    fm, body = read_note(path)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return Note(path, fm, body, text.count("\n", 0, len(text) - len(body)))


def sections(note):
    """[(H2 title, line of the title, [(line, text), ...])]; the block before the first H2 has title ''."""
    out = [("", note.offset + 1, [])]
    for i, line in enumerate(note.body.split("\n"), note.offset + 1):
        if line.startswith("## "):
            out.append((line[3:].strip(), i, []))
        else:
            out[-1][2].append((i, line))
    return out


def tree(vault, root=None):
    base = os.path.join(vault, root) if root else vault
    return {"root": base, "wiki": os.path.join(base, "wiki"), "refs": os.path.join(base, "references"),
            "raw": os.path.join(base, "references", "raw")}


def wiki_notes(vault, root=None):
    w = tree(vault, root)["wiki"]
    if not os.path.isdir(w):
        return []
    return [os.path.join(w, f) for f in sorted(os.listdir(w))
            if f.endswith(".md") and os.path.isfile(os.path.join(w, f))]


def load_cards(vault):
    cards = {}
    for r in (None, "internal"):
        for p in wiki_notes(vault, r):
            try:
                fm, _ = read_note(p)
            except NoteError:
                continue
            if fm.get("type") == "source" and fm.get("key"):
                cards[str(fm["key"])] = {"root": r, "fm": fm, "path": p}
    return cards


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    code: str
    message: str
    level: str = "error"

    def __str__(self):
        return f"{self.path}:{self.line}: {self.level} {self.code} {self.message}"


def relpath(path, vault):
    return os.path.relpath(path, vault).replace(os.sep, "/")
