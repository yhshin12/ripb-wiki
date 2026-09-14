# Review ch7b: TP_Natrium_PSAR2025_ch7_Descriptions for Safety-Significant SSCs.md (md lines 2389–4273, PDF pages 133–245)

검토 범위: 7.2.4 Sodium Processing System (SPS) – 7.2.5 Control Rod Drive System (CRD) – 7.3 Fuel Handling Systems (7.3.1 FHP, 7.3.2 FHE, 7.3.3 FHI) – 7.4 Radwaste Systems (7.4.1 RWG) – 7.5 Ancillary Systems (7.5.1 NHV, 7.5.2 NFP). 수정은 하지 않았으며(READ-ONLY), 아래 수치는 모두 스크립트로 재현 가능하다(스크래치패드 `ch7b_*.py`, 산출물 `ch7b_*.txt`).

## 0. 개요

| 항목 | 값 |
|---|---|
| md 범위 | L2389–4273 = 1,885 lines (non-blank 1,023, blank 862), 245,582 chars |
| PDF 범위 | p.133–245 (113 pages) = PSAR page label 7.2-41 … 7.5-20 (7.2.4 p133=7.2-41, 7.2.5 p150=7.2-58, 7.3 p164=7.3-1, 7.3.2 p180=7.3-17, 7.3.3 p203=7.3-40, 7.4 p217=7.4-1, 7.5 p226=7.5-1, 7.5.2 p235=7.5-10, 끝 p245=7.5-20) |
| 경계 | L2388 이전의 Figure 7.2.3-2 label debris(L2370–2387, `Main Aerosol Filter Skid` 등, PDF p132)는 ch7a 담당. L4274 `- 7.6 Integrated Controls Systems 7.6.1 …`는 ch7c 담당. 본 범위의 첫 줄(L2389)과 마지막 표(L4264–4271)는 경계를 넘는 표/문단 없음 |
| Tables | 24 = bordered 16 (md GFM table로 변환됨) + borderless "Functional Support" 표 8 (md에서 문단으로 분해됨) |
| Figures | 13 = raster 11 (imageFile30–40) + vector 2 (Figure 7.3.1-1, 7.3.1-2; 내용 소실) |
| Sections | 번호 있는 heading 76 + 번호 없는(밑줄) subheading 63 + References 8 + Table caption 16 + Figure caption 13 |
| Word-level 대조 | PDF 38,882 words vs md 38,342 words (header/footer 제외, `difflib`). 차이는 (a) Figure 7.3.1-1/-2의 CID-encoded label, (b) FHP 기능표 header 2회(14 words), (c) 표 셀 내부 어순 차이로 전부 설명됨. 본문 문장 소실은 발견되지 않음 |
| Missing-content 표본 | 9개 문단을 PDF와 word 단위로 대조, 전부 동일: L2396(p133), L2584(p143), L2703(p150), L2820(p157), L3016(p173), L3204(p183), L3822(p221), L4123(p238; PDF text layer의 `NFPA22`는 md `NFPA 22`가 오히려 정확), L4180(p241). page break에 걸친 continuing 문단 19개도 단어 누락 없음(분할만 발생, F5) |
| Pure noise | figure debris 16 lines/86 chars (L3099–3114) + caption 내 header residue 3×21 chars + page-repeat 표 header 2 lines(114 chars) + 잉여 blank line 165 → 약 0.1 % 미만. 본 범위의 문제는 noise가 아니라 **구조 손상**(heading 76+63, 기능표 8, 문단 분할 45/병합 119)이 지배적 |

Lead 검증 요약: (1) `7.3.1`은 누락이 아니라 L2895 끝에 glued(`…to the SFP. 7.3.1 Water Pool Fuel Handling System`). (2) "`Waste gas inputs are received into the RWG vacuum tank…` region" 의 phantom table은 본 범위에서 **확인되지 않음**: L3812–3834는 깨끗하고 Figure 7.4.1-1은 raster(imageFile40). 본 범위의 phantom table은 Figure 7.3.1-1(L3099–3114)뿐. (3) 반복되는 special-treatment program bullet(`- Quality Assurance Program`, `- Design Reliability Assurance Program`, …)은 PDF의 `●` bullet과 1:1 대응하는 **genuine** 내용(8개 list, 44 bullets; PDF p144, 157, 173, 195, 210, 222, 231, 242) — dedupe 금지. (4) 동일 md5 image pair 41=42, 43=44, 45=46은 범위 밖 L4648/4650/4652(Figure 7.6.2-1 NIC Block Diagram의 vector debris 표 셀)에서 참조됨; 263×81~264×84 px의 파란 grid fill tile로, 같은 fill이 행마다 두 번 그려진 **genuine duplication이지만 장식용 fragment** → figure debris와 함께 삭제 대상(ch7c 담당).

## 1. Findings

