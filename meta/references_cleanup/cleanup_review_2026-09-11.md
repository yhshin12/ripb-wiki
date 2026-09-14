---
title: "references/ Markdown 정제 수정 사항 (RAG 대비 검토 보고)"
date: 2026-09-11
scope: "references/*.md 9개 (opendataloader-pdf 2.5.7 기본 옵션 산출물) ↔ references/pdf/*.pdf"
status: 구현 완료·최종 검토 통과(2026-09-13). 계획 implementation_plan_2026-09-11.md, 검토 final_review_2026-09-13.md, 문서별 보고서 build_reports/ (모두 이 폴더)
---

# references/ Markdown 정제 수정 사항

> [!important] 확정 결정 (2026-09-11, 사용자 승인). 아래 본문과 충돌하면 이 블록이 우선한다.
> - **D1 위치:** 원본 PDF, raw 변환본(`<stem>.md`, `<stem>.json`, `<stem>_images/`), `_conversion.json`은 `references/raw/`에 둔다. 이 폴더는 읽기 전용이고 git과 Obsidian 색인에서 제외한다. 정제본은 `references/<stem>.md`이다. 변환은 `scripts/convert_references.py`로 한다.
> - **정제 입력:** 정제 스크립트는 raw md 대신 opendataloader **JSON**(요소 유형, 쪽, 좌표, 글꼴, rowspan/colspan, header/footer 구분)과 PDF(PyMuPDF 보조 데이터)를 읽는다.
> - **D2 지수:** `1E-07` 형식을 쓰고 가수는 유지한다(`3.40x10-5` → `3.40E-05`). 양의 지수는 PDF 윗첨자 근거가 있을 때만 `3.98E+15`로 쓴다. 단위 윗첨자(`m2`)는 추출된 그대로 둔다. §3의 유니코드 윗첨자 안은 폐기한다.
> - **D3 도면:** PDF 도면 영역을 200 dpi PNG로 렌더링해 `references/figures/<doc_key>/Fig_<번호>.png`에 둔다. 캡션을 alt text로 삽입하고, 벡터 잔해는 삭제한다. 비공개 도면은 표시 문구만 둔다.
> - **D4:** TOC, LoT, LoF는 삭제한다. frontmatter의 `tables`/`figures` 목록이 대신한다.
> - **D5:** 파일 분할은 하지 않는다. 원본 PDF 1개당 정제본 1개이며, 파일명은 raw stem과 같다.
> - **D6 record 형식:** RG 1.232 부록 A–C(criterion 178개)와 PSAR ch5 Tables 5.2-1–5.2-4(PSF 62개)에 적용한다. ch7 DL function 표는 Markdown 표로 둔다.
> - **도면 라벨(2026-09-13 확정):** 라벨 전사 정책은 두지 않는다. 라벨은 렌더링된 PNG에 있고, 파일 검토가 유일한 사실 출처로 지목한 범례(예: ch1 Figure 1.2-1 부지 범례)만 표로 전사한다. 도면 수가 적어 별도 규칙을 유지할 필요가 없다는 사용자 결정.
> - **D7 강조:** RG 1.232 Table 1 redline(`~~삭제~~`, `<ins>삽입</ins>`), RG GDC 19 rationale의 "emphasis added" 기울임, ch1 굵은 상태 용어만 보존한다. 그 밖의 기울임과 개정 표시 막대는 복원하지 않는다.

## 0. 요약

1. **데이터 손실의 주원인은 변환 설정이다.** opendataloader-pdf의 기본 content-safety 필터(`off-page`)가 `/Rotate 90` 가로 페이지에서 회전 전 폭(612 pt)을 기준으로 적용되어, 오른쪽 열의 텍스트를 버린다. 영향 규모는 다음과 같다.
   - ch5: SRDC 열 단어 756/2,281개(33 %) 소실
   - ch6: 하중계수 179/522개(34 %) 소실
   - ch4: Table 4.2-2 `Mean Dose Margin[d]` 열 전체 소실
   - RG 1.232: 20개 구간 소실
   - ch1: 부지 배치도 범례 31항목 소실
   - ch11: 조직도 라벨 4개 소실

   `--content-safety-off off-page`로 재변환하면 이 누락이 모두 복원되고, 다른 텍스트 변화는 없다(파일별 교차 검증 완료, §2).
2. **PSAR 7개 장은 `--include-header-footer`를 함께 써야 한다.** 표 캡션(Sheet n of m), 밑줄 소제목(ch5 11개), 표 머리행(ch7 FHP 표)이 페이지 머리글로 오인되어 삭제되었기 때문이다. 함께 되살아나는 머리글과 바닥글은 정규식으로 결정적으로 제거할 수 있다. RG 1.232와 NEI 18-04에는 이 옵션을 쓰지 않는다(가짜 heading 약 240개 증가).
3. **재변환으로 해결되지 않는 구조 결함이 9개 파일 모두에 공통으로 있다.**
   - PSAR 7개 장에서는 번호 절 1,104개 중 3개(0.3 %)만 Markdown heading이고, 나머지는 목록 항목·평문·본문 접착 형태이다. NEI 18-04와 RG 1.232에는 heading이 있으나 수준이 틀리거나 일부가 누락되었다.
   - 쪽 경계에서 표와 문단이 분할되어 있다.
   - 테두리 없는 표가 문단으로 풀려 있다(ch7 27개 표, 167행).
   - 벡터 도면이 라벨 조각과 가짜 표로 남아 있다.
   - TOC, 표지, 머리글·바닥글 잔재가 있다.
   - 이 결함들은 heading 기반 chunking을 불가능하게 하고, 값을 다른 절에 귀속시킨다.
4. **사실 자체를 틀리게 만드는 H급 결함은 파일별 명시 목록으로 교정해야 한다.**
   - NEI 18-04: 지수 부호 소실로 값이 뒤집혔다(`1×104`, `102/plant-year` ×2).
   - RG 1.232: 각주 번호가 결합되어 허위 인용이 생겼다(`10 CFR 50.342` = 50.34 + 각주 2).
   - ch3: LBE 결과표 88개 중 29개가 다음 LBE 절 아래에 붙어 있다. 예를 들어 RRS-SPLX-CN의 선량이 실제 8.13E-02 rem 대신 7.75E+00 rem으로 조회된다.
   - RG 1.232 Table 1: redline(취소선·삽입어) 의미가 소실되어 셀 29개의 제목이 틀리다.
   - NEI 18-04: Table 3-2의 수식 8개는 PDF 텍스트층 자체가 손상되어 수작업 전사만 가능하다.
