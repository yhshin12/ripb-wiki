# Review ch1: TP_Natrium_PSAR2025_ch1_General Plant and Site Description.md (md lines 1–2320, PDF pages 1–115)

## 0. 개요

| 항목 | 값 |
|---|---|
| md | 2,320 lines (non-blank 1,629), 184,936 chars (개행 포함; 개행 제외 182,617), image refs 14, table blocks 62, `#` headings 47 |
| PDF | 115 pages, struct tree 없음. page label: p1 cover; p2–4 i–iii (TOC/LoT/LoF); p5–18 iv–xvii (Acronyms); p19–40 1.1-1…1.1-22; p41–57 1.1-23…1.1-39 (Figures 1.1-1…1.1-17); p58 1.2-1; p59 1.2-2 (Figure 1.2-1); p60–65 1.3-1…1.3-6 (p65 = Figure 1.3-1); p66–68 1.4-1…1.4-3; p69–94 1.4-4…1.4-29 (Table 1.4-1); p95 1.4-30; p96 1.4-31; p97–105 1.4-32…1.4-40 (Table 1.4-4); p106–115 1.4-41…1.4-50 (Table 1.4-5). Landscape: p41–44, 47, 48, 50, 51, 54, 55, 57, 59, 65, 69–94 (39 pages) |
| 논리 table | 6개 (Acronym list 487 rows, Table 1.4-1 183 rows, 1.4-2 14, 1.4-3 4, 1.4-4 47, 1.4-5 167) → md에서 **61개 fragment** + phantom 1 = 62 blocks |
| Figures | 19 (raster 4: 1.1-1…1.1-4; withheld 13: 1.1-5…1.1-17; vector 1: 1.2-1; vector+raster-fill 1: 1.3-1) |
| Sections | 번호 heading 74 (H2 4 / H3 11 / H4 7 / H5 52) + chapter title 1 + unnumbered `References` 4 + `LIST OF ACRONYMS AND ABBREVIATIONS` 1. md에서 heading으로 렌더된 번호 heading = **0** |
| 본문 무결성 | PDF body page(p19–40, 58, 60–64, 66–68) 전체 word-level diff: PDF 13,053 words vs md 12,953 words, SequenceMatcher ratio 0.99615. 차이 = bullet glyph 62개(`●`/`-`, md에서는 list marker로 변환) + 비교 제외 범위(Ref 1.1-1/1.1-2)뿐 → **본문 단어 누락 0** (page-break 인접 문단 13개 포함 전부 완전) |
| Table 무결성 | 62/62 block을 pdfplumber cell과 cell-by-cell 비교 + page별 word-bag 비교: row 수 전부 일치(행 분할·행 누락 0), **단어 소실 1 (RG 1.183 `methodologies`)**, **줄끝 hyphen 소실 7**, 아래첨자 소실 2 |
| Noise 추정 | 순수 noise ≈ **336 non-blank lines (20.6 %) / ≈10.3 k chars (5.7 %)**: TOC/LoT/LoF 42 lines·4,566 ch; Fig 1.2-1 debris 109 lines·593 ch (+ blank 109); Fig 1.3-1 debris 21 lines·798 ch; 중복 table header 110 lines·3,025 ch; `### (Sheet n of 26)` 26 lines·511 ch; withheld 마커 잉여 줄(`[[`/`]]SRI`) 15 lines; header/footer residue 7 lines·127 ch + caption prefix 8×21 ch; cover 6 lines·482 ch. 연속 빈 줄(≥2) run 126개 |

핵심 RAG 영향: 번호 heading이 전부 list item이라 structure-aware chunker 기준으로 **§1.1 본문 전체(L617–1071, ≈455 lines)가 `### LIST OF FIGURES`(L49) 아래**, §1.2 본문이 `### Kemmerer Unit 1 PSAR`(L1168) 아래, **§1.3 본문이 `### Figure 1.2-1 Site Layout`(L1202) 아래**, §1.4 본문이 `### Kemmerer Unit 1 PSAR Figure 1.3-1 …`(L1539) 아래, **Table 1.4-4·1.4-5 (214 rows)가 `### Table 1.4-3 Technical Reports`(L2020) 아래**에 귀속된다(wrong-section attachment → H).

## 1. Findings