| # | T-ID | Sev | Count | md lines (examples) | PDF p. | Evidence / description | Proposed fix | Fix class |
|---|---|---|---|---|---|---|---|---|
| 1 | T6 | H | 8 tables / 49 rows (SPS 12, CRD 3, FHP 7, FHE 12, FHI 1, RWG 1, NHV 10, NNA 3) | L2465–2508, 2769–2777, 2939–2963, 3308–3347, 3605–3607, 3773–3775, 3966–4000, 4097–4110 | 138–139, 155, 168–169, 188–189, 207, 219, 229, 237 | 격자선 없는 3-column 표(`Function ID` / `Function Description` / `<Sys> Functional Support`, header 밑줄)가 문단·list item으로 분해됨. L2465 `Function ID Function Description SPS Functional Support DL3-HR11 SPS Pump Trip on Low Primary` → L2467 설명 → L2469 `Sodium Level (SR)` → L2471 `DL3-RR1b …`: 분류 tag `(SR)`가 ID와 분리되어 다음 행에 붙어 읽힘. L2769 header+`DL3-RC1, DL3-RC2` glued; L3605 header+`DL3-RR1f FHI Seal (SR) The FHI seals to the head perform part of the` / L3607 `primary coolant boundary barrier function.`; 24 행은 `- DL…` list item, 나머지는 plain; page-repeat header L2489, L3334 잔존; DL3-HR10 셀은 2 문단(L2941, L2943). 행 내용 자체는 word diff상 완전 | 표 8개를 GFM 3-col 표로 재구성(ID / Description(분류 tag 포함) / Support), page-split 부분 병합·반복 header 삭제, 다문단 셀은 `<br>`. RWG·NHV는 PDF에도 header 없음 → header 추가 시 "supplied" 표시 또는 FHE 등과 동일 header 사용 | B (pdfplumber words의 x-band [pt]: col1 x0≈162–163; col2 x0≈235 (SPS, FHP, FHI, NHV) / 253 (CRD, FHE) / 227 (RWG, NNA); col3 x0≈404 / 442 (CRD) / 433 (FHE) / 410 (RWG, NNA); 행 경계 = col1에 `DL\d-` 가 나오는 줄) 또는 C |
| 2 | T3 | H | 76 numbered headings, 0개가 `#` heading | list item 70 (L2389 `- 7.2.4 Sodium Processing System` …); 그중 body glued 4 (L2892 `- 7.3 Fuel Handling Systems Fuel handling activities are supported by…`, L3018, L3433, L3855); plain 5 (L2694 `7.2.5 Control Rod Drive System`, L3119 `7.3.2 Ex-Vessel Fuel Handling System The Ex-Vessel…`(glued), L3728, L3898, L4067); line-end glued 1 (L2895 `… 7.3.1 Water Pool Fuel Handling System`) | 133–242 | 범위 내 ATX heading은 caption/References뿐 → heading 기반 chunker는 7.2.5 본문 전체(L2694–2838)를 `### Figure 7.2.4-3` 아래에, 7.3.2 전체를 `### Figure 7.3.1-2` 아래에 귀속시킴(잘못된 section attribution) | `^- (7\.\d(?:\.\d+)+)\s+` 및 plain `^(7\.\d(?:\.\d+)*) [A-Z]` → ATX heading, level = 번호 depth(§4 표). glued 6건은 TOC/PDF title 목록으로 title 끝에서 분리 | A (TOC-derived title list) / B |
| 3 | T3 | M | 63 unnumbered subheadings (PDF에서 밑줄), 0개가 heading | run-in 37 (L2721 `Regulatory Criteria Principal Design Criteria (PDC) are identified…`, L2903 `Spent Fuel Pool The SFP is…`), mid-line 18 (L2905 `…Fuel Pool Cooling The FPC is classified…`, L4013 `…Fuel Handling Building HVAC The FHB normal exhaust…`), 앞 문단 끝 glued 5 (L2780 `…Section 7.2.5.3. Regulatory Guidance`, L3300, L3425, L4090, L2967), standalone plain 3 (L2932, L3461 `References`, L3549) | 151–237 | 폐쇄 어휘 4종 26건(`Regulatory Criteria` 7, `Functional Requirements and Design Criteria` 7, `Regulatory Guidance` 5, `Seismic Classification and Design Codes` 7) + system-specific 37건(`Pool Immersion Cell`, `Ex Vessel Handling Machine`, `In-Vessel Drive Controller`, `Reactor Building HVAC`, `NI Fire Suppression System` 등) | 해당 문자열 앞뒤에서 줄바꿈 후 `#####` heading(§4). 폐쇄 어휘는 regex, 나머지는 PDF 밑줄 검출 목록(§4.2)으로 | A (26) / B (37) |
| 4 | T5 | M | 119 PDF 문단 경계 소실, 52 md lines (subheading run-in 57, RG title/conformance 26, 본문 문단 36) | L2742 (PDC 16 + `Consistent with PDC 26, Reactivity control system…`), L2789 (RG 1.31/1.44/1.87 5문단), L3349 (2 subheading + 4 문단), L3357, L3561 (IVDC 4문단 + FTL subheading·문단), L3641 (3 subheading + 6 문단), L4165 (4문단) | 153–240 | 긴 줄 생성: >1500 chars 9줄, >2000 chars 5줄(L2903 2073, L2905 3035, L3368 2379, L3641 2359, L4165 3124). PDC 26이 PDC 16 항목 안에 들어가 PDC 단위 chunk가 섞임 | 최소: F3 subheading 분리 + `(?<=\. )(Consistent with PDC \d+,)`, `(?<=\. )(RG \d\.\d+,\|Regulatory Guide \d)`, `(?<=\. )(Partial\|Full) [Cc]onformance[.,]` 앞에서 분리(A; 표 안의 `\|`는 regex OR 연산자). 완전 복원은 PDF 문단 gap(line spacing ×1.45) 기반(B) | A (partial) / B |
| 5 | T5 | M | 45 문단 분할 (page break 19 = 범위 내 continuing page break 19/19 전부; intra-page 26) | list item화 28: L2417 `- commensurate with their safety significance.…`, L2420 `- (Reference 7.2.4-2) to maintain isolation.…`, L2815 `- Table 7.2.5-3.`, L4177 `- Section 5.3.`; plain 17: L2431 `make up part of…`, L2599 `well as independent…`, L3291 `via a geometrically sub-critical…` | 133–242 | intra-page 분할은 PDF 줄이 `Section N`, `(Reference`, `Table N`, `described in`으로 시작하거나 subscript가 있는 줄(L3291 keff)에서 발생. 전체 목록 §5.2 | 앞줄이 종결부호 `[.:;?!)”]`로 끝나지 않고 다음 비공백 줄이 소문자/`Section \d`/`(Reference`/`Table \d`/`described` 로 시작하면 `- ` 제거 후 한 줄로 결합. 다음 줄이 대문자로 시작하는 page-break 2건(L2753→2756 `- CRDM has three scram SOVs.`, L4093→4095 `NST. The NNA supports…`)은 page 경계 정보로 결합 | A (+B for 대문자 시작 2건) |
| 6 | T5/T12 | M | 원문에 없는 list marker: PDC 문단 65/77, RG 항목 6, 기타 2 (+F1의 24, F5의 28) | `- Consistent with PDC 2, Design Bases for Protection Against Natural Phenomena, …` L2414; RG L2535, 2536, 3779, 3783, 3947, 3951; L2756, L2779 | 133–237 | PDF의 PDC·RG 문단은 bullet 없는 일반 문단(p135–136 렌더링 확인). PDF의 진짜 bullet(`●`) 92개는 md에서 모두 `- `로 보존됨(프로그램 44, codes 8, CRD 3, SFP 4, FHE 5+15 subsystem, interlock 2, FHI 4, RWG 7, …) | `^- (Consistent with PDC \d+\|RG \d\|Regulatory Guide \d)` → `- ` 제거(표 안의 `\|`는 regex OR 연산자). Reference 목록 77건(`- 7.2.4-1 ASME, …`)은 PDF도 번호 목록이므로 유지 가능 | A |
| 7 | T7/T14 | M | vector figure 2 (내용 전소실) | L3097–3114 (Fig 7.3.1-1: phantom table 4 blocks, 16 lines/86 chars, 셀 전부 공란), L3117 (Fig 7.3.1-2: caption만, 본문/이미지 없음) | 178, 179 | label text가 ToUnicode 없는 CID font(`(cid:51)(cid:82)(cid:82)(cid:79)`=Pool, offset +29)라 opendataloader가 전부 누락. 복호 결과: 7.3.1-1 = Pool Handling Machine, Pool Auxiliary Vault, Intact Fuel Rack, Failed Fuel Rack, Fuel Storage Area, Separation Wall, PIC Cavity, PHM Rails, Cask Loading Pit, Fuel Floor Valve, Spent Fuel Pool, BLTC Rails; 7.3.1-2 = Fuel Storage Area, Cask Loading Pit, Pool Liner, Intact Fuel Rack, Concrete Wall, Separation Wall, PIC Cavity | phantom table 삭제(A). 두 페이지 figure 영역을 PNG로 rasterize(`page.crop(bbox).to_image(resolution=200)`)하여 `![Figure 7.3.1-1 …](…)` 삽입, 복호 label을 alt text/설명으로 추가 | A + B |
| 8 | T6 | M | 3 cells (2 tables) | L2872 CRDM Housing 행: `150 (upper housing in HAA) Note 1 (lower housing)` / `30 (upper housing) 60 (lower housing)`; L2884 Driveline Assembly 행: `Type 316 Stainless Steel Alloy 718` | 161, 162 | 셀 안의 별도 문단 2개가 구분자 없이 연결됨 → "Stainless Steel Alloy 718"처럼 존재하지 않는 재질로 읽히거나 값-대상 결합이 모호 | `150 (upper housing in HAA)<br>Note 1 (lower housing)`, `30 (upper housing)<br>60 (lower housing)`, `Type 316 Stainless Steel<br>Alloy 718` | B/C (3건 수동 patch 권장) |
| 9 | T12 | M | 1 (+12 `*` 셀) | L2680 `* Classification is for integrity of the associated pressure boundary only` | 146 | 선두 `* `가 bullet으로 렌더링되어 Table 7.2.4-1의 `SR*`/`NSRST*`(12 셀) footnote 기호가 사라짐 | `\* Classification is …`(또는 `Note: \* …`), 셀은 `SR\*` escape 권장 | A |
| 10 | T16 | M | 1 | L2980 `…as special treatments, as Table 7.3.1-2.` / L2982 `- described in Section 6.3. Codes and standards that are applicable to the FHP are listed in` | 170 | PDF: "…as special treatments, as described in Section 6.3. Codes and standards that are applicable to the FHP are listed in Table 7.3.1-2." — 문장 순서가 뒤바뀌어 Table 7.3.1-2 cross-reference가 떨어져 나감 | 수동 재배열 | C |
| 11 | T14 | M | 2 | (L2939 앞, L2953 앞) | 168, 169 | FHP 기능표 header `Function ID Function Description FHP Functional Support` 2회 모두 md에 없음(다른 기능표 5개는 header 존재) | F1 재구성 시 header 삽입 | B/C |
| 12 | T4 | M | 3 | L2888 `### Kemmerer Unit 1 PSAR Figure 7.2.5-1 CRD/RPA Cross-Sectional Layout`, L3117, L3894 | 163, 179, 225 (landscape) | page header가 caption heading에 합쳐짐. 본문 내 기타 header/footer residue(`SUBJECT TO DOE…`, `7.x-NN`, `Revision 1`)는 범위 내 0 | `^(#+ )Kemmerer Unit 1 PSAR ` → `\1` | A |
| 13 | T7 | M | 11 raster images, alt text 공란 | L2684, 2688, 2692, 2890, 3521, 3525, 3529, 3718, 3722, 3726, 3896 | 147–225 | Figure 7.2.4-1/-2/-3(imageFile30–32)은 NST/NSRST/SR/Non-SPS 색 legend로 SSC 분류를 표시하며 본문이 이를 인용함(L2522 "Major equipment safety classifications for SPS are identified in Table 7.2.4-1, Figure 7.2.4-1, …") → 분류 정보가 이미지에만 존재 | caption을 alt text로 복사(A) + 핵심 figure 3–4개는 구성요소·분류 설명 추가(C) | A/C |
| 14 | T3 | M | 16 table + 13 figure caption + 7 `### References`; plain `References` 1 | L2644, 2656, 2682, …; L3461 `References` | 145–245 | caption/References가 `###`로 section heading(현재 list item)보다 상위처럼 동작. L3461(7.3.2 References, PDF p196에서 유일하게 bold 대신 밑줄)은 heading이 아님 | F2 적용 후 caption·References를 system heading(`###`)의 하위 `####`로 조정, L3461도 `####` | A |
| 15 | T8 | L | 2 | L3291 `keff ≤ 0.95`, L3368 `B4C` | 187, 191 | 아래첨자 소실(k<sub>eff</sub>, B<sub>4</sub>C). 범위 내 `10-N`, `x10N`, footnote glue는 0 | 대상 치환 | A |
| 16 | T11 | L | 4 | L3469 `Design of Below-theHook Lifting Devices`(PDF p197 `Below-the-⏎Hook`, 줄바꿈 hyphen 결합 시 hyphen 소실; 같은 제목이 L3506/3710에서는 정상), L3691 `Seismic Classificat ion`(좁은 열의 강제 줄바꿈), L4268/L4270 `&amp;` | 197, 212, 245 | 원문 변형 1건(Below-the-Hook) + 표기 잡음 3건. `●` glyph 0, hyphen-space break 0 | `Below-theHook`→`Below-the-Hook`, `Classificat ion`→`Classification`, `&amp;`→`&` | A |
| 17 | T13 | L | italic 129 runs; 밑줄 heading 63 + 기능표 header; change bar 138개/57 pages | 예: L2433 `PDC 30, Quality of Primary Coolant Boundary,`(PDF italic), L2976 `RG 1.13, Spent Fuel Storage Facility Design Basis`(italic) | 133–245 | italic = PDC criterion title ≈78, RG title ≈31, NFPA/IEEE 등 reference title 18, 표 note 1. Revision 1 변경 표시(우측 여백 change bar)가 57/113 pages에 138개(p146 21, p198 8, p234 8 등) | PDC/RG title 이탤릭 복원은 선택(B, fontname 기반). change bar는 필요 시 `<!-- rev1-change -->` 메타데이터로 | B (optional) |
| 18 | T5 | L | 165 | 예: L2390–2391, L2405–2406 | – | blank-after-blank 165줄(1,885줄 중 blank 862) | 연속 blank 1줄로 축약 | A |
| 19 | T15 | M | 범위 전체 | – | 133–245 | page anchor 없음 → 인용 시 PSAR page(7.2-41 … 7.5-20) 추적 불가 | `--markdown-page-separator "<!-- page %%page-number%% -->"` 재변환 또는 page-first-words 매칭으로 anchor 삽입; frontmatter는 file-level 공통 과제 | B |
| 20 | T1/T2/T9/T10 | – | 0 | – | – | 범위 내 cover/TOC/footnote/equation 없음 | – | – |

