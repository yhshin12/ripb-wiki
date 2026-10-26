---
name: wiki-ingest
description: ripb vault에 원문 1단위(절 묶음 또는 장)를 인제스트할 때 쓴다. "ingest", "인제스트", 세션 시작 보고의 inbox 대기·진행 중 원문, 새 원문 등록 요청이 해당한다.
---

# wiki-ingest

규칙은 `CLAUDE.md`, 근거는 `meta/design/2026-09-14-vault-rebuild-design.md` §4.2, §5, §6.3, §7.2. 명령은 모두 `C:\Code\Python\pykaeri\.venv12\Scripts\python.exe`로 vault 루트에서 실행한다.

## 0. 준비
1. `scripts/source.py status`에서 `in_progress` 원문을 먼저 잇는다. 없으면 설계 부록 A 순서의 첫 `pending`. PSAR이 참조하는 topical·technical report 같은 보조 원문은 수시 인제스트(설계 §4.3)이다: 키는 문서 번호, 등록·정제는 전체, 단위는 질의에 필요한 절만.
2. inbox에 새 파일이 있으면 등록 키·제목을 사용자에게 확인한 뒤: `source.py register <pdf> --key KEY --title "…"`(내부 자료는 `--root internal`) → `convert_references.py` → `scripts/refclean/profiles/__init__.py`의 `DOCS` 등록과 프로파일 → `clean_references.py --only KEY --verify`와 pytest → `source.py sync KEY`. PDF가 아닌 형식은 변환 방식을 사용자에게 묻는다.
3. 이번 단위를 소스 카드 `units`에 `{unit: "<범위>", status: in_progress}`로 넣고 `ingest: in_progress`로 둔다(`partial` 원문도 같다).

## 1. 접점 ① — 계획과 용어 질문 (한 메시지)
- 절 범위, 만들거나 고칠 노트(파일명, type, 한 줄 내용), 기존 노트와의 관계.
- 용어 후보: 원문 약어표·용어집 항목과 해설에 쓸 전문 용어 중 `wiki/Terminology.md`에 없는 것. 용어표에 `미정` 행을 넣고(한국어 칸은 비움) `templates/term_question.md` 형식으로 묻는다. 번역 후보를 싣지 않는다.
- 답을 받은 뒤 쓴다. 용어 답은 `wiki-terms`로 반영한다.

## 2. 작성 (`templates/note.md`)
- 순서: 원문 사실 → 해설 → 링크.
- 원문 사실: 정제본 문장을 그대로 복사해 곧은 따옴표 `"…"`로 감싼다(원문 안의 “ ”는 그대로). 긴 문단은 `...`로 줄이되 조각마다 3단어 이상. 표는 `| 항목 | 값 | 출처 |`이고 모든 행에 인용. 인용은 `[KEY 위치 p.N]`, N은 쪽 표지의 첫 번호.
- 해설: 원문 사실 항목만 근거로 쓰고, 수치는 원문 사실에 있는 것만. 전문 용어에는 `%%t:ID%%` 표지를 붙이고 표기는 용어표 규칙대로(미정이면 English).
- 링크는 존재하는 노트만. 없는 주제는 변경 요약의 "누락 주제"에 적는다.
- 원문끼리 모순되면 둘 다 인용하고 `status: disputed`.
- 큰 장은 추출·대조를 읽기 전용 서브에이전트에 나누고, 노트는 이 세션이 쓴다.
- 작성 뒤 대조(읽기 전용 서브에이전트)는 `audit_sample.py`의 판정 형식을 쓴다. 요약·해설 문장마다 근거가 된 원문 사실 줄 번호를 요구하고, 원문에는 맞지만 원문 사실 절에 없는 문장은 `원문 사실에 없음`으로 판정하게 한다. "만", "only", "모두", "없다" 같은 배타적 표현과 문서 구조(절·부록 위치)에 관한 문장은 따로 원문 전체에서 확인하게 한다(2026-10-14 첫 audit의 오류 2건이 이 두 유형).

## 3. 검사
- 편집마다 PostToolUse hook이 검사 결과를 돌려준다. 오류는 바로 고친다.
- 단위 끝: `lint_wiki.py --all`, `verify_quotes.py --all`, `sync_terms.py`(충돌 0 확인, 필요하면 `--apply`), `build_index.py`, `check_absence.py`(A2는 새 노트가 기존 노트의 부재 진술을 낡게 했을 후보이다. 판정하여 고치거나 변경 요약에 적는다. `--accept`는 wiki-lint가 한다). 해소하지 못한 항목은 변경 요약에 적는다. 원문의 오기는 고치지 않는다.
- 원문의 마지막 단위를 닫기 전(수시 인제스트 원문은 해당 없음): `coverage_sections.py --only KEY`로 노트가 인용하지 않은 절을 확인한다. 남은 절은 노트에 넣거나, 반영 대상이 아니면 사유와 함께 `meta/coverage_exclusions.json`에 넣고 변경 요약에 적는다.

## 4. 접점 ② — 변경 요약 (`templates/change_summary.md`)
직접 볼 노트 2–3개를 이유와 함께 고른다. 반려되면 고친 뒤 이 단계부터 다시 한다.

## 5. 승인 뒤 한 번에
1. 이번 단위의 새·고친 노트: `status: checked`, `verified: <오늘>`.
2. 소스 카드의 해당 unit `status: complete`; 마지막 단위면 `source.py finish KEY`, 수시 인제스트 원문은 단위마다 `source.py finish KEY --partial`.
3. `append_log.py --type ingest --title "<KEY> <범위>" --item "새 노트 n, 고친 노트 n" --item "검사: …" --item "미정 용어 n"`.
4. `build_index.py`; `meta/status.md`의 다음 작업·미해결(disputed, 미정 용어, 누락 주제) 갱신.
5. 바뀐 파일만 `git add` → `git commit`(pre-commit 관문 통과). push는 사용자가 요청할 때만.
6. 원문 1건을 마치면 `wiki-lint`, 원문 2건마다 `wiki-audit`를 제안한다.

## 내부 자료
`internal/` 트리와 `--root internal`을 쓰고, 기록은 `internal/log.md`·`internal/status.md`에만 한다. 공개 파일과 커밋 메시지에 내부 문서명을 쓰지 않는다.