| # | T-ID | Sev | Count | md lines (examples) | PDF p. | Evidence / description | Proposed fix | Fix class |
|---|---|---|---|---|---|---|---|---|
| 1 | T3 | H | 74 번호 heading (list item 72, list+body glued 1, paragraph 내 inline 1) + chapter title 1 | L617 `Chapter 1 General Plant and Site Description 1.1 Introduction US SFR Owner, LLC (USO), …`; L619 `- 1.1.1 Reactor Supplier and Model Kemmerer Unit 1 is a Natrium reactor supplied by TerraPower.`; L658 `- 1.1.4.1.1 Reactor Core System`; L1184 `- 1.2 Site Description`; L1424 `- 1.3 Plant Safety Overview`; L1583 `- 1.4 Conformance with Regulatory Criteria and Referenced Material` | 19–68 | PDF heading은 본문과 같은 Arial 11 pt regular(번호+tab)라 폰트로 구분 불가 → list item으로 변환됨. 결과적으로 본문이 무관한 heading에 귀속(§0 참조). L617은 bold chapter title + `1.1 Introduction` + PDF 2개 문단이 한 줄로 병합 | TOC 삭제 후, L615 이후 `^- (1\.\d+(?:\.\d+)*)\s+(.+)$` 중 **§4의 74개 whitelist**와 일치하는 것만 `#`×(점 개수+1) heading으로 변환(1.x→H2 … 1.x.y.z.w→H5); L619는 제목/본문 분리; L617은 `# Chapter 1 General Plant and Site Description` / `## 1.1 Introduction` / 문단1(`…Facilities.”`까지) / 문단2(`This preliminary …`)로 4분할 | A |
| 2 | T14 (T7) | H | Figure 1.2-1 legend 31 항목 + LEGEND 2 + scale 전부 소실 | L1202–1421에는 번호만(`62`, `11`, `51`, `32A` … 31개) 존재; grep `FACILITY|SWITCHYARD|COOLING TOWER|LEGEND` = 0 hit | 59 | PDF text layer에 legend 존재(4.4 pt, upright): `FACILITY NUMBER/DESCRIPTION: 11 REACTOR BUILDING, 12 REACTOR AUXILIARY BUILDING, 21 TURBINE FACILITY BUILDING, 32A/32B MEDIUM VOLTAGE HOUSING, 33 MAIN AND AUXILIARY TRANSFORMERS, 34 RESERVE AUXILIARY TRANSFORMERS, 35 SWITCHYARD, 36 SWITCHYARD CONTROL BUILDING, 37 STANDBY DIESEL GENERATORS, 38 NI CONTROL BUILDING, 41/42 ENERGY STORAGE STRUCTURE SALT TANK HOT/COLD, 43 STEAM GENERATOR BUILDING, 44 CONDENSATE STORAGE TANK, 45 SALT CONTAINMENT BERM, 51 FUEL HANDLING BUILDING, 52 FUEL AUXILIARY BUILDING, 61 TRAINING, ADMINISTRATION BUILDING, 62 NI WAREHOUSE, 71 WATER TREATMENT BUILDING, 72 COOLING TOWER, 73 CIRCULATING WATER PUMP AREA INTAKE FACILITY, 75 FIRE TANKS AND PUMP BUILDING, 76 WASTEWATER TREATMENT, 78 EI DEMINERALIZED WATER TANK, 81A NI ARGON AND NITROGEN BULK STORAGE, 81B HYDROGEN GAS TRAILER, 82 NI/EI (SALT) PIPE RACK, 84 STEAM GENERATOR BUILDING/TURBINE FACILITY BUILDING (STEAM) RACK, 85 AUXILIARY BOILER` + `LEGEND: X X FENCE / FACILITY NUMBER`. site 시설 식별 질의에 필수 | `pdfplumber` `page.crop((880,130,1100,400)).extract_text()`(p59)로 추출하여 caption 아래 2-col table `Facility Number | Description`(31 rows) + legend 주석으로 삽입; debris(#9) 삭제 | B |
| 3 | T14 (T6) | H | 1 단어 | L1825 (RG 1.183) `In general, accident specific and assumptions may be used as guidance` | 82 | PDF: `In general, accident specific methodologies⏎and assumptions …` — 줄끝 단어가 cell 오른쪽 경계에 닿아 누락(render로 확인) | `accident specific methodologies and assumptions`로 복원 | B |
| 4 | T11 | H | 7 (table cell 줄끝 hyphen 소실) | L2007 `NATD-LIC-RPRT0002-A`; L1713 `WaterCooled`; L1961 `TamperIndicating`; L2044 `longterm`; L2073 `nonessential`; L2098 `inplant`; L2108 `Preliminary Design Information Containment Integrity` | 95, 73, 92, 98, 101, 104, 105 | pdfplumber cell의 `-\n`을 opendataloader가 soft-hyphen으로 간주해 삭제. `NATD-LIC-RPRT-0002-A`(PDC Topical Report 식별자)가 훼손되어 exact-match 검색 실패; (3)(v)는 `Information -⏎Containment`의 대시가 사라져 의미 결합 변화. 본문(비표) 줄끝 hyphen 사례는 0 | PDF-검증 7건 치환 목록으로만 수정: `NATD-LIC-RPRT-0002-A`, `Water-Cooled`, `Tamper-Indicating`, `long-term`, `non-essential`(xiv (A) 1회), `in-plant`, `Information - Containment` | B (목록 고정 후 A) |
| 5 | T6 / T14 | H | caption 누락 4종: Table 1.4-1 (26 sheets), 1.4-4 (9 sheets, `(Sheet n of 9)` 포함), 1.4-5 (10 sheets, `(Sheet n of 10)` 포함), `LIST OF ACRONYMS AND ABBREVIATIONS` (14 pages) | L1661 `### (Sheet 1 of 26)` 바로 앞; L2030 앞(직전 heading = L2020 `### Table 1.4-3 Technical Reports`); L2113 앞; L74 앞 | 69–94, 97–105, 106–115, 5–18 | caption은 LoT(L42, 45, 46)에만 존재. 매 page 상단에 반복되는 caption이 header/footer filter에 의해 running header로 제거된 것으로 추정(미검증 가설). 1.4-2·1.4-3(1 page 표)은 caption 정상 | LoT 문자열 그대로 `### Table 1.4-1 Conformance with Regulatory Guides`, `### Table 1.4-4 Applicability of TMI-Related Requirements`, `### Table 1.4-5 Consensus Codes and Standards`, `## LIST OF ACRONYMS AND ABBREVIATIONS` 삽입 (header signature로 위치 결정: `\|Guide Number\|…`, `\|Regulation\|…`, `\|Codes and Standards\|…`, `\|Term\|…`) | A |
| 6 | T6 | M | page-split fragment 59 → 논리 4 table; 중복 header 55 (110 lines, 3,025 ch); pseudo-heading `### (Sheet n of 26)` 26 | L74/115/…/607 `\|Term\|Description\|`; L1661–1987 sheet headings; L2030/2041/…/2103; L2113/2136/…/2310 | 5–18, 69–94, 97–115 | 행 분할(continuation row) 0, key cell 공백 0 — md row 수가 모든 page에서 pdfplumber와 일치(487/183/47/167) → 단순 연결로 병합 가능 | 동일 header 연속 block 연결, 첫 header만 유지, sheet heading 삭제 | A |
| 7 | T6 | M | 26 / 183 rows | L1668 `\|1.20\|…\|4\|Partial Conformance This RG is partially applicable …\|`; L1679 `Full Conformance RG 1.28 Revision 6 is …`; L1697 `Full Conformance Alternate code or standard will be applied.` | 69–89 | PDF는 status label과 comment가 별도 줄/문단. md는 한 cell에 공백 결합(Partial 24, Full 2). status 분포: Full 96, Partial 24, OL-stage 문장 63 | `Conformance Status` = prefix(`Full Conformance`/`Partial Conformance`) 그대로, 신설 `Comments` = 나머지(verbatim). OL-stage 63행은 문장 전체를 status에 유지 | A |
| 8 | T6 | L–M | `<br>` 29개 / 7 cells; 셀 내 줄바꿈→공백 2 | L1667 (1.13, 11개: `exceptions:<br><br>1.Although…<br><br><br>Specific…`); L1686 (1.29, 6); L1919 `Vital<br><br>Areas`; L2024 `3.12,<br>3.13<br>`; L2080 (xvii, 4); L2228 `Limit<br><br>- All Parts`; L2251 `facilities<br><br>- Equipment …`; L2081 `7.1.3 11.2`, L2082 `7.6.5 11.2` | 69, 71, 89, 96, 102, 111, 112 | 열거(1./2./3., C.2/C.8/C.9, C.1–C.4, Section (B)/(C)) 구분용 `<br>`은 의미 있음; 제목 중간 `<br><br>`과 셀 말미 `<br>`은 artefact(셀 내 `-`로 시작하는 줄을 list로 오인) | `<br>{2,}`→`<br>`, 셀 말미 `<br>` 삭제, 제목/식별자 cell(5.7, IEC 61000-3, IEEE 344, TP-LIC-RPT-0011)의 `<br>`→공백; Section cell `7.1.3 11.2`는 `7.1.3, 11.2` 형식(동일 열 `5.3.2.10, 7.6.7`과 일치)으로 정규화 여부 결정 필요 | A (+C) |
| 9 | T7 | M | Fig 1.2-1 debris 218 lines (non-blank 109: `X` fence 69 줄 중 lone `X` 43, 고아 facility 번호 31, label 9) + footer 1 | L1204 `X X XX X X X XX …`; L1228 `62`; L1238 `CL REACTOR`; L1258 `RETENTION POND`; L1370–1414 lone `X` 23줄; L1422 `1.2-2` | 59 | vector drawing(curves 4,487, lines 8,484)의 fence 기호·번호가 xycut 순서로 흩어짐. `HWY 189`×3, `RETENTION POND`×3, `CL REACTOR`×2, `TRUE NORTH AND PLANT NORTH 0°` | L1204–L1422 span 삭제(패턴 기반 전역 삭제 금지), legend table(#2)과 `TRUE NORTH AND PLANT NORTH 0°`만 유지 | A (span) |
| 10 | T7 / T16 | M | Fig 1.3-1 debris 40 lines: label 10, decorative image ref 7, phantom table 1 (2 all-empty rows) | L1541 `Environment`; L1545 `![](…imageFile8.png)`; L1569–1572 `\| \| \| \|`; L1575 `Reactor Auxiliary Building*` | 65 | label 순서 뒤섞임(흐름: Fuel Matrix → Sodium Coolant → Cover Gas → Head Access Area → Reactor Building* / Reactor Auxiliary Building* → Fuel Handling Building* → Environment). imageFile8–14 = 파란 gradient 상자 배경(192–269×165–166 px, 619–673 B). 초록 barrier label 5개(`Fuel Cladding`, `Reactor Vessel & Vessel Head`, `Concrete Structure and Seals`, `Above grade building structures`×2)는 text layer에 없음(vector outline) → md에도 없음 | L1541–L1580 삭제, L1581 note 유지(`\*Sub-compartments …`로 escape). 필요 시 render에서 수동 전사한 barrier chain 설명 추가 | A + C |
| 11 | T12 (T14) | M | `[[` 13 (단독 줄 9, caption 말미 glued 4), `]]SRI` 6, **closer 누락 7** | L1096–1100 (정상 3줄 형태); L1112–1114 (closer 없음); L1124 `Figure 1.1-9 … Looking North [[`; L1180–1182 뒤 곧바로 L1184 `- 1.2 Site Description` | 45–57 | PDF 13 page 모두 `[[` / `This information is withheld in accordance with 10 CFR 2.390` / `]]SRI`(SRI = 7.7 pt 위첨자). closer는 landscape page(p47, 48, 50, 51, 54, 55, 57 = Fig 1.1-7, -8, -10, -11, -14, -15, -17)에서만 소실. 줄 결합 시 Obsidian wikilink(`[[This information …]]`) 생성 위험 | figure당 1줄 canonical marker: `\[\[This information is withheld in accordance with 10 CFR 2.390\]\]<sup>SRI</sup>` (대괄호 escape → wikilink 불가, `^` block-ID 위험 회피). 기계 필터용으로 `<!-- withheld: 10 CFR 2.390; SRI -->` 병기 가능. **다른 줄바꿈/결합 규칙보다 먼저 적용** | A |
| 12 | T4 | M | 15 (`Kemmerer Unit 1 PSAR` 11 = `###` heading 3 + caption prefix 8; page footer 4) | L1122, L1168, L1200 `### Kemmerer Unit 1 PSAR`; L1110 `Kemmerer Unit 1 PSAR Figure 1.1-7 …`; L1539 `### Kemmerer Unit 1 PSAR Figure 1.3-1 …`; L1130 `1.1-31 Revision 1`; L1176 `1.1-38 Revision 1`; L1198 `1.2-1 Revision 1`; L1422 `1.2-2` | 45–65 | 일반 본문 page의 header/footer는 정상 제거, figure page에서만 잔존. `Kemmerer Unit 1 PSAR` 문자열은 본문에 정당하게 쓰이지 않음(11건 모두 residue) | `^### Kemmerer Unit 1 PSAR$` 삭제; `^(### )?Kemmerer Unit 1 PSAR (?=Figure )` prefix 제거; `^\d\.\d-\d+ Revision 1$`, `^1\.2-2$` 삭제 | A |
| 13 | T7 | M | caption 19 중 비-heading 11 (header prefix 7, `[[` glued 4); raster alt text 공백 4; 그림 내 텍스트 픽셀 전용 4 | L1110, L1116, L1124, L1132, L1138, L1144, L1150, L1156, L1162, L1170, L1178; L1080 `![](<…imageFile4.png>)` | 41–57, 65 | Figure 1.1-4 `Safety Features`의 `Simplified Response to Abnormal Events`·`Control`·`Cool`·`Contain` 등 제목 6 + bullet 14, Fig 1.1-3 `RAC Heat Removal - Always-on passive cooling …`, Fig 1.1-2 건물 label은 image에만 존재 | 19개 caption을 모두 `### Figure x.y-z Title`로 통일, alt text = caption; 그림 내 텍스트는 OCR/수동 전사하여 caption 아래 `> Figure text:` 블록으로(선택) | A (+C) |
| 14 | T2 | M | TOC 16 + LoT 5 + LoF 19 = dot-leader 40 lines (L13–71, 42 non-blank, 4,566 ch) | L13 `TABLE OF CONTENTS Chapter 1 General Plant and Site Description . . . . 1.1-1`; L36 `- 1.4.3 … TMI Action Items. . . . 1.4-2`; L51 `- Figure 1.1-1 … . . . 1.1-23` | 2–4 | `TABLE OF CONTENTS` heading이 첫 항목과 결합, 항목은 중첩 list + 빈 줄로 단절 | L13–L71 삭제(삭제 전 #5 caption 문자열 확보; 필요시 table/figure ID 목록은 frontmatter로) | A |
| 15 | T1 | L | cover 6 non-blank lines (L1–11) | L1/L3/L11 imageFile1–3; L5 `# Kemmerer Power Station Unit 1 PSAR, Chapter 1`; L7 `## US SFR Owner, LLC, a wholly owned subsidiary of TerraPower, LLC`; L9 `SUBJECT TO DOE COOPERATIVE AGREEMENT NO. DE-NE0009054 Copyright © 2025 TerraPower, LLC. All rights reserved.` | 1 | imageFile1–3 md5가 PSAR 7개 chapter 전부 동일(6ed777…, 8b325d…, b56e08…). cover 부제가 H2로 승격 | frontmatter로 이관 후 삭제 | A |
| 16 | T5 | M | page-break 문단 분할 13 (+L617 문단 병합 1) | L629/631 `…storage tank for thermal` ‖ `energy storage.`; L688/690; L762/764 `…manipulation of the` ‖ `CRD. During shutdown…`; L1446/1448; L1472/1474; L1518/1520 | 19–64 | 13개 모두 단어 누락 없음(diff 확인). 대문자 시작 continuation(L764 `CRD.`, L1520 `IAC blower.`)이 있어 “소문자 시작” 규칙만으로는 3건 누락 | 이전 문단이 terminal punctuation(`. : ; ? ! ” ’ )`) 없이 끝나고 다음이 일반 문단이면 결합; 대상 13쌍 목록: 629, 654, 669, 688, 745, 762, 804, 924, 952, 1068, 1446, 1472, 1518 | A |
| 17 | T5 (T3) | M | false list item 5; nested list 평탄화 1 (sub-item 2); list 중간 빈 줄 단절 1 | L644–646 `- Section 1.1.4.2 summarizes …`; L1021 `- The RAB is comprised of …`; L1522 `- The RAC provides an inherent means …`; L1598→L1601–1602 `- a different type of reactor design`; L1639–1643 (Ref 1.4-3/1.4-4 사이 빈 줄 2) | 20, 38, 64, 66, 67–68 | PDF에서 해당 5개는 bullet glyph 없는 일반 문단(render 확인). true bullet 62개는 모두 `●`(또는 sub `-`) glyph 보유 | 5개 `- ` 제거(고정 line 목록 또는 PDF glyph 대조), L1601–1602 두 칸 들여쓰기+빈 줄 제거, list 내부 빈 줄 run 제거 | B (고정 목록이면 A) |
| 18 | T11 | M | `&amp;` 17 (15 lines), `&gt;` 1 | L303 `I&amp;C`; L728 (`I&amp;C`×3); L1746 `RG 1.97 Revision 5 &amp; IEEE 497-2016`; L2015 `Instrumentation &amp; Control`; L2079 `Babcock &amp; Wilcox`; L1918 `nearest Quaternary volcano was &gt;117 kilometers` | 10, 14, 17, 20–31, 76, 89, 95, 102–103 | HTML entity가 exact-match와 embedding을 오염; `&gt;117`은 수치 한정자 | `html.unescape` (table cell 내 `>`·`&`는 Markdown에서 안전) | A |
| 19 | T11 | L–M | 1 | L1639 `NUREG/ CR-7046` | 67 | `NUREG/⏎CR-7046` 줄바꿈이 공백으로 → 식별자 분리 | `NUREG/CR-7046` | A |
| 20 | T8 | M | 아래첨자 2 (+위첨자 SRI 13, #11에서 처리) | L603 `\|VS\|Shear-Wave Velocity\|`; L604 `\|VS30\|Time-averaged shear-wave velocity in the upper 30 meters\|` | 17 | PDF: `V` 11 pt + `S`/`S30` 7.7 pt subscript. `TWR®`(L585)은 정상 | `V<sub>S</sub>`, `V<sub>S30</sub>` (plain-text 병기 원하면 `V_S`) | A |
| 21 | T13 | L | bold 정의어 5; change bar 38 | L1592 `Full Conformance – …`; L1594 `Partial Conformance – …`; L1618 `Full Compliance – …`; L1620 `Partial Compliance - …`; L1622 `Not Applicable – …` | 66–67 (bold); change bar p5, 6, 8, 9, 10, 14, 31, 36, 60, 68, 78, 84, 95, 96, 99, 104, 107, 110–113 | bold는 status 값의 정의(용어집 추출 대상). Rev. 1 change bar(우측 여백 폭 < 4 pt rect): Acronyms BEPU, CCF, ES, FMEA, GVH, IDP, PIE; §1.1.4.3.6 4줄; **§1.1.4.3.19 전체**; §1.3.1 2줄; Ref 1.4-18; Table 1.4-1 1.140, 1.204; Table 1.4-2 13 rows; Table 1.4-3 3 rows; Table 1.4-4 (2)(vii), (2)(xxvii), (2)(xxviii); Table 1.4-5 Code Case N-924, ASTM E119, DANU-ISG-2023-01, IEEE 485, NFPA 11 | bold 5개 `**…**` 복원(문단 시작 고정 문자열); change bar는 선택적으로 `<!-- rev1-change -->` 주석(PDF rect 좌표 필요) | A (bold) / B (bar) |
| 22 | T15 | M | frontmatter 0, page anchor 0 | L1 | 전체 | doc id·revision·page label 부재로 인용 불가 | YAML frontmatter(§5) + page anchor(`--markdown-page-separator "<!-- page %page-number% -->"` 재변환 또는 page label 매핑표) | A / B |
| 23 | T12 | L | `*` 4 | L1543 `Fuel Handling Building*`; L1551; L1575; L1581 `*Sub-compartments within building provides additional confinement, depending on event.` | 65 | 현재는 문단 분리로 무해하나 줄 결합 시 `Building* … *Sub` 가 italic으로 짝지어짐 | 유지 줄은 `\*` escape | A |
| 24 | T16 | L | 2 figure | Fig 1.2-1, 1.3-1 label debris | 59, 65 | 본문 reading order는 정상(diff ratio 0.996). 문제는 figure label에 한정 | #9, #10 삭제로 해소 | A |
| 25 | T99-1 | — (보존) | 8 원문 오기 | L286 `\|HCI\|hydrochloric acid\|`; L389 `Manufactures`; L899 `(PCO) and, provides`, `conditions.Each`; L950 `during an station blackout`; L960 `areas.The`; L2035 `power- operated`; image `TO ENVIROMENT` | 10, 12, 33, 35, 36, 97, 44 | pdfplumber text에도 동일 → 변환 결함 아님 | **자동 수정 금지**(verbatim 원칙). 필요 시 `<!-- sic -->` 주석만 | — |
| 26 | T9 / T10 | — | 0 / 0 | — | — | footnote·equation 없음 (Fig 1.3-1 `*` note는 figure note로 처리) | — | — |

## 2. Table verification log

검증 방법: 62개 md table block 전부를 해당 PDF page의 `pdfplumber.extract_tables()` 결과와 cell 단위 비교(공백 정규화, `<br>`·entity 정규화, PDF 측 `-\n` 결합 에뮬레이션) + page별 word-bag 비교. 모든 page에서 md row 수 = PDF row 수. 아래 “값 OK”는 cell text가 PDF와 일치함을 의미(구조 결함 T6은 별도 표기).

| Table ID | md lines | PDF p. | rows md/PDF | Status (OK / defect IDs) | Notes |
|---|---|---|---|---|---|
| Acronyms (1/14) | L74–112 | 5 | 37/37 | T6 | T6 (caption 'LIST OF ACRONYMS AND ABBREVIATIONS' 누락; header 반복 1/14); 값 OK; change bar: BEPU |
| Acronyms (2/14) | L115–153 | 6 | 37/37 | T6 | T6 header 반복; 값 OK; change bar: CCF |
| Acronyms (3/14) | L156–194 | 7 | 37/37 | T6 | T6 header 반복; 값 OK |
| Acronyms (4/14) | L197–235 | 8 | 37/37 | T6 | T6 header 반복; 값 OK; change bar: ES |
| Acronyms (5/14) | L238–276 | 9 | 37/37 | T6 | T6 header 반복; 값 OK; change bars: FMEA, GVH |
| Acronyms (6/14) | L279–317 | 10 | 37/37 | T6; T11 | T6; T11 `I&amp;C` (L303); change bar: IDP |
| Acronyms (7/14) | L320–358 | 11 | 37/37 | T6 | T6 header 반복; 값 OK |
| Acronyms (8/14) | L361–399 | 12 | 37/37 | T6 | T6 header 반복; 값 OK (`NEMA … Manufactures` = 원문) |
| Acronyms (9/14) | L402–440 | 13 | 37/37 | T6 | T6 header 반복; 값 OK |
| Acronyms (10/14) | L443–481 | 14 | 37/37 | T6; T11 | T6; T11 `R&amp;D` (L480); change bar: PIE |
| Acronyms (11/14) | L484–522 | 15 | 37/37 | T6 | T6 header 반복; 값 OK |
| Acronyms (12/14) | L525–563 | 16 | 37/37 | T6 | T6 header 반복; 값 OK (SSC 2회 정의 = 원문) |
| Acronyms (13/14) | L566–604 | 17 | 37/37 | T6; T8; T11 | T6; **T8 `VS`/`VS30` (L603–604) = PDF V<sub>S</sub>, V<sub>S30</sub> (7.7 pt 아래첨자)**; T11 `V&amp;V` (L600); `TWR®` OK |
| Acronyms (14/14) | L607–614 | 18 | 6/6 | T6 | T6 header 반복; 값 OK |
| (phantom, Fig. 1.3-1) | L1569–1572 | 65 | 2/0 (그림) | T7 | T7 phantom table (Figure 1.3-1 상자 격자에서 생성, 2 all-empty rows) → 삭제 |
| 1.4-1 Sheet 1/26 | L1663–1668 | 69 | 4/4 | T6 | Sheet 1. T6 (caption 누락, `### (Sheet 1 of 26)` pseudo-heading); 1.13 `<br>`×11 (이중·말미 `<br>`), 1.13/1.20 status+comment glued; 값 OK |
| 1.4-1 Sheet 2/26 | L1673–1679 | 70 | 5/5 | T6 | Sheet 2. T6; 1.28 status+comment glued; 값 OK |
| 1.4-1 Sheet 3/26 | L1684–1687 | 71 | 2/2 | T6 | Sheet 3. T6; 1.29 `<br>`×6, glued; 값 OK |
| 1.4-1 Sheet 4/26 | L1692–1702 | 72 | 9/9 | T6 | Sheet 4. T6; 1.31/1.36/1.45 glued; 값 OK (`800F` = 원문) |
| 1.4-1 Sheet 5/26 | L1707–1715 | 73 | 7/7 | T6; T11 | Sheet 5. T6; **T11 `WaterCooled` (1.68, L1713) ← PDF `Water-⏎Cooled`**; 1.59 glued |
| 1.4-1 Sheet 6/26 | L1720–1729 | 74 | 8/8 | T6 | Sheet 6. T6; 1.75/1.78 glued; 값 OK |
| 1.4-1 Sheet 7/26 | L1734–1739 | 75 | 4/4 | T6 | Sheet 7. T6; 1.89 glued; 값 OK |
| 1.4-1 Sheet 8/26 | L1744–1752 | 76 | 7/7 | T6; T11 | Sheet 8. T6; T11 `&amp;` (1.97); 1.97/1.100 glued |
| 1.4-1 Sheet 9/26 | L1757–1765 | 77 | 7/7 | T6 | Sheet 9. T6; 1.117/1.118 glued; 값 OK |
| 1.4-1 Sheet 10/26 | L1770–1777 | 78 | 6/6 | T6 | Sheet 10. T6; 1.138 glued; change bar: 1.140 |
| 1.4-1 Sheet 11/26 | L1782–1788 | 79 | 5/5 | T6 | Sheet 11. T6; 1.143/1.147 glued; 값 OK |
| 1.4-1 Sheet 12/26 | L1793–1803 | 80 | 9/9 | T6 | Sheet 12. T6; 1.168/1.169 glued; 값 OK |
| 1.4-1 Sheet 13/26 | L1808–1817 | 81 | 8/8 | T6 | Sheet 13. T6; 1.180 glued; 값 OK |
| 1.4-1 Sheet 14/26 | L1822–1830 | 82 | 7/7 | T6; T14 | Sheet 14. T6; **T14 1.183 comment에서 단어 `methodologies` 소실 (L1825)**; 1.183 glued |
| 1.4-1 Sheet 15/26 | L1835–1843 | 83 | 7/7 | T6 | Sheet 15. T6; 1.195/1.196 glued; 값 OK |
| 1.4-1 Sheet 16/26 | L1848–1856 | 84 | 7/7 | T6 | Sheet 16. T6; 1.209 glued; change bar: 1.204 |
| 1.4-1 Sheet 17/26 | L1861–1870 | 85 | 8/8 | T6 | Sheet 17. T6; 값 OK (`(OUO-SRI)` 1.214 = 원문) |
| 1.4-1 Sheet 18/26 | L1875–1883 | 86 | 7/7 | T6 | Sheet 18. T6; 값 OK |
| 1.4-1 Sheet 19/26 | L1888–1896 | 87 | 7/7 | T6 | Sheet 19. T6; 값 OK (1.247 Revision `Trial` = 원문) |
| 1.4-1 Sheet 20/26 | L1901–1911 | 88 | 9/9 | T6 | Sheet 20. T6; 값 OK |
| 1.4-1 Sheet 21/26 | L1916–1923 | 89 | 6/6 | T6; T11 | Sheet 21. T6; T11 `&gt;117 kilometers` (4.26, L1918); 4.26 glued; 5.7 제목 `Vital<br><br>Areas` 가짜 줄바꿈 |
| 1.4-1 Sheet 22/26 | L1928–1937 | 90 | 8/8 | T6 | Sheet 22. T6; 값 OK |
| 1.4-1 Sheet 23/26 | L1942–1953 | 91 | 10/10 | T6 | Sheet 23. T6; 값 OK |
| 1.4-1 Sheet 24/26 | L1958–1968 | 92 | 9/9 | T6; T11 | Sheet 24. T6; **T11 `TamperIndicating` (5.80, L1961) ← PDF `Tamper-⏎Indicating`** |
| 1.4-1 Sheet 25/26 | L1973–1984 | 93 | 10/10 | T6 | Sheet 25. T6; 값 OK |
| 1.4-1 Sheet 26/26 | L1989–1997 | 94 | 7/7 | T6 | Sheet 26. T6; 값 OK |
| 1.4-2 | L2002–2017 | 95 | 14/14 | T11 | caption OK (`### Table 1.4-2 Topical Reports`); **T11 `NATD-LIC-RPRT0002-A` (L2007) ← PDF `NATD-LIC-RPRT-⏎0002-A` (식별자 훼손)**; T11 `&amp;` (NAT-4950-A); ML 번호 14개 OK; change bars 13행 |
| 1.4-3 | L2022–2027 | 96 | 4/4 | T6 | caption OK; T6 `3.12,<br>3.13<br>` (TP-LIC-RPT-0011); 값 OK; change bars 3행 |
| 1.4-4 Sheet 1/9 | L2030–2038 | 97 | 7/7 | T6 | Sheet 1/9. **T6 caption `Table 1.4-4 Applicability of TMI-Related Requirements` + `(Sheet n of 9)` 누락 → 현재 `### Table 1.4-3 Technical Reports` 아래에 귀속**; `power- operated` = 원문 |
| 1.4-4 Sheet 2/9 | L2041–2049 | 98 | 7/7 | T6; T11 | Sheet 2/9. T6; **T11 `longterm` (L2044) ← `long-⏎term`** |
| 1.4-4 Sheet 3/9 | L2052–2058 | 99 | 5/5 | T6 | Sheet 3/9. T6; 값 OK; change bar: (2)(vii) |
| 1.4-4 Sheet 4/9 | L2061–2067 | 100 | 5/5 | T6 | Sheet 4/9. T6; 값 OK |
| 1.4-4 Sheet 5/9 | L2070–2074 | 101 | 3/3 | T6; T11 | Sheet 5/9. T6; **T11 `nonessential` (L2073, (A) 항목) ← `non-⏎essential`** (같은 셀의 (B) `non-essential`은 정상) |
| 1.4-4 Sheet 6/9 | L2077–2083 | 102 | 5/5 | T6; T11 | Sheet 6/9. T6; T11 `&amp;` (xvi); (xvii) `<br>`×4; Section 셀 `7.1.3 11.2`, `7.6.5 11.2` (셀 내 줄바꿈→공백) |
| 1.4-4 Sheet 7/9 | L2086–2092 | 103 | 5/5 | T6; T11 | Sheet 7/9. T6; T11 `&amp;` ×2 (xxii, xxiii) |
| 1.4-4 Sheet 8/9 | L2095–2100 | 104 | 4/4 | T6; T11 | Sheet 8/9. T6; **T11 `inplant` (L2098) ← `in-⏎plant`**; change bars (xxvii), (xxviii) |
| 1.4-4 Sheet 9/9 | L2103–2110 | 105 | 6/6 | T6; T11 | Sheet 9/9. T6; **T11 `Preliminary Design Information Containment Integrity` (L2108) ← PDF `Information -⏎Containment`** |
| 1.4-5 Sheet 1/10 | L2113–2133 | 106 | 19/19 | T6 | Sheet 1/10. **T6 caption `Table 1.4-5 Consensus Codes and Standards` + `(Sheet n of 10)` 누락**; 값 OK |
| 1.4-5 Sheet 2/10 | L2136–2157 | 107 | 20/20 | T6 | Sheet 2/10. T6; 값 OK; change bar: Code Case N-924 |
| 1.4-5 Sheet 3/10 | L2160–2179 | 108 | 18/18 | T6 | Sheet 3/10. T6; 값 OK |
| 1.4-5 Sheet 4/10 | L2182–2198 | 109 | 15/15 | T6 | Sheet 4/10. T6; 값 OK |
| 1.4-5 Sheet 5/10 | L2201–2217 | 110 | 15/15 | T6 | Sheet 5/10. T6; 값 OK; change bar: ASTM E119 |
| 1.4-5 Sheet 6/10 | L2220–2240 | 111 | 19/19 | T6 | Sheet 6/10. T6; `IEC 61000-3` 제목 `Limit<br><br>- All Parts` (셀 내 '-'가 list로 오인); change bar: DANU-ISG-2023-01 |
| 1.4-5 Sheet 7/10 | L2243–2259 | 112 | 15/15 | T6 | Sheet 7/10. T6; `IEEE 344` 제목 `facilities<br><br>- Equipment…`; change bar: IEEE 485 |
| 1.4-5 Sheet 8/10 | L2262–2281 | 113 | 18/18 | T6 | Sheet 8/10. T6; 값 OK; change bar: NFPA 11 |
| 1.4-5 Sheet 9/10 | L2284–2307 | 114 | 22/22 | T6 | Sheet 9/10. T6; 값 OK |
| 1.4-5 Sheet 10/10 | L2310–2317 | 115 | 6/6 | T6 | Sheet 10/10. T6; 값 OK |

요약: 값 결함 = 단어 소실 1 (1.183), hyphen 소실 7 (1.68, 5.80, NATD-LIC-RPRT-0002-A, ix, xiv, xxvii, (3)(v)), 아래첨자 2 (V<sub>S</sub>, V<sub>S30</sub>), entity 18. 열 소실·열 이동·행 분할·rowspan 미충전 = 0. 구조 결함 = caption 누락 4종, fragment 59 → 4, 중복 header 55, pseudo-heading 26, status+comment 결합 26, `<br>` artefact.

## 3. Figure inventory

| Figure ID | md lines | raster/vector | image file | debris lines to delete | Notes |
|---|---|---|---|---|---|
| 1.1-1 Heat Transport Systems Overview Highlighting Operational Interface | L1078–1080 | raster | imageFile4.png (3399×1405, 1,417,467 B) | — | caption `###` 정상, alt 공백. image 내 label(Primary Pool (Sodium), Intermediate Loop (Sodium), NI Salt System (Nitrate Salt), EI Salt System (Nitrate Salt), Power Cycle Loop (Water), Decoupling Boundary, Radioactive Coolant Boundary, Operational Interface, Nuclear/Commercial Constructor Scope) 픽셀 전용. p41 |
| 1.1-2 Plant Layout | L1082–1084 | raster | imageFile5.png (3399×1682, 3,945,780 B) | — | 건물 label(Warehouse & Admin, Fuel Handling Building, Rx Building, Fuel Aux Building, Control Building, Rx Aux Building, NI Electric Modules, Salt Piping, Energy Storage Tanks, Firewater, Steam Generation, Turbine Building, Cooling Tower, Standby Diesels, Nuclear/Energy Island Boundary) 픽셀 전용. p42 |
| 1.1-3 Heat Removal | L1086–1088 | raster | imageFile6.png (3399×2507, 825,854 B) | — | `RAC Heat Removal` / `IAC Heat Removal` bullet 5개 픽셀 전용. p43 |
| 1.1-4 Safety Features | L1090–1092 | raster | imageFile7.png (3399×2202, 973,758 B) | — | `Simplified Response to Abnormal Events`, `No Safety-Related Operator Actions or Safety-Related Power Systems`, `Technology Based on U.S. SFR Experience`, `Control`, `Cool`, `Contain` 제목 6 + bullet 14 픽셀 전용(질의 가치 높음 → 전사 권장). p44 |
| 1.1-5 General Arrangement RXB Section A Looking East | L1094–1100 | withheld | — | L1096–1100 → canonical 1줄 | caption `###` 정상, 마커 3줄 완전. p45 (portrait) |
| 1.1-6 General Arrangement RXB Section B Looking North | L1102–1108 | withheld | — | L1104–1108 → 1줄 | 정상. p46 |
| 1.1-7 General Arrangement FHB Section A Looking West | L1110–1114 | withheld | — | L1112–1114 → 1줄 | caption에 header prefix, `]]SRI` 소실. p47 (landscape) |
| 1.1-8 General Arrangement FHB Section B Looking North | L1116–1120 | withheld | — | L1118–1120 → 1줄; L1122 `### Kemmerer Unit 1 PSAR` 삭제 | prefix, closer 소실. p48 |
| 1.1-9 General Arrangement FHB Section C Looking North | L1124–1128 | withheld | — | L1124 말미 ` [[` 분리, L1126–1128 → 1줄; L1130 footer 삭제 | caption+`[[` glued. p49 |
| 1.1-10 General Arrangement RAB Section A Looking North | L1132–1136 | withheld | — | L1134–1136 → 1줄 | prefix, closer 소실. p50 |
| 1.1-11 General Arrangement RAB Section B Looking East | L1138–1142 | withheld | — | L1140–1142 → 1줄 | prefix, closer 소실. p51 |
| 1.1-12 General Arrangement NCB Substructure | L1144–1148 | withheld | — | L1144 ` [[` 분리, L1146–1148 → 1줄 | glued. p52 |
| 1.1-13 General Arrangement NCB Ground Floor | L1150–1154 | withheld | — | L1150 ` [[` 분리, L1152–1154 → 1줄 | glued. p53 |
| 1.1-14 General Arrangement NCB Looking West | L1156–1160 | withheld | — | L1158–1160 → 1줄 | prefix, closer 소실. p54 |
| 1.1-15 General Arrangement NCB Looking South | L1162–1166 | withheld | — | L1164–1166 → 1줄; L1168 `### Kemmerer Unit 1 PSAR` 삭제 | prefix, closer 소실. p55 |
| 1.1-16 General Arrangement FAB Ground Floor | L1170–1174 | withheld | — | L1170 ` [[` 분리, L1172–1174 → 1줄; L1176 footer 삭제 | glued. p56 |
| 1.1-17 General Arrangement FAB Looking West | L1178–1182 | withheld | — | L1180–1182 → 1줄 | prefix, closer 소실; 바로 뒤 L1184 `- 1.2 Site Description`. p57 |
| 1.2-1 Site Layout | L1202 (caption `###` 정상) | vector (curves 4,487 / lines 8,484) | — | L1198 `1.2-1 Revision 1`, L1200 `### Kemmerer Unit 1 PSAR`, **L1204–L1422** (218 lines; non-blank 109 + footer) | **legend 31 항목 소실(#2)** → PDF crop으로 복원 삽입. p59 (landscape) |
| 1.3-1 Diverse Barriers in Functional Containment | L1539 (`### Kemmerer Unit 1 PSAR Figure 1.3-1 …`) | vector 상자/화살표 + raster gradient fill 7 | imageFile8–14.png (192–269×165–166 px, 619–673 B; 모두 파란 gradient 상자 배경 = 장식) | **L1541–L1580** (label 10, image ref 7, phantom table L1569–1572); L1581 note 유지 | barrier label 5개 text layer 부재; caption prefix 제거. p65 |
| (cover) logos | L1, L3, L11 | raster | imageFile1–3.png (1581×454, 2472×1388, 512×176) | L1–L11 | PSAR 전 chapter 공통(md5 동일) |

## 4. Heading outline check

요약 (의도 outline = PDF 본문 번호 heading 74 + 비번호 heading):

| 구분 | 수 | md 현재 형태 |
|---|---|---|
| Chapter title `Chapter 1 General Plant and Site Description` (H1) | 1 | L617 문단 선두에 glued |
| 번호 heading (H2 4 / H3 11 / H4 7 / H5 52) | 74 | list item 72, list+body glued 1 (L619), 문단 내 inline 1 (L617) — heading 0 |
| `References` (H3, §1.1/1.2/1.3/1.4 말미) | 4 | `### References` (L1072, 1193, 1534, 1636) — 형태 OK. 번호 heading 수정 후 §1.x 하위로 올바르게 귀속됨 |
| `LIST OF ACRONYMS AND ABBREVIATIONS` (H2) | 1 | **누락** |
| Table caption (H3) | 5 | 1.4-2, 1.4-3 정상; **1.4-1, 1.4-4, 1.4-5 누락** |
| Figure caption (H3) | 19 | heading 8 (L1539는 header prefix 포함), plain 11 |
| 비-heading의 heading 승격 | 30 | L7 `## US SFR Owner, LLC, …`(cover), `### Kemmerer Unit 1 PSAR` ×3 (L1122, 1168, 1200), `### (Sheet n of 26)` ×26, (`### LIST OF TABLES/FIGURES`는 TOC 삭제로 소멸) |
| Wrong level | 1 | L5 `# Kemmerer Power Station Unit 1 PSAR, Chapter 1`(cover title) → frontmatter `title`로; H1은 chapter title |

Level 규칙: `1.x`→H2, `1.x.y`→H3, `1.x.y.z`→H4, `1.x.y.z.w`→H5 (최대 깊이 5, H6 불필요). Figure/Table caption과 `References`는 소속 H2 section 아래 H3.

결함 heading 전체 목록 (74):

| # | md line | 현재 형태 | 번호 | 제목 (verbatim) | 의도 level | PDF p. |
|---|---|---|---|---|---|---|
| 1 | L617 | paragraph 안 inline (chapter title과 함께) | 1.1 | Introduction | H2 | 19 |
| 2 | L619 | list item + body glued | 1.1.1 | Reactor Supplier and Model | H3 | 19 |
| 3 | L620 | list item | 1.1.2 | Intended Use of the Reactor | H3 | 19 |
| 4 | L624 | list item | 1.1.3 | Overall Configuration | H3 | 19 |
| 5 | L637 | list item | 1.1.4 | Description of Plant Structures, Systems, and Components | H3 | 20 |
| 6 | L651 | list item | 1.1.4.1 | Reactor Systems and Components | H4 | 20 |
| 7 | L658 | list item | 1.1.4.1.1 | Reactor Core System | H5 | 21 |
| 8 | L664 | list item | 1.1.4.1.2 | Reactor Enclosure System | H5 | 21 |
| 9 | L673 | list item | 1.1.4.1.3 | Reactor Air Cooling System | H5 | 22 |
| 10 | L679 | list item | 1.1.4.1.4 | Primary Heat Transport System | H5 | 22 |
| 11 | L685 | list item | 1.1.4.1.5 | Intermediate Heat Transport System | H5 | 22 |
| 12 | L694 | list item | 1.1.4.1.6 | Intermediate Air Cooling System | H5 | 23 |
| 13 | L700 | list item | 1.1.4.1.7 | Sodium Cover Gas System | H5 | 23 |
| 14 | L709 | list item | 1.1.4.1.8 | Sodium Processing System | H5 | 24 |
| 15 | L719 | list item | 1.1.4.1.9 | Control Rod Drive System | H5 | 24 |
| 16 | L726 | list item | 1.1.4.1.10 | Instrument and Control Systems | H5 | 25 |
| 17 | L732 | list item | 1.1.4.1.11 | Reactor Protection System | H5 | 25 |
| 18 | L738 | list item | 1.1.4.1.12 | Nuclear Instrumentation System | H5 | 25 |
| 19 | L742 | list item | 1.1.4.1.13 | Radiation Monitoring System | H5 | 25 |
| 20 | L749 | list item | 1.1.4.1.14 | Reactor Instrumentation System | H5 | 26 |
| 21 | L753 | list item | 1.1.4.1.15 | Nuclear Island Control System | H5 | 26 |
| 22 | L757 | list item | 1.1.4.1.16 | Rod Monitoring and Control System | H5 | 26 |
| 23 | L766 | list item | 1.1.4.1.17 | Coolant Temperature Monitoring and Control System | H5 | 27 |
| 24 | L772 | list item | 1.1.4.1.18 | Utility Monitoring and Control System | H5 | 27 |
| 25 | L778 | list item | 1.1.4.1.19 | Auxiliary Monitoring and Control System | H5 | 27 |
| 26 | L785 | list item | 1.1.4.1.20 | Fuel Handling Supervisory Control System | H5 | 28 |
| 27 | L789 | list item | 1.1.4.1.21 | Plant Monitoring and Control System | H5 | 28 |
| 28 | L794 | list item | 1.1.4.2 | Secondary Systems and Components | H4 | 28 |
| 29 | L801 | list item | 1.1.4.2.1 | Salt Systems (NSS, ESS, TSS) | H5 | 28 |
| 30 | L810 | list item | 1.1.4.2.2 | Power Cycle Systems (SGS, CFW, STS, GEN, HRS) | H5 | 29 |
| 31 | L814 | list item | 1.1.4.2.3 | Main Power | H5 | 29 |
| 32 | L828 | list item | 1.1.4.3 | Significant Support Systems and Components | H4 | 30 |
| 33 | L831 | list item | 1.1.4.3.1 | In-Vessel Fuel Handling System | H5 | 30 |
| 34 | L837 | list item | 1.1.4.3.2 | Ex-Vessel Fuel Handling System | H5 | 30 |
| 35 | L841 | list item | 1.1.4.3.3 | Water Pool Fuel Handling System | H5 | 30 |
| 36 | L848 | list item | 1.1.4.3.4 | Main Control Room | H5 | 31 |
| 37 | L854 | list item | 1.1.4.3.5 | Nuclear Island Distributed Control System | H5 | 31 |
| 38 | L858 | list item | 1.1.4.3.6 | Nuclear Island Auxiliary Electrical Systems | H5 | 31 |
| 39 | L867 | list item | 1.1.4.3.7 | Gaseous Radwaste Processing | H5 | 32 |
| 40 | L873 | list item | 1.1.4.3.8 | Liquid Radwaste Processing | H5 | 32 |
| 41 | L877 | list item | 1.1.4.3.9 | Solid Radwaste Processing | H5 | 32 |
| 42 | L881 | list item | 1.1.4.3.10 | Nuclear Island HVAC System | H5 | 32 |
| 43 | L890 | list item | 1.1.4.3.11 | Nuclear Island Ancillary Electrical System | H5 | 33 |
| 44 | L896 | list item | 1.1.4.3.12 | Nuclear Island Plant Communication System | H5 | 33 |
| 45 | L905 | list item | 1.1.4.3.13 | Nuclear Island Cranes and Hoists | H5 | 34 |
| 46 | L911 | list item | 1.1.4.3.14 | Energy Island Auxiliary Electrical System | H5 | 34 |
| 47 | L917 | list item | 1.1.4.3.15 | Nuclear Island Air and Inert Gas Distribution Systems | H5 | 34 |
| 48 | L921 | list item | 1.1.4.3.16 | Seismic Monitoring System | H5 | 34 |
| 49 | L947 | list item | 1.1.4.3.17 | Nuclear Island Emergency Operating Lighting | H5 | 35 |
| 50 | L958 | list item | 1.1.4.3.18 | Nuclear Island Fire Protection System | H5 | 36 |
| 51 | L962 | list item | 1.1.4.3.19 | Nuclear Island Major Maintenance Equipment | H5 | 36 |
| 52 | L979 | list item | 1.1.4.4 | Major Structures | H4 | 37 |
| 53 | L982 | list item | 1.1.4.4.1 | Nuclear Island Major Structures | H5 | 37 |
| 54 | L986 | list item | 1.1.4.4.2 | Reactor Building | H5 | 37 |
| 55 | L1006 | list item | 1.1.4.4.3 | Fuel Handling Building | H5 | 38 |
| 56 | L1019 | list item | 1.1.4.4.4 | Reactor Auxiliary Building | H5 | 38 |
| 57 | L1032 | list item | 1.1.4.4.5 | Nuclear Island Control Building | H5 | 38 |
| 58 | L1046 | list item | 1.1.4.4.6 | Fuel Auxiliary Building | H5 | 39 |
| 59 | L1057 | list item | 1.1.4.4.7 | Support Buildings and Facilities | H5 | 39 |
| 60 | L1061 | list item | 1.1.4.4.8 | Nuclear Island E-Modules | H5 | 39 |
| 61 | L1065 | list item | 1.1.4.4.9 | Energy Island Facilities | H5 | 39 |
| 62 | L1184 | list item | 1.2 | Site Description | H2 | 58 |
| 63 | L1424 | list item | 1.3 | Plant Safety Overview | H2 | 60 |
| 64 | L1427 | list item | 1.3.1 | Licensing Basis Methodology | H3 | 60 |
| 65 | L1433 | list item | 1.3.2 | Fundamental Safety Functions | H3 | 60 |
| 66 | L1458 | list item | 1.3.2.1 | Retaining Radionuclides | H4 | 61 |
| 67 | L1501 | list item | 1.3.2.2 | Controlling Heat Generation | H4 | 63 |
| 68 | L1513 | list item | 1.3.2.3 | Controlling Heat Removal | H4 | 63 |
| 69 | L1525 | list item | 1.3.3 | Defense-in-Depth | H3 | 64 |
| 70 | L1583 | list item | 1.4 | Conformance with Regulatory Criteria and Referenced Material | H2 | 66 |
| 71 | L1586 | list item | 1.4.1 | Regulatory Guidance | H3 | 66 |
| 72 | L1607 | list item | 1.4.2 | Topical Reports and Technical Reports | H3 | 66 |
| 73 | L1612 | list item | 1.4.3 | Generic Safety Issues, Unresolved Safety Issues and TMI Action Items | H3 | 67 |
| 74 | L1631 | list item | 1.4.4 | Codes and Standards | H3 | 67 |

## 5. File-specific observations and recommendations for the cleanup script

### 5.1 권장 적용 순서 (ordered rules)
1. **Withheld 마커 정규화(#11)** — 다른 모든 줄 결합보다 먼저. 패턴: caption(선택적 `Kemmerer Unit 1 PSAR ` prefix, 선택적 말미 ` [[`) → (선택) `[[` 줄 → `This information is withheld in accordance with 10 CFR 2.390` → (선택) `]]SRI`. figure당 `### Figure 1.1-n …` + `\[\[This information is withheld in accordance with 10 CFR 2.390\]\]<sup>SRI</sup>` 2줄로 치환(13건, 모두 PDF에 closer 있음).
2. Cover(L1–11) → frontmatter 추출 후 삭제; TOC/LoT/LoF(L13–71) 삭제(삭제 전 LoT caption 4종 문자열 확보).
3. Header/footer residue 삭제·prefix 제거(#12, 15건).
4. Figure debris span 삭제: L1204–L1422(Fig 1.2-1), L1541–L1580(Fig 1.3-1). **line 번호 또는 caption-anchored span으로만** 삭제하고, legend table(#2, B)과 Fig 1.3-1 note(escape)를 삽입.
5. Figure caption 통일(#13) + raster alt text = caption.
6. Heading 변환(#1): L617 4분할, L619 분리, whitelist 74개 변환. 정규식 `^- (\d+(?:\.\d+)+)\s` 는 reference 항목(`- 1.1-1 TerraPower…`, hyphen 번호)과 구분됨; TOC가 먼저 삭제되어야 중복 매칭이 없음.
7. False list item 5개 marker 제거, nested list(L1598–1602) 복원, list 내부 빈 줄 제거(#17).
8. Page-break 문단 결합 13쌍(#16).
9. Table: Acronym 14 → 1(+`## LIST OF ACRONYMS AND ABBREVIATIONS`), 1.4-1 26 → 1, 1.4-4 9 → 1, 1.4-5 10 → 1 병합; caption 삽입(#5); sheet pseudo-heading 삭제; phantom table 삭제; `Conformance Status`/`Comments` 분리(#7); `<br>` 정규화(#8).
10. 값 수정: `methodologies`(#3), hyphen 7건(#4), `V<sub>S</sub>`/`V<sub>S30</sub>`(#20), `NUREG/CR-7046`(#19), entity unescape(#18).
11. Bold 정의어 5개 복원(#21), 남는 `*` escape(#23), 연속 빈 줄 1개로 축소(126 runs).
12. Frontmatter + page anchor(#22). 제안:
```yaml
---
doc_id: KU1-PSAR-CH01
title: "Kemmerer Unit 1 PSAR, Chapter 1 General Plant and Site Description"
facility: "Kemmerer Power Station Unit 1 (Kemmerer Unit 1), Natrium reactor"
applicant: "US SFR Owner, LLC (USO), a wholly owned subsidiary of TerraPower, LLC"
revision: "Revision 1"
copyright_year: 2025
doe_agreement: "DE-NE0009054"
adams_accession: null   # 문서 내 미기재 (미검증)
source_pdf: "references/pdf/TP_Natrium_PSAR2025_ch1_General Plant and Site Description.pdf"
pdf_pages: 115
page_labels: {"cover": 1, "i-iii": "2-4", "iv-xvii": "5-18", "1.1-1..1.1-39": "19-57", "1.2-1..1.2-2": "58-59", "1.3-1..1.3-6": "60-65", "1.4-1..1.4-50": "66-115"}
tables: ["1.4-1", "1.4-2", "1.4-3", "1.4-4", "1.4-5"]
figures: ["1.1-1", "…", "1.1-17", "1.2-1", "1.3-1"]
withheld_figures: ["1.1-5", "…", "1.1-17"]   # 10 CFR 2.390, SRI
---
```

### 5.2 Pitfalls / 자동 수정 금지 항목
- **원문 오기 보존(#25)**: `HCI`(hydrochloric acid), `Manufactures`, `and, provides`, `conditions.Each`, `an station blackout`, `areas.The`, `power- operated`(Table 1.4-4 원문), `800F`, `Division I`, `TO ENVIROMENT`. 일반 hyphen-space 정규화 규칙(`\w- \w`→`\w-\w`)을 적용하면 `Low-, Medium- and High-Expansion`(L2277)도 훼손되므로 금지.
- **일반 dehyphenation/re-hyphenation 사전 적용 금지**: 복원은 PDF에서 `-\n`이 확인된 7건만. `noncondensible`(L2057), `Nonconservative`, `Noncompliance`, `nonmetallic` 등은 원문 표기. 같은 셀 안에서도 `nonessential`(소실)과 `non-essential`(정상)이 공존(L2073).
- `X` 줄 전역 삭제 금지: `X/Q`(L613), legend의 `X X FENCE` 등 정당한 사용 존재 → span 삭제만.
- `Kemmerer Unit 1`(PSAR 없는 형태)은 본문 고유명사 → `Kemmerer Unit 1 PSAR` 정확 일치만 제거.
- Table 병합 시 행 결합 불필요(분할 행 0 확인). 단 `SSC` 중복 정의(L557–558)는 원문 그대로 유지.
- `<br>` 전역 제거 금지: 1.13(1./2./3., C.2/C.8/C.9), 1.29(C.1–C.4), (xvii) (B)/(C)의 열거 구분은 유지.
- `E[M]`(L200)은 wikilink 아님 — 수정 불필요. Ref 1.4-19 URL은 그대로.
- Fig 1.3-1 barrier label, raster figure 내부 텍스트는 text layer에 없으므로 자동 추출 불가 → C(수동/OCR).
- 번호 heading 판별은 폰트로 불가(heading = Arial 11 regular) → whitelist 또는 “번호 + Title Case + 종결부호 없음 + 단독 줄” 규칙 사용.

### 5.3 Retrieval용 식별자 (frontmatter/tag 후보)
- Plant/site parameters (본문 원문 값): 840 MWt; up to 500 MWe net; pool-type SFR, near-atmospheric; sodium-bonded metallic fuel, HT9 cladding; PHT 2 IHX + 2 PSP; IAC 2 AHX; CRD 13 CRDM (9 primary + 4 secondary CRA); RPS 4 divisions; XIS 4 divisions; 230 kV switchyard, 6.9 kV MV, 480 V; 2 SDG; Lincoln County, Wyoming, ≈3 miles (4.8 km) SW of Kemmerer; Elkol 7.5-minute quadrangle, Zone 12T; 334 acre (135 ha) property, ≈290 acre (117 ha) site; plant north = true north; plant elevation 500 ft-0 in = 6,758 ft-0 in NAVD88 (RXB center coordinates → Table 2.2-1, 타 chapter).
- System/building 약어: RCC, RES, RAC, PHT, IHT, IAC, SCG, SPS(-P/-I/-E), CRD, RPS, XIS, RMS, RIS, NIC(RMC, CTC, UMC, AMC, FHC, PMC, DCS), NSS, ESS, TSS, SGS, CFW, STS, GEN, HRS, FHI, FHE, FHP, NMV, NLV, NDC, NUP, NHT, NHV, NLS, NGL, NCH, NGS, SMS, NFP, NME, RWG, RWL, RWS, PCO, EMV, ELV, EDC, EUP, EHT, ESP; RXB, FHB, RAB, NCB, FAB, E-Modules; Figure 1.2-1 facility no. 11–85.
- Safety concepts: FSF 3종(retaining radionuclides / controlling heat generation / controlling heat removal), DL 5, SARRDL, functional containment barrier 목록(L1486–1498).
- Regulatory keys: RG 번호 183(Table 1.4-1; Full 96 / Partial 24 / OL-stage 63), 10 CFR 50.34(f)(1)(i)…(3)(vii) 47항 + TMI Action Plan ID(`II.B.8`, `I.A.4.2` …), NUREG-0933, Topical Report 14(`NAT-\d{4}-A`, `NATD-LIC-RPRT-000[12]-A`, `TP-QA-PD-0001`), Technical Report 4, ADAMS `ML\d{8}`형 15개, Codes & Standards 167.
- Cross-reference 패턴: `Sections? \d+(\.\d+)*` (62), `Figure 1.x-y` (본문 참조 18; caption 19, LoF 19 별도), `Table \d\.\d-\d+` (본문 참조 11; 타 chapter 표 2.1-1, 2.1-2, 2.2-1 포함), `Reference 1.x-y` (22), `Chapter \d+`.
