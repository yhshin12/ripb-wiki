import os
import shutil
import sys

import pytest

SCRIPTS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REAL_VAULT = os.path.dirname(SCRIPTS)
sys.path.insert(0, SCRIPTS)


@pytest.fixture
def vault(tmp_path, monkeypatch):
    """A throw-away vault with the real template and empty inbox/references/wiki (public and internal)."""
    import source
    for d in ("inbox", "inbox/internal", "references/raw", "wiki", "templates",
              "internal/references/raw", "internal/wiki"):
        os.makedirs(tmp_path / d)
    shutil.copy(os.path.join(REAL_VAULT, "templates", "source_card.md"), tmp_path / "templates" / "source_card.md")
    monkeypatch.setattr(source, "VAULT", str(tmp_path))
    monkeypatch.setattr(source, "load_docs", lambda: {"DOC_A": ("DOC_A_Some Title", "generic", None)})
    return tmp_path


MINI_CLEANED = """---
pdf_pages: 12
---

<!-- page 1 -->

# Cover

<!-- page 2 | 1 -->

## 3.2 Frequency

The **F-C Target** is not a boundary between “acceptable” and unacceptable.[^1] ^fc-target

| Event | Frequency<sup>1</sup> |
|---|---|
| AOO | 1E-02/plant-year |

<!-- page 3 | 2 -->

> [!withheld] SRI — This information is withheld in accordance with 10 CFR 2.390.

> [!figure] Figure 3-1 text
> Licensing basis events include AOOs, DBEs, and BDBEs.

<!-- page 5-7 | 4..6 -->

| Table 5-1 | Value |
|---|---|
| Range row | 5E-07 |

<!-- page 9 | 8 -->

Criterion text on nine\\* continues.

<!-- page 8 | 7 -->

Back on eight: sodium leakage shall be considered.

<!-- page 9 | 8 -->

<!-- source: note supplied by the build -->
Tail of nine.
"""

CARD_BODY = """# T (DOC_A)

> [!abstract] 요약
> (인제스트 완료 시 작성)

## 서지
- 키: `DOC_A`

## 구조
<!-- sync:begin -->
- PDF 쪽 수: 12
<!-- sync:end -->

## 알려진 모순
- 없음

## 관련 문서
- 없음
"""

TERMINOLOGY = """---
type: map
aliases: [용어표]
sources: []
status: draft
verified:
term:
tags: [terminology]
terms_pending: []
---
# 용어표 (Terminology)

> [!abstract] 요약
> 시험용 용어표이다.

## 용어

| ID | English | 약어 | 한국어 | 이후 표기 | 금지 표기 | 정의 출처 | 상태 | 비고 |
|---|---|---|---|---|---|---|---|---|
| LBE | Licensing Basis Event | LBE | 가나 | 약어 | 나가 | [DOC_A §3.2 p.3] | 확정 | |
| RAC | Reactor Air Cooling System | RAC |  | 약어 |  | [DOC_A §3.2 p.3] | 미정 | |

## 관련 문서
- 없음
"""

GOOD_NOTE = """# 가나 시험 (Sample Concept)

> [!abstract] 요약
> 가나(Licensing Basis Event)%%t:LBE%%에 관한 시험 노트이다.

## 원문 사실
- "Licensing basis events include AOOs, DBEs, and BDBEs." [DOC_A §3.2 p.3]

| 항목 | 값 | 출처 |
|---|---|---|
| AOO | 1E-02/plant-year | [DOC_A Table x p.2] |

## 해설
빈도 1E-02/plant-year가 표에 있다. LBE%%t:LBE%%는 세 종류이다.

## 관련 문서
- [[DOC_A]]
"""


@pytest.fixture
def mini_vault(tmp_path):
    """Public tree with one source card (DOC_A, 12 pages), its cleaned file, and a two-row terminology table."""
    import hashlib

    import notes
    for d in ("wiki", "references/raw", "internal/wiki", "internal/references/raw", "inbox", "meta", "templates"):
        os.makedirs(tmp_path / d, exist_ok=True)
    cleaned = tmp_path / "references" / "DOC_A_T.md"
    cleaned.write_text(MINI_CLEANED, encoding="utf-8", newline="\n")      # LF on Windows too
    pdf = tmp_path / "references" / "raw" / "DOC_A_T.pdf"
    pdf.write_bytes(b"%PDF fake DOC_A")
    fm = {"type": "source", "key": "DOC_A", "title": "T", "file": "references/DOC_A_T.md",
          "pdf": "references/raw/DOC_A_T.pdf", "sha256_pdf": hashlib.sha256(pdf.read_bytes()).hexdigest(),
          "sha256_md": hashlib.sha256(cleaned.read_bytes()).hexdigest(), "pdf_pages": 12, "build": {},
          "ingest": "pending", "units": []}
    notes.write_note(str(tmp_path / "wiki" / "DOC_A.md"), fm, CARD_BODY)
    (tmp_path / "wiki" / "Terminology.md").write_text(TERMINOLOGY, encoding="utf-8", newline="\n")
    import build_index
    build_index.write(str(tmp_path))
    return tmp_path


@pytest.fixture
def make_note(mini_vault):
    import notes

    def make(name, body, root=None, **fm):
        base = {"type": "concept", "aliases": [], "sources": ["DOC_A"], "status": "draft", "verified": None,
                "term": None, "tags": [], "terms_pending": []}
        base.update(fm)
        p = (mini_vault / root / "wiki" if root else mini_vault / "wiki") / f"{name}.md"
        notes.write_note(str(p), base, body)
        return str(p)
    return make


@pytest.fixture
def good_note_body():
    return GOOD_NOTE
