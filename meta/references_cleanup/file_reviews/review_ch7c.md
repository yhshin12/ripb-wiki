# Review ch7c: TP_Natrium_PSAR2025_ch7_Descriptions for Safety-Significant SSCs.md (md lines 4274–7207, PDF pages 246–372)

범위: 7.6 Integrated Controls Systems (7.6.1–7.6.8), 7.7 Electrical Systems (7.7.1), 7.8 Buildings and Structures (7.8.1–7.8.4).
검증 도구: pdfplumber 0.x (page text, words+fontname, rects → underline/change-bar 검출), Read 도구 page rendering (pp. 251–257, 262, 268–270, 283–284, 286, 295–296, 308, 322, 325, 328, 331, 334, 339–340), md5/PIL (images).
보조 산출물(scratchpad): `ch7c_pages.json`(PDF page text), `ch7c_fmt2.json`(underline/italic spans), `ch7c_heads2.py`, `ch7c_lists2.py`, `ch7c_splits.py`, `ch7c_subheads.py`, `ch7c_dltab.py`(DL table row reconstruction prototype), `ch7c_cover.py`, `ch7c_paras.py`, `ch7c_headblock.txt`.

## 0. 개요

| 항목 | 값 |
|---|---|
| md 범위 | L4274–L7207 = 2,934 lines (non-blank 1,499; blank 1,435, 그중 연속 blank 잉여 323), 295,185 chars, 43,978 words |
| PDF 범위 | pp. 246–372 = 127 pages (PSAR page label 7.6-1…7.6-80, 7.7-1…7.7-10, 7.8-1…7.8-37). 경계: p.245 = Table 7.5.2-2 (범위 밖), L4273 이전 |
| Numbered sections | 146 (depth: 7.x 3개, 7.x.y 13개, 7.x.y.z 39개, 7.x.y.z.w 91개) — md에서 ATX heading으로 올바르게 렌더된 것 0개 |
| Unnumbered sub-headings | ≈202 (underline 172 + italic-only RG heading 30) — 약 93 %가 본문과 glued |
| Tables | ruled 3 (7.6.1-1, 7.6.3-1, 7.6.5-1) + borderless DL-function tables 12 logical (77 rows; page-split 4: UMC, RPS(3 pp.), XIS, RIS) = 15. 추가로 figure debris 내 phantom table 46개 |
| Figures | 8 (raster 2: 7.6.4-1, 7.6.7-1 / vector 6: 7.6.2-1, 7.6.5-1, 7.6.6-1, 7.6.8-1, 7.7.1-1, 7.7.1-2) |
| 본문 텍스트 손실 | 없음: PDF body line 4,013개 전수 대조(공백 무시 substring) 결과 table-cell 행(열 interleave)과 1건(Ref. 7.6.3-12의 " - " 소실)을 제외하고 모두 md에 존재. 역방향(md sentence → PDF)에서도 converter가 만든 가짜 텍스트 없음 |
| Noise 추정 | figure debris 289 lines / 3,422 chars (L4629–4693, L5651–5653, L5851–5853, L6284–6401, L6405–6504) + caption 헤더 잔재 3×21 chars + 반복 table header 3 lines(≈160 chars) + `&amp;` 67×4 chars + 잉여 blank 323 lines. 즉 line 기준 ≈10 %(non-blank 기준 183/1,499 ≈12 %), char 기준 ≈1.3 %. noise 자체보다 **구조 붕괴(heading/sub-heading/table/list)**가 이 범위의 주 결함 |

## 1. Findings

