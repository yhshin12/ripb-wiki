---
title: 인수인계 — references/ 정제 파이프라인 완료, 다음은 위키 재구축
date: 2026-09-14
from_session: 2026-09-11 ~ 2026-09-13 (Claude Code, refclean 구축)
status: 커밋 완료(31f826e, main, 미푸시)
---

# 1. 현재 상태 (한 문단)

원본 PDF 9개(Natrium PSAR ch1·3·4·5·6·7·11, RG 1.232, NEI 18-04)가 `references/raw/`(git·Obsidian 제외)에 있고, 재현 가능한 파이프라인(`scripts/convert_references.py` → `scripts/clean_references.py`, 패키지 `scripts/refclean/`)이 이를 RAG용 정제본 `references/<stem>.md` 9개와 도면 PNG 65개(`references/figures/`)로 만든다. 테스트 211건 통과, 전체 빌드 9/9, 실패 패치 0, 잔재 0, PDF 대비 토큰 누락 0.00–1.66 %(문서별 원인 규명·테스트 고정). 최종 검토(치명 0·중요 9→모두 수정·경미 16 보류)와 재검토를 통과했고, `31f826e`로 main에 커밋했다(푸시는 요청 시).

# 2. 다음 세션이 처음 할 일 (순서대로)

1. 읽기: `AGENTS.md` §3(파이프라인 계약) → `log.md` 마지막 2항목 → `meta/references_cleanup/final_review_2026-09-13.md`(Minor 절 포함) → 이 문서.
2. 환경 확인(2분):
   ```bash
   C:\Code\Python\pykaeri\.venv12\Scripts\python.exe -m pytest scripts/refclean/tests -q
   ```
   211 passed가 나와야 한다. 빌드 확인이 필요하면 `python scripts/clean_references.py --only PSAR_ch04 --verify`.
3. 이전부터 남아 있던 미커밋 변경을 사용자와 정리한다(이번 커밋에서 의도적으로 제외함): `wiki/` 수정 4건, `GEMINI.md`·`wiki/index.md` 삭제, 루트 `index.md`, `conversations/`, Gemini 시기 스크립트 4개(`batch_create_sfrdc.py`, `patch_underlines.py`, `process_all_pdfs.py`, `validate-template.sh`), `.obsidian/community-plugins.json`. 위키는 clean-slate 재구축(방안 A)이 결정되어 있으므로 대부분 폐기 대상일 가능성이 높다.
4. 본 과제 시작: **위키 재구축 사양 작성**. 메모리에 기록된 2026-09-11 설계 결정 7개(아직 사양 문서 없음)를 사양으로 옮기고 사용자 확인을 받는다.
   - 하나의 vault, 두 git 저장소(`internal/`은 로컬 전용 git, 외부 저장소는 무시).
   - git 이력 새로 시작(옛 `.git`은 `internal/`에 번들), GitHub `yhshin12/ripb-wiki`는 사용자가 정리.
   - 언어: "원문 사실" 절은 영문 원문 + 위치 인용, 요약·해설은 한국어, 용어는 첫 등장 시 "한국어(영어)".
   - 용어: 한국어 번역을 추측하지 않는다. 미정 용어는 모아 한 번에 묻는다. 대조표가 단일 진실 원천이며 변경 시 스크립트가 전파(용어 span 표시).
   - 규제 노트는 vault 소스가 말하는 범위만(CFR/IAEA 원문 추가 없음).
   - 변경 요약 승인 = 커밋 승인, 푸시는 요청 시.
   - 소스 파이프라인 = 이번에 완성된 것.
5. 사양이 확정되면 `references/<stem>.md`를 입력으로 ingest를 설계한다. 정제본의 구조(아래 §4)가 chunking·인용의 단위다.

# 3. 절대 하지 말 것

- `references/<stem>.md`와 `references/figures/`를 손으로 고치지 않는다. 생성물이다. 고칠 것이 있으면 `scripts/refclean/profiles/<doc>.py` 또는 `patches/<KEY>.json`을 고치고 재빌드한다.
- `references/raw/`를 수정하지 않는다(원본 + 변환 원시 출력; `_verify/`만 빌드가 쓴다).
- 원문 오기를 "교정"하지 않는다(파일별 금지 목록: `meta/references_cleanup/file_reviews/review_*.md` §5).
- `scripts/patch_underlines.py`, `process_all_pdfs.py`, `batch_create_sfrdc.py`, `wiki_utils.py`, `draw_eta.py`는 Gemini 시기 스크립트로 검토 없이 쓰지 않는다(`draw_eta.py`는 원문에 없는 "Core Damage" 결과를 그린다).

# 4. 정제본 형식 (ingest 설계 시 알아야 할 것)