## 2. Table verification log

bordered 16개는 `pdfplumber.extract_tables()` 결과와 셀 단위(공백 정규화, `&amp;`→`&`) 비교에서 **전 행 일치**(차이 0). 모든 표(24개, ≤30)를 검증함.

| Table ID | md lines | PDF p. | Status (OK / defect IDs) | Notes |
|---|---|---|---|---|
| Table 7.2.4-1 SPS Major Equipment Safety Classifications | L2656–2680 | 146 | OK / T12 (F9) | 18 rows × 2 cols 일치; note `* Classification…`(L2680, PDF italic)의 선두 `*`가 bullet로 오파싱; `SR*`/`NSRST*` 12셀 |
| Table 7.2.5-1 CRD Safety and Seismic Classifications | L2848–2855 | 159 | OK | 4 rows × 2; 제목의 "Seismic"에 해당하는 열은 PDF에도 없음(원문 그대로) |
| Table 7.2.5-2 Applicable Codes and Standards | L2858–2865 | 160 | OK | 4 rows × 3 |
| Table 7.2.5-3 Preliminary CRD Design Conditions | L2868–2877 | 161 | T6 (F8) | 수치 1080/80, 400/300 일치; CRDM Housing 두 셀이 2문단 flatten(`150 (upper housing in HAA) Note 1 (lower housing)`, `30 (upper housing) 60 (lower housing)`); `Note 1: …` 문장 L2877 보존 |
| Table 7.2.5-4 Preliminary CRD Materials of Construction | L2879–2885 | 162 | T6 (F8) | `Type 316 Stainless Steel Alloy 718` = PDF 2줄 flatten |
| Table 7.3.1-1 Primary FHP and Component Classifications | L3061–3075 | 176 | OK | 11 rows × 3 (SR/NSRST, SCS1/SCS2/SCN3) |
| Table 7.3.1-2 Codes and Standards | L3078–3094 | 177 | OK | 13 rows × 3 |
| Table 7.3.2-1 FHE Major Component Classifications | L3481–3496 | 198 | OK | 12 rows × 3 |
| Table 7.3.2-2 Codes and Standards | L3499–3516 | 199 | OK | 14 rows × 3; `…Nuclear Facilities Nuclear Material Lifting`는 원문 |
| Table 7.3.3-1 FHI Safety-Significant Components Classifications | L3689–3698 | 212 | T11 (F16) | 6 rows × 3; header `Seismic Classificat ion` |
| Table 7.3.3-2 Codes and Standards | L3701–3713 | 213 | OK | 9 rows × 3 |
| Table 7.4.1-1 RWG Codes and Standards | L3882–3891 | 224 | OK | 6 rows × 2 |
| Table 7.5.1-1 Codes and Standards Applicable to NI HVAC | L4047–4052 | 233 | OK | 2 rows × 5; 2줄 header(`Author / Organization`, `Year / Revision`)가 올바르게 병합됨 |
| Table 7.5.1-2 NHV Major Equipment Safety Classifications | L4055–4064 | 234 | OK | 6 rows × 2 |
| Table 7.5.2-1 NFP Design Codes | L4240–4261 | 244 | OK | 18 rows × 2 (`NFPA 70®`, `NFPA 72®`) |
| Table 7.5.2-2 NNA Major Equipment Safety Classifications | L4264–4271 | 245 | T11 (F16) | 4 rows × 2; `&amp;` ×2 |
| SPS Functional Support (unnumbered) | L2465–2508 | 138–139 | T6 H (F1) | 12 rows(DL3-HR11, DL3-RR1b, DL3-RR4, DL4-HR1, DL2-RR7, DL2-RR8, DL4-RR8 / DL4-RR3, -RR3a, -RR3b, -RR3c, DL5-PAM1); page-split, 반복 header L2489; DL3-HR11 이름이 설명을 사이에 두고 분리 |
| CRD Functional Support | L2769–2777 | 155 | T6 H (F1) | 3 rows(DL3-RC1/DL3-RC2, DL4-RC3, DL3-RR1); header와 첫 ID glued |
| FHP Functional Support | L2939–2963 | 168–169 | T6 H, T14 (F1, F11) | 7 rows(DL3-HR10, DL3-HR13, DL3-RR8, DL3-RR5a / DL4-HR4, DL2-RR2, DL5-PAM1); header 2회 소실; DL3-HR10 셀 2문단 |
| FHE Functional Support | L3308–3347 | 188–189 | T6 H (F1) | 12 rows(DL3-HR6–HR9, DL3-RR3, -RR3a, -RR4 / DL3-RR5, -RR5a, -RR6, DL4-RR5, DL5-PAM1); 반복 header L3334; 표 직후 subheading·문단이 L3349로 병합 |
| FHI Functional Support | L3605–3607 | 207 | T6 H (F1) | 1 row(DL3-RR1f); header glued, 셀 문장이 두 줄로 분리. 직후 문단(L3609)은 PDF에서도 표 밖 일반 문단(행 누락 아님) |
| RWG (header 없음) | L3773–3775 | 219 | T6 (F1) | 1 row(DL2-RR4) |
| NHV (header 없음) | L3966–4000 | 229 | T6 H (F1) | 10 rows(DL4-RR1, -RR1a, -RR1c, -RR3, -RR3c, -RR4, -RR4b, -RR4c, -RR7, DL5-PAM1) |
| NNA Functional Support | L4097–4110 | 237 | T6 H (F1) | 3 rows(DL4-RR3a, -RR3b, -RR3c) |

