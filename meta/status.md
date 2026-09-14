---
updated: 2026-09-15
phase: 3
---
# 상태

## 현재 단계
Phase 3 인제스트 진행 중. 시범 단위 NEI 18-04 §3.1·§3.2.1 완료(노트 3개, 2026-09-15). 도구 계획: `meta/design/2026-09-14-rebuild-plan-phase2.md`.

## 존재하는 도구
- 정제: `scripts/convert_references.py`, `scripts/clean_references.py`, `scripts/refclean/` (psar·nei1804·rg1232·generic 프로파일, 공용 `levels.py`)
- 원문: `scripts/source.py` (`register`/`adopt`/`sync`/`finish`/`status`)
- 검사: `scripts/lint_wiki.py` (파일 단위 L01–L20, `--all` L30–L36), `scripts/verify_quotes.py` (V1–V5)
- 변경: `scripts/sync_terms.py` (dry-run 기본), `scripts/build_index.py` (`--check`), `scripts/append_log.py`
- 보고: `scripts/session_start.py`, `scripts/audit_sample.py`
- 보조: `scripts/notes.py`, `scripts/citations.py`, `scripts/terms.py`, `scripts/leak_guard.py`, `scripts/hook_post_edit.py`
- 생성물·설정: `index.md`, `internal/index.md`, `wiki/Terminology.md` (빈 표), `meta/terms_state.json`, `templates/` (source_card, note, term_question, change_summary), `.claude/settings.json`, `.claude/skills/` (wiki-ingest, wiki-terms, wiki-query, wiki-lint, wiki-audit), `meta/views/*.base` (Bases 보기 4종), Obsidian Shell Commands 4종
- 관문: git pre-commit(두 저장소: 경로, `[[HSFR_`, 내부 문서명, lint, 인용 검증, index), git commit-msg(내부 문서명), Claude SessionStart·PostToolUse hook (2026-09-15 동작 확인)
- 테스트: 388건 (`python -m pytest scripts/refclean/tests scripts/tests -q`; 원문을 읽는 109건은 `refs` marker)

## 원문
| 키 | 정제본 | 소스 카드 | ingest |
|---|---|---|---|
| PSAR_ch01, ch03, ch04, ch05, ch06, ch07, RG_1.232, NEI_18-04 | 있음 (2026-09-13 빌드 (RG_1.232, PSAR_ch04는 2026-09-14 재빌드)) | 있음 (`wiki/<KEY>.md`) | pending |
| PSAR_ch11 | 있음 (2026-09-14 재빌드, 출력 동일) | 있음 | pending |
| RG_1.233 | 있음 (2026-09-14 빌드) | 있음 (`wiki/RG_1.233.md`) | pending |
| ACRS_ML25293A458 | 있음 (2026-09-14 빌드) | 있음 (`wiki/ACRS_ML25293A458.md`) | pending |

## 다음 작업
1. 규칙 보완 2건 (2026-09-15 시범에서 드러남): 영어 유지 용어 노트의 H1 형식(`# English (약어)`)을 CLAUDE.md §4와 설계 §5.1에 추가. 기관·규정 약어(NRC, EPA, CFR 등)를 용어표에 `용어 아님`으로 등록하고, 그 상태의 약어는 lint L13 경고를 내지 않도록 고친다.
2. NEI 18-04 §3 나머지 인제스트: §3.2.2 LBE 선정 절차(그림 3-2), §3.2.3 단계별 변화, §3.3 PRA의 역할.
3. 본 인제스트: 설계 부록 A 순서. 원문 1건마다 `wiki-lint`, 2건마다 `wiki-audit`.

## 미해결
- ACRS_ML25293A458: 전용 프로파일 `acrs_slides.py` (2026-09-15 결정: 슬라이드 제목 `##`, 글머리표 제목 승격 방지, 캡션 없는 그림 37개를 `[!figure] Slide N`으로 포함). Phase 3에서 인제스트 순서 10번 전에 구현.
- `meta/metrics.md`는 첫 표본 재검증(`wiki-audit`) 때 만든다. 목표 오류율은 그때 사용자와 정한다(설계 §10).
- 그림 처리 방침 미정: 정제본의 PNG를 노트에 embed할지, 문서별로 파일 이름이 겹치지 않는지 확인이 필요하다. NEI 18-04 Figure 3-1은 이번 단위에서 넣지 않았다.
