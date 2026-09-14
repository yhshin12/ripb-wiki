# Review ch45 — PSAR Chapter 4 + Chapter 5 (READ-ONLY)

두 파일 모두 전 범위를 검토함. Part A = ch4, Part B = ch5. 공통 결론과 재변환 실험은 Part C에 정리함.

**핵심 결론(두 장 공통, 실험으로 검증됨)**

1. **`/Rotate 90` 가로 페이지의 텍스트 손실 원인 = opendataloader `off-page` content-safety filter.** 가로 페이지(ch4 p.12–15, ch5 p.6–20)에서 표시 좌표 x ≈ 792 pt(세로 MediaBox 폭) 너머에서 시작하는 text chunk가 버려짐. ch4 Table 4.2-2 `Mean Dose Margin[d]` 열 소실과 Table 4.2-1 헤더 소실, ch5 SRDC 셀 55/57개 절단, Table 5.2-4 SSC 5셀 절단, Table 5.2-3 Note 1 절단이 모두 이 원인임. `--content-safety-off off-page`로 재변환하면 전부 복원되고 다른 차이는 생기지 않음(ch4: 차이 = 복원된 열뿐, ch5: 704 token / 104 span 복원). 참고: `reconv/ch4_cluster`(`--table-method cluster`)는 이 열을 복원하지 **못함**.
2. **ch5에서 underline 소제목이 빠진 원인 = header/footer filter 오판.** underline된 소제목(`Implementation Summary`, `Relevant PSAR Chapters and Sections`)이 여러 페이지에서 running header 바로 아래 같은 y = 286.7 pt에 반복되는데, 이 반복 요소를 header로 판단해 삭제함. `--include-header-footer`로 재변환하면 53/53, 53/53이 모두 돌아옴(형태: `#### Kemmerer Unit 1 PSAR Implementation Summary`). 두 옵션을 함께 쓰면 ch5의 PDF token 누락이 724 → 0으로 줄어듦. 늘어나는 것은 header/footer 줄뿐이며 결정적으로 제거할 수 있음.
3. 코퍼스 전체 영향(미검증, 추정): `/Rotate 90` 페이지가 RG 1.232 109쪽, ch1 39쪽, ch7 25쪽, ch6 14쪽, ch3 4쪽, ch11 2쪽에 있음. 이 페이지들의 오른쪽 부분 텍스트도 같은 방식으로 잘렸을 가능성이 높음.

---

# Part A — Review ch45/ch4: `TP_Natrium_PSAR2025_ch4_integrated evaluations.md` (md lines 1–287, PDF pages 1–16)

## 0. 개요

| 항목 | 값 |
|---|---|
| md | 287 lines(Read 기준), 26,252 chars |
| PDF | 16 pages. p.1 표지, p.2 TOC, p.3 LOT, p.4–11 본문(4.1-1 … 4.2-6), p.12–16 Tables 4.2-1…4.2-5. **p.12–15는 `/Rotate 90`** |
| Tables | 5개(전수 검증) |
| Figures | 0개(본문 figure 없음). 표지 raster 3개 |
| Sections | 장 제목 1 + 번호 절 15(4.1, 4.1.1–3, 4.2, 4.2.1, 4.2.1.1–4, 4.2.2, 4.2.2.1–3, 4.2.3) + `References` 2 |
| 누락 검사 | bag-of-words: PDF 3,720 token 중 md에 없는 것은 **19 token**(A1/A2의 열 헤더 2개와 값 11개)뿐. md prose 85줄은 모두 PDF와 verbatim 일치 |
| Noise 추정 | 표지 6줄/446 chars + TOC·LOT 15줄/1,554 chars + header 잔재 1(20 chars) + `<br>` 4 ≈ **2,040 chars(7.8 %)**. 3줄 이상 연속 빈 줄 33곳 |
| 개정 표시 | change bar 9개 / 6쪽(≈73 text lines) 소실 |

## 1. Findings