5. **변환 결함이 아닌 원문 오기가 파일마다 7–20건 있다.** 이 항목은 자동 교정 대상에서 제외해야 한다(§7). 사전 기반 하이픈 복원은 원문 표기(`watercooled`, `leaktight` 등)를 훼손하므로 금지한다.

권장 순서는 다음과 같다. **(P0) 재변환 → (P1) PDF 보조 데이터 추출 → (P2–P8) 결정적 후처리 → (P9) 수작업 목록 → (P10) 회귀 검증**(§4).

---

## 1. 대상과 검토 방법

| 파일 (약칭) | md 크기 | md 행 | PDF 쪽 | /Rotate 90 쪽 | PDF 태그 | 비고 |
|---|---:|---:|---:|---:|---|---|
| NEI 18-04 Rev 1 (nei) | 243 KB | 1,921 | 95 | 0 (가로 MediaBox 13) | tagged, outline 61 | Word 원본 |
| RG 1.232 Rev 0 (rg) | 312 KB | 1,359 | 133 | **109** | 없음 | 부록 A–C 표 |
| PSAR ch1 | 185 KB | 2,320 | 115 | 39 | 빈 struct tree | withheld 13 |
| PSAR ch3 | 249 KB | 3,647 | 132 | 4 | 빈 struct tree | LBE 106절 |
| PSAR ch4 | 26 KB | 287 | 16 | 4 | 빈 struct tree | |
| PSAR ch5 | 113 KB | 996 | 52 | 15 | 빈 struct tree | PSF 62개 |
| PSAR ch6 | 157 KB | 1,697 | 80 | 14 | 빈 struct tree | 하중조합 표 |
| PSAR ch7 | 828 KB | 7,207 | 372 | 25 | 빈 struct tree | 3개 구간으로 분할 검토 |
| PSAR ch11 | 152 KB | 1,615 | 77 | 2 | 빈 struct tree | 운전 모드 |

방법은 다음과 같다.

- **전역 구조 스캔:** 정규식 기반으로 heading 분포, dot leader, 반복 행, 표 열 수, `<br>`, entity, 지수, 문단 분할 후보를 집계했다.
- **파일별 정밀 검토 10건:** md 전량을 순차 판독하고 PDF와 대조했다. 대조는 pdfplumber 단어·셀·폰트·색상 비교와 페이지 렌더링 육안 확인으로 했다.
- **재변환 실험:** 옵션 조합별로 JDK 17에서 수행했고, 출력은 scratchpad에만 두었다.

파일별 상세 근거(행 번호, PDF 쪽, 표·그림 대장, heading whitelist, 원문 오기 목록)는 부록 A의 검토 파일 10개에 있다. **검토 파일의 행 번호는 현행 md 기준이다.** 재변환 후에는 행 번호가 달라지므로 텍스트 앵커로 위치를 찾아야 한다.

---

## 2. 변환 단계 진단과 재변환 옵션

### 2.1 옵션별 효과 (실측)

| 옵션 | 효과 | 근거 | 적용 |
|---|---|---|---|
| `--content-safety-off off-page` | 가로 페이지 오른쪽 열의 누락 텍스트 복원. 기존 텍스트는 바뀌지 않고, 잘린 조각이 온전한 단어로 대체될 뿐이다 | 복원 단어 수(기본 변환 대비): ch5 +701, ch6 +312, ch1 +157(범례, `]]SRI` 6→13, `methodologies`), ch7 +24, ch3 +16(Table 3.5-4 LPZ 열 머리), ch11 +11(조직도 4 라벨), ch4 Table 4.2-2 8열(값 11개)·4.2-1 머리, RG 20개 구간(부록 criteria 178개가 PDF와 단어 수준 일치). NEI는 바이트 단위 동일 | **전 파일 필수** |
| `--include-header-footer` | 머리글 영역에 있던 표 캡션, 밑줄 소제목, 표 머리행 복원 | ch3 캡션 15개(6개 표), ch1 Table 1.4-1/-4/-5 캡션과 약어표 제목, ch6 캡션 6개, ch11 캡션 11개, ch5 `Implementation Summary` 9개·`Relevant PSAR…` 2개, ch7 `Function ID … FHP Functional Support` 머리행 | **PSAR 7개 장.** 추가 잡음(`SUBJECT TO DOE…`, `Kemmerer Unit 1 PSAR`, `x.y-n Revision 1`)은 P2에서 제거하고, 바닥글은 쪽 앵커로 전환 |
| `--markdown-page-separator "<!-- page %page-number% -->"` | 쪽 앵커 삽입. 그 밖의 출력은 동일(결정적) | ch4·NEI·RG에서 확인. Python API의 자리표시자는 `%page-number%` | **전 파일** |
| `--detect-strikethrough` | RG Table 1의 삭제어 33군을 `~~…~~`로 표시. 삽입어(청색 밑줄)는 표시하지 않음 | RG 검토 §2.7 | **RG 1.232** |
| `--space-ratio 0.12` | NEI의 공백 소실 89건을 모두 정확히 복원, 부작용 0 | NEI 검토 §5.1 | **NEI 18-04** (다른 파일은 미시험) |
| `--use-struct-tree` | NEI의 표(3-1, 3-2, 4-1, 5-x, Glossary, 약어)는 정확해진다. heading은 55절 중 3개만 heading이 되고, 본문 23단락이 heading으로 승격되어 악화된다 | NEI 검토 §5.1 | **NEI 표 이식용 보조 변환에만 사용** |
| `--keep-line-breaks` | 줄끝 하이픈 보존 → PDF 근거 하이픈 사전 생성에 활용 | NEI 검토 | 보조 변환 |
| `--table-method cluster` | 효과 없음(Table 4.2-2 누락 불변) | ch4, NEI | 사용 안 함 |
| `--markdown-with-html` | 2.5.7에서 `<td>`가 `&lt;td&gt;`로 이스케이프되는 버그(NEI 804건) | ch4, NEI | **사용 금지** |

실행 환경: PATH의 `java`는 Java 8이어서 실패한다(`UnsupportedClassVersionError`). `C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot\bin`을 PATH 앞에 두어야 한다.

### 2.2 재변환으로 해결되지 않는 결함 (후처리 대상)

