"""citations.py — citation syntax, page split and text normalisation for quote checks (spec §5.2, §5.4; plan P6).

Citation: `[KEY locator p.N]`, `[KEY locator p.N-M]`, or `[KEY §heading path]` for sources without pages.
Citations are the bracket groups at the end of a list item or table cell (split_trailing).
"""
import re
from dataclasses import dataclass

KEY = r"[A-Za-z][A-Za-z0-9_.\-]*"
_INNER = re.compile(rf"^({KEY}) (.+)$")
_PAGE = re.compile(r"^(?P<loc>.*?)\s*\bp\.(?P<p1>\d+)(?:-(?P<p2>\d+))?$")
_TRAIL = re.compile(r"(?:\s*\[[^\[\]\n]+\])+\s*$")
_ONE = re.compile(r"\[([^\[\]\n]+)\]")
# same pattern as refclean.verify.ANCHOR
ANCHOR = re.compile(r"^<!-- page (\d+)(?:-(\d+))?(?: \| [^>]*)? -->$")


@dataclass(frozen=True)
class Citation:
    key: str
    locator: str
    p1: int | None
    p2: int | None
    raw: str


def parse_citation(inner):
    m = _INNER.match(inner.strip())
    if not m:
        return None
    key, rest = m.group(1), m.group(2).strip()
    pm = _PAGE.match(rest)
    if pm:
        p1 = int(pm.group("p1"))
        return Citation(key, pm.group("loc").strip(), p1, int(pm.group("p2") or p1), f"[{inner}]")
    return Citation(key, rest, None, None, f"[{inner}]")


def split_trailing(text):
    m = _TRAIL.search(text)
    if not m:
        return text, []
    cites = [parse_citation(x) for x in _ONE.findall(m.group(0))]
    if not cites or any(c is None for c in cites):
        return text, []
    return text[:m.start()].rstrip(), cites


def page_map(text):
    """{page: text} split on page anchors, as refclean.verify.md_pages (range anchors credit every page)."""
    pages, cur, buf = {}, None, []

    def flush():
        if cur is not None:
            for p in cur:
                pages[p] = pages.get(p, "") + "\n" + "\n".join(buf)

    for line in text.split("\n"):
        m = ANCHOR.match(line.strip())
        if m:
            flush()
            a, b = int(m.group(1)), int(m.group(2) or m.group(1))
            cur, buf = list(range(a, b + 1)), []
            continue
        buf.append(line)
    flush()
    return pages


def has_pages(text):
    return any(ANCHOR.match(line.strip()) for line in text.split("\n"))


_TYPO = str.maketrans({"‘": "'", "’": "'", "‚": "'", "′": "'", "“": '"', "”": '"',
                       "„": '"', "″": '"', "–": "-", "—": "-", "‐": "-", "‑": "-",
                       " ": " "})


def normalize(text):
    kept, withheld = [], False
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith(">"):
            inner = s.lstrip(">").strip()
            if re.match(r"\[!withheld\]", inner, re.I):
                withheld = True
                continue
            if withheld or re.match(r"\[![A-Za-z-]+\]", inner):
                continue
            line = inner
        else:
            withheld = False
        kept.append(line)
    t = "\n".join(kept)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"<sup>.*?</sup>", "", t, flags=re.S)
    t = re.sub(r"!\[\[[^\]]*\]\]", " ", t)
    t = re.sub(r"\[\^\d+\]:?", "", t)
    t = re.sub(r"</?[A-Za-z][^>]*>", "", t)
    t = re.sub(r"(?m)\s\^[A-Za-z0-9-]+\s*$", "", t)
    t = re.sub(r"(?m)^\s*#{1,6}\s+", "", t)
    t = re.sub(r"(?m)^\s*(?:[-*+]|\d+[.)])\s+", "", t)
    t = re.sub(r"(?m)^\s*\|?(?:\s*:?-{3,}:?\s*\|?)+\s*$", "", t)
    t = t.replace("**", "")
    t = re.sub(r"(?<!\\)\*", "", t)
    t = re.sub(r"\\(.)", r"\1", t)
    t = t.replace("|", " ").translate(_TYPO)
    return re.sub(r"\s+", " ", t).strip()


def quotes(text):
    return re.findall(r'"([^"]+)"', text)


def fragments(quote):
    return [f.strip() for f in re.split(r"\.\.\.|…", quote) if f.strip()]


_STRIP_FOR_NUMBERS = [
    re.compile(r"\[\[[^\]]*\]\]"),
    re.compile(r"\[[^\[\]\n]+\]"),
    re.compile(r"%%t:[^%]+%%"),
    re.compile(r"§\S+"),
    re.compile(r"\b(?:Table|Figure|Section|Chapter|Appendix)\s+\S+"),
    re.compile(r"\bp\.\d+(?:-\d+)?"),
]
# ASCII boundaries: Python's \w includes Hangul, which would cut '1,000개' down to '1'
_NUM = re.compile(r"(?<![A-Za-z0-9_.\-])(\d+(?:[.,]\d+)*(?:[Ee][-+]?\d+)?)(?![A-Za-z0-9_\-]|[.,]\d)")


def _canon(n):
    m = re.fullmatch(r"(.+?)[Ee]([-+]?)(\d+)", n)
    if m:
        return f"{m.group(1)}E{'-' if m.group(2) == '-' else ''}{int(m.group(3))}"
    if re.fullmatch(r"\d{1,3}(?:,\d{3})+", n):
        return n.replace(",", "")
    return n


def numbers(text):
    for pat in _STRIP_FOR_NUMBERS:
        text = pat.sub(" ", text)
    return {_canon(n) for n in _NUM.findall(text)}
