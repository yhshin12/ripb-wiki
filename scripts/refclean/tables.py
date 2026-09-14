"""Table model built from opendataloader JSON cells (with spans), plus Markdown/record rendering."""
import re
from dataclasses import dataclass, field


@dataclass
class Cell:
    text: str
    row: int
    col: int
    rowspan: int = 1
    colspan: int = 1
    bold: bool = False
    filled: bool = False


@dataclass
class Table:
    grid: list
    header_rows: int = 1
    page: int = 0
    pages: list = field(default_factory=list)
    caption: str = ""
    notes: list = field(default_factory=list)
    id: int = 0
    meta: dict = field(default_factory=dict)

    @property
    def n_rows(self):
        return len(self.grid)

    @property
    def n_cols(self):
        return len(self.grid[0]) if self.grid else 0

    def texts(self, r):
        return [c.text for c in self.grid[r]]


def _cell_text(cell):
    """All text of a cell in pre-order (paragraphs, list items, and anything nested under them)."""
    parts, bold = [], []

    def walk(node):
        t = (node.get("content") or "").strip()
        if t:
            parts.append(t)
            bold.append("Bold" in (node.get("font") or ""))
        for kid in node.get("kids", []) or []:
            walk(kid)
        for it in node.get("list items", []) or []:
            walk(it)

    for kid in cell.get("kids", []) or []:
        walk(kid)
    return "\n".join(parts), bool(bold) and all(bold)


def from_odl(node):
    n_r = int(node.get("number of rows") or len(node.get("rows", [])))
    n_c = int(node.get("number of columns") or 0)
    if not n_c:
        n_c = max((len(r.get("cells", [])) for r in node.get("rows", [])), default=0)
    grid = [[None] * n_c for _ in range(n_r)]
    overlaps = []
    for row in node.get("rows", []):
        for cell in row.get("cells", []):
            r = int(cell.get("row number", 1)) - 1
            c = int(cell.get("column number", 1)) - 1
            rs = max(1, int(cell.get("row span", 1)))
            cs = max(1, int(cell.get("column span", 1)))
            text, bold = _cell_text(cell)
            for i in range(r, min(r + rs, n_r)):
                for j in range(c, min(c + cs, n_c)):
                    old = grid[i][j]
                    if old is not None and old.text:
                        # two cells claim the same grid position (a malformed span in the converter output):
                        # keep the first and record the conflict so the build report shows the loss
                        if old.text != text:
                            overlaps.append({"row": i + 1, "col": j + 1, "kept": old.text[:60], "dropped": text[:60]})
                        continue
                    grid[i][j] = Cell(text, i, j, rs, cs, bold, filled=(i, j) != (r, c))
    for i in range(n_r):
        for j in range(n_c):
            if grid[i][j] is None:
                grid[i][j] = Cell("", i, j)
    pages = sorted({c.get("page number", node.get("page number", 0))
                    for row in node.get("rows", []) for c in row.get("cells", [])} or {node.get("page number", 0)})
    t = Table(grid=grid, page=node.get("page number", 0), pages=pages, id=node.get("id", 0))
    if overlaps:
        t.meta["overlaps"] = overlaps
    t.header_rows = detect_header(t)
    return t


def overlap_warnings(doc):
    """`doc.meta['table_warnings']` entries for every table whose ODL cells claimed the same grid position."""
    out = []
    for e in doc.els:
        t = getattr(e, "table", None)
        for ov in (t.meta.get("overlaps") if t is not None else None) or []:
            out.append(f"table id={t.id} p{t.page} r{ov['row']}c{ov['col']}: kept {ov['kept']!r}, "
                       f"dropped {ov['dropped']!r} (overlapping ODL cell spans)")
    if out:
        doc.meta.setdefault("table_warnings", []).extend(out)
    return out


def detect_header(t):
    """Leading rows whose non-empty cells are all bold; at least 1."""
    h = 0
    for r in range(t.n_rows):
        cells = [c for c in t.grid[r] if c.text]
        if cells and all(c.bold for c in cells):
            h += 1
        else:
            break
    return max(1, min(h, t.n_rows - 1 if t.n_rows > 1 else 1))


ENUM = re.compile(r"^(?:\(?\d{1,2}[.)](?!\d)|\([a-z]\)|[a-z]\)|[A-Z]\.\d+(?!\d)|[•●▪o]\s|\d+(?:\.\d+)+$)")
DASH_ITEM = re.compile(r"^-\s")


def cell_md(text):
    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
    out = ""
    for i, ln in enumerate(lines):
        if i == 0:
            out = ln
        elif ENUM.match(ln) or (DASH_ITEM.match(ln) and (lines[i - 1].endswith(":") or DASH_ITEM.match(lines[i - 1]))):
            out += "; " + ln
        else:
            out += " " + ln
    return out.replace("|", "\\|")


def header_names(t):
    names = []
    for j in range(t.n_cols):
        parts = []
        for i in range(t.header_rows):
            s = cell_md(t.grid[i][j].text)
            if s and (not parts or parts[-1] != s):
                parts.append(s)
        names.append(": ".join(parts))
    return names


def render_md(t):
    names = header_names(t)
    if not any(names):
        names = [f"Column {j + 1}" for j in range(t.n_cols)]
    lines = ["| " + " | ".join(names) + " |", "|" + "---|" * t.n_cols]
    for r in range(t.header_rows, t.n_rows):
        vals = [cell_md(c.text) for c in t.grid[r]]
        if not any(vals):
            continue
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines)


def same_header(a, b):
    return a.n_cols == b.n_cols and header_names(a) == header_names(b)


def append_rows(a, b, drop_header=True):
    """Append table b's body rows to a (b's header dropped when it repeats a's)."""
    start = b.header_rows if drop_header else 0
    for r in range(start, b.n_rows):
        a.grid.append(b.grid[r])
    a.pages = sorted(set(a.pages) | set(b.pages))
    a.notes.extend(b.notes)