Lead 수치 대비(범위 내): column-count mismatch 1(L3111–3114, figure debris), empty header cell 4 blocks(전부 Fig 7.3.1-1 debris), all-empty rows 0, single-column table 1(L3111). 실제 데이터 표에는 column mismatch·empty header 0.

## 3. Figure inventory

| Figure ID | md lines | raster/vector | image file | debris lines to delete | Notes |
|---|---|---|---|---|---|
| 7.2.4-1 Block Flow Diagram of the Primary SPS | L2682–2684 | raster | imageFile30 (4197×2236) | – | p147 landscape; NST/NSRST/SR/Non-SPS 색 legend(분류 정보 이미지에만); alt 공란 |
| 7.2.4-2 Block Flow Diagram of the Intermediate SPS | L2686–2688 | raster | imageFile31 (3282×2004) | – | p148; alt 공란 |
| 7.2.4-3 Block Flow Diagram of the EVST SPS | L2690–2692 | raster | imageFile32 (3212×1421) | – | p149; alt 공란 |
| 7.2.5-1 CRD/RPA Cross-Sectional Layout | L2888–2890 | raster | imageFile33 (2362×2009) | caption 내 `Kemmerer Unit 1 PSAR ` | p163 landscape |
| 7.3.1-1 FHP Top-Down View | L3097–3114 | vector (CID labels) | 없음 | **L3099–3114 전부**(phantom table 4 blocks) | p178; label 20여 개 소실(복호 가능, F7) |
| 7.3.1-2 SFP Side View | L3117 | vector (CID labels) | 없음 | caption 내 `Kemmerer Unit 1 PSAR ` | p179 landscape; md에 caption 외 아무것도 없음 |
| 7.3.2-1 Ex-Vessel Handling Machine Primary Components | L3519–3521 | raster | imageFile34 (2711×1780) | – | p200 |
| 7.3.2-2 Bottom Loading Transfer Cask Primary Components | L3523–3525 | raster | imageFile35 (2665×1772) | – | p201 |
| 7.3.2-3 Ex-Vessel Storage Tank Primary Components | L3527–3529 | raster | imageFile36 (1875×1518) | – | p202 |
| 7.3.3-1 FHI General Arrangement within Reactor Vessel | L3716–3718 | raster | imageFile37 (1548×2464) | – | p214 |
| 7.3.3-2 IVTM Primary Components and Motions | L3720–3722 | raster | imageFile38 (2162×1718) | – | p215 |
| 7.3.3-3 FTL Primary Components | L3724–3726 | raster | imageFile39 (2274×2791) | – | p216 |
| 7.4.1-1 Gaseous Radwaste Processing System Overview | L3894–3896 | raster | imageFile40 (3124×1900) | caption 내 `Kemmerer Unit 1 PSAR ` | p225 landscape |

