---
updated: 2026-09-14
phase: 2
---
# 상태

## 현재 단계
Phase 1 (소스 계층 정합) 완료. 다음 단계는 Phase 2 계획 작성. 계획: `meta/design/2026-09-14-rebuild-plan-phase0-1.md`.

## 존재하는 도구
- `scripts/convert_references.py`, `scripts/clean_references.py`, `scripts/refclean/` (정제 파이프라인 + generic 프로파일, 테스트 215건)
- `scripts/source.py` (`register`/`adopt`/`sync`/`finish`/`status`)
- 없음: `lint_wiki.py`, `verify_quotes.py`, `sync_terms.py`, `build_index.py`, `append_log.py`, `session_start.py`, `audit_sample.py`, `index.md`, `wiki/Terminology.md`, `.claude/`

## 원문
| 키 | 정제본 | 소스 카드 | ingest |
|---|---|---|---|
| PSAR_ch01, ch03, ch04, ch05, ch06, ch07, ch11, RG_1.232, NEI_18-04 | 있음 (2026-09-13 빌드) | 있음 (`wiki/<KEY>.md`) | pending |
| RG_1.233 | 있음 (2026-09-14 빌드) | 있음 (`wiki/RG_1.233.md`) | pending |
| ACRS_ML25293A458 | 있음 (2026-09-14 빌드) | 있음 (`wiki/ACRS_ML25293A458.md`) | pending |

## 다음 작업
1. Phase 2 계획 작성 (도구: lint_wiki, verify_quotes, sync_terms, build_index, append_log, session_start, audit_sample, hooks, skills)

## 미해결
- ACRS_ML25293A458 정제본: 슬라이드 제목 미추출, 글머리표 문장의 제목 오승격, 캡션 없는 그림 37개 미포함 → 인제스트 전 전용 프로파일 또는 그림 처리 방침 결정 필요 (`wiki/ACRS_ML25293A458.md` 서지 참조)