| # | T-ID | Sev | Count | md lines (examples) | PDF p. | Evidence / description | Proposed fix | Fix class |
|---|---|---|---|---|---|---|---|---|
| A1 | T6/T14 | H | 1열(헤더 + 값 11개) | L236 `…[rem][c]\| \|`, L238 `\|RFH-FDIV-1\|DBE\|8.73x10-3\|0.290\|3.45x10-1\|39.5\|1.10\| \|` | 13 | Table 4.2-2의 마지막 열 `Mean Dose Margin[d]`가 헤더와 값 11개(3.79, 3.09, 4.25, 9.90, 4.10, 17.2, 8.22, 3.08, 13.3, 4.42, 15.0) 모두 사라지고 빈 8번째 열만 남음. Note [d] 정의(L251)는 남아 있어 사라진 열을 설명하는 모순 상태. **원인: off-page filter(C.1).** `--content-safety-off off-page`로 재변환하면 헤더와 11개 값이 모두 복원됨(검증) | 재변환(권장). 대안은 PDF 값 11개 주입 | B |
| A2 | T6 | H | 헤더 1셀 | L219 `…Frequency (rem)[c]\| \|` | 12 | Table 4.2-1의 8번째 열 헤더 `Mean Dose Margin[d]`가 없고 값 15.1/15.8/11.3만 있음. 라벨 없는 열이라 retrieval에서 의미를 알 수 없음. 원인 동일, 재변환으로 복원(검증) | 재변환. 또는 헤더 문자열 삽입 | B (A 가능) |
| A3 | T8 | H | 40(본문 11, 표 29) | L47 `5×10-7`, L61 `3.12×10-3`, L70 `3.86×10-9`, L128 `1x10-2 … 1x10-4`, L221 `3.40x10-5`, L241 `3.72 x10-4` | 4–5, 7–8, 12–14 | 위첨자 지수가 사라져 `10-7`이 "10 − 7"로 읽힘. `×` 8건과 `x` 32건이 섞여 있고, 공백이 있는 변형 1건(L241)은 PDF 원문도 `3.72 x10-4`임. Table 4.2-3 헤더(L255 `1x10-4/plant-year`)도 포함 | regex `(\d(?:\.\d+)?)\s?[x×]\s?10-(\d+)` → `\1×10⁻\2`(Unicode 위첨자). 공백·`x` 정규화 여부는 정책으로 결정 | A |
| A4 | T6 | M | 2 tables | L255–257, L267–269 `\| \|DL Function\|Description\| \|` | 14–15 | 2단 헤더가 평탄화됨. 상위 헤더 `Maintain Frequency of all BDBEs &lt; 1x10-4/plant-year`(colspan 2)는 2열에만 있고 3열 헤더는 공백. 하위 헤더가 데이터 행으로 들어감. Table 4.2-4도 `Functions to Maintain Individual Risks &lt; QHOs`로 같은 문제 | 헤더 합성(예: `DL Function (Maintain Frequency of all BDBEs < 1×10⁻⁴/plant-year)`) 후 하위 헤더 행 삭제 | A(규칙) / C(표기) |
| A5 | T6 | M | 2 rows | L259 `\| \|DL3-RR3a\|Ex-Vessel Handling Machine to Head Barrier Function\| \|`, L261 | 14 | rowspan이 채워지지 않음. RFH-FDIV-1/-3의 두 번째 기능 행에서 DBE ID와 4열 판정(`No. There is no single…`)이 공백이라 행만 떼어 검색하면 DBE를 알 수 없음 | fill-down | A |
| A6 | T6/T11 | L | `<br>` 4, `&lt;` 2 | L262 `The only difference between the DBE,<br><br>RFH-FDSP-1, and BDBE,<br>RFH-FDSP-2, events…<br>`; L255, L267 | 14–15 | 셀 안 줄바꿈 잔재와 HTML entity | `<br>` → 공백, `&lt;` → `<` | A |
| A7 | T6 | L | 1 | L251 `Notes: [a] Frequency value … [d] Ratio of the dose in Note [c] …` | 13 | Table 4.2-2의 Notes [a]–[d]가 한 문단으로 합쳐짐(Table 4.2-1은 목록 L226–231) | ` \[([b-d])\]` 앞에서 나누어 목록화 | A |
| A8 | T4 | M | 1 | L280 `### Kemmerer Unit 1 PSAR Table 4.2-5 DBA with Single Feature Reliance` | 16 | 페이지 헤더가 표 캡션 heading에 병합됨 | 접두어 `Kemmerer Unit 1 PSAR ` 제거 | A |
| A9 | T1 | M | 6줄(446 chars) + images 3 | L1, L3, L11(images), L5 `# Kemmerer Power Station Unit 1 PSAR, Chapter 4`, L7 `## US SFR Owner, LLC, a wholly owned subsidiary of TerraPower, LLC`, L9 DOE/copyright | 1 | 표지 로고와 조감도. md5가 ch5와 동일(imageFile1 182,866 B, imageFile2 2,236,298 B, imageFile3 26,035 B). 표지 문구가 H1/H2로 승격되어 있음 | 삭제 후 frontmatter(title, owner, DOE agreement no., copyright)로 이동 | A |
| A10 | T2 | M | dot-leader 14줄(1,554 chars) | L13 `TABLE OF CONTENTS Chapter 4 Integrated Evaluations. . . . 4.1-1`(제목과 첫 항목 병합), L15–27, L30–36 | 2–3 | TOC + LOT | 삭제 | A |
| A11 | T3 | M | list 15 + wrong level 1 + promoted 3 | L41 `- 4.1 Overall Plant Risk Performance Summary`, L140 `- 4.2.1.1 LBE Margin`, L191 `- 4.2.3 Integrated DID Evaluation`, L39 `### Chapter 4 Integrated Evaluations`, L30 `### LIST OF TABLES` | 4–10 | 번호 절 heading 15개가 모두 목록 항목임. 장 제목은 H3. `### References` 2개(L72, L212)는 제목이 같아 chunk를 구분할 수 없음 | §4의 outline 적용: `^- (\d+(?:\.\d+)+) ` → depth에 맞는 `#`. References에는 소속 절 표기(편집 표시) 검토 | A |
| A12 | T3/T5 | M | 8 | L82 `- Section 4.2.1 presents the plant capability DID…`, L90, L97, L137 `- Chapter 5 and their…`, L148 `- DL1 prevents off-normal operation…`, L149–151 | 6–8 | PDF에서는 일반 문단인데, `Section 4.2.x` / `Chapter 5` / `DLn`으로 시작하는 줄이 목록 항목으로 오검출됨. 그 결과 하위 bullet(L84–87 `Evaluation of …`, L92–94)과 같은 계층이 되어 중첩이 사라짐 | 이 8줄에서 `- ` 제거(패턴 고정), 하위 bullet은 유지 | A |
| A13 | T5 | M | 1 | L135 `…as a result of the DID evaluations are documented in` / L137 `- Chapter 5 and their performance criteria…` | 7 (4.2-2) | 문단 분리. **선행 확인과 달리 페이지 경계가 아니라 같은 페이지 안의 줄바꿈임.** 다음 줄이 `Chapter 5`로 시작해 목록으로 오검출된 것 | 병합 | A |
| A14 | T5 | L | 1 | L107 DL1 / L110 DL2 | 6→7 | DL1–DL5 목록이 페이지 경계에서 빈 줄 2개로 끊김 | 빈 줄 제거 | A |
| A15 | T13 | M | change bar 9개 / 6쪽(≈73줄) | L51 `…The operating license (OL) stage integrated risk evaluation will utilize…`, L53, L107, L116–122, L130, L157–161, L166, L194–210 | 4, 6, 7, 8, 9, 10 | Revision 1 개정 막대(오른쪽 여백 x = 691.2 pt)가 사라짐. **ch4에는 italic, underline, strikethrough가 없음**(font는 Arial, Arial,Bold뿐. underline 후보는 header rule과 표 테두리뿐) | (선택) PDF 좌표로 개정 문단을 식별해 `<!-- rev1 change bar -->` 주석이나 frontmatter `revised_passages`로 보존 | B |
| A16 | T15 | M | — | 전체 | — | frontmatter와 page anchor가 없음. footer page label(4.1-1 … 4.2-11)은 `--include-header-footer`로 확보 가능 | frontmatter(doc_id, title, revision = Revision 1, © 2025 TerraPower, DOE DE-NE0009054, source_pdf, pages = 16) + `<!-- p. 4.2-8 / pdf 13 -->` | A/B |
| A17 | T7, T9, T10, T12, T16, T11(glyph/hyphen) | — | 0 | — | — | 해당 없음: 본문 figure, 각주, 수식, Obsidian 위험 문자(`[[ $ == ^ %% #tag`), 단일 컬럼 reading-order 오류, bullet glyph, hyphen-join 모두 0 | — | — |
| A18 | T14 | — | 추가 0 | — | — | A1/A2 외 누락 없음(bag-of-words, verbatim 85/85) | — | — |

## 2. Table verification log

| Table ID | md lines | PDF p. | Status (OK / defect IDs) | Notes |
|---|---|---|---|---|
| 4.2-1 Mean Risk Margins | L217–231 | 12 (rot.) | T6(헤더 8열 공백, A2), T8 | 3행×8열 값 24개가 PDF와 일치(8열 15.1/15.8/11.3 포함). Notes [a]–[d] 목록 OK |
| 4.2-2 95th Percentile Risk Margins | L234–251 | 13 (rot.) | **T6/T14 H(A1)**, T8, T6 notes(A7) | 11행. 1–7열 값 77개는 PDF 이미지와 일치(RFH-FDIV-1 … RFH-FDPI-1). 8열 헤더와 값 11개 소실. 6열 헤더 `Mean Frequency Margin[b]`는 95th 표이지만 PDF 원문 그대로이므로 **수정 금지** |
| 4.2-3 DL Functions for DBEs | L253–262 | 14 (rot.) | T6 2단 헤더 평탄화(A4), rowspan 2(A5), `<br>` 4, `&lt;`, T8(헤더) | DBE 3개와 기능 행 5개의 셀 텍스트가 완전함(RFH-FDSP-1 설명문 완전) |
| 4.2-4 DL Functions for BDBEs | L265–277 | 15 (rot.) | T6 2단 헤더 평탄화(A4), `&lt;` | BDBE 8행 완전(DL4-RR7 1행 + `None.` 7행) |
| 4.2-5 DBA with Single Feature Reliance | L280–284 | 16 | T4 캡션 병합(A8) | RRS-ISPL-CN 1행 완전. Comment 셀의 PDF 2문단은 공백으로 연결됨(허용) |

## 3. Figure inventory

| Figure ID | md lines | raster/vector | image file | debris lines to delete | Notes |
|---|---|---|---|---|---|
| (표지 로고 Natrium) | L1 | raster | imageFile1.png (182,866 B) | L1 | 모든 PSAR 장과 md5 동일 |
| (표지 조감도) | L3 | raster | imageFile2.png (2,236,298 B) | L3 | 동일 |
| (TerraPower 로고) | L11 | raster | imageFile3.png (26,035 B) | L11 | 동일 |
| 본문 Figure | — | — | — | — | ch4 PDF와 md 모두 "Figure" 0건 |