imageFile30–40은 모두 md5 고유. 7.5절(NHV, NFP)에는 figure 없음(PDF 확인).

## 4. Heading outline check

### 4.1 요약

| 구분 | PDF | md에서 heading으로 렌더링 | list item | plain paragraph | glued (body/앞문단) |
|---|---|---|---|---|---|
| 번호 heading (7.x … 7.x.y.z.w) | 76 | 0 | 70 (그중 body glued 4) | 5 (그중 body glued 1) | line-end glued 1 (7.3.1) |
| 번호 없는 밑줄 subheading | 63 | 0 | 0 | 3 (standalone) | run-in 37, mid-line 18, 앞문단 끝 5 |
| References | 8 | 7 (`###`) | – | 1 (L3461) | – |
| Table / Figure caption | 16 / 13 | 16 / 13 (`###`, 3개는 header residue) | – | – | – |

제안 level(ch7a/ch7c와 일치 필요): `#` 7 → `##` 7.3, 7.4, 7.5 (7.2는 범위 밖) → `###` 7.2.4, 7.2.5, 7.3.1–7.3.3, 7.4.1, 7.5.1, 7.5.2 → `####` 7.x.y.z 및 References/Table/Figure caption → `#####` 7.x.y.z.w 및 번호 없는 subheading(7.2.4.2.1–.3의 번호 체계와 동일 위상).

### 4.2 결함 heading 목록 (번호 heading 76)

