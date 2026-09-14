# log

작업 1건당 항목 1개를 끝에 덧붙인다. 형식: `## [YYYY-MM-DD] <type> | <제목>` + 요점. 구 log(2026-05-02 ~ 2026-09-14)는 `internal/_legacy/log-before-rebuild.md`.

## [2026-09-14] init | vault 재구축 시작 (Phase 0)
- 구 이력 전체를 `internal/_legacy/ripb-before-rebuild.bundle`로 보존하고 새 이력을 시작했다.
- 구 wiki 267개 노트, Gemini 시기 스크립트·설정, 구 `raw/`(압축 보관)를 제거했다. 근거: `meta/design/2026-09-14-vault-rebuild-design.md` §1.
- 정제 파이프라인(`scripts/refclean/`, 커밋 31f826e)과 그 기록(`meta/references_cleanup/`)은 그대로 승계했다.
