---
name: wiki-terms
description: 사용자가 용어 질문에 답했을 때, "용어 반영"을 요청했을 때, 세션 시작 보고가 용어표 변경을 알릴 때 쓴다. 용어표 기록, sync_terms.py 전파, 승인과 커밋.
---

# wiki-terms

규칙: `CLAUDE.md` §5, 설계 §6. 한국어 표기를 추측하거나 제안하지 않는다.

1. 답을 `wiki/Terminology.md`에 기록한다. 한국어 표기 → `한국어` 칸에 사용자가 준 문자열 그대로, `상태: 확정`. "영어 유지" → `상태: 영어 유지`. "용어 아님" → `상태: 용어 아님`. 약어가 있는 용어의 `이후 표기`(약어/한국어)를 사용자가 정하지 않았으면 묻는다.
2. `lint_wiki.py wiki/Terminology.md`로 L20이 없는지 확인한다.
3. `sync_terms.py`(dry-run)로 갱신될 노트, `conflict`, `check particle`을 확인한다.
4. `conflict`(표지 앞 표기를 손으로 고친 곳)는 해당 줄을 보여 주고 어느 표기를 따를지 묻는다. `check particle`(영어 표기 뒤 조사)은 목록으로 보이고 사용자의 답대로 고친다.
5. 요약(바뀐 용어, 갱신 노트, 충돌·조사 처리) → 승인 → `sync_terms.py --apply` → `lint_wiki.py --all` → `build_index.py --check` → `append_log.py --type terms --title "용어 반영" --item "…"` → 커밋.