## 4. Heading outline check

- Intended outline(PDF 본문 기준. TOC는 3단계까지만 수록): `# Chapter 4 Integrated Evaluations` → `## 4.1` → `### 4.1.1–4.1.3` → `### References`(4.1) → `## 4.2` → `### 4.2.1` → `#### 4.2.1.1–4.2.1.4` → `### 4.2.2` → `#### 4.2.2.1–4.2.2.3` → `### 4.2.3` → `### References`(4.2) → 표 캡션 5개.
- 집계: 대상 heading 16(장 1 + 절 15). 목록 항목 15, 잘못된 레벨 1, plain/glued 0, 누락 0. heading이 아닌데 heading으로 승격된 것 3(L5 H1 표지 제목, L7 H2 소유자, L30 H3 `LIST OF TABLES`).

| line | current | intended |
|---|---|---|
| L39 | `### Chapter 4 Integrated Evaluations` | `# Chapter 4 Integrated Evaluations` |
| L41, L77 | `- 4.1 …`, `- 4.2 Defense-in-Depth` | `##` |
| L59, L63, L67, L102, L168, L191 | `- 4.1.1 …` 등 | `###` |
| L140, L144, L154, L163, L175, L181, L186 | `- 4.2.1.1 LBE Margin` 등 | `####` |
| L72, L212 | `### References` | `###`(소속 절 아래 유지) |
| L5, L7, L30 | 표지·LOT가 H1/H2/H3 | 삭제(frontmatter) |

## 5. File-specific observations / cleanup recommendations (ch4)

1. **먼저 재변환**(C.1): `--content-safety-off off-page --include-header-footer`. A1/A2가 복원되고 footer page label을 anchor로 쓸 수 있음. 재변환 없이 고칠 경우 A1의 값 11개를 PDF p.13에서 수동 주입해야 함.
2. 표지(L1–11)와 TOC/LOT(L13–36)를 삭제하고 frontmatter를 생성.
3. heading 변환(A11)과 false list 8줄의 `- ` 제거(A12)를 **먼저** 적용한 뒤 A13(L135+L137 병합)과 A14(빈 줄 제거) 적용.
4. 표: 캡션 접두어 제거(A8), 4.2-3/4.2-4 헤더 합성 및 하위 헤더 행 삭제(A4), fill-down(A5), `<br>`/`&lt;` 정규화(A6), 4.2-2 Notes 목록화(A7).
5. sci notation 정규화(A3): 표 셀과 본문에 같은 규칙 적용. `3.72 x10-4`처럼 원문에 공백이 있는 값은 공백 제거 여부를 정책으로 결정하고 기록.
6. **자동 수정 금지:** Table 4.2-2 헤더 `Mean Frequency Margin[b]`(원문), `summed over all AOO, DBEs`(L70, 원문 단수형), Table 4.2-3 헤더 `design or operation feature`(원문).
7. frontmatter/tag 후보: LBE IDs(RFH-ESWR-2/-3, RFH-FDBL-2, RFH-FDEM-2, RFH-FDIV-1/-2/-3, RFH-FDPI-1, RFH-FDSP-1/-2, RFH-LMCA-2), DBA `RRS-ISPL-CN`, DL functions `DL3-RR1`, `DL3-RR3a`, `DL4-RR7`, `DL1–DL5`. 수치: site boundary 3.12×10⁻³/plant-yr, EAB early fatality 0, latent cancer 3.86×10⁻⁹/plant-yr. 참조: NEI 18-04 Rev 1 (ML19241A472), RG 1.233, §3.1.1, §1.3.1.

---

# Part B — Review ch45/ch5: `TP_Natrium_PSAR2025_ch5_Safety Functions, Design Criteria, and SSC Safety Classification.md` (md lines 1–996, PDF pages 1–52)

## 0. 개요

| 항목 | 값 |
|---|---|
| md | 996 lines(Read 기준), 112,919 chars |
| PDF | 52 pages. p.1 표지, p.2 TOC, p.3 LOT, p.4 §5.1, p.5 §5.2, **p.6–20 Tables 5.2-1…5.2-4(sheet 15개, 모두 `/Rotate 90`)**, p.21–50 §5.3 PDC, p.51 §5.4, p.52 §5.5 |
| Tables | md 15개 = PDF sheet 15개 = 논리 표 4개(5.2-1: 2 sheets, 5.2-2: 4, 5.2-3: 5, 5.2-4: 4). 전수 검증 |
| Records | PSF ID 62개(SR 25, NSRST 37). LBE 항목 222개. distinct LBE ID는 md 72개, PDF 73개(`RFH-FDIV-CN`이 md에서 사라짐) |
| Sections | 본문 heading 67개(level 2: 5, level 3: 9, PDC level 4: 53) + underline 소제목 106개(IS 53 + RPCS 53) + `References` 3개 |
| Figures | 0개(본문). 표지 raster 3개 |
| Noise 추정 | 표지 572 + TOC/LOT 20줄 2,197 + header 잔재 15줄 300 + 반복 표 헤더 11행 1,208 + `<br>` 123개 492 ≈ **4,770 chars(4.2 %)**. 3줄 이상 연속 빈 줄 107곳 |
| **데이터 손실** | bag-of-words 기준 PDF 16,348 token 중 **724 token 누락**. SRDC 셀 **55/57개 절단**(단어 756/2,281개 = 33 % 손실), Table 5.2-4 SSC 5셀 절단(23 단어, AMC 약어 소실), Table 5.2-3 Note 1 절단, 소제목 라벨 11개 누락. 재변환(C.1)으로 **0 token 누락** 달성 |
| Prose verbatim | md prose 246줄 중 245줄이 PDF와 verbatim 일치(예외는 L269 Note 1 절단) |
| 개정 표시 | change bar 25개 / 16쪽 소실 |

## 1. Findings