| md line | 현재 형태 | 번호 / title | intended |
|---|---|---|---|
| L2389, 2392, 2404, 2409, 2460, 2524, 2561, 2580, 2586, 2590, 2594, 2601, 2605, 2609, 2614, 2639 | list item | 7.2.4 SPS / .1 Summary Description / .2 Design Basis / .2.1 Compliance with Principal Design Criteria / .2.2 Functional Requirements and Design Criteria / .2.3 Conformance with Applicable Regulatory Guidance / .3 System Design and Performance Evaluation / .3.1 Plugging Temperature Indicator / .3.2 Hydrogen Meters / .3.3 Process Radiation Monitors / .3.4 Multipurpose Sampler / .3.5 SPS Filtration / .3.6 Cold Traps / .3.7 Cesium Traps / .4 Special Treatments / .5 Instrumentation Requirements | `###` 7.2.4, `####` 7.2.4.x, `#####` 7.2.4.x.y |
| L2694 | plain | 7.2.5 Control Rod Drive System | `###` |
| L2696, 2716, 2806, 2822, 2834 | list item | 7.2.5.1–7.2.5.5 | `####` |
| L2892 | list item + body glued | 7.3 Fuel Handling Systems + `Fuel handling activities are supported by…` | `##` + 본문 분리 |
| L2895 (끝) | 앞 list item 끝에 glued | 7.3.1 Water Pool Fuel Handling System | `###` (별도 줄) |
| L2898, 2909, 2985, 3034 | list item | 7.3.1.1, .2, .3, .5 | `####` |
| L3018 | list item + body glued | 7.3.1.4 Special Treatments + `Special treatments are initially selected…` | `####` + 분리 |
| L3119 | plain + body glued | 7.3.2 Ex-Vessel Fuel Handling System + `The Ex-Vessel Fuel Handling System (FHE) includes…` | `###` + 분리 |
| L3124, 3272, 3359, 3446 | list item | 7.3.2.1, .2, .3, .5 | `####` |
| L3144, 3177, 3206, 3243, 3247, 3251, 3259 | list item | 7.3.2.1.1 EVHM, .2 BLTC, .3 EVST, .4 EVST Cover Gas, .5 Fueling Floor Valve, .6 CATT, .7 PRC | `#####` |
| L3433 | list item + body glued | 7.3.2.4 Special Treatments + body | `####` + 분리 |
| L3531 | list item | 7.3.3 In-Vessel Fuel Handling System | `###` |
| L3534, 3574, 3625, 3649, 3664 | list item | 7.3.3.1–7.3.3.5 | `####` |
| L3728 | plain | 7.4 Radwaste Systems | `##` |
| L3738 | list item | 7.4.1 Gaseous Radwaste Processing System | `###` |
| L3741, 3751, 3806, 3844 | list item | 7.4.1.1, .2, .3, .4 | `####` |
| L3809, 3836, 3840 | list item | 7.4.1.3.1 System Description, .2 Modes of Operation, .3 Materials and Construction | `#####` |
| L3855 | list item + body glued | 7.4.1.5 Instrumentation Requirements + `The RWG includes the following instrumentation, controls, and displays.` | `####` + 분리 |
| L3898 | plain | 7.5 Ancillary Systems | `##` |
| L3900 | list item | 7.5.1 NI HVAC System | `###` |
| L3903, 3911, 4004, 4015, 4028 | list item | 7.5.1.1–7.5.1.5 | `####` |
| L4067 | plain | 7.5.2 Nuclear Island Fire Protection System | `###` |
| L4069, 4075, 4114, 4199, 4210 | list item | 7.5.2.1–.5 | `####` |
| L4119, 4125, 4144, 4152, 4188 | list item | 7.5.2.3.1–7.5.2.3.5 | `#####` |

### 4.3 번호 없는 subheading 63 (PDF 밑줄; `#####` 권장)

