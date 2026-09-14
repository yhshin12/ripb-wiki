---
updated: 2026-09-15
phase: 3
---
# 상태

## 현재 단계
Phase 2 (도구) 완료. 다음은 Phase 3 시범 인제스트(NEI 18-04 §3). 계획: `meta/design/2026-09-14-rebuild-plan-phase2.md`.

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
1. Phase 3 시범 인제스트 계획: NEI 18-04 §3 (LBE 정의, 빈도 구분, F-C Target). `wiki-ingest` skill과 접점 ①②, 용어 질문 형식, 검사 관문을 시범으로 점검하고 CLAUDE.md·skill을 보정한다.
2. 본 인제스트: 설계 부록 A 순서. 원문 1건마다 `wiki-lint`, 2건마다 `wiki-audit`.

## 미해결
- ACRS_ML25293A458: 전용 프로파일 `acrs_slides.py` (2026-09-15 결정: 슬라이드 제목 `##`, 글머리표 제목 승격 방지, 캡션 없는 그림 37개를 `[!figure] Slide N`으로 포함). Phase 3에서 인제스트 순서 10번 전에 구현.
- `meta/metrics.md`는 첫 표본 재검증(`wiki-audit`) 때 만든다. 목표 오류율은 그때 사용자와 정한다(설계 §10).