| # | T-ID | Sev | Count | md lines (examples) | PDF p. | Evidence / description | Proposed fix | Fix class |
|---|---|---|---|---|---|---|---|---|
| B1 | T6/T14 | **H** | SRDC 셀 55/57개, 단어 756/2,281개 | L91 `Upon receipt of a scram release the control rod assemblies in radionuclide release results in calc 10 CFR 50.34 dose criteria…`; L117 `The Primary Sodium Pu transition to natural circulat establish…`; L148 `The Botto from spent fuel…`; L164 `…necessary to est circulation in the primary sodi\|`; L180–185(DL3-RR1 163/210 단어 손실) | 6–16 | Tables 5.2-1–5.2-3의 SRDC 열이 줄 단위로 잘림. 단어 중간 절단 조각 69개(`calc`, `radionuc`, `assu`, `bounda`, `establ`…). PDF p.6 원문: `Upon receipt of a scram signal from RPS, the Control Rod Drive System shall release the control rod assemblies in time to establish reasonable assurance…`. 손실 부분의 font, size, color는 남은 부분과 같음(hidden text 아님). **원인: off-page filter(C.1)**. 재변환으로 복원됨(검증). pdfplumber `extract_tables()`도 셀을 완전하게 반환함(p.6/8/12/13/15/16/17/19 확인) | 재변환(권장) 또는 pdfplumber 셀로 SRDC 재구성 | B |
| B2 | T6/T14 | **H** | 5셀, 23 단어 | L318 `…\|RFH-ESWR-1\|DBE\|Water\|`, L319 `\|Gaseous Radwaste\|`, L344 `\|Auxiliary NI Fire Protection System (NFP) Sodium Processing System (SPS)\|`, L345, L348 | 18–19 | Table 5.2-4 SSC(s) 절단. 원문은 `Water Pool Fuel Handling System (FHP)`, `Gaseous Radwaste Processing System (RWG)`, `Auxiliary Monitoring and Control System (AMC)`(3회). 그 결과 **AMC 약어가 md 전체에서 사라지고** "Auxiliary NI Fire Protection System"이라는 존재하지 않는 SSC 명칭이 생김 | B1과 동일 | B |
| B3 | T14 | **H** | 1 note, 조각 2개 | L269 `…LFF-SAO-CN, RF LFF-SAO-1, and LFF-SAO-2. … LBE analyses will evaluate radionuclide release from` | 16 | Table 5.2-3 Note 1에서 `H-FDIV-CN, DHP-LOOP-3, DHP-LOOP-4,`와 문장 끝 `the SCG pathways, including mitigation provided by DL3-RR10.`이 빠짐. `RFH-FDIV-CN`이 md에서 0회 | B1과 동일 | B |
| B4 | T14/T3 | **H** | 라벨 11개(IS 9, RPCS 2) | IS: PDC 11 (L443), 13 (L469), 16 (L513), 29 (L660), 33 (L704), 46 (L767), 61 (L788), 79 (L952), 82 (L980). RPCS: PDC 73 (L893), 75 (L912) | IS: 25, 26, 28, 33, 36, 38, 41, 49, 50. RPCS: 46, 47 | 페이지 첫 줄(y = 286.7 pt)에 있는 underline 소제목이 running header로 오판되어 삭제됨(C.2). 그 결과 **PDC 요건(규제 기준 문장)과 신청자의 이행 설명(Implementation Summary)을 구분할 수 없음.** 예: L467→L469(PDC 13)에서 요건 문단 바로 뒤에 `Instrumentation and controls are provided…`가 라벨 없이 이어짐. RPCS가 빠진 PDC 73/75에서는 참조 목록이 이행 설명 bullet 뒤에 라벨 없이 붙음 | `--include-header-footer` 재변환 후 `^#+ Kemmerer Unit 1 PSAR (Implementation Summary\|Relevant PSAR Chapters and Sections)$` → 라벨 | B |
| B5 | T13/T3 | M | PDF 라벨 106개. md: IS 44(41개 본문에 glue, 3개 독립), RPCS 51(15개 독립, 36개 glue) | L384 `Implementation Summary Codes and standards for design…`, L397 `…and Chapter 7. Relevant PSAR Chapters and Sections Chapter 2, Section 6.1.1…`, L585, L610, L410(독립), L629(독립) | 21–50 | PDF에서 **underline은 소제목 표시**임. 각 PDC가 criterion / `Implementation Summary` / `Relevant PSAR Chapters and Sections` 세 부분으로 나뉨. md에서는 underline이 사라져 라벨이 문단에 붙거나 독립 줄로 남음(IS와 RPCS가 같은 줄에 있는 경우 29줄). 선행 확인의 "`Relevant PSAR…` ×15 = 표 헤더 잔재" 가설은 **틀림**: 53개 PDC 모두에 있는 소제목이고 그중 15개만 독립 줄임 | 라벨 분리 → `##### Implementation Summary` / `##### Relevant PSAR Chapters and Sections`(verbatim) | A |
| B6 | T3 | M | 본문 heading 67개: list 61, plain+glued 5, list+glued 1, 매몰 1. 장 제목 H3 | L47 `- 5.1 Safety Classification of SSCs`, L380 `- 5.3.1.1 PDC 1 - Quality Standards and Records`, L428 `5.3.1.5 PDC 5 - Sharing of Structures, Systems, and Components Safety-significant structures…`, L428 끝 `…Section 1.1 5.3.2 Multiple Barriers`, L618 `- 5.3.3.7 PDC 26 - Reactivity Control Systems A minimum of two…`, L45 `### Chapter 5 …` | 4–52 | Markdown heading인 절은 0개. glue: PDC 5 (L428), 15 (L503), 26 (L618), 32 (L694), 34 (L712), 36 (L728). §5.3.2 heading은 L428 끝에 매몰됨. PDC 15/32/34/36의 한 줄에는 heading + 요건 + IS + RPCS가 모두 들어 있음 | PDF heading 목록(정확한 제목 67개)으로 분리하고 레벨 부여(§4) | A |
| B7 | T3/T5 | M | 1 | L982 `Relevant PSAR Chapters and Sections Section 7.8.1 References 5.3-1 TerraPower, "Principal Design Criteria for the Natrium Advanced Reactor,"` / L984 `NATD-LIC-RPRT-0002-A, Revision 1` | 50 | §5.3 `References` heading이 문단에 매몰되고 참고문헌 5.3-1이 둘로 나뉨 | `### References` 분리, 5.3-1 병합 | A |
| B8 | T6 | **H** | 빈 key 행 93개(data row 156개 중) | L92–96, L197–225, L277–281, L303–312 | 6–20 | rowspan 미충전. 5.2-1–5.2-3에서는 PSF ID·Description·LBE·Type, 5.2-4에서는 PSF ID·Description·Criteria·SSC가 빔. 행 단위 chunk에서 PSF를 식별할 수 없음 | fill-down | A |
| B9 | T6 | **H** | 1 record(DL3-RR2) | L195 `\|DL3-RR2\|Cladding barrier\|DHP-L1PP-BL\|AOO\|Reactor Core System (RCC)\|During accident conditions\|`, L196 `\| \| \|DHP-LOOP-BL DHS-ISTL-BL OTH-LMAC-BL\|AOO AOO AOO\| \|products to establish r calculated…\|`, L197–225(LBE 1개/행), L235 `\|DL3-RR2 (continued)\|Cladding barrier (continued)\|…` | 13–14 | PDF에서는 한 셀(LBE 51개)인데 md에서는 sheet 2의 31행과 sheet 3의 1행으로 나뉨. **SRDC 문장이 행 경계에서 잘림.** 재변환 후에도 남음(`…retain radionuclide fission\|` / `products to establish…`) | DL3-RR2 행 병합, SRDC 결합, `(continued)` 제거 | A |
| B10 | T6 | M | 표 4개 / sheet 15개, 반복 헤더 11행(1,208 chars) | L104, L128, L142, L161, L193, L233, L246, L263, L300, L327, L355 | 6–20 | page-split sheet가 병합되지 않음. `(Sheet n of m)` 캡션 15개 | 표별로 병합(헤더 1회) | A |
| B11 | T6 | M | 4 | L273/L300/L327/L355 `…\|Associated LBE ID\| \|SSC(s)\|` | 17–20 | Table 5.2-4의 `Associated LBE ID`가 colspan 2라서 5열 헤더가 공백(값은 BDBE/DBE/N/A) | 헤더 명명 결정(예: `Associated LBE ID` \| `[LBE type]`, 편집 표시 필수) | C |
| B12 | T6 | M | SR record 25개의 LBE/type 쌍 222개 | L91 `DHP-L1PP-BL DHP-LOOP-BL … DHP-L1PP-2<br><br>DHP-LOOP-1<br>…` \| `AOO AOO … BDBE` | 6–16 | 5.2-1–5.2-3에서 LBE와 Type이 다른 셀에 공백/`<br>`로 나열되어 쌍 관계는 위치로만 남음. PSF 62개 모두 순서가 PDF와 동일(222 = 222) → 결정적으로 복원 가능 | `DHP-L1PP-BL (AOO); DHP-LOOP-BL (AOO); …` 또는 PSF×LBE 행 전개 | A |
| B13 | T6 | L | `<br>` 123개(`<br><br>` 31개) | L91, L117, L118, L130, L235, L266 | 6–16 | LBE 셀 안 줄바꿈 잔재 | B12 처리 시 제거 | A |
| B14 | T6 | M | 5.2-4 SSC 셀 전부 + 5.2-2/5.2-3 다중 SSC 셀(L120, L133, L134, L253) | L276 `Control Rod Drive System (CRD) Nuclear Island (NI) DC Power Supply System (NDC) NI Uninterruptible AC Power Supply System (NUP) …` | 8–20 | SSC 목록이 구분자 없이 한 셀에 이어짐(PDF는 줄 단위) | PDF 줄 좌표로 `; ` 구분 삽입. **`) ` 단순 분할 금지**(`Nuclear Island (NI) DC …`) | B |
| B15 | T4 | M | 15 | plain 10(L84, L99, L110, L123, L137, L156, L173, L188, L228, L241), H3 2(L259, L351), 캡션 병합 3(L271, L298, L325) | 6–20 | 표 페이지의 `Kemmerer Unit 1 PSAR` 잔재 | 삭제 또는 접두어 제거 | A |
| B16 | T3/T6 | M | 캡션 15: list 10, H3 2, H3+header 병합 3. LOT list 4 | L86 `- Table 5.2-1 … (Sheet 1 of 2)`, L261 `### Table 5.2-3 … (Sheet 5 of 5)`, L271 `### Kemmerer Unit 1 PSAR Table 5.2-4 NSRST Functions (Sheet 1 of 4)` | 6–20 | 캡션 렌더링이 세 가지로 갈림. 선행 확인의 "18 list items"는 부정확: sheet 캡션 10 + LOT 4 = 14 | B10에서 표마다 캡션 heading 1개 | A |
| B17 | T2 | M | dot-leader 19줄(2,197 chars) | L13 `TABLE OF CONTENTS Chapter 5 … . . . . 5.1-1`, L15–34, L39–42 | 2–3 | TOC와 LOT. TOC 항목 14개가 `- 5.x` 목록이라, 번호 목록 75개 = TOC 14 + 본문 61 | 삭제 | A |
| B18 | T1 | M | 6줄(572 chars) + images 3 | L1–L11 | 1 | ch4와 같은 표지 | frontmatter | A |
| B19 | T5 | M | 16 | page break 6: L393/395, L404/406, L491/493, L590/592, L637/640 `- rods succeeding to drop by gravity…`, L686/688. 같은 페이지 줄바꿈 6: L366/368 `application.`, L520/522 `(2) safety functions…`, L605/607 `- as to assure that safety…`, L682/684 `(2) the effects…`, L857/859 `(1) chemical attack…`, L927/929 `(1) periodic inspection…`. 참조 목록 3: L503/505, L811/814, L893/896. 참고문헌 1: L982/984 | 20–50 | 문단이나 목록 항목이 분리됨. **예외:** L940 `(1) postulated leakage…`(PDC 78)는 PDF에서 실제 새 문단(행간 25 pt, 일반 14 pt)이므로 병합 금지 | 병합 규칙: 앞 줄 끝이 `[.:;]`가 아니고 다음 줄이 소문자, `(n)`, `- 소문자`, `- Section`으로 시작하면 병합. PDC 73 bullet 5개(L886–890)는 예외 | A |
| B20 | T5 | L | 32 | L412 `- Section 7.5.2, Section 8.2`, L426, L461, L483 | 21–50 | 참조 목록이 목록 항목으로 렌더링됨(PDF는 일반 줄) | `- ` 제거 | A |
| B21 | T3 | L | 12 | L445 `- 1. Doppler – temperature…`, L621–626, L635–641 | 25, 33–35 | 번호 목록이 bullet + 번호로 이중 표기됨 | `^- (\d+)\. ` → `\1. ` | A |
| B22 | T5 | L | ≥ 3 | L397, L610, L616 | 22, 33 | PDF에서 2문단인 Implementation Summary가 한 줄로 병합됨(라벨 glue와 함께 발생) | B5 처리 후 PDF 문단 경계 복원(선택) | B/C |
| B23 | T13 | M | change bar 25개 / 16쪽 | L72, L163/166–167(DL3-HR11/12), L254(DL3-RR5a), L266+L269(DL3-RR10 + Note 1 = Rev.1 추가), L334–335, L373, L408, L422, L503, L644, L686–688, L704, L714, L888, L896, L903, L931, L984 | 5, 11, 15, 16, 19, 21, 23, 27, 35, 36, 37, 38, 45, 46, 47, 50 | Revision 1 개정 막대(세로 페이지 x = 691.2 pt, 가로 페이지 x = 1213.2 pt. x = 1151.8의 긴 막대는 표 오른쪽 테두리이므로 제외)가 사라짐. **ch5 font는 Arial과 Arial,Bold뿐이어서 italic과 strikethrough가 없음. underline은 소제목 라벨 106개에만 쓰였고, PDC 요건 본문에는 RG 1.232 SFR-DC 대비 수정 표시(underline/italic/strike)가 없음.** 따라서 "md에서 사라진 수정 표시"도 없음 | A15와 동일 | B |
| B24 | T15 | M | — | 전체 | — | frontmatter와 page anchor가 없음 | frontmatter + anchor(footer label 5.1-1 … 5.5-1) | A/B |
| B25 | T8, T9, T10, T11, T12, T16 | — | 0 / 표 note 2 | L269, L366 | 16, 20 | sci notation 없음. 표 Note 2개는 위치가 적절함(B3, B19 제외). 수식, entity, Obsidian 위험 문자, reading-order 오류, bullet glyph, hyphen-join 모두 0 | — | — |

