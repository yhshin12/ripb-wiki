---
updated: 2026-09-14
phase: 1
---
# 상태

## 현재 단계
Phase 1 (소스 계층 정합) 진행 중. 계획: `meta/design/2026-09-14-rebuild-plan-phase0-1.md`.

## 존재하는 도구
- `scripts/convert_references.py`, `scripts/clean_references.py`, `scripts/refclean/` (정제 파이프라인, 테스트 211건)
- `scripts/source.py` (`register`/`adopt`/`sync`/`finish`/`status`)
- 없음: `lint_wiki.py`, `verify_quotes.py`, `sync_terms.py`, `build_index.py`, `append_log.py`, `session_start.py`, `audit_sample.py`, `index.md`, `wiki/Terminology.md`, `.claude/`

## 원문
| 키 | 정제본 | 소스 카드 | ingest |
|---|---|---|---|
| PSAR_ch01, ch03, ch04, ch05, ch06, ch07, ch11, RG_1.232, NEI_18-04 | 있음 (2026-09-13 빌드) | 있음 (`wiki/<KEY>.md`) | pending |
| RG 1.233, ACRS ML25293A458 | 없음 (`inbox/`) | 없음 | 대기 |

## 다음 작업
1. `inbox/`의 ACRS 슬라이드(ML25293A458, 22쪽)와 RG 1.233(31쪽)을 등록·변환·정제. 프로파일은 각각 신규(RG 1.233은 RG 1.232 프로파일 기반). (Task 11)
2. 소스 카드 9장의 인제스트(`ingest: pending` → `complete`) 및 단위(units) 작성. (Task 12)

## 미해결
- 없음
