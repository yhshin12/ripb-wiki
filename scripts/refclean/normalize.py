"""Pure text normalisers."""
import html
import re

# mantissa x 10 - exponent   (5×10-7, 3.40x10-5, 3.72 x10-4, 1 x 10-2)
_MANT_NEG = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?)\s?[x×X]\s?10\s?-\s?(\d{1,2})(?![\d.]?\d)")
# mantissa x 10 exponent (positive, sign-less; needs PDF evidence)
_MANT_POS = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?)\s?[x×X]\s?10(\d{1,2})(?!\d)")
# bare 10-N (needs PDF evidence)
_BARE_NEG = re.compile(r"(?<![\w.\-/])10-(\d{1,2})(?![\d.]?\d)")


def _e(mant, sign, exp):
    return f"{mant}E{sign}{int(exp):02d}"


def exponents(s, sups=None):
    """Normalise powers of ten to E-notation.

    sups: superscript strings found after '10' on the same PDF page (e.g. ['-7', '15']).
    Mantissa forms with an explicit minus are always converted; positive and bare forms only
    when the superscript is attested on the page.
    """
    s = _MANT_NEG.sub(lambda m: _e(m.group(1), "-", m.group(2)), s)
    if sups:
        sset = set(x.replace("−", "-").replace(" ", "") for x in sups)
        s = _MANT_POS.sub(lambda m: _e(m.group(1), "+", m.group(2)) if m.group(2) in sset else m.group(0), s)
        s = _BARE_NEG.sub(lambda m: f"1E-{int(m.group(1)):02d}" if ("-" + m.group(1)) in sset else m.group(0), s)
    return s


def decode_entities(s):
    return html.unescape(s) if "&" in s else s


_BULLET = re.compile(r"^\s*([•●▪■◦·])\s*")
_SUB_O = re.compile(r"^\s*o\s+(?=\S)")


def bullets(s):
    """Line-level: leading bullet glyphs -> Markdown list markers."""
    out = []
    for ln in s.split("\n"):
        if _BULLET.match(ln):
            ln = _BULLET.sub("- ", ln, count=1)
        elif _SUB_O.match(ln):
            ln = _SUB_O.sub("  - ", ln, count=1)
        out.append(ln)
    return "\n".join(out)


def strip_bullet(s):
    """Remove one leading bullet glyph from a list-item text."""
    return _BULLET.sub("", s, count=1)


def apply_hyphen_map(s, m):
    if not m:
        return s
    for k, v in m.items():
        if k in s:
            s = re.sub(rf"(?<![\w-]){re.escape(k)}(?![\w-])", v, s)
    return s


def obsidian_escape(s):
    s = re.sub(r"(?<!\\)\$", r"\\$", s)
    return s


def squash_ws(s):
    return re.sub(r"[ \t ]+", " ", s).strip()


def text_pipeline(s, sups=None, hyphen_map=None):
    s = decode_entities(s)
    s = squash_ws(s)
    s = apply_hyphen_map(s, hyphen_map)
    s = exponents(s, sups)
    s = obsidian_escape(s)
    return s