## 2. Table verification log

전 sheet 15개를 pdfplumber `extract_tables()`와 셀 단위로 대조했고, 재변환본(C.1)과는 셀 558개를 비교함. 재변환 전후로 다른 셀은 60개이며 전부 6번째 열(5.2-1–5.2-3 SRDC 55, 5.2-4 SSC 5)임.

| Table ID | md lines | PDF p. | Status (OK / defect IDs) | Notes |
|---|---|---|---|---|
| 5.2-1 Sheet 1/2 | L84–96 | 6 | B1(SRDC 5/6 절단), B8(빈 key 5), B12/B13(`<br>` 31), B15, B16 | DL3-RC1: LBE 31 = PDF 31, Type 31 일치 |
| 5.2-1 Sheet 2/2 | L99–107 | 7 | B1(2/2), B8(1) | DL3-RC2 |
| 5.2-2 Sheet 1/4 | L110–120 | 8 | B1(4/4), B8(2), `<br>` 40 | DL3-HR1, HR2(LBE 각 14) |
| 5.2-2 Sheet 2/4 | L123–134 | 9 | B1(5/5), B8(2), `<br>` 16 | DL3-HR3–HR5 |
| 5.2-2 Sheet 3/4 | L137–153 | 10 | B1(10/10), B8(5) | DL3-HR6–HR10 |
| 5.2-2 Sheet 4/4 | L156–170 | 11 | B1(8/8), B8(5), `<br>` 4 | DL3-HR11–HR13. L164 RIS 셀은 `sodi\|`로 끝남 |
| 5.2-3 Sheet 1/5 | L173–185 | 12 | B1(6/6, 163/210 단어), B8(5), `<br>` 4 | DL3-RR1 |
| 5.2-3 Sheet 2/5 | L188–225 | 13 | **B9**(31행 폭발, SRDC 행 분리), B1(2/2), B8(30) | DL3-RR2 LBE 33 |
| 5.2-3 Sheet 3/5 | L228–238 | 14 | B9(`(continued)` key), B1(3/3), SSC rowspan 공백 2, `<br>` 20 | DL3-RR2(계속, LBE 18), DL3-RR3 |
| 5.2-3 Sheet 4/5 | L241–256 | 15 | B1(9/9), B8(4) | DL3-RR4, RR5, RR5a, RR6, RR7 |
| 5.2-3 Sheet 5/5 | L259–269 | 16 | B1(1/1), **B3**(Note 1), 캡션 H3 | DL3-RR8, DL3-RR10(`See Note 1`) |
| 5.2-4 Sheet 1/4 | L271–295 | 17 | B11, B8(12), B14, B15/B16 | PSF 9개, LBE/Type 일치 |
| 5.2-4 Sheet 2/4 | L298–322 | 18 | **B2**(DL2-RR2, DL2-RR4), B8(10), B11 | PSF 11개 |
| 5.2-4 Sheet 3/4 | L325–348 | 19 | **B2**(DL4-RR3a/3b/4a), B8(10), B11 | PSF 10개 |
| 5.2-4 Sheet 4/4 | L351–368 | 20 | B11, B19(Note L366/368) | PSF 7개 |