- **하이픈 결합:** 줄끝 하이픈을 hyphenation으로 보고 제거한다. NEI는 식별자 7개와 단어 59개, RG는 식별자 21개와 단어 45개가 영향을 받는다.
- **윗첨자 소실:** 지수 부호와 각주 번호가 사라진다. PDF 문자 크기(본문 11.0 pt, 윗첨자 7.7 pt)로 식별할 수 있다.
- **각주 본문의 삽입:** 각주 본문이 문장 중간에 들어간다.
- **heading 판정 실패:** PSAR 번호 절이 목록 항목으로 분류된다. JSON 출력에서도 `list`로 분류되며, PSAR의 heading과 본문은 모두 Arial 11 pt라서 폰트로도 구분할 수 없다.
- **표 구조:** 테두리 없는 표를 인식하지 못하고, 쪽 분할 표를 병합하지 않고, rowspan을 채우지 않는다.
- **reading order 오류:** xycut 방식 때문에 ch3 LBE 표 29개가 이동했고, RG 2단 레이아웃에서 소제목 순서가 역전되었다.
- **벡터 도면:** 도면이 라벨 조각으로 분해된다.
- **PDF 텍스트층 자체의 손상:** NEI Cambria Math 수식, ch7b Figure 7.3.1-1/-2 라벨 인코딩, ch1 Figure 1.3-1 방벽 라벨 부재, ch7c 윤곽선화된 텍스트 도면 3개가 해당한다. 모두 수작업 대상이다.

### 2.3 원시 산출물 보존 원칙

- 재변환 원시 출력은 불변 원본으로 별도 보관한다(예: `references/_odl/`, 결정 사항 D1).
- 정제본은 스크립트로 재생성할 수 있어야 한다.
- `scripts/patch_underlines.py`는 적용하지 않는다. ch5에서 탐지 440개 중 실제 밑줄은 105개이고, ch4에서는 147개 전부가 오탐이다. 탐지 대상 경로도 현재 파이프라인과 다르다.

---

## 3. 목표 형식 (RAG 대비 규약)

| 요소 | 규약 | 근거 |
|---|---|---|
| frontmatter | `doc_id`, `title`, `doc_type`, `issuer/applicant`, `revision`, `date`, `adams`(있을 때), `source_pdf`, `pdf_pages`, `page_labels`(PDF 쪽↔인쇄 쪽), `converter`(버전과 옵션), `cleanup`(스크립트 버전과 날짜), `tables[]`, `figures[]`, `withheld[]`, `aliases`, `tags` | 인용, 필터링, 문서 식별 |
| 쪽 앵커 | `<!-- page 12 \| 4.2-7 -->` (PDF 쪽 \| 인쇄 쪽). PSAR은 바닥글 `4.2-7 Revision 1`에서 인쇄 쪽을 얻는다 | Obsidian 읽기 화면에서 보이지 않고, chunk별 쪽 인용 가능 |
| heading | 문서당 `#` 1개. 번호 절은 번호 성분 수 = 수준(`4.1` → `##`, `4.2.1` → `###`, `3.7.4.2.3` → `######`). 제목에 번호를 유지한다(`### 4.2.1 Plant Capability Summary`). 번호 없는 소제목(PSAR 밑줄, NEI BoldItalic)은 부모+1이며, H6을 넘으면 `**굵은 단락**`으로 쓴다. `References`는 `References (4.1)`로 고유화한다 | heading 경로가 chunk breadcrumb가 되며, 동명 heading(ch7 `References` 19개, NEI `Task 1` 3개)의 충돌을 막는다 |
| 표 캡션 | PSAR처럼 표·그림이 절 끝에 모이는 문서: 캡션을 heading으로 쓴다(소속 절 수준+1, 소속은 표 번호로 결정: Table 4.2-2 → 4.2). NEI·RG처럼 본문 중간에 표가 있는 문서: `**Table 3-1. …**` 단락 | PSAR에서 캡션이 heading이 아니면 표가 직전 `References` chunk에 귀속된다 |
| 표 본문 | 논리 표 1개 = Markdown 표 1개(sheet 병합, 반복 머리행 삭제). 머리행은 1행(다단 머리는 `상위: 하위`로 평탄화). rowspan은 fill-down으로 채워 행을 자기완결로 만든다. `<br>`은 공백으로 치환하되 열거 구분(`(1)`, `C.1` 등)은 `; `로 유지. 주석 `[a]`는 표 바로 아래 목록 | 행 단위 검색 시 문맥 손실 방지 |
| 긴 텍스트 표 | 셀 텍스트가 약 500자를 넘는 표(RG 부록 A–C, ch5 Tables 5.2-1–5.2-4, ch7 DL function 표)는 **record 형식**으로 쓴다. 예: `#### SFR-DC 4 — Environmental and dynamic effects design bases` + `Status` / `Criterion text` / `NRC rationale` 필드. 예시는 RG 검토 §5.1 | criterion·PSF 단위 검색. `wiki/SFRDC_n.md` 내용 채움과 대응 |
| 그림 | raster: 캡션 + `![Figure 1.1-2 Plant Layout](…png)` (alt = 캡션). 벡터 도면의 잔해는 삭제하고 `> [!figure] Figure 7.2.3-1 … (벡터 도면, 미전사; PDF p.N)` 콜아웃으로 대체. 정보성 라벨(범례, 설명 박스)은 콜아웃 안에 보존. 장식 이미지는 참조 삭제 | 임베딩 오염 제거와 사실 보존의 균형 |
| 지수 | `1×10⁻⁷` (유니코드 윗첨자; 결정 사항 D2). 표의 `8.13E-02` 표기는 원문대로 유지 | `10-7`은 범위·문서번호와 혼동됨. `^` 표기는 Obsidian 블록 참조와 충돌 가능 |
| 기타 첨자 | 기호: `k<sub>eff</sub>`, `σ<sub>bias</sub>`, `V<sub>S30</sub>`. 단위: `m²`, `n/cm²-s` | |
| 각주 | `[^n]` 참조와 절 끝(또는 문서 끝)의 `[^n]:` 정의 | Obsidian 네이티브 문법 |
| withheld | `> [!withheld] SRI — This information is withheld in accordance with 10 CFR 2.390` (문장 verbatim, `[[ ]]` 괄호 제거) | `[[…]]`은 Obsidian wikilink 문법과 충돌 |
| 개정 표시 | 선택: Rev. 1 change bar를 `<!-- rev1 -->` 주석으로 표시 (결정 사항 D7) | |

