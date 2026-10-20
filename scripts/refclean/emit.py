"""Serialise a Doc to Markdown with YAML frontmatter and page anchors."""
import re

from . import tables as T


def _yaml_scalar(v):
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def frontmatter(meta):
    lines = ["---"]
    for k, v in meta.items():
        if v is None or v == [] or v == "":
            continue
        if isinstance(v, list):
            lines.append(f"{k}:")
            lines.extend(f"  - {_yaml_scalar(x)}" for x in v)
        elif isinstance(v, dict):
            lines.append(f"{k}:")
            lines.extend(f"  {kk}: {_yaml_scalar(vv)}" for kk, vv in v.items())
        else:
            lines.append(f"{k}: {_yaml_scalar(v)}")
    lines.append("---")
    return "\n".join(lines)


def page_label_ranges(labels):
    """{5: '4.1-2', 6: '4.2-1', ...} -> compact 'p4-5: 4.1-1..4.1-2; ...' grouped by label prefix."""
    groups, cur = [], None
    for p in sorted(labels):
        lab = labels[p]
        pre = re.sub(r"-?\d+$", "", lab) or "front"
        if cur and cur["pre"] == pre and p == cur["p1"] + 1:
            cur["p1"], cur["l1"] = p, lab
        else:
            cur = {"pre": pre, "p0": p, "p1": p, "l0": lab, "l1": lab}
            groups.append(cur)
    return "; ".join(f"p{g['p0']}-{g['p1']} = {g['l0']}..{g['l1']}" if g["p0"] != g["p1"] else f"p{g['p0']} = {g['l0']}"
                     for g in groups)


def _block(e):
    """Markdown lines for one non-item element (without surrounding blank lines)."""
    if e.kind == "heading":
        return ["#" * max(1, min(e.level or 2, 6)) + " " + e.text.strip()]
    if e.kind in ("para", "caption", "hdr"):
        return [e.text.strip()] if e.text.strip() else []
    if e.kind == "raw_md":
        return [e.text]
    if e.kind == "table":
        t = e.table
        lines = []
        if t.caption:
            lvl = e.meta.get("caption_level", 0)
            lines += [("#" * lvl + " " + t.caption) if lvl else f"**{t.caption}**", ""]
        lines.append(e.meta.get("rendered") or T.render_md(t))
        if t.notes:
            from .structure import split_notes
            split_notes(t)
            lines.append("")
            for n in t.notes:
                lines.append(n if re.fullmatch(r"Notes?:", n) else f"- {n}")
        return lines
    return []


def render(doc, meta):
    out = [frontmatter(meta), ""]
    cur_page = None
    in_list = False
    for e in doc.els:
        anchor = None
        tpages = e.table.pages if (e.kind == "table" and e.table is not None) else []
        if len(tpages) > 1 and tpages[-1] > tpages[0]:
            # a table merged from several PDF pages: one range anchor covers all of them
            a, b = tpages[0], tpages[-1]
            la, lb = doc.page_labels.get(a), doc.page_labels.get(b)
            anchor = f"<!-- page {a}-{b}{' | ' + la + '..' + lb if la and lb else ''} -->"
            # what follows the table re-announces page b, or citations of it would take the range's first number
            cur_page = None
        elif e.page and e.page != cur_page:
            cur_page = e.page
            lab = doc.page_labels.get(e.page)
            anchor = f"<!-- page {e.page}{' | ' + lab if lab else ''} -->"
        if e.kind == "item":
            if not in_list:
                if anchor:
                    out += [anchor, ""]
                in_list = True
            elif anchor:
                out.append("  " * (e.level + 1) + anchor)   # stays inside the list
            out.append("  " * e.level + "- " + e.text.strip())
            continue
        lines = _block(e)
        if not lines and not anchor:
            continue
        if in_list:
            out.append("")
            in_list = False
        if anchor:
            out += [anchor, ""]
        if lines:
            out += lines + [""]
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.rstrip() + "\n"