### 2a. Per-PSF-ID integrity list (전 62개)

열 설명: rows(빈 key) = md 행 수(그중 PSF ID가 빈 행). LBE = PDF LBE 수(md와 순서까지 일치). SRDC lost = 누락 단어 / PDF 단어. 모든 PSF에서 PSF ID, Description, LBE 순서, Type 순서는 PDF와 일치함. "OK"는 B8(fill-down), B11(헤더), B14(SSC 구분자) 같은 표 공통 결함만 있다는 뜻.

| PSF ID | Table/Sheet | PDF p. | md lines | rows(빈 key) | LBE | SRDC lost | Other |
|---|---|---|---|---|---|---|---|
| DL3-RC1 | 5.2-1/1 | 6 | L91–96 | 6(5) | 31 | 78/240 | `<br>` 31. XIS 행만 무손실 |
| DL3-RC2 | 5.2-1/2 | 7 | L106–107 | 2(1) | 0 (None) | 30/82 | — |
| DL3-HR1 | 5.2-2/1 | 8 | L117 | 1 | 14 | 25/48 | `<br>` 20 |
| DL3-HR2 | 5.2-2/1 | 8 | L118–120 | 3(2) | 14 | 43/122 | `<br>` 20 |
| DL3-HR3 | 5.2-2/2 | 9 | L130–132 | 3(2) | 12 | 34/125 | `<br>` 16 |
| DL3-HR4 | 5.2-2/2 | 9 | L133 | 1 | 9 | 10/40 | SSC 3개 연결 |
| DL3-HR5 | 5.2-2/2 | 9 | L134 | 1 | 9 | 6/44 | SSC 3개 연결 |
| DL3-HR6 | 5.2-2/3 | 10 | L144–145 | 2(1) | 1 | 26/83 | — |
| DL3-HR7 | 5.2-2/3 | 10 | L146–147 | 2(1) | 1 | 26/83 | — |
| DL3-HR8 | 5.2-2/3 | 10 | L148–149 | 2(1) | 1 | 22/83 | — |
| DL3-HR9 | 5.2-2/3 | 10 | L150–151 | 2(1) | 0 (None) | 17/82 | — |
| DL3-HR10 | 5.2-2/3 | 10 | L152–153 | 2(1) | 2 | 23/81 | — |
| DL3-HR11 | 5.2-2/4 | 11 | L163–165 | 3(2) | 2 | 68/123 | 셀 끝 단어 절단(`sodi`) |
| DL3-HR12 | 5.2-2/4 | 11 | L166–168 | 3(2) | 5 | 34/179 | `<br>` 4 |
| DL3-HR13 | 5.2-2/4 | 11 | L169–170 | 2(1) | 0 (None) | 27/84 | — |
| DL3-RR1 | 5.2-3/1 | 12 | L180–185 | 6(5) | 6 | 163/210 | `<br>` 4 |
| DL3-RR2 | 5.2-3/2+3 | 13–14 | L195–235 | 32(30) | 51 | 14/34 | **sheet 분할, key `(continued)`, SRDC 행 분리(L195/196)**, `<br>` 20 |
| DL3-RR3 | 5.2-3/3 | 14 | L236–238 | 3(2) | 4 | 24/125 | SSC rowspan 공백 2 |
| DL3-RR4 | 5.2-3/4 | 15 | L248–250 | 3(2) | 2 | 25/121 | SSC rowspan 공백 2 |
| DL3-RR5 | 5.2-3/4 | 15 | L251–253 | 3(2) | 3 | 26/130 | SSC rowspan 공백 1 |
| DL3-RR5a | 5.2-3/4 | 15 | L254 | 1 | 2 | 11/46 | Rev.1 change bar |
| DL3-RR6 | 5.2-3/4 | 15 | L255 | 1 | 2 | 6/32 | — |
| DL3-RR7 | 5.2-3/4 | 15 | L256 | 1 | 0 (None) | 4/43 | `system functional containment design` 소실 |
| DL3-RR8 | 5.2-3/5 | 16 | L265 | 1 | 0 (None) | 14/38 | — |
| DL3-RR10 | 5.2-3/5 | 16 | L266 | 1 | 7 | 0 (`See Note 1`) | `<br>` 8. **Note 1 절단(B3)** |
| DL4-RC1 | 5.2-4/1 | 17 | L275 | 1 | 0 (None) | n/a | OK |
| DL4-RC3 | 5.2-4/1 | 17 | L276–281 | 6(5) | 6 | n/a | OK(SSC 5개 연결) |
| DL4-RC4 | 5.2-4/1 | 17 | L282 | 1 | 0 | n/a | OK |
| DL4-RC6 | 5.2-4/1 | 17 | L283–288 | 6(5) | 6 | n/a | OK(`See Note 1`) |
| DL4-RC6a | 5.2-4/1 | 17 | L289 | 1 | 1 | n/a | OK |
| DL4-RC6b | 5.2-4/1 | 17 | L290–292 | 3(2) | 3 | n/a | OK |
| DL4-RC6c | 5.2-4/1 | 17 | L293 | 1 | 0 | n/a | OK |
| DL4-RC6d | 5.2-4/1 | 17 | L294 | 1 | 0 | n/a | OK |
| DL2-HR2 | 5.2-4/1 | 17 | L295 | 1 | 0 | n/a | OK |
| DL4-HR1 | 5.2-4/2 | 18 | L302–312 | 11(10) | 11 | n/a | OK |
| DL4-HR2 | 5.2-4/2 | 18 | L313 | 1 | 0 | n/a | OK |
| DL4-HR3 | 5.2-4/2 | 18 | L314 | 1 | 0 | n/a | OK |
| DL4-HR4 | 5.2-4/2 | 18 | L315 | 1 | 1 | n/a | OK |
| DL4-HR6 | 5.2-4/2 | 18 | L316 | 1 | 0 | n/a | OK |
| DL4-HR7 | 5.2-4/2 | 18 | L317 | 1 | 0 | n/a | OK |
| DL2-RR2 | 5.2-4/2 | 18 | L318 | 1 | 1 | n/a | **SSC `Water`(5 단어 소실)** |
| DL2-RR4 | 5.2-4/2 | 18 | L319 | 1 | 0 | n/a | **SSC `Gaseous Radwaste`(3 단어 소실)** |
| DL2-RR7 | 5.2-4/2 | 18 | L320 | 1 | 0 | n/a | OK |
| DL2-RR8 | 5.2-4/2 | 18 | L321 | 1 | 0 | n/a | OK |
| DL2-RR10 | 5.2-4/2 | 18 | L322 | 1 | 0 | n/a | OK |
| DL4-RR1 | 5.2-4/3 | 19 | L329–335 | 7(6) | 7 | n/a | OK. DHP-LOOP-3/4는 Rev.1 change bar |
| DL4-RR1a | 5.2-4/3 | 19 | L336–339 | 4(3) | 4 | n/a | OK |
| DL4-RR1b | 5.2-4/3 | 19 | L340 | 1 | 0 | n/a | OK |
| DL4-RR1c | 5.2-4/3 | 19 | L341–342 | 2(1) | 2 | n/a | OK |
| DL4-RR3 | 5.2-4/3 | 19 | L343 | 1 | 1 | n/a | OK |
| DL4-RR3a | 5.2-4/3 | 19 | L344 | 1 | 0 | n/a | **SSC: AMC 5 단어 소실** |
| DL4-RR3b | 5.2-4/3 | 19 | L345 | 1 | 0 | n/a | **SSC: AMC 5 단어 소실** |
| DL4-RR3c | 5.2-4/3 | 19 | L346 | 1 | 0 | n/a | OK |
| DL4-RR4 | 5.2-4/3 | 19 | L347 | 1 | 0 | n/a | OK |
| DL4-RR4a | 5.2-4/3 | 19 | L348 | 1 | 0 | n/a | **SSC: AMC 5 단어 소실** |
| DL4-RR4b | 5.2-4/4 | 20 | L357 | 1 | 0 | n/a | OK |
| DL4-RR4c | 5.2-4/4 | 20 | L358 | 1 | 0 | n/a | OK |
| DL4-RR5 | 5.2-4/4 | 20 | L359 | 1 | 0 | n/a | OK |
| DL4-RR7 | 5.2-4/4 | 20 | L360 | 1 | 1 | n/a | OK |
| DL4-RR8 | 5.2-4/4 | 20 | L361 | 1 | 0 | n/a | OK |
| DL4-DID1 | 5.2-4/4 | 20 | L362 | 1 | 0 | n/a | OK |
| DL5-PAM1 | 5.2-4/4 | 20 | L363 | 1 | 0 | n/a | OK(SSC 12개 연결) |