| # | T-ID | Sev | Count | md lines (examples) | PDF p. | Evidence / description | Proposed fix | Fix class |
|---|---|---|---|---|---|---|---|---|
| 1 | T6/T16 | H | RPS DL table 22 rows 중 4 rows 오정렬 | L4834–4844, L4862–4867 | 269–270 | `DL3-RC2 Reactor scram on loss of power RPS outputs fail in the safe state in the event` / `of a loss of incoming power. DL3- HR2 PSP trip on high-high primary` / (HR2 support) / `sodium temperature` / (**HR3 support "…the ISPs are tripped."**) / `DL3-HR3 Intermediate sodium pump (ISP) trip…` → HR3의 support 문장이 HR3 ID **앞**(HR2 뒤)에 위치. ID→다음 문단 규칙으로 chunking하면 HR2/HR3(PSP vs ISP trip) 대응이 뒤바뀜. `- DL4-HR7 Manual ISP trip ISP pumps are tripped on manual switch. DL4-RR8 Manual SPS pump trip on low` 뒤에 RR8 support, 그 뒤 `primary sodium level` 파편 | 12개 DL table 전체를 PDF word 좌표(underlined header x0 = column 경계)로 재구성하여 3-col Markdown table로 교체 (`ch7c_dltab.py` prototype: 77/77 row ID·cell 텍스트 복원 확인, 마지막 row는 vertical gap으로 절단 필요) | B |
| 2 | T6/T16 | H | RIS DL table 14 rows 중 3 rows | L5458–5466 | 295 | L5461 한 문단에 RC1e·RC1h·RC1j 세 support 문장이 병합되어 `- DL3-RC1e …` 아래 붙고, `- DL3-RC1h Reactor scram on low-low primary sodium level`(L5463)·`- DL3-RC1j …loss of primary sodium flow`(L5466)은 support 없음 → RC1j의 "PSP speed and PSP current" 사실이 RC1e에 귀속 | #1과 동일 (재구성) | B |
| 3 | T16 | H | 1 table (4 rows) | L5705–5727 | 308 | RMS DL table이 PDF에서는 `7.6.6.2.1 Defense Line Functions` 아래인데 md에서는 `- 7.6.6.2.2 Principal Design Criteria`(L5709) **다음**(L5712–5727)에 위치 → DL4-RR1c/RR4a/RR4b/DL5-PAM1이 PDC 절로 chunk됨 | table block을 L5709 앞으로 이동 후 재구성 | B (+C 확인) |
| 4 | T6 | M | 12 logical tables / 77 rows 전부 prose화 | L4465–4478 (AMC), L4482–4495 (CTC), L4499–4518 (UMC), L4790–4869 (RPS), L5161–5196 (XIS), L5444–5504 (RIS), L5712–5727 (RMS), L6038–6040 (AST), L6156–6178 (NDC/NUP), L6574–6582 (RXB sub), L6776–6778 (FHB super), L6898–6900 (RAB sub) | 254–256, 268–270, 283–284, 295–296, 308, 322, 328, 339, 350, 356 | borderless table(underlined header만 존재) → default table-method가 미검출. header가 첫 row와 glued 8건(L4482, L4499, L5161, L5712, L6038, L6574, L6776, L6898); page-split 반복 header 잔존 3건(L4505, L5170, L5496), RPS는 p.269/270 header 소실; Function Description cell이 support 문장을 사이에 두고 분리 7건(L4482/4486 `pump (ISP) trip on low IHT level`, L4499/4503 `(HAA) HVAC operations following postulated release`, L5712/5716, L4836/4840, L4862/4867, L6159/6162, L6169/6172); XIS: RC1a support가 header와 함께 ID 앞(L5161), RC1g+RC1i support 병합(L5179), RC1i ID 뒤 support 없음(L5181) — support 문장이 모두 동일하므로 사실 오류는 아님; NDC/NUP: 12 rows가 공유하는 rowspan support(`The NDC and NUP provide electric power to support performance of these functions.`)가 DL4-RC3 행에만 붙고, RC4+DL2-HR2(L6159), HR7+RR3b(L6169), `Detection DL4-RR4c …`(L6172) row 병합 | 재구성 시 (a) page-split sheet 병합·반복 header 제거, (b) NDC/NUP support cell fill-down, (c) 각 table 앞에 원문 context line(예: `Function ID | Function Description | RPS Functional Support`)을 header로 유지 — 원문에 table caption이 없으므로 caption은 합성하지 말고 section heading으로 식별 | B |
| 5 | T3 | M | 146 numbered headings: ATX 0, list item 131, plain 14, `####` 1; glued-with-following 31, glued-after-preceding 3 | L4274 `- 7.6 Integrated Controls Systems 7.6.1 Instrumentation and Control Systems Introduction`; L4368 `7.6.2 Nuclear Island Control System`; L4696; L5685 (`… 7.6.6.1.2 Equipment Locations` 문단 끝에 glued); L6101 `7.7 Electrical Systems Electrical systems include…`; L6669 `7.8.2 Fuel Handling Building The Fuel Handling Building (FHB) houses…`; L6726 `#### 7.8.2.1.3 …` | 246–372 | 전체 목록은 §4. 7.6.6.1.2, 7.8.2.1.4는 앞 문단 끝에 붙어 있어 해당 절 본문이 이전 절로 chunk됨 | PDF 추출 heading whitelist(146개, `^7\.[678](\.\d+)*\s+Title`)로 exact title 경계에서 split → level = dot수+1 (`7.6`→`##`, `7.6.1`→`###`, `7.6.1.1`→`####`, `7.6.1.1.1`→`#####`) | A (whitelist는 B로 1회 생성) |
| 6 | T3 | M | ≈202 unnumbered sub-headings 중 ≈187 glued (standalone ≈15) | L4333 (`SR I&amp;C Systems The Reactor Protection System…`, 중간에 `NSRST I&amp;C Systems`), L4497 (FHC/PMC/RMC/UMC Sub-System 4개가 한 줄), L5035, L5609, L6598 (`External Hazard Protection for SR SSCs, (SR) … Regulatory Guides … Seismic Classification and Design Codes The SR RXB substructure seismic classification is SCS1 … Loads and Load Combinations …`), L7085, L7144, L7181 | 248–372 | underline로 표시된 소제목(“Seismic Classification and Design Codes” 12회, “Loads and Load Combinations”, “Functional Requirements”, “Regulatory Criteria/Guidance”, “Structural Acceptance Criteria”, “Repair/Identification/Reliability…”, “RPS Workstation”…)과 RG conformance heading(`RG 1.xx, Revision n, *Title*` 41개: standalone 9, 나머지 glued) — agent가 질의할 anchor가 문장 중간에 매몰 | PDF underline geometry(`ch7c_fmt2.json`)+italic RG line으로 whitelist 생성 후 **정확한 위치**에서 split, `######` 또는 bold line으로 승격 | B (generic 제목은 C) |
| 7 | T99-1 (paragraph merge) | M | ≈300(±10 %) PDF paragraph/sub-heading block이 md에서 줄 중간 시작; 91 md lines에 집중; >1,000 chars 17 lines, >2,000 chars 2 lines | L4333 (2,430 chars = PDF 6 문단+2 소제목), L6236 (2,636 chars = PDF p.331의 8 문단: 72 h/2 h 배터리, VRLA, BTS, 모니터링, 접지, 서지, 독립성, battery room), L6598 (1,611), L7181 (1,760), L5703 (RG 8 blocks) | 248, 331, 340, 371 | 수치(72 hours, 2 hours, 24 hours, 480/120 VAC, 250 VDC 등)는 보존되나 chunk가 과대·경계 부정확 | #6 split 후, 남은 병합은 PDF paragraph 시작 좌표(vertical gap > 1.25×line pitch)로 split | B |
| 8 | T5 | M | 91 split continuations | mid-page false list item 70 (예: L4304 `- Section 6.3. Special treatments…`, L4713 `- as defined by IEEE 497-2016…`, L5136 `- Generating Station Safety Systems,” (Reference 7.6.4-2)…`, L5284 `- Section 2.6.2) without loss…`, L6686 `- 5 foot thick walls extending…`); page-break paragraph split 13 (L4337→4339, L4530→4533, L5116→5118, L5679→5681, L5691→5694, L5735→5737, L6017→6019, L6149→6152, L6594→6596, L6622→6624, L6795→6797, L6813→6815, L6986→6988); page-break list split 1 (L5358→5360); mid-page plain split 2 (L6140→6142, L6699→6701); table-cell split 5 (#4에 포함) | 전역 | L5691→5694는 PRM 위치 목록 `…FHB,` / `(airborne), SCG Cell (airborne)…`를 끊어 “FHB (airborne)”가 분리. 추가로 genuine list가 page break에서 빈 줄로 끊긴 사례 ≈9 (L5404/5407, L5769/5772, L6061/6063, L6959/6962, 참고문헌 L5055/5058, L5628/5631, L6656/6659, L7029/7032 등) | 직전 문단이 종결부호(`.:;?!)”`) 없이 끝나고 다음 줄이 `- `+(소문자 \| `Section ` \| `described in` \| `in Section` \| `(Reference` \| `Generating` \| `Power Generating` \| `Commentary` \| `10 CFR` \| `\d+ foot`)이거나 소문자 시작 plain이면 공백 1개로 join | A |
| 9 | T99-2 (spurious list marker) | M | ≈121 | `- Consistent with PDC …` 66/93 (L4530, L4883, L5209, L6140, L6547…), DL rows 48 (L4467, L4792…L4850, L5163, L5446…, L6158–6175), RG heading 4 (L4771, L4776, L5146, L5147), 기타 3 (L4937, L4944, L5232) | 256–372 | PDF에는 bullet 없음(PDF genuine list = ● 170 + sub-bullet “-” 21 + numbered 3 = 194; md genuine bullet 186 + `- 1.` 3 + raw ● 5와 일치) | `^- (?=Consistent with PDC \d)` 제거; DL rows는 #1/#4 재구성으로 해소; RG heading은 #6 | A |
| 10 | T7 | M | debris 289 lines / 3,422 chars; phantom tables 46; all-empty rows 36; `<br>` 96; decorative image ref 6; figure label→heading 2 | L4629–4693, L5651–5653, L5851–5853, L6284–6401, L6405–6504; `###### NUP` L6350, L6466 | 262, 304, 313, 334, 335 | Fig 7.6.2-1: `IOIO ModulesModules`(PDF가 글자를 이중 overprint), imageFile41–46 = 파란 grid pattern fill(42×13 pt) 3종이 PDF 자체에서 **동일 좌표에 2회씩 배치**(p.262 image list: (476,458),(542,459),(610,459) 각 2회) → md5 중복(41=42, 43=44, 45=46)은 genuine이나 정보가치 0. Fig 7.7.1-1/-2: `1Ø 120V` 8, `1Ø INVERTER` 4, `BATTERY CHARGER` 6 등 label 조각 | span 삭제 후 caption 아래 PDF page raster(예: 150–200 dpi PNG) 삽입 + caption 기반 alt text. SLD의 고유 사실(Div A/B = `480V RXB MCC A/B`, Div C/D = `480V FHB MCC A/B`, TVSS, MTS, portable DG 연결점)은 alt text/짧은 label 목록으로 보존 | A (삭제) + B (raster) |
| 11 | T14 | M | 3 figures 내용 전무 | L5649–5653 (7.6.5-1), L5849–5853 (7.6.6-1), L6099 (7.6.8-1) | 304, 313, 325 | text가 outline화된 vector drawing(텍스트 layer에 caption만 존재; curves 411/2,103/937) → md에는 caption(+빈 3×2 table)만. Fig 7.6.8-1에는 본문에 없는 사실(AST 4 channel의 전원 “Nuclear Energy Island 120 V AC, Division A/A/B/B”, Signal Processing→Bi-stable Generator→RTB Shunt Trip Division A–D; channel C box label “Bi-stable Generator B” — 원문 그대로) 존재 | page raster 삽입(B); 필요 시 figure label을 C로 전사 | B/C |
| 12 | T99-3 (nesting) | M | 21 sub-items / 3 parents | L4379–4415 | 251–252 | AMC(7), CTC(5), UMC(9)의 “-” 하위 항목이 부모와 같은 level + 빈 줄로 분리 → “(monitoring only)” 하위 시스템 목록이 부모 subsystem과 분리 | 하위 항목 4-space indent 복원 (PDF “- ” 마커 기반) | B |
| 13 | T6 | M(low) | 17/23 rows | L5070–5091 | 280 | Table 7.6.3-1 rowspan group cell(`RPS Electronics Cabinets`, `RPS Divisional SVDUs (MCR)`, `RPS Manual Switches`, `Remote Shutdown SVDUs`, `Reactor Trip Breakers`) 첫 행 외 공란 → row 단위 retrieval 시 group 소실. 값 자체는 23 rows 모두 일치 | col 1 fill-down | A |
| 14 | T11 | M | `&amp;` 67 / 42 lines | L4277, L4333, L4350(caption `I&amp;C`), L4605, L7181 (`Analysis &amp; Design`) | — | exact match “I&C” 실패 | `&amp;`→`&` | A |
| 15 | T4 | L | 3 | L4627, L5378, L5849 `### Kemmerer Unit 1 PSAR Figure …` | 262, 292, 313 | 그 외 header/footer 잔재 0 | prefix 제거 | A |
| 16 | T7 | L | 2 | L5380 imageFile47, L5980 imageFile48 | 292, 319 | raster, alt text 빈 값 | caption을 alt text로 | A |
| 17 | T11 | L | ● 5 (3 lines); dash 소실 1; ® 뒤 공백 소실 2 | L5559 `● IEEE 603-2018 ● IEEE 379-2014 ● IEEE 384-2018`(3 bullet 한 줄), L6061, L6063; L5061 `…important to safety Seismic qualification` (PDF p.279 `safety -` + 줄바꿈); L6922, L7153 `GT STRUDL®Version 40` (PDF `STRUDL® Version 40`) | 279, 298, 322–323, 357, 370 | — | ● → list item 분리; `®(?=\S)`→`® `; 7.6.3-12는 수동 복원 | A (dash는 C) |
| 18 | T13 | L | italic PDC title 93, italic RG title 41; underline(소제목 표지) ≈172; revision change bar 37 (24 pages) | 예: L4522 `Consistent with PDC 2, Design bases for protection…`(title italic 소실); change bar: p.331 `Divisions C and D batteries are sized … for 2 hours`, p.351/352/360/361 SCN1 문장, p.246–249 NAT-4950-A Rev. 2 참조 | 246–361 | Rev. 1 변경 표시가 md에서 완전히 소실(개정 추적 질의 불가) | italic 복원(`*…*`)은 font span 기반; change bar는 `<!-- rev1-change -->` 등 marker 선택 적용 | B |
| 19 | T3 | L | `### References` 7, 비-heading “References” 6; `### Table/Figure` caption 11 | L4341…L7198; L4620 (`…not a stand-alone system. References`), L5620, L5972 (`…into the SAR. Reference`), L6653, L6840, L7023 | — | section이 heading이 아닌 상태에서 caption·References만 h3 → hierarchy 역전. glued “References”는 참고문헌 목록을 앞 문단/list에 귀속 | References → 해당 section level+1 heading; caption은 heading 대신 bold line 또는 최하위 level로 통일 | A |
| 20 | T99-4 | L | 3 | L6992–6994 `- 1. The envelope…` | 361 | numbered list가 bullet+번호로 이중 표기 | `^- (\d+\. )`→`\1` | A |
| 21 | T15 | M | 1 (범위 전체) | — | 246–372 | page anchor 없음 → 인용 시 PSAR page label(7.6-23 등) 확인 불가 | `--markdown-page-separator "<!-- page %page-number% -->"` 재변환 또는 PDF body line 매칭으로 anchor 삽입 | B |
| 22 | T8/T9/T10/T12/T1/T2 | — | 0 | — | — | 범위 내 superscript는 `®` 3개뿐(보존됨), footnote·equation 없음, `[[`/`#word`/`$`/`==`/`^`/`*`/`_` 없음, cover·TOC 없음. 선행 lead의 `8 x 101`, `DL5-PAM1 Post Accident Monitoring (NSRST)`(L1979–3998)는 **범위 밖** | — | — |

## 2. Table verification log

| Table ID | md lines | PDF p. | Status (OK / defect IDs) | Notes |
|---|---|---|---|---|
| Table 7.6.1-1 I&C System Classification and DL Functions | L4350–4365 | 250 | OK (T11 caption `&amp;`) | 12 rows × 3 cols 전부 pdfplumber와 일치 (NIC Not Applicable; RMC NST DL2, DL4, DL5; CTC/UMC/AMC NSRST DL2, DL4, DL5; PMC NST; FHC NST No DLs identified; RPS SR DL3, DL4, DL5; XIS SR DL2, DL3, DL5; RIS SR `DL2, DL3, DL4,DL5`(공백 누락은 원문); AST NSRST DL4; RMS NSRST DL4, DL5) |
| Table 7.6.3-1 RPS Equipment and Classifications | L5065–5091 | 280 | OK (T6 rowspan 공란 17) | 23 rows 값 일치: SR/SCS1 12 (Cabinet A–D, RTB A1–D2), NSRST/SCN1 10 (SVDU A–D, Manual Switch Panel A–D, Remote Shutdown SVDU A/B), NST/None 1 (Data Gateway) |
| Table 7.6.5-1 RIS Variable Summary | L5635–5646 | 303 | OK | 8 rows: Hot Pool Temp 4 SR; Hot Pool Level 4 SR; Cold Pool Temp 8 SR; PSP Shaft Speed 8 SR; PSP Current Detector 8 SR; RV-GV Liquid Sodium Detection 3 NSRST; Core Exit Temp 15 NSRST; Reactor Head Temp 3 NST |
| DL table – AMC | L4463–4478 | 254 | T6 (prose), 값 OK | 3 rows: DL4-RR3a, DL4-RR3b, DL4-RR4a; 소제목 `AMC Sub-System` glued (L4463) |
| DL table – CTC | L4480–4495 | 255 | T6, T16 | 3 rows: DL2-HR2, DL4-HR2, DL4-HR3; header+`DL2-HR2 Intermediate sodium` glued, 설명 나머지 `pump (ISP) trip on low IHT level`가 support 뒤(L4486) |
| DL table – UMC | L4497–4518 | 255–256 | T6 (page-split, 반복 header L4505), T16 | 4 rows: DL4-RR1c, RR3c, RR4b, RR4c; RR1c 설명 `(HAA) HVAC operations following postulated release`가 support 뒤(L4503); `poistion`은 원문 오타 |
| DL table – RPS | L4790–4869 | 268–270 | **T6, T16 (H)** | 22 rows (DL3-RC1a–j, RC2, HR2, HR3, HR11, HR12; DL4-RC1, RC3, RC4, HR6, HR7, RR8; DL5-PAM1). 수치 setpoint는 원문에도 없음(정성 기술만). 오정렬: RC2 support 분할(L4834/4836), HR2 설명 분할(L4836/4840), HR3 support가 ID 앞(L4842→L4844), HR7+RR8 병합(L4862), RR8 설명 분할(L4867). p.269/270 반복 header 소실 |
| DL table – XIS | L5161–5196 | 283–284 | T6, T16 (M) | 9 rows (RC1a, RC1d, RC1f, RC1g, RC1i, HR2, HR3, HR12, PAM1). `XIS includes sensors that monitor neutron flux and send signals to the RPS.` 8회 = PDF 8회(genuine) + PAM1 변형 1. 반복 header L5170. `DL3- HR2`(공백)는 원문 |
| DL table – RIS | L5444–5504 | 295–296 | **T6, T16 (H)** | 14 rows (RC1b, c, d, e, h, j; HR2, HR3, HR11, HR12; DL4-HR2, DL4-HR3; DL4-RR8; DL5-PAM1). RC1e/h/j support 병합(L5461), RC1h·RC1j 고아. 반복 header L5496 |
| DL table – RMS | L5712–5727 | 308 | **T16 (H)**, T6 | 4 rows (DL4-RR1c, RR4a, RR4b, DL5-PAM1); 잘못된 section(7.6.6.2.2) 아래; RR1c 설명 분할 |
| DL table – AST | L6038–6040 | 322 | T6 | 1 row DL4-RC4; header+row 한 문단, support 문장 중간 분할 |
| DL table – NDC/NUP | L6154–6178 | 328 | T6 (rowspan, row merge) | 12 rows (DL4-RC3, RC4, DL2-HR2, DL4-HR2, HR3, HR6, HR7, RR3b, RR4c, RR7, RR8, DL5-PAM1) ID 모두 존재; 공유 support는 RC3에만 |
| DL table – RXB substructure | L6574–6582 | 339 | T6 | 3 rows (DL3-HR4, DL4-RR1, DL4-RR1a); header+HR4 glued, support 분할(L6574/6576). 이어지는 ID 없는 PSF(Load Path for SR SSCs (SR) 등)는 table이 아니라 underline 소제목 |
| DL table – FHB superstructure | L6776–6778 | 350 | T6 | 1 row DL4-RR7; header+row glued, 분할 |
| DL table – RAB substructure | L6898–6900 | 356 | T6 | 1 row DL4-RR3; header+row glued, 분할 |

검증 방법: ruled table 3개는 `pdftool.py tables`와 cell 단위 대조; DL table 12개는 page rendering 육안 대조 + `ch7c_dltab.py`로 column x-경계 기반 cell 재구성 후 md 포함 여부 확인(77 rows 모두 ID·Function Description·Support 텍스트 존재, 분할/순서만 결함). 범위 내 table 15개 → 전수 검사.

## 3. Figure inventory

| Figure ID | md lines | raster/vector | image file | debris lines to delete | Notes |
|---|---|---|---|---|---|
| 7.6.2-1 Nuclear Island Control System Block Diagram | caption L4627 | vector (+ 6 tiny raster pattern fills) | imageFile41–46 (263×81/264×84 px; 41=42, 43=44, 45=46) | L4629–4693 (65 lines, 2,192 chars, 30 phantom tables, 96 `<br>`, 8 empty rows) | caption에 `Kemmerer Unit 1 PSAR` prefix. image 중복은 PDF 자체의 동일좌표 이중 배치(genuine)이나 장식용 → 6개 ref 모두 삭제. 텍스트 layer가 이중 overprint(`PPaanneell`) → debris에 `IOIO ModulesModules`. page raster로 대체 권장 |
| 7.6.4-1 XIS Overview | L5378–5380 | raster | imageFile47 (2781×1804) | 없음 | prefix 제거, alt text 필요 |
| 7.6.5-1 Reactor Instrumentation System Block Diagram | L5649–5653 | vector (outlined text) | 없음 | L5651–5653 (빈 3×2 table) | 내용 전무 → page raster 필요 |
| 7.6.6-1 RMS Interface Diagram | L5849–5853 | vector (outlined text) | 없음 | L5851–5853 (빈 3×2 table) | prefix 제거; 내용 전무 → raster |
| 7.6.7-1 MCR Layout | L5978–5980 | raster | imageFile48 (2040×2677) | 없음 | alt text 필요 |
| 7.6.8-1 AST Signals and Interface | L6099 | vector (outlined text) | 없음 | 없음 (caption 바로 다음이 `7.7 Electrical Systems…` glued heading) | 내용 전무; figure 전용 사실(전원 Division A/A/B/B 등) 존재 |
| 7.7.1-1 Simplified NSRST Electrical Systems SLD – Div A/B | L6282–6401 | vector (text layer 있음) | 없음 | L6284–6401 (118 lines, 683 chars, 8 phantom tables, 13 empty rows, `###### NUP` L6350) | 고유 label: `480V RXB MCC A/B`, TVSS, NDC/NUP/NLV 경계, `PROVISION FOR CONNECTION TO PORTABLE DIESEL GENERATOR` → alt text 보존 |
| 7.7.1-2 Simplified NSRST Electrical Systems SLD – Div C/D | L6403–6504 | vector (text layer 있음) | 없음 | L6405–6504 (100 lines, 493 chars, 6 phantom tables, 11 empty rows, `###### NUP` L6466) | 고유 label: `480V FHB MCC A/B`(Div C/D 급전 MCC가 FHB 소재라는 사실은 figure에만 존재). 범위 내 두 caption 모두 `###` 보유(“caption without ###” lead는 L209 List of Figures로 범위 밖) |

## 4. Heading outline check

요약 (numbered headings 146, PDF pp.246–372 text line `^7\.[678](\.\d+)*\s+Title` 기준; 누락 0):

| md form | count |
|---|---|
| list item, 단독 | 109 |
| list item + 뒤 텍스트 glued | 21 (본문 glued 11, underline 소제목 glued 10) |
| list item + 앞 텍스트 glued | 1 (7.6.1, L4274) |
| plain paragraph, 단독 | 4 (7.6.2 L4368, 7.6.2.2.2 L4520, 7.6.3 L4696, 7.6.5.1.1 L5389) |
| plain + 뒤 glued | 8 |
| plain + 앞 glued (+뒤 glued 포함) | 2 (7.6.6.1.2 L5685, 7.8.2.1.4 L6736) |
| `####` (level 오류 + glued) | 1 (7.8.2.1.3 L6726) |
| 올바른 ATX heading | **0** |

목표 level: `7.6/7.7/7.8`→`##`, `7.x.y`→`###`, `7.x.y.z`→`####`, `7.x.y.z.w`→`#####`, unnumbered 소제목→`######`.

단독 list-item 109개(모두 `- ` 제거 + level 부여): L4281 7.6.1.1→####; L4286 7.6.1.1.1→#####; L4290 7.6.1.1.2→#####; L4294 7.6.1.1.3→#####; L4299 7.6.1.1.4→#####; L4305 7.6.1.2→####; L4370 7.6.2.1→####; L4429 7.6.2.1.1→#####; L4438 7.6.2.1.2→#####; L4443 7.6.2.2→####; L4458 7.6.2.2.1→#####; L4557 7.6.2.3→####; L4583 7.6.2.3.2→#####; L4598 7.6.2.3.3→#####; L4606 7.6.2.3.5→#####; L4611 7.6.2.4→####; L4698 7.6.3.1→####; L4722 7.6.3.1.1→#####; L4730 7.6.3.1.2→#####; L4785 7.6.3.2.1→#####; L4959 7.6.3.3→####; L4970 7.6.3.3.1→#####; L4982 7.6.3.3.2→#####; L5017 7.6.3.3.3→#####; L5039 7.6.3.3.4→#####; L5094 7.6.4→###; L5097 7.6.4.1→####; L5113 7.6.4.1.1→#####; L5124 7.6.4.1.2→#####; L5129 7.6.4.2→####; L5156 7.6.4.2.1→#####; L5204 7.6.4.2.2→#####; L5263 7.6.4.3→####; L5308 7.6.4.3.2→#####; L5326 7.6.4.3.3→#####; L5344 7.6.4.3.4→#####; L5348 7.6.4.3.5→#####; L5355 7.6.4.4→####; L5382 7.6.5→###; L5385 7.6.5.1→####; L5395 7.6.5.2→####; L5436 7.6.5.2.1→#####; L5551 7.6.5.3→####; L5561 7.6.5.3.1→#####; L5573 7.6.5.3.2→#####; L5597 7.6.5.3.3→#####; L5615 7.6.5.3.4→#####; L5656 7.6.6→###; L5659 7.6.6.1→####; L5698 7.6.6.2→####; L5705 7.6.6.2.1→#####; L5709 7.6.6.2.2→#####; L5781 7.6.6.3.1→#####; L5789 7.6.6.3.2→#####; L5807 7.6.6.3.3→#####; L5825 7.6.6.3.4→#####; L5829 7.6.6.3.5→#####; L5834 7.6.6.4→####; L5856 7.6.7→###; L5864 7.6.7.1→####; L5876 7.6.7.1.1→#####; L5887 7.6.7.1.2→#####; L5921 7.6.7.1.3→#####; L5952 7.6.7.2.1→#####; L5961 7.6.7.2.2→#####; L5965 7.6.7.3→####; L5982 7.6.8→###; L5985 7.6.8.1→####; L5993 7.6.8.1.1→#####; L6001 7.6.8.1.2→#####; L6006 7.6.8.2→####; L6033 7.6.8.2.1→#####; L6053 7.6.8.3→####; L6077 7.6.8.3.3→#####; L6086 7.6.8.3.4→#####; L6103 7.7.1→###; L6106 7.7.1.1→####; L6133 7.7.1.2→####; L6185 7.7.1.3→####; L6188 7.7.1.3.1→#####; L6214 7.7.1.3.2→#####; L6238 7.7.1.4→####; L6250 7.7.1.5→####; L6506 7.8→##; L6513 7.8.1→###; L6520 7.8.1.1→####; L6523 7.8.1.1.1→#####; L6676 7.8.2.1→####; L6679 7.8.2.1.1→#####; L6691 7.8.2.1.2→#####; L6746 7.8.2.2→####; L6749 7.8.2.2.1→#####; L6755 7.8.2.2.2→#####; L6830 7.8.2.2.4→#####; L6855 7.8.3→###; L6872 7.8.3.1→####; L6875 7.8.3.1.1→#####; L6879 7.8.3.1.2→#####; L6951 7.8.3.1.4→#####; L6966 7.8.3.2→####; L7013 7.8.3.2.4→#####; L7039 7.8.4→###; L7050 7.8.4.1→####; L7053 7.8.4.1.1→#####; L7058 7.8.4.1.2→#####; L7110 7.8.4.2→####; L7113 7.8.4.2.1→#####; L7120 7.8.4.2.2→#####; L7188 7.8.4.2.4→#####

특수 결함 37개 (split 위치 주의):

| md line | PDF p. | heading | current form | intended | glued text |
|---|---|---|---|---|---|
| L4274 | 246 | 7.6 Integrated Controls Systems | list + glued | `##` | “7.6.1 Instrumentation and Control Systems Introduction” |
| L4274 | 246 | 7.6.1 Instrumentation and Control Systems Introduction | glued after 7.6 | `###` | — |
| L4321 | 247 | 7.6.1.2.1 Instrumentation and Control Systems | list + glued | `#####` | “The I&amp;C system architecture, to include representative figures…” |
| L4368 | 251 | 7.6.2 Nuclear Island Control System | plain | `###` | — |
| L4520 | 256 | 7.6.2.2.2 Principal Design Criteria | plain | `#####` | — |
| L4581 | 259 | 7.6.2.3.1 Qualified Instrumentation and Control | plain + glued | `#####` | “The NIC meets the quality standards…” |
| L4605 | 260 | 7.6.2.3.4 Secure Instrumentation and Control | list + glued | `#####` | “Security for I&amp;C systems is addressed…” |
| L4696 | 263 | 7.6.3 Reactor Protection System | plain | `###` | — |
| L4735 | 265 | 7.6.3.2 Reactor Protection System Design Bases and Associated Safety Functions | plain + glued | `####` | “The RPS is designed to perform assigned…” |
| L4880 | 270 | 7.6.3.2.2 Principal Design Criteria | list + glued | `#####` | “PDC are identified in Section 5.3…” |
| L5302 | 288 | 7.6.4.3.1 Qualified Instrumentation and Control | list + glued | `#####` | “The XIS meets the quality standards…” |
| L5389 | 293 | 7.6.5.1.1 Reactor Instrumentation System Architecture | plain | `#####` | — |
| L5393 | 293 | 7.6.5.1.2 Reactor Instrumentation System Equipment Location | plain + glued | `#####` | “The RIS measurement sensors are located…” |
| L5510 | 296 | 7.6.5.2.2 Principal Design Criteria | list + glued | `#####` | “PDC are identified in Section 5.3…” |
| L5685 | 306 | 7.6.6.1.1 System Architecture | plain + glued | `#####` | “The RMS provides local and control room indication…” |
| L5685 | 306 | 7.6.6.1.2 Equipment Locations | glued at end of L5685 | `#####` | (다음 L5687이 본문) |
| L5741 | 309 | 7.6.6.3 Fundamental Design Principles in the System Design | list + glued | `####` | “System performance of each RMS monitor meets…” |
| L5945 | 317 | 7.6.7.2 Remote Shutdown Complex | plain + glued | `####` | “In the event that the MCR cannot be inhabited…” |
| L6042 | 322 | 7.6.8.2.2 Principal Design Criteria | list + glued | `#####` | “PDC are described in Section 5.3…” |
| L6067 | 323 | 7.6.8.3.1 Qualified Instrumentation and Control | list + glued | `#####` | “The AST is qualified per…” |
| L6068 | 323 | 7.6.8.3.2 Reliable Instrumentation and Control | list + glued | `#####` | “The method for confirming…” (+ L6070 `- described in Section 6.2. Identification`) |
| L6101 | 326 | 7.7 Electrical Systems | plain + glued | `##` | “Electrical systems include the Nuclear Island (NI) Auxiliary Electrical Systems…” |
| L6542 | 337 | 7.8.1.1.2 Design Bases | list + glued | `#####` | 소제목 “Regulatory Criteria” |
| L6600 | 340 | 7.8.1.1.3 Structure Design and Performance Evaluation | list + glued | `#####` | 소제목 “SR Structural Characteristics that Support SR Functions” |
| L6626 | 342 | 7.8.1.1.4 Special Treatments | list + glued | `#####` | “Special treatments are initially selected…” |
| L6637 | 342 | 7.8.1.2 Reactor Building Superstructure | list + glued | `####` | 소제목 “Summary Description” |
| L6669 | 345 | 7.8.2 Fuel Handling Building | plain + glued | `###` | “The Fuel Handling Building (FHB) houses…” |
| L6726 | 348 | 7.8.2.1.3 Structure Design and Performance Evaluation | `####` + glued | `#####` | 소제목 “SR Structural Characteristics that Support RSFs” |
| L6736 | 348 | 7.8.2.1.4 Special Treatments | glued after Structural Acceptance Criteria 문단 + glued | `#####` | “Special treatments are initially selected as described in” |
| L6790 | 351 | 7.8.2.2.3 Structure Design and Performance Evaluation | list + glued | `#####` | 소제목 “NSRST Structural Characteristics that Support Risk-Significant or Defense-in-Depth Functions” |
| L6917 | 357 | 7.8.3.1.3 Structure Design and Performance Evaluation | list + glued | `#####` | 소제목 “NSRST Structural Characteristics that Support Safety-Significant Functions” |
| L6969 | 359 | 7.8.3.2.1 Summary Description | list + glued | `#####` | “The steel-framed RAB superstructure is 144 feet wide…” |
| L6970 | 359 | 7.8.3.2.2 Design Basis | list + glued | `#####` | 소제목 “Regulatory Criteria” |
| L6981 | 360 | 7.8.3.2.3 Structure Design and Performance Evaluation | list + glued | `#####` | 소제목 “NSRST Structural Characteristics that Support Risk-Significant or DID Functions” |
| L7087 | 366 | 7.8.4.1.3 Structure Design and Performance Evaluation | list + glued | `#####` | 소제목 “SR Structural Characteristics that Support PSFs” |
| L7100 | 367 | 7.8.4.1.4 Special Treatments | plain + glued | `#####` | “Special treatments are initially selected…” |
| L7146 | 369 | 7.8.4.2.3 Structure Design and Performance Evaluation | list + glued | `#####` | 소제목 “NSRST Structural Characteristics that Support Risk-Significant or Defense-in-Depth Functions” |

Unnumbered 소제목(≈202)은 개별 목록 대신 whitelist 생성 방법을 권고(§5 rule 5). 대표 glued 사례: L4333 (`SR I&amp;C Systems`, `NSRST I&amp;C Systems`), L4463/4480/4497 (AMC/CTC/FHC/PMC/RMC/UMC Sub-System), L4620 (`Post Accident Monitoring / Safety Parameter Display System`), L4757–4769 (RPS RG 1.22–1.118, 한 줄에 최대 3개), L4987–5037 (RPS Repair…Predictable and Repeatable Behavior, 16개), L5578–5611 (RIS 동일 계열 17개), L5812/5818 (RMS Redundancy/Power Supply), L5899–5919 (MCR workstation 5개), L6075–6084 (AST), L6138/6154/6180 (NDC/NUP), L6584–6605, L6644–6648 (RXB), L6696–6736, L6760–6828 (FHB), L6884–6947, L6973–7011 (RAB), L7063–7098, L7125–7185 (NCB). Standalone로 올바르게 분리된 것: L5593 `Maintenance Bypass`, L6584, L6590, L6784, L6904, L7134, L7140 등 ≈15개.

## 5. File-specific observations and recommendations for the cleanup script

### 5.1 권장 처리 순서 (범위 L4274–7207)
1. **Entity/glyph 정규화 (A)**: `&amp;`→`&` (67); `●` 분리(L5559 → 3 items, L6061/6063 → list items); `STRUDL®Version`→`STRUDL® Version` (L6922, L7153); `^- (\d+\. )`→`\1` (L6992–6994).
2. **Figure 처리**: caption의 `Kemmerer Unit 1 PSAR ` prefix 제거(L4627, L5378, L5849) (A); debris span 삭제(§3 표의 5개 span, 289 lines) (A); imageFile41–46 ref 삭제 (A); 모든 vector figure(7.6.2-1, 7.6.5-1, 7.6.6-1, 7.6.8-1, 7.7.1-1, 7.7.1-2; PDF pp.262/304/313/325/334/335)는 page raster를 새로 생성해 삽입 (B); alt text = caption (A). SLD label 중 `480V RXB MCC A/B`, `480V FHB MCC A/B`는 alt text에 보존.
3. **DL-function table 재구성 (B)**: `ch7c_dltab.py` 방식(“Function ID” underlined header의 x0로 3 column 경계 산출, row 시작 = col 1의 `DL\d-` 토큰, row 종료 = vertical gap > 30 pt 또는 다음 비-table 텍스트). 대상 16 page-segment → 12 tables / 77 rows. 기대 row ID 목록으로 QA:
   AMC {DL4-RR3a, RR3b, RR4a}; CTC {DL2-HR2, DL4-HR2, DL4-HR3}; UMC {DL4-RR1c, RR3c, RR4b, RR4c}; RPS {DL3-RC1a–j, DL3-RC2, DL3-HR2, HR3, HR11, HR12, DL4-RC1, RC3, RC4, HR6, HR7, RR8, DL5-PAM1}; XIS {DL3-RC1a, d, f, g, i, DL3-HR2, HR3, HR12, DL5-PAM1}; RIS {DL3-RC1b, c, d, e, h, j, DL3-HR2, HR3, HR11, HR12, DL4-HR2, HR3, DL4-RR8, DL5-PAM1}; RMS {DL4-RR1c, RR4a, RR4b, DL5-PAM1}; AST {DL4-RC4}; NDC/NUP {DL4-RC3, RC4, DL2-HR2, DL4-HR2, HR3, HR6, HR7, RR3b, RR4c, RR7, RR8, DL5-PAM1} (support cell fill-down); RXB {DL3-HR4, DL4-RR1, DL4-RR1a}; FHB super {DL4-RR7}; RAB sub {DL4-RR3}. RMS table은 `7.6.6.2.1` 아래로 이동. 재구성 후 원 prose block(§2의 md lines) 삭제.
4. **Numbered heading (A, whitelist B)**: 146개 whitelist로 exact title 문자열을 찾아 split·승격. 7.6.7.1.3 제목은 `…Compliance with 10 CFR 50.34(f)`까지(2줄 제목). Reference entry(`- 7.6.3-9 IEEE…`, hyphen 형식)는 절대 heading으로 승격하지 말 것.
5. **Unnumbered 소제목 (B/C)**: PDF underline rect(높이 < 1.5 pt, 단어 bottom과 −2.5…+3 pt 겹침) + italic RG heading line으로 whitelist(page, 문자열, 순서) 생성 → md에서 **순서 보존 cursor**로 위치를 찾아 split. “Redundancy”, “Independence”, “Reliability”, “Identification”, “Human Factors”, “Repair”, “System Integrity” 등 일반명사는 본문 문장에도 등장하므로(예: L5537 “…high functional reliability…”) 반드시 PDF 순서 cursor와 “앞이 문장 종결 + 뒤가 대문자 본문” 조건을 함께 사용. RG heading은 `RG 1.xx, Revision n, <Title>` 다음에 오는 `The <SYS> …conform` / `Application-specific elements …` / `NIC sub-systems …` / `RMS components …`에서 split.
6. **Continuation merge (A)**: §1 #8 규칙. 70 false list items + 16 plain split. 단, 직전 줄이 heading(whitelist)이거나 table/figure caption이면 병합 금지.
7. **Spurious bullet 제거 (A)**: `^- (?=Consistent with PDC \d+,)` 66개, L4937/L4944/L5232의 `- ` 제거.
8. **Paragraph re-split (B)**: rule 5 이후에도 1,000 chars 초과 line(L6236 등)은 PDF paragraph 시작 좌표로 split.
9. **기타 (A)**: Table 7.6.3-1 col 1 fill-down; nested sub-bullet 21개 indent 복원(L4381–4387, L4392–4396, L4407–4415); `References` 정규화(L4620, L5972의 glued “References/Reference” 분리); caption/References level 조정; 잉여 blank 323 lines 축소.
10. **Formatting (B, 선택)**: PDC 93개·RG 41개 title italic 복원; revision change bar 37개(24 pages) marker; page anchor 삽입(재변환 `--markdown-page-separator` 권장).

### 5.2 자동 수정 금지 (원문 그대로여야 하는 항목; PDF 대조 완료)
- **genuine 반복**(md 횟수 = PDF 횟수): `Security for I&C systems is addressed through the physical security…` 6 (NIC, RPS, XIS, RIS, RMS, AST; pp.260/278/290/301/311/324 — lead의 “×5”보다 1회 많음); `XIS includes sensors that monitor neutron flux and send signals to the RPS.` 8 (+PAM 변형 1); `The neutron flux measurement signals are replicated and isolated…` **연속 2회**(L5200, L5202 = PDF p.284에도 2회) — 원문 중복이므로 dedupe 금지; `Special treatments are initially selected` 15; `Quality Assurance Program Description` 17; `Design Reliability Assurance Program` 15; `Equipment Qualification Program` 11; `PRA safety functions (PSFs) are determined` 10; `The method for confirming specific reliability…` 7; `NRC regulatory guidance documents are listed in Section 1.4.1` 6; `DL5-PAM1` 5 (RPS/XIS/RIS/RMS/NDC-NUP 각 1).
- **원문 오타·불일치**(수정 금지, 필요 시 metadata alias만): `poistion` (L4518), `compares Them` (L4798), `DL3- HR2` (L4836, L5184; PDF pp.269/284 — ID 정규화는 frontmatter/tag에만), `IEEE Standard for the Decide and Qualification` (L4976, p.275), `ANSI/ISI` (L5052, p.278), `redundancy.The divisional` 및 문단 끝 `RG 1.75 R3.` (L5232, p.286 가시 텍스트), `IEEE 379-2000, March 9, 2001` (L5846), NIC/RMS의 `fully conform to RG 1.180, Revision 4` (L4456, L5703; heading은 Revision 2), `Design based for protection against natural phenomena` (PDC 2 title 변형), `DL2, DL3, DL4,DL5` (Table 7.6.1-1), NIC seismic class `SCN3` (L4577, p.258), Fig 7.6.8-1 channel C의 `Bi-stable Generator B`, `PDC are identified in Chapter 5.3` (L5729).
- figure debris 삭제 시 SLD 고유 사실(MCC 소재 건물)을 잃지 않도록 alt text 선기록.
- `1Ø`의 `Ø`는 phase 기호(원문) — encoding 오류로 오판하지 말 것.

### 5.3 Retrieval용 식별자 (frontmatter/tag 후보)
- **DL function IDs (38 unique)**: DL2-HR2; DL3-RC1a…RC1j, DL3-RC2, DL3-HR2, HR3, HR4, HR11, HR12; DL4-RC1, RC3, RC4, HR2, HR3, HR6, HR7, RR1, RR1a, RR1c, RR3, RR3a, RR3b, RR3c, RR4a, RR4b, RR4c, RR7, RR8; DL5-PAM1.
- **Systems/acronyms**: NIC (AMC, CTC, FHC, PMC, RMC, UMC; DCS), RPS (RadICS, SVDU, RTB), XIS, RIS, RMS (DRMS, ARM, ERM, PRM), AST, NUP, NDC, NLV, RVT, STS, RMBS, BTS, SDG, MCR, RSC, ERF, GVDS, EIC; RXB, FHB, RAB, NCB, MCRE, HAA, RAC, IAC, SFP, EVHM, FHE.
- **Classification records (agent 질의 대상, 모두 md 본문에 존재)**: I&C: RPS SR / XIS SR (SCS1) / RIS SR (SCS1) / RMS NSRST (SCN1) / AST NSRST (SCN1) / NIC AMC·CTC·UMC NSRST (SCN3); NDC/NUP NSRST (SCN1); 건물: RXB substructure SR SCS1, RXB superstructure NST(ASCE 7-16, SCN1 수준 설계), FHB substructure SR SCS1, FHB superstructure NSRST SCN1, RAB sub/superstructure NSRST SCN1, NCB substructure SR SCS1, NCB superstructure NSRST SCN1. 전기 수치: 120 VAC 1-phase inverter/250 VDC/480-120 VAC RVT, battery 72 h (Div A/B)·2 h (Div C/D), charger recharge 24 h, VRLA (IEEE 1187-2013, 1189-2007, 485-2020, 1491-2012).
- **PDC**: 1, 2, 3, 4, 10, 13, 15, 16, 17, 18, 19, 20–26, 28, 29, 35–37, 60, 61, 63, 64, 72, 81, 82. **RG**: 1.13, 1.21, 1.22, 1.47, 1.53, 1.75, 1.76, 1.89, 1.97, 1.100, 1.105, 1.118, 1.142, 1.143, 1.152, 1.153, 1.180, 1.204. **Standards**: IEEE 603-2018/-1991, 379-2014/-2000, 384-2018/-1992, 338-2022, 420-2013, 497-2016, 7-4.3.2-2016, IEEE/IEC 60780-323-2016, 60980-344-2020; ACI 349-13, 318-19, 318-08, 350.3-20; AISC N690-18, 360-16, 341-16; ASCE 7-16, 43-19, 4-16; IBC 2021; ASME NOG-1-2020. **Topical reports**: NAT-4950-A Rev. 2 (ML25232A241), RadICS 2016-RPC003-TR-001 (ML20202A030, SE ML19134A193).
- Cross-reference 패턴: `Section \d+(\.\d+)+` 462회, `Table 8.0-1`, `Table 6.4-x`, `Figure 1.1-x`.

### 5.4 검증하지 못한 항목
- 종결부호로 끝나는 줄에서 page break가 난 문단 분리(문장 경계 분할)는 텍스트만으로 판별 불가 → 미집계.
- ≈300 paragraph-merge 수치는 vertical-gap heuristic 기반(±10 %).
- Fig 7.6.5-1/7.6.6-1 도면 내부 label은 전사하지 않음(7.6.8-1만 rendering으로 확인).
