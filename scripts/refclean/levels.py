"""Heading levels for numbered-section documents (shared by the psar and generic profiles)."""
import re

CHAPTER_TITLE = re.compile(r"^Chapter\s+(\d+)\s+(.+)$")


def depth(num):
    return len(num.split("."))


def _owner(num_with_dash):
    """'4.2-7' -> '4.2'; '7.2.3-1' -> '7.2.3'."""
    return num_with_dash.rsplit("-", 1)[0]


def assign_levels(doc, aux=None):
    cur = 1
    els = doc.els
    for i, e in enumerate(els):
        if e.kind == "heading":
            m = CHAPTER_TITLE.match(e.text.strip())
            if m and not e.meta.get("numbered"):
                e.level = 1
                e.meta["chapter_title"] = True
                cur = 1
                continue
            if e.meta.get("numbered"):
                e.level = min(depth(e.meta["num"]), 6)
                cur = e.level
                continue
            if e.meta.get("sub"):
                if cur >= 6:
                    e.kind, e.text = "para", f"**{e.text}**"
                else:
                    e.level = cur + 1
                continue
            if e.meta.get("figure"):
                e.level = min(depth(_owner(e.meta["figure"])) + 1, 6)
                continue
            if e.meta.get("keep_heading") and re.fullmatch(r"References?", e.text.strip()):
                owner = None
                for nxt in els[i + 1:i + 4]:
                    mm = re.match(r"^(\d+(?:\.\d+)+)-\d+\s", nxt.text)
                    if mm:
                        owner = mm.group(1)
                        break
                if owner:
                    e.text = f"References ({owner})"
                    e.level = min(depth(owner) + 1, 6)
                else:
                    e.level = min(cur + 1, 6)
                continue
            e.level = e.level or min(cur + 1, 6)
        elif e.kind == "table" and e.table.caption:
            mm = re.match(r"^Table\s+(\d+(?:\.\d+)*)-\d+", e.table.caption)
            e.meta["caption_level"] = min(depth(mm.group(1)) + 1, 6) if mm else min(cur + 1, 6)