합계: SR PSF 25개 중 SRDC 손실이 있는 것 24개(무손실은 DL3-RR10 `See Note 1`뿐). NSRST PSF 37개 중 SSC 손실 5개. LBE 항목 222개는 모두 보존됨(PDF 222 = md 222, 순서 일치).

## 3. Figure inventory

| Figure ID | md lines | raster/vector | image file | debris lines to delete | Notes |
|---|---|---|---|---|---|
| 표지 로고/조감도/TerraPower 로고 | L1, L3, L11 | raster | imageFile1–3.png(ch4와 md5 동일) | L1–L11 | frontmatter로 대체 |
| 본문 Figure | — | — | — | — | PDF와 md 모두 "Figure" 0건. vector debris 없음 |

## 4. Heading outline check

Intended outline(PDF 본문 기준. TOC 3단계 + PDC):
`# Chapter 5 Safety Functions, Design Criteria, and SSC Safety Classification` → `## 5.1` → `### References` → `## 5.2` → `### 5.2.1 / 5.2.2 / 5.2.3` → `### References` → Tables 5.2-1–5.2-4 → `## 5.3 Principal Design Criteria` → `### 5.3.1 Overall Requirements` → `#### 5.3.1.1 PDC 1 - Quality Standards and Records` → (`##### Implementation Summary`, `##### Relevant PSAR Chapters and Sections`) ×53 … → `### References`(5.3) → `## 5.4` → `## 5.5`.

**집계:** 본문 heading 67개 중 Markdown heading 0, 목록 항목 61(glue 1 포함), plain+glue 5, 문단 끝 매몰 1. 장 제목 H3 1. underline 소제목 106개 중 heading 0: IS 누락 9 / glue 41 / 독립 3, RPCS 누락 2 / glue 36 / 독립 15. References는 3개 중 2개가 H3이고 1개는 매몰됨. 비-heading 승격 3(L5, L7, L37 `### LIST OF TABLES`), 표 헤더 잔재 H3 2(L259, L351).

| line(s) | current form | intended |
|---|---|---|
| L45 | `### Chapter 5 …` | `#` |
| L47, L57, L370, L986, L991 | `- 5.1 …`, `- 5.2 …`, `- 5.3 …`, `- 5.4 …`, `- 5.5 …` | `##` |
| L60, L68, L74, L377, L564, L667, L774, L845 | `- 5.2.1 …`, `- 5.3.1 …`, `- 5.3.3 …` 등 | `###` |
| L428 끝 | `…Section 1.1 5.3.2 Multiple Barriers`(매몰) | `### 5.3.2 Multiple Barriers`(분리) |
| PDC 목록 항목 48개: L380 (P1), 390 (P2), 399 (P3), 415 (P4), 430 (P10), 436 (P11), 455 (P12), 464 (P13), 486 (P14), 508 (P16), 517 (P17), 533 (P18), 539 (P19), 567 (P20), 581 (P21), 587 (P22), 596 (P23), 602 (P24), 612 (P25), 618 (P26, **glue**), 646 (P28), 655 (P29), 670 (P30), 679 (P31), 699 (P33), 717 (P35), 733 (P37), 745 (P44), 753 (P45), 762 (P46), 777 (P60), 783 (P61), 817 (P62), 829 (P63), 838 (P64), 848 (P70), 854 (P71), 870 (P72), 879 (P73), 899 (P74), 905 (P75), 915 (P76), 925 (P77), 933 (P78), 947 (P79), 959 (P80), 969 (P81), 975 (P82) | `- 5.3.x.y PDC n - Title` | `#### 5.3.x.y PDC n - Title` |
| L428, L503, L694, L712, L728 | heading + 본문 한 줄(PDC 5, 15, 32, 34, 36) | `####` 분리 + 요건/IS/RPCS 분리 |
| IS/RPCS 라벨(B4, B5) | glue / 독립 / 누락 | `#####`(verbatim) |
| L52, L79, L982 | `### References`, `### References`, 매몰 | `###`(각 절 아래) |

## 5. File-specific observations / cleanup recommendations (ch5)

**순서 있는 규칙**