| PDF p. | md line | subheading | 현재 형태 |
|---|---|---|---|
| 151 | L2721 | Regulatory Criteria | run-in |
| 154 | L2764 | Functional Requirements and Design Criteria | run-in |
| 155 | L2780 | Regulatory Guidance | 앞 list item 끝 glued |
| 156 | L2797 | Seismic Classification and Design Codes | run-in |
| 164 | L2903 | Spent Fuel Pool | run-in |
| 165 | L2905 | Pool Immersion Cell | run-in |
| 165 | L2905 | Fuel Pool Cooling | mid-line |
| 165 | L2905 | Fuel Pool Purification | mid-line |
| 166 | L2914 | Regulatory Criteria | run-in |
| 167 | L2932 | Functional Requirements and Design Criteria | standalone plain |
| 169 | L2965 | Structural Support (SR) – Load Path for SR SSCs (FHP에서는 밑줄 없음) | run-in |
| 169 | L2967 | Temporary Load Path for SR SSCs (NSRST) (밑줄 없음) | 앞문단 끝 glued |
| 169 | L2972 | External Hazard Protection (밑줄 없음) | run-in |
| 170 | L2976 | Regulatory Guidance | mid-line |
| 170 | L2980 | Seismic Classification and Design Codes | mid-line |
| 171 | L2994 | Spent Fuel Pool | run-in |
| 172 | L3010 | Pool Immersion Cell | run-in |
| 186 | L3277 | Regulatory Criteria | run-in |
| 188 | L3300 | Functional Requirements and Design Criteria | 앞 list item 끝 glued |
| 189 | L3349 | Temporary Load Path for SR SSCs (NSRST) | run-in |
| 189 | L3349 | Structural Support (SR) – Load Path for SR SSCs | mid-line |
| 190 | L3357 | Seismic Classification and Design Codes | mid-line (FHE에는 PDF에도 `Regulatory Guidance` subheading 없음) |
| 191 | L3368 | Ex Vessel Handling Machine | run-in |
| 192 | L3389 | Ex-Vessel Storage Tank | run-in |
| 193 | L3403 | Bottom Loading Transfer Cask | run-in |
| 194 | L3419 | Pin Removal Cell | run-in |
| 195 | L3425 | New Assembly Preconditioning Station | run-in |
| 195 | L3425 | Assembly Receipt Inspection Stand | 앞문단 끝 glued |
| 196 | L3461 | References | standalone plain (다른 References는 `###`) |
| 203 | L3549 | In-Vessel Transfer Machine | standalone plain |
| 204 | L3561 | In-Vessel Drive Controller | run-in |
| 204 | L3561 | Fuel Transfer Lift | mid-line |
| 204 | L3570 | Rotatable Plug Jack | run-in |
| 204 | L3570 | Rotatable Plug Drive | mid-line |
| 205 | L3572 | Fuel Transfer Lift Shield Plug | run-in |
| 205 | L3579 | Regulatory Criteria | run-in |
| 207 | L3603 | Functional Requirements and Design Criteria | run-in |
| 207 | L3611 | Regulatory Guidance | mid-line |
| 207 | L3619 | Seismic Classification and Design Codes | run-in |
| 208 | L3632 | In-Vessel Transfer Machine | run-in |
| 209 | L3641 | Fuel Transfer Lift | run-in |
| 209 | L3641 | Functional Containment Boundary Seals | mid-line |
| 209 | L3641 | Fuel Transfer Lift Shield Plug | mid-line |
| 218 | L3756 | Regulatory Criteria | run-in |
| 219 | L3771 | Functional Requirements and Design Criteria | run-in |
| 219 | L3777 | Regulatory Guidance | run-in |
| 220 | L3804 | Seismic Classification and Design Codes | run-in |
| 226 | L3916 | Regulatory Criteria | run-in |
| 227 | L3935 | Regulatory Guidance | run-in |
| 228 | L3962 | Functional Requirements and Design Criteria | run-in |
| 230 | L4002 | Seismic Classification and Design Codes | run-in |
| 230 | L4009 | Reactor Building HVAC | run-in |
| 230 | L4009 | Reactor Auxiliary Building HVAC | mid-line |
| 231 | L4013 | NI Contol Building HVAC (원문 오타) | run-in |
| 231 | L4013 | Fuel Handling Building HVAC | mid-line |
| 231 | L4013 | Controlled Release Path | mid-line |
| 235 | L4073 | NI Fire Water Distribution System | run-in |
| 235 | L4073 | NI Fire Suppression System | mid-line |
| 235 | L4073 | NI Fire Detection and Alarm System | mid-line |
| 235 | L4073 | Sodium Leak Detection, Collection, and Containment System | mid-line |
| 236 | L4080 | Regulatory Criteria | run-in |
| 236 | L4090 | Functional Requirements and Design Criteria | 앞 list item 끝 glued |
| 237 | L4112 | Seismic Classification and Design Codes | mid-line (NFP에는 PDF에도 `Regulatory Guidance` subheading 없음) |

## 5. File-specific observations and recommendations for the cleanup script

### 5.1 권장 규칙 순서 (본 범위 기준)

1. **Debris 삭제**: L3099–3114(Fig 7.3.1-1 phantom tables). 규칙: `### Figure …` caption 직후 셀이 전부 공란인 table block 연속 → 삭제. 동시에 두 vector figure(p178, p179)를 rasterize해 image link 삽입(B).
2. **Caption 정리**: `^(#+ )Kemmerer Unit 1 PSAR (Figure|Table) ` → `\1\2 `(3건). 모든 `![](…)` alt에 caption 복사.
3. **Entity/문자**: `&amp;`→`&`(2), `Below-theHook`→`Below-the-Hook`(1), `Classificat ion`→`Classification`(1), `keff`→`k<sub>eff</sub>`(1), `B4C`→`B<sub>4</sub>C`(1), L2680 `* Classification`→`\* Classification`.
4. **번호 heading 승격**(F2): 먼저 glued 6건 분리(L2892 `7.3 Fuel Handling Systems` | body, L2895 끝 ` 7.3.1 Water Pool Fuel Handling System`, L3018, L3119, L3433, L3855) — title은 TOC(ch7a 범위) 또는 PDF에서 가져온 목록으로 정확 일치 분리. 이후 `^- (7\.\d(?:\.\d+)+) ` 및 `^(7\.\d(?:\.\d+)*) [A-Z]`(길이 ≤ 80, 종결부호 없음)을 level 매핑.
5. **번호 없는 subheading 분리·승격**(F3): 폐쇄 어휘 4종은 `(?:(?<=^)|(?<=^- )|(?<=\. ))(Regulatory Criteria|Functional Requirements and Design Criteria|Regulatory Guidance|Seismic Classification and Design Codes)(?= [A-Z]|$)`로 분리(단, `7.2.4.2.2 …`, `7.2.4.2.3 Conformance with Applicable Regulatory Guidance` 등 번호 heading 내부는 제외). system-specific 37건은 §4.3 목록(또는 PDF 밑줄 검출 결과)으로만 분리 — 일반 regex 금지.
6. **기능표 재구성**(F1): `Function ID Function Description` 또는 `^(- )?DL\d-[A-Z]{2,3}\d` 로 시작하는 block을 PDF words(x-band)로 재추출하여 3-col 표로 대체. 반복 header(L2489, L3334) 삭제, FHP header 추가.
7. **문단 분할 결합**(F5): 앞줄이 종결부호로 끝나지 않고, 다음 비공백 줄이 소문자·`Section \d`·`(Reference`·`Table \d`·`described` 로 시작하면 `^- ` 제거 후 공백 하나로 결합. 다음 줄이 대문자로 시작하는 2건(L2753→2756, L4093→4095)은 page-break 위치 기반으로 결합(앞줄이 `Each`, `safety classification`처럼 종결부호 없이 끝나는 것이 단서).
8. **가짜 list marker 제거**(F6): `^- (?=Consistent with PDC \d)`, `^- (?=(RG|Regulatory Guide) \d)`, L2756, L2779.
9. **문단 병합 분리**(F4, 부분): `(?<=\. )(?=Consistent with PDC \d+, )`, `(?<=\. )(?=RG \d\.\d+, (Rev|Revision))`, `(?<=\S )(?=(Partial|Full) [Cc]onformance[.,] )` 앞에서 줄바꿈. 나머지 body 병합 36건은 PDF 문단 gap 기반(B).
10. **Multi-paragraph cell**(F8) 3건 수동 patch, reading-order(F10) L2980–2982 수동 patch.
11. 연속 blank line 축약, page anchor 삽입(B).