---

## 4. 공통 수정 사항: 권장 처리 파이프라인

Fix class는 세 가지로 나눈다.
- **A:** md만으로 가능한 결정적 규칙
- **B:** PDF 측 데이터 또는 재변환이 필요
- **C:** 수작업이나 판단이 필요

| 단계 | 내용 | class | 대상 |
|---|---|---|---|
| **P0 재변환** | §2.1 옵션으로 원시 출력 생성(PSAR: off-page + header-footer + page-sep; RG: off-page + strikethrough + page-sep; NEI: page-sep + space-ratio 0.12, 표 이식용 struct-tree 보조본). 재변환 후 PDF 대비 bag-of-words 비교로 누락 0 확인 | B | 전체 |
| **P1 보조 데이터 추출** | (a) heading whitelist: PSAR은 TOC 문자열, NEI는 pypdf outline 55개 + BoldItalic 소제목 68개, RG는 서체 위계. (b) 캡션 목록: LoT/LoF. (c) 밑줄 소제목 목록: 높이 약 0.8 pt의 filled rect, 페이지 header rule·표 격자 제외. (d) 줄끝 하이픈 사전: PDF `a-⏎b` 중 인라인 결합형이 0회인 형태만. (e) 윗첨자·각주 지도: 7.7 pt 문자. (f) 결함 표의 pdfplumber 셀. (g) 인쇄 쪽 라벨 | B | 전체 |
| **P2 잡음 제거·쪽 앵커** | 표지, 장식 이미지 참조, TOC/LoT/LoF(P1 수확 후), 머리글(`Kemmerer Unit 1 PSAR`, `SUBJECT TO DOE…`), 바닥글 → 쪽 앵커. 기타: `THIS PAGE INTENTIONALLY BLANK`, 2 pt 불가시 마침표(ch3 6줄), `##### .`(ch11), 캡션 접두어 `Kemmerer Unit 1 PSAR ` 제거 | A | 전체 |
| **P3 heading 재구성** | whitelist와 정확히 일치하는 위치에서 분리·승격. 목록 항목형, 평문형, 본문 앞뒤 접착형을 모두 처리. 번호 depth로 수준 결정. 가짜 heading 강등(ch3 문장 3개, `### σ`, `(Sheet n of m)`; NEI 도면 라벨; RG 각주·약어). RG 2단 역전 2쌍 교환. 참고문헌 항목(`- 4.1-1 …`, 하이픈 번호)은 heading 정규식에서 제외 | A (+B whitelist) | 전체 |
| **P4 문단·목록 복원** | 쪽 경계 분할 결합: 앞 줄에 종결부호가 없고 다음 줄이 소문자, `Section`, `(Reference`로 시작하면 `- `를 제거하고 결합. 가짜 목록 기호 제거(ch7 `- Consistent with PDC` 230개, NEI `- As/At …`). 중첩 목록 복원(PDF x0 기준). 목록 내부 빈 줄 제거. 2,000자 초과 병합 문단은 PDF 문단 시작 좌표로 재분할 | A / B | 전체 |
| **P5 각주** | 명시 목록 기반으로 `[^n]` 치환(RG 14, NEI 16, ch6 표 각주). 각주 본문을 이동하고 끊긴 문장을 재결합. 일반 정규식(`[a-z]\d`)은 `SFR-DC17` 등을 오탐하므로 금지 | A (목록) | rg, nei, ch6 |
| **P6 표** | 논리 표 단위 sheet 병합, 반복 머리행·`(continued)` 삭제, group label을 캡션·부제로, fill-down. 결함 표는 pdfplumber 셀로 교체(ch6 하중조합 12 sheet, ch11 Table 11.5-1 row 5.0). 테두리 없는 표 재구성(ch7 27개/167행; `ch7c_dltab.py` 방식). NEI 표는 struct-tree본 이식 후 교정. 긴 텍스트 표는 record 형식으로 | A / B | 전체 |
| **P7 그림** | 벡터 잔해 span 삭제(캡션 앵커 기준, `X` 전역 삭제 금지). 정보성 라벨은 콜아웃이나 표로 보존(ch1 부지 범례 31항목 → 표). raster alt text 부여. 장식 fill 이미지 참조 삭제(ch1 imageFile8–14, ch11 imageFile4–12, ch7 imageFile41–46, NEI imageFile5) | A / C | 전체 |
| **P8 문자·수치** | entity decode(`&amp;` ch7 72개 외). bullet glyph(`•`, `o`, `●`, `▪`) → Markdown 목록. PDF 근거 하이픈만 복원. em dash 복원. 지수 정규화(`(\d)\s?[x×]\s?10-(\d+)` → `×10⁻ⁿ`, TOC 쪽번호·문서번호 오검출 제외, NEI는 `/plant` lookahead). 첨자 토큰 사전. Obsidian 위험 문자(`$`, 행두 `*`, `[[`) escape | A / B | 전체 |
| **P9 수작업** | §6 목록 | C | 파일별 |
| **P10 frontmatter** | §3 키. 식별자 목록(LBE ID, PSF/DL ID, PDC/SFR-DC 번호, 계통 약어)은 검토 파일 §5 참조 | A | 전체 |
| **P11 회귀 검증** | §8 | B | 전체 |

### 4.1 공통 결함 규모 (검토 파일 집계)

