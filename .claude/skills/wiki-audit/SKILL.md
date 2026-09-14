---
name: wiki-audit
description: 원문 2건의 인제스트가 끝날 때마다, 또는 사용자가 "audit"나 "표본 재검증"을 요청할 때 쓴다. checked 노트 10개를 무작위로 골라 읽기 전용 서브에이전트가 원문과 대조하고 오류율을 meta/metrics.md에 기록한다.
---

# wiki-audit

1. `audit_sample.py sample --n 10 --out <scratchpad>/audit_<YYYY-MM-DD>`. 출력의 seed와 모집단 수를 기록한다.
2. 각 `<Note>.prompt.md`를 읽기 전용 서브에이전트 하나에 준다(파일 편집 금지를 지시에 명시, 병렬 실행). 답 JSON을 이 세션이 `<Note>.result.json`으로 저장한다. JSON이 아니면 한 번 다시 요청한다. 세션 한도로 멈춘 서브에이전트는 SendMessage로 재개한다.
3. `audit_sample.py summarize <dir>`로 표 행을 얻는다.
4. `meta/metrics.md`에 행을 덧붙인다. 파일이 없으면 `# 표본 재검증 지표`와 머리 `| 날짜 | seed | 표본/모집단 | 오류 노트 | 노트 오류율 | 불일치·원문 없음 항목/전체 항목 | 경미 |`로 만든다. 첫 측정 행 아래에 목표 오류율을 사용자와 정해 적는다(설계 §10).
5. 오류 판정(불일치, 원문 없음, 원문 사실에 없음, 원문과 모순)은 이 세션이 원문으로 다시 확인한다. 확인된 오류마다 노트 수정안과 원인(규칙·도구·절차)을 보고하고, 승인 뒤 노트와 원인을 함께 고친다(설계 §7.4).
6. 승인 뒤 `append_log.py --type audit`과 함께 커밋한다.