### 5.2 문단 분할 45건 전체 목록 (F5)

- Page break 19: L2414→2417(p133/134, list), L2428→2431, L2449→2452(list), L2519→2522, L2597→2599, L2738→2741(list), L2753→2756(list, 대문자 `CRDM`), L2990→2992, L2999→3002, L3168→3170, L3262→3264, L3389→3391, L3619→3621, L3671→3673, L3828→3830, L3962→3964, L4009→4011, L4093→4095(`NST.`), L4182→4184.
- Intra-page 26: L2418→2420, L2435→2437(plain), L2514→2516, L2516→2519, L2705→2707, L2723→2726, L2764→2766, L2779→2780, L2797→2799, L2813→2815, L2892→2895, L2916→2918, L2934→2936, L2965→2967, L2974→2976, L3018→3021, L3021→3022, L3119→3121, L3289→3291(plain, subscript 줄), L3303→3305, L3378→3380, L3433→3436, L3561→3563, L3632→3634, L3651→3653, L4175→4177.

### 5.3 자동 수정 금지 (원문 그대로인 항목; PDF 대조 확인)

- 원문 오타/비표준 표기: `ASME B.31.1`(L2418, p134), `described in Section 7.6.3 Venting`(마침표 없음, L2703, p150), `e.q., pipe rupture`(L3241, p184), `(N872)`, `N862`(L3355, p190), `configurations.The`(L3600), `(Section 7.8.1.1).The`(L3630), `system.The`(L3822), `NI Contol Building HVAC`, `alertsr operators`(L4013, p231), `If the BLTC losses plant power`(L3204), `complimentary monitoring`(L2599), `rotating carousal`(L3393), `it's aerosols`(L2922), `Concrete Strutures`(L2996), `multi purpose sampler`(L2597), `Ex Vessel Handling Machine`(hyphen 없음, p191), `Carousel Rotation-The`, `BLTC-EVHM Lockout-An`(p196), `-- Design Stage Man-Rem Estimates`(L2559), `define the RES design basis`(CRD 절 L2719의 원문 copy-paste), FHI 절의 `listed in Table 7.3.2-2`(L3623, 원문도 7.3.2-2), 참고문헌 연도 불일치(`ASME B31.1, 2020` vs 본문 2022).
- 원문 편집 메모가 PSAR에 그대로 실린 문장: L3277 `Licensing management has decided to delete PDC 1 from all PSAR sections since it is addressed globally in PSAR Chapter 5.` — 삭제 금지.
- p237 NFP의 순서(`Regulatory Guide 1.189 … Plants` → `Safety classifications for major … Table 7.5.2-2.` → `Full Conformance. …`)는 PDF 자체 배치이므로 재배열 금지.
- Genuine 소문자 bullet L3541–3544(`- shuffle core assemblies …` 등 4개; 선행 줄이 `:`로 끝남) — 결합 규칙에서 제외(연속 `- ` 항목끼리는 결합 금지).
- 반복되는 program bullet list 8개(44 bullets)와 SPS codes list 8 bullets — genuine.
- 표 셀의 `SR*`, `NSRST*` 별표 — 삭제 금지(escape만).
- `Revision 0`(md) vs PDF `Revision0`(p154) — md 쪽이 더 정확, 수정 불필요.

### 5.4 기타 관찰

- 7.2.4 SPS만 Design Basis 하위가 번호(7.2.4.2.1–.3)이고 나머지 7개 시스템은 동일 내용을 번호 없는 밑줄 subheading으로 표기 → heading level을 동일 위상(`#####`)으로 맞추면 시스템 간 동형 chunk 구성이 가능.
- Italic PDC criterion title(≈78)은 `Consistent with PDC N, <Title>, …` 형식에서 comma로 경계가 보존되어 있어 RAG 영향은 작음(L).
- Revision 1 change bar 138개(57 pages)는 PSAR 개정 추적용 정보로, 필요 시 별도 메타데이터로만 보존 권장.

### 5.5 Retrieval용 식별자 (frontmatter/tag 후보)

- System acronyms: SPS(SPS-P/-I/-E), CRD/CRDM/CRA/SOV, FHP(SFP, PIC, FPC, FPP, FFC, PHM), FHE(EVHM, BLTC, EVST, FFV, CATT, PRC, PEM, NAPS, ARIS, CAP, FTA), FHI(IVTM, RPD, RPJ, FTL, FTLSP, IVDC), RWG, NHV, NFP(NFD, NFS, NFA, NNA).
- Defense-line PSF IDs 41종: DL2-RR2, -RR4, -RR7, -RR8; DL3-HR6–HR11, HR13; DL3-RC1, RC2; DL3-RR1, RR1b, RR1f, RR2, RR3, RR3a, RR4, RR5, RR5a, RR6, RR8; DL4-HR1, HR4; DL4-RC3; DL4-RR1, RR1a, RR1c, RR3, RR3a, RR3b, RR3c, RR4, RR4b, RR4c, RR5, RR7, RR8; DL5-PAM1 (정규식 `\bDL\d-[A-Z]{2,3}\d+[a-z]?\b`).
- PDC 인용 33종: 1, 2, 3, 4, 12, 13, 14, 15, 16, 19, 26, 28–33, 44, 60–64, 70–78, 80. RG 31종(1.13 … 1.244, 4.21, 8.8, 8.19). Seismic class: SCS1 19, SCN3 9, SCN1 8, SCS2 3.
- Cross-reference 패턴: `Section \d+(\.\d+)+` 195, `Table 7.x.y-n` 37, `Figure 7.x.y-n` 32, `Reference 7.x.y-n` 60 → wikilink/anchor 변환 후보.