1. **재변환(B, 필수):** `--content-safety-off off-page --include-header-footer`(선택: `--markdown-page-separator`). 이 단계 없이는 B1–B4를 복원할 수 없음(규칙 기반 복원 불가).
2. header/footer 처리(A): `^(#+ )?Kemmerer Unit 1 PSAR$` 삭제. `^(#+ )?Kemmerer Unit 1 PSAR (?=Table |Implementation Summary|Relevant PSAR)`는 접두어만 제거. `^SUBJECT TO DOE COOPERATIVE AGREEMENT NO\. DE-NE0009054 Copyright © 2025 TerraPower, LLC\. All Rights Reserved$` 삭제. `^(\d\.\d-\d+|[ivx]+) Revision 1$` → `<!-- p. 5.3-5 -->`(page anchor).
3. 표지와 TOC/LOT 삭제, frontmatter 생성.
4. heading 복원(A): PDF에서 추출한 heading 67개의 정확한 제목 문자열로 glue 분리(PDC 5/15/26/32/34/36, §5.3.2). 레벨은 번호 depth로 결정.
5. 소제목 라벨(A): `Implementation Summary`와 `Relevant PSAR Chapters and Sections`를 앞뒤 텍스트와 분리해 `#####`로 만듦. 뒤따르는 `- Section …` 목록 표기 제거(B20). 분리된 참조 목록 병합(L503/505, L811/814, L893/896).
6. 문단 병합(A): B19 규칙과 예외(PDC 78 L940, PDC 73 bullet L886–890). 번호 목록 `- 1.` → `1.`(B21).
7. 표(A): sheet 병합 → 반복 헤더 삭제 → key의 `(continued)` 제거 → fill-down → DL3-RR2 병합(SRDC 결합) → LBE/Type 쌍 결합 → `<br>` 제거. 5.2-4 5열 헤더는 C 결정. SSC 구분자는 PDF 줄 좌표(B) 사용.
8. change bar(B): 25개 위치를 개정 표시 메타데이터로 보존(선택).

**자동 수정 금지(원문 그대로 유지)**

- `sends a sends a signal`(L631), `from effecting all rods`(L631), `radionuclide release limits design`(L635), `one rod bundle form the reactor core`(L641), `…is described in Section 8.1`(L386 문법), `design limits is not exceeded`(L570).
- SSC 명칭 불일치 `Water Fuel Pool Handling System (FHP)`(L152, L169, L363) vs `Water Pool Fuel Handling System (FHP)`(L253, L265, L315)는 원문의 불일치임. 정규화하지 말고 alias로만 기록.
- 헤더 표기 `PSF-ID`(5.2-3) vs `PSF ID`, `Associated LBE(s)`(5.2-1) vs `Associated LBE`는 원문 그대로.
- PDC 73의 소문자 bullet 5개는 PDF의 실제 bullet임.

**`scripts/patch_underlines.py` 관련 경고(T13)**

- 이 스크립트를 `references/*.md`에 그대로 적용하면 **안 됨**. read-only로 탐지 함수만 실행한 결과, ch5에서 phrase 440개가 나왔고 그중 진짜 underline은 105개(IS 53 + RPCS 52)뿐임. 나머지는 header rule 아래의 `Kemmerer Unit 1 PSAR` 51, 표 테두리 위의 `BDBE` 36, `10 CFR 50.34 dose criteria…` 21, 표 헤더 셀 등 오탐임. ch4에서는 147개 전부가 오탐(ch4에는 underline이 없음).
- 원인: `height < 2`인 rect에 폭 필터가 없어 표 격자와 header rule을 거르지 못함.
- 같은 phrase가 반복되면 `if f'<u>{p}</u>' in content: continue` 때문에 **첫 번째만** 감싸짐(53개 중 1개).
- 대상 경로가 `raw/Natrium_PSAR_{ch}_text.md`로 현 파이프라인과 다름.
- ch5의 underline 의미는 "소제목"뿐이므로 `<u>` 태그 대신 heading(`#####`)으로 변환하는 편이 RAG에 유리함.

**frontmatter/tag 후보(요약)**

- PSF ID 62개(SR: DL3-RC1–2, DL3-HR1–13, DL3-RR1–8/5a/10. NSRST: DL4-RC1/3/4/6/6a–d, DL2-HR2, DL4-HR1–4/6/7, DL2-RR2/4/7/8/10, DL4-RR1/1a–c/3/3a–c/4/4a–c/5/7/8, DL4-DID1, DL5-PAM1).
- LBE ID 73개(`RFH-FDIV-CN` 포함). PDC 번호 53개(1–5, 10–26, 28–37, 44–46, 60–64, 70–82 — RG 1.232 SFR-DC 번호와 대응).
- SSC 약어 56개 이상(+AMC).
- 참고문헌: NATD-LIC-RPRT-0002-A Rev 1, RG 1.232 Rev 0, RG 1.233, RG 1.189 Rev 5, RG 1.194 Rev 0, NEI 18-04 Rev 1 (ML19241A472).
- cross-ref 242개(`Section x.y.z`/`Chapter n`, distinct 52) → link 후보.

---

# Part C — 재변환 실험(재현 절차)과 공통 권고

## C.1 off-page filter(가로 페이지)

- 증거 1: 가로 페이지는 `/Rotate 90`이고 MediaBox는 792×1224, CropBox = MediaBox임. 세로 페이지는 CropBox [90, 216, 702, 1008].
- 증거 2: md에 남은 조각은 표시 좌표에서 시작 x < 792 pt인 chunk이고, 사라진 것은 시작 x > 792 pt인 chunk임. 예: `Water` x0 = 762.3은 남고 `Pool` x0 = 794.3부터 사라짐. `Auxiliary` 762.3은 남고 `Monitoring` 806.9는 사라짐. `RFH-FDIV-CN,` 927.4는 사라짐.
- 증거 3: pdfplumber 속성(font Arial 11 pt, color (0), upright)이 남은 부분과 사라진 부분에서 동일함. 따라서 hidden text 필터가 아님.
- 실험(scratchpad `ch45_tmp/`, vault는 변경 안 함):
  - `java -jar opendataloader-pdf-cli.jar <pdf> --format markdown --image-output off --content-safety-off off-page`
  - ch4: 원본과 차이는 Table 4.2-1/4.2-2 8열 복원뿐.
  - ch5: 704 token / 104 span 복원. 원본에만 있던 token 69개는 모두 절단 조각임.
- 주의: PATH의 `java`는 Java 8이라 `UnsupportedClassVersionError`(class file 55)가 남. `C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot\bin\java.exe`로 실행해 성공함.

## C.2 header/footer filter(ch5 소제목)

- 증거: `Implementation Summary`가 10쪽, `Relevant PSAR…`가 5쪽에서 페이지 첫 줄(y = 286.7 pt)에 있음. 이 가운데 9/10, 2/5가 md에서 사라짐.
- 실험: `--include-header-footer`를 추가하면 IS 53/53, RPCS 53/53이 됨. 두 옵션을 함께 쓴 결과의 bag-of-words 비교에서 PDF token 누락 0이고, 추가된 것은 header/footer token(`Kemmerer Unit 1 PSAR` 51, DOE/copyright 52, `x.y-n Revision 1` 52)뿐임.

## C.3 코퍼스 적용 권고

- 가로 페이지가 있는 모든 PDF(RG 1.232, ch1, ch3, ch6, ch7, ch11)를 같은 옵션으로 재변환하고 bag-of-words 비교로 확인할 것.
- 반복되는 페이지 첫 줄 소제목 손실은 ch6/ch7에서도 가능성이 있음(미검증).

## 산출물 위치(참고용, vault 밖)

- `…\scratchpad\ch45_tmp\full4\…ch4….md`, `…\full5\…ch5….md`: off-page 해제
- `…\ch45_tmp\hf5\…ch5….md`: off-page 해제 + header-footer 포함
- 비교 스크립트: `ch45_tmp\{cmp,bag,psf,pdc,verb,counts,ul}.py`, `ch45_*.py`