| 항목 | nei | rg | ch1 | ch3 | ch4 | ch5 | ch6 | ch7 | ch11 |
|---|---|---|---|---|---|---|---|---|---|
| off-page 누락 (재변환 복원) | 0 | 20 구간 | 157 단어 | 16 | 1열(11값)+머리 | 701 | 312 | 24 | 11 |
| 번호 절 중 Markdown heading | 41/55 (35개 수준 오류) | 본문 28/32 (수준 오류), criterion 0/178 | 0/74 | 2/458 | 0/15 | 0/67 | 0/74 | 1/289 (수준 오류) | 0/127 |
| heading–본문 접착 | 6 | 4 | 2 | 45행 | – | 7 | 10 | 39 | 8 |
| 밑줄/BoldItalic 소제목 미heading | 9/68 | – | – | – | – | 11 소실 | 98 | 약 284 | 7 |
| 캡션 누락 (header-footer로 복원) | 0 | 1 | 3 표 | 6 표/15 sheet | 0 | 0 | 6 표 | 0 (FHP 표 머리행 누락) | 2 표/11 sheet |
| 쪽 분할 표 미병합 | 4 표 | 123 블록 → 4 표 | 59 조각 | 7 표/17 블록 | – | 다중 sheet 18 | 8 표 | 반복 머리 6 | 2 표/11 sheet |
| 테두리 없는 표 붕괴 | 14 블록 1열화 | – | – | – | – | – | – | 27 표/167 행 | row 5.0 |
| 문단 분할 (가짜 목록 포함) | 27 | 13 | 13 (+5) | 24 | 1 (+8) | 16 | 13 | 210 | 26 |
| 지수 윗첨자 소실 | 47 (+ 부호 반전 3) | 0 | 0 | 10 | 40 | 0 | 1 | 1 (+단위 4) | 0 |
| 각주 결합·삽입 | 16 | 14 | – | – | – | – | 약 10 | `*`/`**` 파손 | – |
| 하이픈 결합 (식별자) | 59 (7) | 45 (21) | 7 | 7 | – | – | 3 | 소수 | 1 (C) |
| HTML entity | 11 | 0 | 18 | 1 | 2 | 0 | 0 | 72 | 24 |
| 벡터 도면 잔해 | 5 도면, 5.0 k자 | – | 258 행 | – | – | – | – | 약 300 행, 가짜 표 46+ | 3 조직도 |
| 순수 잡음 비율 (문자) | 7.9 % | 5.0 % | 5.7 % | 4.2 % | – | – | – | 5.7 % (7a 구간) | 4.2 % |
| 강조(italic) 소실 | 3.4 k자 | 315 run | bold 5 | – | – | – | – | 약 395 run | 23 |
| Rev. 1 change bar | – | – | 38 | 140 | 9 | 25 | 미집계 | 175+ | 48 |

값은 각 검토 파일의 집계를 그대로 옮긴 것이다. "약"으로 표시한 값은 추정치이고, "–"는 해당 없음 또는 미집계이다.

---

## 5. 파일별 핵심 수정 사항 (H 우선)

### 5.1 NEI 18-04

- **H 지수 부호 반전 3건:** L347 `1×104/plant-year`, L370 `10-4 to 102/plant-year`, L911 `greater than 102/plant-year`. PDF에서 `10-⏎2`로 줄이 바뀌는 위치에서 부호가 제거된 것이다. DBE 하한과 SSC 위험중요도 기준이 오염되어, md 안에서 L427·L1873의 정상값과 서로 모순된다. 명시 치환으로 교정한다.
- **H 표 붕괴:** Tables 3-1, 3-2, 5-1, 5-3, 5-4, 5-5, 5-7, 5-8과 Glossary 6블록이 1열로 붕괴했다. Table 4-1(√ 26개)과 5-9·5-10은 체크 행렬을 잃었다. 약어표는 문단 조각으로 풀렸다. struct-tree 보조본의 표를 이식하고, Table 4-1 RISC-2 행은 1칸 교정한다. Table 5-2는 rowspan 때문에 수동 재작성한다.
- **H 수식:** Table 3-2 수식 8개와 식 R_j는 PDF 텍스트층의 Cambria Math ToUnicode가 손상되어 있어(`base` → `𝑏𝑏𝑏𝑏…`) 재변환으로도 복구할 수 없다. 렌더링 이미지를 기준으로 수작업 전사한다. 정답 수식은 검토 파일 §2에 있다.
- **H heading:** outline 55절 중 14절이 heading이 아니다(4.2, 4.2.1, 5.9.x 등). 이 때문에 본문이 직전 절에 귀속된다. 나머지 35절은 깊이와 무관하게 모두 `#####`이다. outline과 BoldItalic 11 pt 소제목 68개로 재구성한다.
- **H 식별자 7건:** `NEI-0004`, `ASME/ANS-Ra-S-1.42013`, `RIPBDM`, `TIRIPB`, `defense-indepth` 등. 각주 16개 중 6개가 문장을 둘로 나눈다.
- **M:** 하이픈 결합 59건(`risksignificant` ×10 등), 공백 소실 89건(재변환으로 해결), 벡터 도면 5개의 잔해, raster 그림 5개에 alt text 없음(Fig 5-3의 층별 목표 문구는 본문에 없음), 중첩 목록 33항목의 평탄화.

### 5.2 RG 1.232

- **H Table 1 redline:** 셀 29개가 영향을 받는다. 삭제어가 일반 텍스트로 남은 경우가 22개이고(예: ARDC 14가 `Reactor coolant pressure boundary.`로 표기되나 실제 제목은 "Reactor coolant boundary"), 단어가 누락된 경우가 7개이다. 재변환(`detect_strikethrough`)으로 삭제어를 표시하고, 삽입어는 PDF 청색 문자로 `<ins>`를 붙인다. 이후 "최종 제목 / 상태 / redline" 열로 분리한다.
- **H 누락 20개 구간:** off-page 필터로 사라졌다. GDC 19 rationale의 `safely` ×3, `Refer to the` ×3 등이 해당하며, 재변환으로 복원된다.
- **H 각주 결합 14건:** `10 CFR 50.342`, `PDC4`, `(Ref. 2)1`, URL 끝 `…580012`, `### REFERENCES7` 등. 명시 목록으로 `[^n]`을 적용한다.
- **H 식별자 하이픈 21건:** `SFRDC` ×13, `MHTGRDC` ×3, `SECY-150002`, `SECY94-084`, `NUREG1368`, `gen4.org`, `NPTDSmexico`.
- **M 표 분할:** 표 4개가 123블록으로 쪼개져 있다. 연속행 73개에는 criterion 번호가 없고, criterion 178개 중 62개가 여러 블록에 분산되어 있으며 그중 43개는 문장 중간에서 끊긴다. 부록 셀에서는 italic 제목, 상태행, 본문이 한 문자열로 이어져 있다. 개선안은 criterion record 형식이다(§3). 부록 B 65개 criterion 전수 무결성 표는 검토 파일 §2.2에 있다.
- **M 기타:** 각주 본문 14개가 본문 중간에 삽입되어 있다. 2단 레이아웃 heading 역전 2쌍, 가짜 heading 5개, 매몰 heading 4개가 있다. 약어 42개가 두 문단으로 평탄화되어 있다. 표지 텍스트 박스가 목록 사이에 삽입되어 있다.

### 5.3 PSAR ch1

