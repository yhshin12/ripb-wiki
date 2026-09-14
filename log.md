# log

작업 1건당 항목 1개를 끝에 덧붙인다. 형식: `## [YYYY-MM-DD] <type> | <제목>` + 요점. 구 log(2026-05-02 ~ 2026-09-14)는 `internal/_legacy/log-before-rebuild.md`.

## [2026-09-14] init | vault 재구축 시작 (Phase 0)
- 구 이력 전체를 `internal/_legacy/ripb-before-rebuild.bundle`로 보존하고 새 이력을 시작했다.
- 구 wiki 267개 노트, Gemini 시기 스크립트·설정, 구 `raw/`(압축 보관)를 제거했다. 근거: `meta/design/2026-09-14-vault-rebuild-design.md` §1.
- 정제 파이프라인(`scripts/refclean/`, 커밋 31f826e)과 그 기록(`meta/references_cleanup/`)은 그대로 승계했다.

## [2026-09-14] chore | 새 이력 첫 커밋
- git #1 첫 커밋. `references/`, `internal/`, `inbox/`는 추적하지 않는다. pre-commit 관문 확인.

## [2026-09-14] feat | 소스 카드 9장
- `scripts/source.py adopt`로 정제본 9건의 소스 카드를 만들었다(`wiki/<KEY>.md`, `ingest: pending`). RG 1.232 원문 파일명에 제목을 붙였다(재변환, 본문 동일).

## [2026-09-14] feat | 대기 원문 2건 등록 (RG 1.233, ACRS ML25293A458)
- `source.py register` → 변환 → generic 프로파일로 정제 → 소스 카드. 누락률: RG 1.233 0.12 %, ACRS ML25293A458 0.11 %. Phase 1 완료.

## [2026-09-15] feat | Phase 2 완료: 도구
- 검사(lint_wiki L01–L36, verify_quotes V1–V5), 변경(sync_terms, build_index, append_log), 보고(session_start, audit_sample), 보조 모듈(notes, citations, terms, leak_guard, hook_post_edit).
- 관문: Claude SessionStart·PostToolUse hook, git pre-commit 전체 검사(두 저장소), commit-msg 내부 문서명 검사. 탐침으로 거부 동작 확인.
- skill 5종(wiki-ingest/terms/query/lint/audit), 템플릿 3종, 빈 용어표, Bases 보기 4종, Obsidian 명령 4종(Gemini 실행 명령 제거).
- Phase 1 이관 항목 처리: source.py 보강 7건, generic 프로파일 2건, 설계 부록 B·§8.1 수정, refs marker(원문 의존 테스트 109건), internal .gitattributes.
- 결함 1건 수정: 템플릿의 dict 형 frontmatter 값이 lint·index·audit·sync를 중단시키던 문제. 회귀 테스트 5건 추가.
- 테스트 388건 통과. lint·인용 검증 오류 0, index 최신, 용어 동기화 변경 0.

## [2026-09-15] ingest | NEI 18-04 §3.1, §3.2.1 (시범)
- 새 노트 3개(Licensing_Basis_Event, LBE_Frequency_Categories, F_C_Target), 고친 노트 1개(소스 카드 NEI_18-04 단위 등록·완료).
- 용어 11건을 영어 유지로 확정(LBE, AOO, DBE, BDBE, DBA, F-C Target, SSC, ES, QHO, EAB, TLST). 미정 용어 0.
- 검사: lint 오류 0·경고 0, 인용 검증 오류 0, 용어 충돌 0, 조사 확인 5건 중 2건 수정. 작성 중 PostToolUse hook이 링크·용어 첫 등장·해설 수치 문제 8건을 잡아 고쳤다.
- 시범에서 드러난 규칙 보완 2건은 meta/status.md 다음 작업에 적었다: 영어 유지 용어 노트의 H1 형식, 기관·규정 약어의 용어표 등록과 lint 경고 처리.
