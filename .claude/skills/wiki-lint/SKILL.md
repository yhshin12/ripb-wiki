---
name: wiki-lint
description: 원문 1건의 인제스트가 끝났을 때, 또는 사용자가 "lint"나 "점검"을 요청할 때 쓴다. 기계 검사 뒤 노트 간 의미 점검을 하고 meta/lint/YYYY-MM-DD.md 보고서를 쓴다.
---

# wiki-lint

1. 기계 검사: `lint_wiki.py --all`, `verify_quotes.py --all`, `build_index.py --check`, `sync_terms.py`. 결과를 요약한다.
2. 의미 점검 범위: 완료한 원문의 노트, 그 노트와 링크로 이어진 노트, `sources`가 겹치는 노트.
3. 점검 항목과 근거: 노트 간 모순(같은 대상의 다른 수치·분류), 중복(같은 개념의 두 노트, 겹치는 alias), 누락 주제(원문 사실·해설이 언급하나 노트가 없는 주제), 낡은 서술(새 원문이 대체한 사실, `deprecated` 후보). 판정마다 해당 노트들의 원문 사실 항목을 인용과 함께 근거로 적는다.
4. 보고서 `meta/lint/YYYY-MM-DD.md`: `# 의미 점검 YYYY-MM-DD (<KEY>)` 아래 `## 기계 검사`, `## 모순`, `## 중복`, `## 누락 주제`, `## 낡은 서술`, `## 제안 조치`. 해당 없는 절은 "없음". 내부 자료 점검은 `internal/status.md`에만 적는다.
5. 사용자에게 요약을 보이고, 조치는 항목별로 승인을 받는다. 보고서는 승인 뒤 `append_log.py --type lint`와 함께 커밋한다.