- **H heading 부재:** 번호 절 74개가 모두 heading이 아니다. 이 때문에 §1.1이 `LIST OF FIGURES` 아래로, §1.3이 `Figure 1.2-1` 아래로, Tables 1.4-4/-5(214행)가 `Table 1.4-3` 아래로 귀속된다.
- **H 재변환으로 복원되는 누락:**
  - Figure 1.2-1 범례 31항목(시설 번호↔명칭). 복원 후 표로 구성한다.
  - RG 1.183 행의 `methodologies`
  - `]]SRI` 7개
- **H 하이픈 소실 7건:** `NATD-LIC-RPRT0002-A` 등. PDF에서 `-⏎`로 확인된 7건만 복원한다.
- **M 캡션 누락:** Tables 1.4-1/-4/-5와 약어표 제목이 없다(header-footer로 복원).
- **M Table 1.4-1:** 26 sheet를 병합해야 하며, 183행 중 26행은 Conformance Status와 Comments가 붙어 있어 분리해야 한다.
- **M 기타:**
  - withheld 표시 13건은 콜아웃으로 정규화한다.
  - Figure 1.2-1의 `X` 울타리 잔해 218행과 Figure 1.3-1 잔해 40행을 정리한다. Figure 1.3-1의 방벽 라벨 5개는 PDF 텍스트층에 없다.
  - `V_S`, `V_S30`의 아래첨자가 소실되었다.

### 5.4 PSAR ch3

- **H LBE 결과표 29/88개가 다른 절에 있다(19개 LBE).** PDF에서는 표가 모두 "… are listed below." 바로 뒤에 있으나, md에서는 다음 heading 뒤로 밀렸다. 문장 88개와 표 88개는 종류별 순서가 일치하므로, i번째 문장 뒤로 i번째 표를 옮기는 결정적 규칙으로 교정할 수 있다(모의 적용 88/88 일치). 이동 후 각 LBE에 종류별 표가 1개씩 있는지 검증한다. 이동 전 모든 heading 수준을 추적해야 한다.
- **H Table 3.5-4:** LPZ 열 머리가 소실되었고(재변환으로 복원), DBE 7행에서 DBA ID·제목·선량이 비어 있다(fill-down).
- **H fill-down 필요:** Table 3.1-3 `Analysis` 27행, Table 3.1-2 `Screening Category` 105행.
- **H 캡션·배치:** 캡션 15개가 누락되었다(header-footer로 복원). 초기조건 표는 §3.3.4.2가 아닌 §3.3.4.3 아래에 있다(수작업 이동).
- **H 지수 10건:** AOO/DBE/BDBE 빈도 경계가 포함된다.
- **H §3.14 수식:** 기호 9개 소실, 고아 기호 줄 5개, 식 번호 순서 역전. 정답 블록은 검토 파일 §5-4에 있다.
- **H 매몰 heading:** L2388에 RPD-SS-4 heading이 행 중간에 매몰되어 있다.
- **M heading:** 번호 절 458개 중 heading은 2개이다. 접착 45행, LBE 제목 2줄 분할 5건, 가짜 heading 10개가 있다.
- **M 선원항 표:** 머리행이 틀렸고, Tables 3.2-4 to 3.2-6은 Plenum/Non-Plenum 부분표가 섞여 동일 동위원소가 2회 나온다. 표에 `Release` 열을 추가하거나 부분표를 분리한다.
- **보존:** 반복 문장(51회 등), 서로 다른 LBE의 동일 선량표, `K-effective 1.0`(PDF에도 ≤ 기호 없음).

### 5.5 PSAR ch4

- **H Table 4.2-2:** `Mean Dose Margin[d]` 열의 머리와 값 11개(3.79, 3.09, 4.25, 9.90, 4.10, 17.2, 8.22, 3.08, 13.3, 4.42, 15.0)가 없다. Table 4.2-1도 머리가 없다. 재변환으로 복원된다.
- **H 지수 40건:** `5×10-7` 등.
- **M 표 머리·rowspan:** Tables 4.2-3/-4의 2단 머리가 평탄화되었고 rowspan이 채워지지 않았다.
- **M 기타:** heading 15개가 모두 목록 항목이다. 가짜 목록 8건, Notes 반복, change bar 9개.

### 5.6 PSAR ch5

- **H 재변환(off-page)으로 복원되는 누락:**
  - SRDC 열 57셀 중 55셀이 절단되어 756/2,281 단어(33 %)가 소실되었다.
  - Table 5.2-4의 SSC 셀 5개가 잘렸다. `AMC`가 소실되고 존재하지 않는 계통명이 생성되었다.
  - Table 5.2-3 Note 1이 잘려 `RFH-FDIV-CN`이 소실되었다.
- **H 밑줄 소제목 11개 소실:** 이 때문에 PDC 요건 본문과 이행 요약이 서로 이어진다. header-footer 옵션으로 복원된다.
- **H PSF ID 빈 행 93개:** DL3-RR2는 32행으로 쪼개져 있고, 문장 하나가 두 행에 걸쳐 있다. 이 분할은 재변환 후에도 남으므로 fill-down과 행 병합이 필요하다. 다중 sheet 표는 병합하고, PSF 62개는 record 형식을 검토한다. PSF별 무결성 목록은 검토 파일 §2a에 있다.
- **M:** heading 67개 중 61개가 목록 항목이고 6개가 접착형이며, §5.3.2는 문단 끝에 매몰되어 있다. 문단 분할 16건.
- **주의:** ch5의 밑줄은 소제목 표시일 뿐이다. RG 1.232 대비 변경 표시가 아니다.

### 5.7 PSAR ch6

- **H 하중조합 Tables 6.4-5/-6/-7/-8/-11/-12:** 셀 245개가 누락되었다. 하중계수 179/522개(34 %)와 하중 case·식 번호 라벨 66개이며, SSE(Ess) 계수 11개가 전부 사라져 SSE가 어떤 조합에도 없는 것처럼 보인다. 재변환으로 복원되며, 검증 기준은 비공란 하중계수 522개이다.
- **H 캡션 6개 누락:** 6.4-2, -4, -7, -8, -11, -12. 6.4-7/6.4-11, 6.4-8/6.4-12는 구조가 같아서 캡션 없이는 값을 어느 표에 귀속할지 판별할 수 없다. 페이지 번호로만 귀속한다.
- **H 표 주석 9개 절단(11곳):** 재변환 출력에서 절단 조각(`Guidanc`, `wi`, `fact`, `Y`)이 온전한 단어로 대체되므로 복원되는 것으로 판단된다. 주석별 대조는 정제 단계에서 수행한다.
- **M:**
  - heading 74개가 목록 항목이고 10개는 접착형이다.
  - 밑줄 소제목 98개 중 88개가 문단에 접착되어 있고, 설계 과도 제목 30개는 목록 항목이다.
  - IBC 하중조합 7개가 한 줄에 있고, 기호 범례가 압착되어 있으며, λ 블록이 깨졌다.
  - 각주 첨자가 결합되어 있다(`FHB2`, `RAB2`, `Motion1`).
