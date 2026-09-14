"""notes.py — note files shared by the vault scripts: YAML frontmatter + Markdown body (spec §5.1, §8.1).

Every write goes through write_text, which refuses CR, BOM and U+FFFD before touching the file.
"""
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
