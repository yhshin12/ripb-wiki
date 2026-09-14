"""terms.py — the terminology table wiki/Terminology.md and term display rules (spec §6; plan P2, P3).

Table columns: ID | English | 약어 | 한국어 | 이후 표기 | 금지 표기 | 정의 출처 | 상태 | 비고.
금지 표기 holds several forms separated by '; '. Only the user fills 한국어 (spec D5).
"""
import re
from dataclasses import dataclass

COLUMNS = ["ID", "English", "약어", "한국어", "이후 표기", "금지 표기", "정의 출처", "상태", "비고"]
STATES = {"미정", "확정", "영어 유지", "용어 아님"}
LATER = {"약어", "한국어", ""}
ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_\-]*$")
MARKER = re.compile(r"%%t:([A-Za-z0-9][A-Za-z0-9_\-]*)%%")
# Korean reading of the last character of an abbreviation (spec §6.2)
READ = {"A": "에이", "B": "비", "C": "씨", "D": "디", "E": "이", "F": "에프", "G": "지", "H": "에이치", "I": "아이",
        "J": "제이", "K": "케이", "L": "엘", "M": "엠", "N": "엔", "O": "오", "P": "피", "Q": "큐", "R": "알",
        "S": "에스", "T": "티", "U": "유", "V": "브이", "W": "더블유", "X": "엑스", "Y": "와이", "Z": "제트",
        "0": "영", "1": "일", "2": "이", "3": "삼", "4": "사", "5": "오", "6": "육", "7": "칠", "8": "팔", "9": "구"}
PAIRS = {"은": ("은", "는"), "는": ("은", "는"), "이": ("이", "가"), "가": ("이", "가"), "을": ("을", "를"),
         "를": ("을", "를"), "과": ("과", "와"), "와": ("과", "와"), "으로": ("으로", "로"), "로": ("으로", "로")}
_JOSA = re.compile(r"^(으로|로|은|는|이|가|을|를|과|와)(?![가-힣])")


class TermError(Exception):
    pass


@dataclass(frozen=True)
class Term:
    id: str
    english: str
    abbr: str
    korean: str
    later: str
    forbidden: tuple
    source: str
    state: str
    note: str


def _cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_table(text):
    lines = text.split("\n")
    start = next((i for i, l in enumerate(lines) if l.strip().startswith("|") and _cells(l) == COLUMNS), None)
    if start is None:
        raise TermError("terminology header row not found (columns: " + " | ".join(COLUMNS) + ")")
    out = {}
    for i in range(start + 2, len(lines)):
        line = lines[i]
        if not line.strip().startswith("|"):
            break
        where = f"line {i + 1}"
        c = _cells(line)
        if len(c) != len(COLUMNS):
            raise TermError(f"{where}: {len(c)} cells, expected {len(COLUMNS)}")
        tid, eng, abbr, kor, later, forb, src, state, note = c
        if not ID_RE.match(tid):
            raise TermError(f"{where}: bad ID {tid!r}")
        if tid in out:
            raise TermError(f"{where}: duplicate ID {tid}")
        if state not in STATES:
            raise TermError(f"{where}: {tid}: state {state!r} not in {sorted(STATES)}")
        if later not in LATER:
            raise TermError(f"{where}: {tid}: 이후 표기 {later!r} must be 약어, 한국어 or empty")
        if state == "확정" and not kor:
            raise TermError(f"{where}: {tid}: 확정 needs 한국어")
        if later == "한국어" and state != "확정":
            raise TermError(f"{where}: {tid}: 이후 표기 한국어 needs 상태 확정")
        if later == "약어" and not abbr:
            raise TermError(f"{where}: {tid}: 이후 표기 약어 needs 약어")
        forbidden = tuple(x.strip() for x in forb.split(";") if x.strip())
        out[tid] = Term(tid, eng, abbr, kor, later, forbidden, src, state, note)
    return out


def load(path):
    with open(path, encoding="utf-8") as f:
        return parse_table(f.read())


def display(term, first):
    """Display form before a marker (plan P2); None for 용어 아님 (no marker allowed)."""
    if term.state == "용어 아님":
        return None
    if term.state == "확정":
        if first:
            return f"{term.korean}({term.english})"
        return term.abbr if term.later == "약어" else term.korean
    if not first and term.later == "약어" and term.abbr:
        return term.abbr
    return term.english


def final(word):
    """'none' / 'rieul' / 'other' for the last syllable of Hangul or an abbreviation; None for English words (P3)."""
    w = re.sub(r"\([^()]*\)\s*$", "", word).strip()
    if not w:
        return None
    c = w[-1]
    if "가" <= c <= "힣":
        k = (ord(c) - 0xAC00) % 28
        return "none" if k == 0 else ("rieul" if k == 8 else "other")
    if c in READ and re.fullmatch(r"[A-Z0-9][A-Z0-9\-]*", w):
        return final(READ[c])
    return None


def retarget(after, fin):
    """Correct the particle at the start of `after` for a word whose last syllable is `fin`."""
    m = _JOSA.match(after)
    if not m or fin is None:
        return after
    with_final, without = PAIRS[m.group(1)]
    if with_final == "으로":
        new = without if fin in ("none", "rieul") else with_final
    else:
        new = without if fin == "none" else with_final
    return new + after[m.end():]


def snapshot(terms):
    return {t.id: {"english": t.english, "abbr": t.abbr, "korean": t.korean, "later": t.later,
                   "forbidden": list(t.forbidden), "state": t.state} for t in terms.values()}