- **보존(원문 결함):**
  - α 값 부재, Table 6.4-9 열 어긋남, L577 교차참조 오류
  - `Yi (7)`, `A. 9`, mesh 식의 좌변 부재
  - 값을 추정하거나 이동하지 않는다. 필요하면 편집 주석만 단다.

### 5.8 PSAR ch7 (3개 구간)

- **H 테두리 없는 DL function / Functional Support 표 27개(167행)가 산문으로 풀렸다.**
  - 행 순서 오류: RPS DL3-HR3의 지원 설명이 ID보다 앞에 있고, DL4-HR7과 DL4-RR8이 병합되었다.
  - RIS: RC1e/h/j의 지원 설명이 RC1e 하나로 병합되었다.
  - RMS: 표가 §7.6.6.2.2 아래에 있으나 §7.6.6.2.1에 속한다.
  - SR/NSRST 태그가 행에서 벗어난 경우가 6건이다.
  - 재구성 방법: PDF 단어 좌표로 3열 경계를 산출한다(`ch7c_dltab.py`, 77행 재구성 확인). 기대 ID 목록으로 품질을 검사한다.
- **H 가로 페이지 셀:** Table 7.1.2-4와 7.1.3-6의 Notes 7셀이 누락되었다(재변환으로 복원).
- **H 지수:** `3.98 x 1015 n/cm2-s`는 10¹⁵이다.
- **M heading 체계:** 번호 절 289개 중 Markdown heading은 1개(수준 오류)이다. 밑줄 소제목 약 284개가 문단에 접착되어 있고, 그중 6개는 앞 문단 끝에 붙어 있다.
- **M 문단:** 가짜 목록 기호가 약 430개이며 그중 `- Consistent with PDC`가 230개이다. 분할 210건이 있고, PDF 문단 경계 약 480개가 소실되었다(병합).
- **M 도면:**
  - 도면 잔해 약 300행과 가짜 표 46개 이상이 있다.
  - Figure 7.3.1-1/-2(라벨 인코딩 불가)와 7.6.5-1, 7.6.6-1, 7.6.8-1(윤곽선 텍스트)은 md에 내용이 없다.
  - Figures 7.2.3-1/-2의 SR/NSRST/NST 분류는 상자 색으로만 표시되어 있어 PDF 채움색에서 복원해야 한다.
- **L:**
  - `&amp;` 72개
  - italic 약 395 run 소실(PDC·RG 제목)
  - change bar 175개 이상
- **보존:**
  - 반복 문장(`Security for I&C…` 6회, `XIS includes sensors…` 8회, 연속 중복 1쌍)
  - 원문 오기(`poistion`, `Contol`, `DL3- HR2`, `SCN3` 등)
- **결정 사항 D5:** 828 KB 단일 파일을 계통 단위로 분할할지 여부

### 5.9 PSAR ch11

- **H Table 11.5-1 row 5.0:** 병합 셀이 12행 × 3열로 절단되었다. 단어 14개가 중간에서 쪼개졌고 글자 3개가 중복되었다(`res|sponsibility`). 재변환으로도 남으므로 pdfplumber 셀로 교체한다.
- **H 캡션 11개 누락:** Tables 11.2-2와 11.5-1(header-footer로 복원). 표 귀속이 틀어진다.
- **H heading 접착 8건:** §11.3 heading과 도입부 1,684자가 한 문단이다. §11.4는 `[[…]]SRI`와 결합되어 있다. L1599(2,889자)는 소제목 3개와 문단 6개를 합친 것이다.
- **H 조직도 라벨 4개:** 회전 쪽 p17–18에서 누락되었다(재변환으로 복원, 확인 완료).
- **M:**
  - 번호 절 127개 중 heading 0개
  - 운전 모드 정의 4개가 모두 가짜 목록 항목이고, Mode-2 정의는 쪽 경계에서 분할되어 있다. 이 결과는 PDF p65–66과 반드시 대조한다.
  - Figure 11.1-2는 raster 전용(22개 직위)이므로 alt text나 전사가 필요하다.
  - imageFile4–12는 흰색·검은색 사각형이다(삭제).
- **파일명 유지:** `wiki/Natrium_Reactor_Operating_Modes.md`가 `[[TP_Natrium_PSAR2025_ch11_Conduct of Operations]]`로 참조한다.

---

## 6. 수작업(C) 목록

| 파일 | 항목 | 비고 |
|---|---|---|
| nei | Table 3-2 수식 8개와 식 R_j 전사 | PDF 텍스트층 손상. 정답은 review_nei §2 |
| nei | Table 5-2 재작성(5행 × 4지침열, rowspan 채움) | struct-tree본도 어긋남 |
| nei | raster 그림 alt text와 필요한 전사 (Fig 3-1 F-C target 앵커, Fig 5-3 층별 목표, Fig 4-1 주석) | 수치 추정 금지 |
| rg | `Background` 하위 7개 소제목의 수준(H3/H4) 결정 | PDF 서체로는 판별 불가 |
| ch1 | Figure 1.3-1 방벽 라벨 5개 | 텍스트층 부재. OCR 또는 수동 |
| ch3 | §3.14 수식 블록 치환(정답 블록 있음), 초기조건 표 이동, LBE 2개의 하위절 순서 | review_ch3 §5-4 |
| ch6 | λ = V/f 블록, 기호 범례 12항목, Table 6.4-9 편집 주석 | 원문 결함은 값 불변 |
| ch7 | Figure 7.3.1-1/-2 라벨, 7.6.5-1/7.6.6-1/7.6.8-1 도면 처리(쪽 raster 삽입 여부 D3), Figures 7.2.3-1/-2 분류 색 복원 | |
| ch11 | Figure 11.1-2 직위 22개 전사 여부, `ChiefNuclear` 등 판단 항목 | |