| 요소 | 형식 |
|---|---|
| frontmatter | `doc_id`, `title`, `revision`, `source_pdf`, `raw_json`, `pdf_pages`, `page_labels`, `tables[]`, `figures[]`, `withheld[]`, `converter`, `cleaned` |
| 쪽 앵커 | `<!-- page 12 \| 4.2-7 -->` (PDF 쪽 \| 인쇄 쪽). 여러 쪽에 걸친 표는 `<!-- page 12-14 \| 4.2-7..4.2-9 -->`. RG 1.232는 criterion 레코드 안에서 앵커가 되돌아감(본문 쪽 → rationale 첫 쪽) |
| 제목 | 번호 절 = 번호 성분 수가 수준(`## 4.1`, `### 4.2.1`, … `######`), 번호 없는 소제목 = 부모+1, `References (4.1)`처럼 절 번호로 고유화 |
| 표 | 논리 표 1개 = Markdown 표 1개(sheet 병합, rowspan 채움), 캡션은 PSAR에서 heading, 주석은 표 아래 목록, 주석 표시 `<sup>n</sup>` |
| 레코드 형식 | RG 1.232 부록 A–C: `#### SFR-DC 4 — <title>` + Status / Criterion text / NRC rationale. PSAR ch5 Tables 5.2-1~5.2-4: `#### DL3-RC1 — <function>` + Associated LBE(s)/Type + SSC·SRDC 표 |
| 지수 | `5E-07`, `3.40E-05`(가수 유지). 표의 `8.13E-02`는 원문 그대로 |
| 도면 | `![Figure 7.2.3-1 …](figures/PSAR_ch07/Fig_7.2.3-1.png)`; 라벨은 PNG에만 있음(전사 정책 없음, 사용자 결정) |
| 비공개 | `> [!withheld] SRI — This information is withheld in accordance with 10 CFR 2.390` |
| 각주 | 본문 `[^n]`, 정의는 절 끝(RG 1.232 14개, NEI 18-04 16개) |
| 강조 | RG Table 1 redline(`~~삭제~~`, `<ins>삽입</ins>`), RG GDC 19의 "emphasis added" 기울임, ch1 굵은 상태 용어만 보존 |

# 5. 알아 두면 시간이 절약되는 것

- 변환(`convert_references.py`)은 JDK 17이 필요하다. PATH의 `java`는 Java 8이라 실패한다(`C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot\bin`을 앞에 두거나 `JAVA17_BIN` 설정). 정제(`clean_references.py`)에는 Java가 필요 없다.
- Python은 `C:\Code\Python\pykaeri\.venv12\Scripts\python.exe`만 쓴다(PyMuPDF·pdfplumber·pypdf·pytest 설치됨).
- `--verify`의 누락 비율은 회귀 탐지용이지 완전성 증명이 아니다. 맹점 8가지가 `scripts/refclean/verify.py` 첫머리에 적혀 있다(머리글·바닥글 띠, 쪽 하단 표 테두리, sheet 보전, 하이픈 토큰화 등). 값의 정확성은 문서별 테스트가 표 셀 단위로 확인한다.
- 기본값 `--max-missing-pct 2.0`을 넘으면 빌드가 실패한다. 문서별 잔차는 테스트에 ±10 토큰으로 고정되어 있어, 프로필을 바꾸면 그 테스트의 기댓값을 근거와 함께 다시 계산해야 한다.
- 새 소스 문서 추가 절차는 `AGENTS.md` §3에 있다(PDF를 `references/raw/`에 → 변환 → `profiles/__init__.py`에 등록 → 프로필 작성 → 빌드·검증).
- 병렬 서브에이전트를 쓸 때 Opus·Fable 세션 사용량 한도로 여러 번 끊겼다. 끊긴 에이전트는 SendMessage로 재개할 수 있었고 디스크의 부분 산출물은 남아 있었다. 문서별로 파일 소유권을 나누면 병렬이 안전했다.
- 패치 스크립트로 파일을 고칠 때 `io.open(..., "w", newline=...)`은 newline 값이 잘못돼도 파일을 먼저 비운다(한 번 `verify.py`를 날려 다시 썼음). 문자열 치환 후 검증한 뒤에만 쓰도록 한다.

# 6. 보류·미결 목록

- 경미 지적 16건(`final_review_2026-09-13.md` Minor 절): 모두 "있으면 좋은 것". 특히 `nei1804.py` 546행의 쪽별 표 사전은 같은 쪽 두 번째 표를 덮어쓰는 잠재 결함(현재 데이터 순서에서는 정상)이라 NEI 프로필을 다시 만질 때 단언문을 넣는다.
- 검증기 맹점: 쪽 하단 14 % 안의 표 테두리를 바닥글 선으로 오인하면 마지막 행이 PDF 쪽 집계에서 빠진다(ch1 p17 약어표). 출력에는 있다.
- ch3·ch6의 `- 1.` 이중 목록 표지, ch1의 약어표 H2가 H1보다 앞에 오는 순서 — 표기 통일 여지.
- 푸시하지 않았다. 원격 저장소 정리(설계 결정 2)와 함께 결정할 사항.

# 7. 파일 지도

- 사양·결정: `meta/references_cleanup/cleanup_review_2026-09-11.md`(맨 위 확정 결정 블록이 우선)
- 파일별 검토(원본 대조 근거, 금지 목록): `meta/references_cleanup/file_reviews/`
- 계획·브리프: `meta/references_cleanup/implementation_plan_2026-09-11.md`, `agent_brief_2026-09-11.md`
- 최종 검토·수정 기록: `meta/references_cleanup/final_review_2026-09-13.md`
- 문서별 빌드 보고서·작업 원장(판정 15건 포함): `meta/references_cleanup/build_reports/`
- 같은 내용의 원본은 `docs/superpowers/`에도 있으나 그 경로는 git이 무시한다.