---

## 7. 자동 수정 금지 (원문 그대로 유지)

- **원칙:** PDF에 그대로 있는 표기는 변환 결함이 아니다. 필요하면 `<!-- sic -->` 주석만 단다. 파일별 전수 목록은 각 검토 파일 §5에 있다.
- **대표 예:**
  - NEI: `stan`, `mean -frequency`, `complimentary`, `Acronymns`
  - RG: `watercooled`, `fire- resistant`, `SFR-DC17`, `(Criterion 1 – 15)`, `SFR-DFC`, `SARRDLS`
  - ch1: `HCI`, `conditions.Each`, `power- operated`, `an station blackout`
  - ch5: `sends a sends a signal`, FHP 계통명 불일치
  - ch6: α 값 부재, Table 6.4-9 열 어긋남, `Yi (7)`
  - ch7: `poistion`, `Contol`, `B.31.1`, `e.q.`
  - ch11: `Program Plant and Methodologies`, `NRSRT`
- **하이픈:** 사전 기반 dehyphenation과 re-hyphenation을 금지한다. PDF에서 줄끝 `-⏎`로 확인된 형태만 복원한다. 같은 셀 안에서도 `nonessential`(소실)과 `non-essential`(정상)이 공존한다.
- **반복 제거 금지:** 반복 문장, 동일 값 표, 원문 각주 중복(RG fn 1 = fn 4 등), 반복 special-treatment 목록은 모두 원문이다.
- **전역 삭제 금지:**
  - `X` 줄: `X/Q`, 범례 `X X FENCE`가 있다. 캡션 앵커 기준 span 삭제만 허용한다.
  - `<br>`: 열거 구분이 있다.
  - `Kemmerer Unit 1`: 본문 고유명사이다. `Kemmerer Unit 1 PSAR`와 정확히 일치할 때만 제거한다.

---

## 8. 회귀 검증 기준

1. **본문 보존:** 쪽 단위로 PDF 대비 정제본의 bag-of-words 차이를 계산한다. 허용 잔차는 머리글·바닥글, 표지, TOC, 도면 잔해, 원문 오기 교정 불가 항목뿐이다.
2. **표 셀:** 결함이 확인된 표 전부와 무작위 표본에 대해 pdfplumber 셀과 비교한다. 예: ch6 하중계수 비공란 522개, ch4 Table 4.2-2 8열 11값, RG 부록 criteria 178개의 단어 diff 0.
3. **heading:** whitelist 대비 누락 0, 가짜 heading 0, 수준 규칙 위반 0.
4. **귀속 검사:**
   - ch3: 각 LBE 절에 announced 표 종류별로 표가 정확히 1개 있어야 한다.
   - ch7: DL 표의 기대 ID 목록과 일치해야 한다.
   - ch5: PSF 62개 각각에 SRDC가 있어야 한다.
5. **잔재 0:** dot leader, `&amp;`류 entity, `[[` 비링크 사용, 단독 `Kemmerer Unit 1 PSAR`, `(Sheet n of m)` heading.
6. **검증 스크립트:** 검토에 사용한 스크립트(`ch3_simfix.py`, `ch6_cmp.py`, `ch7c_dltab.py`, `rg_crit.py` 등)는 scratchpad에 있다. 정제 스크립트의 테스트로 전환할 수 있다.

---

## 9. 결정이 필요한 사항

| ID | 사항 | 권장 |
|---|---|---|
| D1 | 원시 재변환 출력과 정제본의 위치 | `references/_odl/`(원시, 불변, RAG 색인 제외) + `references/*.md`(정제본, 동일 파일명) |
| D2 | 지수 표기 | `1×10⁻⁷` (유니코드 윗첨자). 대안: `1×10^-7`, `1E-07` |
| D3 | 벡터 도면 처리 | 잔해 삭제 + 콜아웃. 내용 보존이 필요한 도면(ch7 SLD, I&C 구조도)만 쪽 raster 이미지를 추가 |
| D4 | TOC/LoT/LoF | 삭제(heading과 frontmatter `tables[]`/`figures[]`로 대체) |
| D5 | ch7(828 KB) 분할과 파일명 정규화(공백, 쉼표 제거) | 분할은 선택. 파일명 변경 시 `wiki/Natrium_Reactor_Operating_Modes.md`의 wikilink 1건 갱신 필요 |
| D6 | 긴 텍스트 표의 record 형식 전환 범위 | RG 부록 A–C(178 criteria), ch5 PSF 표, ch7 DL 표 |
| D7 | Rev. 1 change bar, italic 강조 | 선택 사항. RG criterion 제목 italic은 필드 분리로 대체되므로 불필요 |

---

## 부록 A. 파일별 상세 검토 파일 (scratchpad, 세션 한정 경로)

`C:\Users\User\AppData\Local\Temp\claude\C--Obsidian-ripb\db35be0e-3624-48f5-a63d-95732c7feeca\scratchpad\`

| 파일 | 범위 | 주요 내용 |
|---|---|---|
| review_nei.md | NEI 18-04 전체 | 40 findings, 표 정답 행렬, outline 55 + 소제목 68, struct-tree 비교 |
| review_rg.md | RG 1.232 전체 | redline 29셀 목록, 각주 14, 하이픈 67, 부록 B 65 criteria 무결성 표, record 예시 |
| review_ch1.md | ch1 전체 | 표 62개 전수 대조, withheld 13, 도면 잔해 span |
| review_ch3.md | ch3 전체 | LBE 표 88개 귀속 표, 수식 정답 블록, outline 458 |
| review_ch45.md | ch4 + ch5 | off-page·header-footer 원인 규명, PSF 62개 무결성 |
| review_ch6.md | ch6 전체 | 하중조합 셀 대조, 원문 결함 목록 |
| review_ch7a.md | ch7 L1–2388 | TOC, §7.1–7.2.3, 분할 74건 목록 |
| review_ch7b.md | ch7 L2389–4273 | §7.2.4–7.5, 분할 45건 목록, 소제목 63 |
| review_ch7c.md | ch7 L4274–7207 | §7.6–7.8, DL 표 재구성 기대 ID 목록 |
| review_ch11.md | ch11 전체 | heading whitelist 127, row 5.0 재구성 |

재변환 실험 출력은 scratchpad `reconv/`(ch1·3·4·5·6·7·11)와 `nei/`, `reconv_offpage*/`(RG), `ch45_tmp/`에 있다.
