# Review ch6: TP_Natrium_PSAR2025_ch6_Safety-Significant SSC Criteria and Capabilities.md (md lines 1–1697, PDF pages 1–80)

## 0. 개요

| 항목 | 값 |
|---|---|
| md | 1,697 lines (non-blank 1,029), 156,265 chars; 최장 행 L674 = 2,529 chars; 1,000 chars 초과 행 12개 (L188, 205, 292, 333, 534, 538, 542, 551, 623, 674, 682, 1087) |
| PDF | 80 pages (p1 cover, p2–3 TOC/LOT, p4–11 §6.1 [6.1-1…6.1-8], p12 §6.2, p13 §6.3, p14–53 §6.4 본문+References [6.4-1…6.4-40], p54–80 Tables [6.4-41…6.4-67]; p59–68, p71–74 = landscape(rot 90)); struct tree 없음 |
| md ↔ PDF 매핑 | L1–11 → p1; L13–56 → p2–3; L59–253 → p4–11; L255–266 → p12; L268–275 → p13; L277–1122 → p14–53; L1125–1694 → p54–80 |
| Tables | 20개 table ID (6.1-1, 6.4-1A, 6.4-1B, 6.4-2 … 6.4-18) → md table block 28개 (2-sheet table 8개 = 16 blocks + 단일 12개) |
| Figures | 0 (본문 figure 없음; "Figure 1.2-1"은 타 chapter 교차참조). raster 3개는 cover 장식 이미지 (md5가 PSAR 7개 chapter에서 동일) |
| Sections | 번호 section 74개 (depth1 4, depth2 8, depth3 28, depth4 34) + chapter title 1; underlined 소제목 98개 + underlined run-in lead phrase 6개; design-transient 소제목 30개 |
| 본문 텍스트 완전성 | p4–53 PDF token 18,691 vs md 18,647, SequenceMatcher 전체 대조 결과 **본문 prose 누락 없음** (차이는 subscript 재결합, 하이픈 결합 1건, λ 수식 배치뿐). 누락은 **표 셀·표 caption·표 note**에 집중 |
| 순수 noise 추정 | cover 11 lines/534 chars + TOC/LOT 44 lines/4,261 chars + header 잔재 2 standalone lines(+2 caption 혼입) + sheet-2 반복 header 24 lines/1,523 chars ≈ **81 lines, ≈6.4k chars (≈4.1 %)**; 추가로 `<br>` 44, 셀 내 `•` 15, 연속 빈 줄(≥2) 162 runs, 값이 모두 빈 표 행 49개(대부분 손실의 결과) |

**핵심 결론**: (1) 하중조합 표 6개(Table 6.4-5/6/7/8/11/12)에서 **load factor 179개(전체 522개의 34 %)와 load case/equation header 66개, 합계 245 셀이 소실**되었다. 특히 SSE(Ess) 행은 6개 표 모두에서 md상 비어 있어(원본 11개 값) "SSE가 어떤 조합에도 포함되지 않는다"는 오답을 유도한다. (2) 표 6개(6.4-2, 6.4-4, 6.4-7, 6.4-8, 6.4-11, 6.4-12)의 caption이 사라져, 구조가 동일한 6.4-7↔6.4-11(concrete, C-9…C-17), 6.4-8↔6.4-12(steel, S-17…S-25)를 md만으로는 구별할 수 없다. (3) 표 note 9개에서 줄 끝 단어가 잘렸다(11개 지점). (4) 번호 heading 74개가 전부 list item이고 underlined 소제목 98개가 heading으로 인식되지 않아 structure-aware chunking이 불가능하다. pdfplumber는 모든 표를 완전하게 추출하므로(검증 완료) 표 계열 결함은 class B로 결정론적 복구가 가능하다.

## 1. Findings

| # | T-ID | Sev | Count | md lines (examples) | PDF p. | Evidence / description | Proposed fix | Fix class |
|---|---|---|---|---|---|---|---|---|
| 1 | T6 | **H** | 245 셀 (factor 179 + header 66), 6 tables / 12 sheets | L1231 `|Design Load Cases(1)(5)| |C-1|…|C-9| | | | | | | |`; L1233 `|Dead|D (3)|1.4|1.2|…|1.2| | | | | | | |`; L1246 `|Safe Shutdown Earthquake|Ess| | | …|`; L1294 `…|S-13(5)| | | | | | | | | | |`; L1529 `|…|NB2-8| | |` | 61–68, 71–74 | "Extreme and Abnormal" 구간(및 6.4-6의 S-14…S-17 구간) 값이 대량 소실. 표별 손실(값/헤더): 6.4-5 48/14 (C-9(6)…C-17 7개 ID 소실, Dead·Live·Soil·Thermal·Crane·SE·Ess·Wtw·Wtp·Wtm·Fa·Pa·Ta·Ra·Yr·Yj·Ym 값 소실), 6.4-6 63/40 (S-14…S-25 11개 ID + NB2-5…NB2-9 소실), 6.4-7 19/0, 6.4-8 12/4 (S-24(8), S-25 ID), 6.4-11 18/0, 6.4-12 19/8 (S-24(8), S-25, NB2-9×2). SSE 값 11개 전부 소실. 셀 이동(shift)·잘못된 값은 0 (손실만 발생). | pdfplumber `extract_tables()` 결과로 12개 sheet를 교체 (셀 단위 대조로 완전성 확인됨). 기호열 subscript 재결합 필요("L r"→"Lr", "W (2) tw"→"Wtw (2)"), 6.4-12는 선두 빈 열 제거 | B |
| 2 | T14/T6 | **H** | 6 tables (11 sheets) caption 없음 | L1142–1143 (6.4-2 s1, caption·sheet 표기 모두 없음), L1170 (6.4-2 s2), L1207 `### (Sheet 1 of 2)` (6.4-4), L1350 (6.4-7), L1397 (6.4-8), L1479 (6.4-11), L1525 (6.4-12) | 56–57, 59–60, 65–68, 71–74 | caption 문자열이 누락되고 `(Sheet n of 2)`만 heading으로 남음. 6.4-7/6.4-11, 6.4-8/6.4-12는 열·행 구조가 동일하여 귀속 불가(값이 잘못된 표에 붙을 위험) | PDF 각 쪽 상단 caption 행(bold, "Table 6.4-x …")을 추출하여 heading으로 복원; sheet 병합 후 caption 1개만 유지 | B |
| 3 | T14 | **H** | 9 notes, 11 지점 | L1273 `…occurs simultaneously with the is zero.` (누락: "other loads. Otherwise, the factor for that load"); L1339 `…0.90 of the assigned factor shall be zero.` (누락: "s and that on other gravity loads (e.g., L, Lr, S, Ccr)"); L1387 `effects o the…`, `factor that load`, `wi other`; L1390 `Guidanc`; L1433/L1562 `the load fact is 0.90` (누락 "or on dead load"); L1436 `…loads are taken as Y` (누락 "j."); L1516 `factor for load`, `with th loads`; L1517 `Section 1.2 RG 1.199` (누락 "in") | 62, 64, 66, 68, 72, 74 | landscape 표 note에서 줄 끝 단어(우측 경계 부근)가 잘림. 본문 prose에는 동일 현상 없음(전체 token 대조) | note 블록을 pdfplumber text line으로 재추출하여 교체 | B |
| 4 | T99-1 (source defects) | **H** (RAG 오답 위험) | 7 | L354–355 `- for systems with single supports, and` (α 값 없음); L1454–1457 (6.4-9 FS block); L577 `…are provided in Table 6.4-11 and Table 6.4-12.`; L1330 `Yi (7)`; L1630 `A. 9`; L814 vs L1635 (B.3 명칭); L672/674 `For soft soil and backfill: = […]` | 17, 69, 29, 64, 78, 41 | **원본 PDF 자체의 결함이며 변환 오류가 아님**: (a) ASCE/SEI 4-16 §4.5.1 dynamic amplification factor α 값이 PDF text layer·렌더 모두에 없음(p17, 수식 객체 누락 추정); (b) Table 6.4-9 "Minimum Factors of Safety" 값이 St-헤더보다 한 열 왼쪽에 인쇄됨 (기호열에 1.1, St-1(4) 아래 1.5, St-7 공란) — 문자 그대로 읽으면 St-1 overturning FS = 1.5로 오독됨(SRP 3.8.5 논리상 St-1=1.1, St-2=1.5, St-7 floatation=1.1이 의도로 보임); (c) SR substructure 하중조합을 Table 6.4-11/12로 지칭(표 내용상 6.4-5/6.4-6이 해당); (d) 6.4-6 sheet 2 기호 `Yi (7)` (다른 표는 `Yj`); (e) `A. 9`; (f) B.3 "Loss of One Intermediate Sodium Pump"(본문) vs "…Sodium Loop"(표); (g) mesh size 식 좌변 "L" 없음 | **자동 수정 금지**. 원문 유지 + `<!-- source note: … -->` 형태의 편집 주석만 부가(α 누락, 6.4-9 열 어긋남) | C |
| 5 | T3 | M | 74 (전부) | L61 `- 6.1 Design Requirements for Safety-Related SSCs`; L321 `- 6.4.1.3.1 Seismic Analysis Methods`; L1070 `- 6.4.5.2 ASME B31.1 and B31.3` | 4–51 | 번호 heading이 모두 list item (PDF에서 heading이 본문과 같은 Arial 11 regular라 미검출). `#` heading은 cover 2개, chapter title(`###`, L59), `### References`(L232), 표 caption/sheet 26개뿐 | `^- (6(?:\.\d+)+)\s+(.+)$` → `#`×(depth+1) (6.x=H2 … 6.x.x.x.x=H5); chapter title → H1. TOC(L15–31)는 제거 후 적용 | A |
| 6 | T3 | M/H | 10 glued | L80 `- 6.1.1.2 External Flood The design basis external flood…`; L109 `- 6.1.1.4.1 Missile Selection The design basis missile…`; L557 `- 6.4.2.2.4 Abnormal Loads Abnormal loadings are…`; L711 `- 6.4.2.4.3 Special Construction Techniques No special…`; L415/L517/L574/L603/L627/L1005 (소제목 결합: `…Floor Response Spectra Effects of Parameter Variations…`, `Normal Loads Dead Loads (D)`, `Loading Combinations SR Substructure Loading Combinations`, `…Stability SR Substructure Foundations`, `…Substructures FE Model Geometry`, `Piping Analysis Methods Flexibility`) | 4, 5, 20, 25, 28–31, 37, 47 | heading 뒤에 본문(4) 또는 underlined 소제목(6)이 붙음 | PDF에서 추출한 heading title 목록(§4)으로 정확 분리 | B |
| 7 | T3/T13 | M/H | underlined 소제목 98 (+ run-in 6) | 자기 줄 plain 3 (L360 `SSSI Effects`, L733, L868); list item 7 (L736 `- Level B Service Loadings`, L751 `- Service Level A Conditions`…); numbered heading에 결합 6; 문단 앞 결합 47 (L326 `Dynamic Analysis Methods For the calculation…`); 문단 중간 결합 41, 이 중 **선행 문단 끝에 붙은 것 7**: L368 `…RG 1.92. Supporting Media for SR Substructures`, L374, L475 `…Modal Response Parameters`, L551 `…Tornado - Generated Missiles (Wtm)`, L689 `…Load Input`, L911 `…Basis for Selection of Frequencies`, L1087 `…Section 6.4.1. References` | 16–51 | PDF에서 밑줄(높이≈0.8 pt rect)로 표시된 run-in 아닌 독립 소제목. 선행 문단 끝 결합 7건은 소제목이 **엉뚱한 chunk**에 속하게 됨. 하중 기호 정의(D, L, Lr, S, I, H, R, F', F, To, Ro, Ccr, Eo, W, Ess, Wtw, Wtp, Wtm, SE)가 L517–555의 6개 초장문 행에 뭉쳐 있음 | PDF underline rect(높이<1.5, 단어 bottom 부근) 검출 → 소제목 목록 확정 → H6로 분리. run-in 6건(L112–123)은 `**…**` 강조로만 표시 | B |
| 8 | T3 | M | 30 | L754 `- Service Level A Transient 1 – Cold Shutdown to Hot Standby`; L806; L847; L859; L870 `- Test 1 – Hydrostatic or Pneumatic Test` | 39–43 | design transient 소제목(PDF: 독립 행, 비강조)이 list item. Table 6.4-16 event ID(A.1…Test 6)와 1:1 대응 | `^- (Service Level [A-D] Transient \d+|Test \d) – ` → H6 (상위 "Service Level X Conditions"는 bold 행) | A |
| 9 | T5 | M | 13 문장 분리 + 2 문단 list화 | page break 분리 4: L83→L85 `…flood level described in` ‖ `Table 2.1-1. Additionally…`, L296→L298, L379→L381, L451→L453; 줄바꿈 후 continuation이 list item 9: L216→L218 `Per ASCE 43-19` ‖ `- Section 7.3, elastically…`, L372→L374, L394→L396, L418→L420, L492→L494 `- Section 7.8.3.1.3.`, L632→L634 `- 3) definition…`, L944→L946 `- 10 CFR 50 Appendix S; …`, L946→L949 `- as applicable, where…`, L1028→L1030 `- at a minimum, …`; 문단 전체 list화: L64, L735 | 4–5, 9, 14–15, 18–22, 32, 45–46, 48 | 선행 행이 종결부호 없이 끝나고 다음 행이 `Section \d`, `\d\)`, `10 CFR`, 소문자로 시작 | A 규칙: 선행 행 끝이 `[.:;?!)]`가 아니고 다음이 `- (Section \d|10 CFR|\d\) |[a-z])` 이면 결합. **예외**: L354–355(선행 행이 `:`로 끝나는 진짜 하위 bullet), L595–596(`- f1 =`, `- f2 =` 범례) | A |
| 10 | T5 | M | ≈40 body 문단 병합 (61개 md 행에 PDF block 시작 164개가 행 중간에 존재) | L358 (PDF 문단 3개), L542 (4), L623 (소제목 4 + 문단 5), L674 (소제목 4 + 문단 7, 2,529 chars), L682, L705, L749, L1087 (소제목 3 + 문단 4) | 17–51 | 소제목 결합(#7)과 별개로 일반 문단끼리도 병합됨(블록 간격 >6 pt 기준 검출; 수치는 근사) | 소제목 분리 후, PDF 문단 경계(line gap)로 재분할 또는 `--keep-line-breaks` 재변환 비교 | B |
| 11 | T10 | M/H | 5 수식군 | L581 (IBC-2021 LRFD 조합 7개가 1행: `1.4 (D + F) 1.2 (D + F) + 1.6 (L + H) + 0.5 (Lr or S or R) 1.2 …`); L590 `- F – … H – … L – Live Load`, L593 `Lr – Roof Live Load S – Snow Load R – Rain Load W – Wind Load` (범례 12개가 7행, p29→p30 경계); L648 `t' = 0.707 × t E’ = 1.414 × E G’ = 1.414 × G γ' = 1.414 × γ`; L650/L652 (정의 10개가 2행); L658 `λ V f = ---` + L662 `λ V f` + L664–668 `= The wavelength` 등 (기호와 정의 분리) | 29–30, 32–33 | 수식·범례 줄 구조 소실. L593은 수식 행이 아니라 page break로 끊긴 범례 후반부임(선행 스캔의 "legend glued to formula"는 L581/L590/L593의 조합 문제) | IBC 조합 7행 분리(선두 `1.4 (`/`1.2 (`/`0.9 ` 기준, 결과가 정확히 7개인지 검증), 범례 `\s(?=[A-Z][a-z]?\s–\s)` 분리, t' 식 4행 분리; λ 블록은 `λ = V / f`, `λ = The wavelength`, `V = …`, `f = …`로 수작업 재배치 | A (targeted) / C (λ) |
| 12 | T8 | M | 표 footnote 첨자 10; 지수 1 | L1137–1139 `Ground Motion1 ≥ SSE` ×3; L1594 `Tornado Wind3`, `Protection2` ×2; L1599 `Yes1` ×2; L1600 `FHB2`; L1603 `RAB2`; L112 `less than 1x10-7 per year` | 55, 77, 5 | superscript footnote 표지가 본문에 붙어 가짜 식별자 생성("FHB2", "RAB2", "Yes1"); 1×10⁻⁷의 지수 부호 소실 | `Motion<sup>1</sup>` 등 corpus 공통 규약으로 변환; `1x10<sup>-7</sup>`. 위치는 pdfplumber `words`(size 축소)로 확정 | B (A 가능: 목록 고정) |
| 13 | T8 | L | subscript 소실 ≈150 token | `Lr, Ro, To, Ccr, Eo, Ess, Wtw, Wtp, Wtm, SE, Fa, Pa, Ta, Ra, Yr, Yj, Ym, Di, Wi, Tdesign, Pdesign, f1, f2, Ie, Cd, Vt, Cs, Rp, Fμ, 0.5EIg, Ig` (예 L477 `R/Ie`, L486 `CsW`, L646 `0.5EIg`) | 23–34, 61–80 | 기호가 결합된 형태로 일관 표기되어 식별 가능. 단 L1436 `Y`(Yj 소실)는 #3에 포함 | 선택: `L<sub>r</sub>` 등. 검색 일관성을 위해 plain(`Lr`) 유지 권장 | A |
| 14 | T6 | M | 8 tables / 16 blocks; sheet heading 10; 반복 header 24 lines | L1207/1218, L1350/1374, L1397/1418, L1479/1502, L1525/1548 `### (Sheet n of 2)`; L1259, L1324 (caption 포함 sheet 2) | 56–74 | page-split 표 미병합, sheet 2의 header 2–4행 반복 | caption 복원(#2) 후 sheet 병합, 반복 header 제거 | A |
| 15 | T6 | M | 헤더 결함 16 tables | L1229 `| | |Normal and Severe| …|Extreme and Abnormal|…` (group label이 header); L1187–1189 (6.4-3 2단 header 평탄화: `|Code|Applicability|Safety Classification| |` / `| | |SR|NSRST|`); L1594 `|SSC| | |` (3열 span); L1596–1608 rowspan 미충전 13셀 (건물명 9, "Superstructure" 4) | 58, 61–74, 77 | 하중조합 표는 3단 header(group / load case / equation no.) 구조. group 범위(어느 case가 Extreme and Abnormal인지)가 md에서 소실. Table 6.4-5에 `C-9`와 `C-9(6)` 2개 열이 공존(원본 그대로) | 단일 header로 합성(예: `C-10 [Extreme and Abnormal; ACI 349-13 Eq. 9-6]`) 또는 case ID를 header, equation no.를 첫 데이터 행으로; rowspan fill-down; 열 key 유일성 유지 | B/C |
| 16 | T6 | L | 3 | L1140 `|1 See Section 6.4.1.2.3| |` (표 footnote가 데이터 행); L1129–1139 (5행) `•` 15, `<br>` 42 (그중 `<br><br>` 9, 중첩 bullet `- ` 포함); L1681 `VIBR(2)<br><br>+/- OBE(4) + DISP` | 54–55, 80 | 셀 내부 bullet/개행이 record 추출 방해 | footnote 행 → 표 아래 note; `<br>• ` → `; `; L1681 `<br><br>` → 공백 | A |
| 17 | T2 | M | 44 lines (dot-leader 33), 4,261 chars | L13 `TABLE OF CONTENTS Chapter 6 … . . . 6.1-1`; L34 `LIST OF TABLES Table 6.1-1 …` | 2–3 | 제목이 첫 항목과 결합; page 번호 noise | 삭제(필요 시 table→PSAR page 매핑만 frontmatter로 보존) | A |
| 18 | T1 | L/M | 11 lines, 534 chars | L1, L3, L11 (이미지 3개), L5 `# Kemmerer Power Station Unit 1 PSAR, Chapter 6`, L7 `## US SFR Owner, LLC…`, L9 `SUBJECT TO DOE COOPERATIVE AGREEMENT NO. DE-NE0009054 Copyright © 2025…` | 1 | 장식 이미지(PSAR 7개 chapter 동일 md5)와 cover 문구; H1/H2가 문서 outline을 오염 | 삭제 후 frontmatter로 이관(title, applicant, DOE agreement no., copyright) | A |
| 19 | T4 | M | 4 | L1227 `### Kemmerer Unit 1 PSAR Table 6.4-5 …(Sheet 1 of 2)`; L1257 `### Kemmerer Unit 1 PSAR`; L1290; L1322 | 61–64 | running header가 caption에 혼입 또는 독립 heading | `^### Kemmerer Unit 1 PSAR\s*$` 삭제, caption 앞 접두 제거 | A |
| 20 | T11 | L | 3 hyphen join + 15 glyph | L630 `safetysignificant`; L1165 `ColumbiumVanadium`; L1222 `Light-WaterCooled`; `•` 15 (표 6.4-1A/1B 셀) | 31, 56, 60 | 줄끝 하이픈 결합 소실 | 3건 사전 치환(→ safety-significant, Columbium-Vanadium, Light-Water-Cooled) | A |
| 21 | T5 | L | list 끊김/중첩 소실 | L337–344 (빈 줄로 2개 list로 분할), L560–571, L1033–1049 (`The attachment of:` 하위 항목 L1038–1039 중첩 소실), L354–355 (dash 하위 bullet 중첩 소실); 번호 list가 `- 1.` 형태 27개 (L131…L1694) | 16–17, 28–29, 48–49 | 가독성·list chunk 경계 문제 | 연속 list 병합, 들여쓰기 복원(PDF x0), `- 1.` → `1.` | A/B |
| 22 | T13 | L | underline 104 + change bar ≥27쪽 | 예: L112 `Pressurized systems and components.` (PDF 밑줄); change bar p4–10, 14–15, 22, 24, 28, 30, 35, 37, 39, 46–51, 53–55, 64, 66 | 4–66 | underline은 소제목 표지(#7), change bar는 Rev. 1 변경 표지로 모두 소실 | underline → heading/bold; change bar는 필요 시 `<!-- rev-bar -->` 주석 (선택) | B |
| 23 | T15 | M | 1 | 파일 전체 | – | frontmatter 없음, PSAR page label(6.1-1…6.4-67)·PDF page anchor 없음 → 인용 불가 | frontmatter 추가; `--markdown-page-separator "<!-- page %%page-number%% -->"` 재변환 또는 PSAR page label 삽입 | A (frontmatter) / B (anchors) |
| 24 | T16 | L | 1 | L658 `λ V f = ---`, L662 `λ V f` | 33 | 수식 기호 순서 뒤섞임(국소) — 그 외 reading-order 오류 없음(전체 token 대조) | #11과 함께 수작업 | C |
| 25 | T12 | – | 0 | – | – | `[[`, `$`, `#tag`, `==`, `%%`, 텍스트 내 pipe 모두 0. `[ADAMS Accession No. ML19241A472]`(L235)는 단일 대괄호로 무해. L664–668의 `= …`로 시작하는 행은 setext underline 조건 불충족(무해) | 조치 불필요 (단 superscript 규약으로 `^` 사용 시 Obsidian block-ref 충돌 주의) | – |

## 2. Table verification log

전 28 block을 pdfplumber `extract_tables()` 및 페이지 렌더링과 셀 단위로 대조함(스크립트 `ch6_cmp.py`, `ch6_cmp2.py`). "lost" = PDF에 값이 있으나 md 셀이 빈 경우. 값의 이동·오기는 전 표에서 0건.

| Table ID | md lines | PDF p. | Status (OK / defect IDs) | Notes (lost values, split rows, …) |
|---|---|---|---|---|
| 6.1-1 Design Basis Hazard Levels | L240–252 | 11 | OK | 10×3 일치. 값은 모두 교차참조("See Section 2.1/6.1.1.x") — 수치 없음 |
| 6.4-1A SR SSC Seismic Classification | L1125–1130 | 54 | OK / T6(#16) | 내용 일치. 셀 내 `•`+`<br>` |
| 6.4-1B NSRST SSC Seismic Classifications | L1133–1140 | 55 | 내용 OK / T8(#12), T6(#16) | SCN1 I=1.5, Risk Cat. IV; SCN2 I=1.25, Risk Cat. III; SCN3 I=1.0 — 일치. `Motion1`×3 (superscript 1), footnote가 표 행(L1140), `<br><br>` 중첩 bullet |
| 6.4-2 s1 Design Codes and Standards | L1143–1168 | 56 | T14(#2), T6(#14), T11 | 24행 일치. **caption·"(Sheet 1 of 2)" 모두 없음**. `ColumbiumVanadium` |
| 6.4-2 s2 | L1171–1182 | 57 | T14(#2), T6(#14) | 10행 일치. caption 없음, header 반복 |
| 6.4-3 Applicability of Primary Design Codes | L1185–1204 | 58 | OK / T6(#15) | X 표시 30개 모두 일치. 2단 header 평탄화(L1187–1189) |
| 6.4-4 s1 Applicability of RGs | L1207–1215 | 59 | T14(#2), T6(#14) | 5행 일치. caption 대신 `### (Sheet 1 of 2)` |
| 6.4-4 s2 | L1218–1224 | 60 | T14(#2), T6(#14), T11 | 3행 일치. `Light-WaterCooled` |
| **6.4-5 s1** Concrete SR Substructures | L1227–1254 | 61 | **T6(#1) H**, T4, T6(#15) | 소실 53: header C-9(6),C-10,C-11,C-12,C-13,C-16,C-17; Dead 1.0×7; Live 1.0(16)×7; Soil 1.0×7; Thermal 1.0×5; Crane 1.0×3 (C-9(6),C-10,C-16); SE 1.0 (C-9(6)); Ess 1.0 (C-10, C-17); Wtw 1.0 (C-12); Wtp 1.0/0.5/0.5 (C-11–13); Wtm 1.0 (C-12); Fa, Pa 1.4(4)/1.0, Ta, Ra (C-16, C-17); Yr 1.0 (C-17). Hydrostatic·Pipe Reactions 행은 온전 |
| **6.4-5 s2** | L1257–1266 | 62 | **T6(#1) H**, T4 | 소실 9: header 7 + Yj 1.0, Ym 1.0 (C-17) |
| 6.4-5 notes (1)–(17) | L1269–1287 | 62 | T14(#3) | note (3) 8단어 누락 |
| **6.4-6 s1** Structural Steel SR Substructures | L1290–1319 | 63 | **T6(#1) H**, T4 | 소실 81: header S-14…S-25 (10) + NB2-5…NB2-9 (10); Dead ×10; Live ×10; Lr 0.2 (S-14); R 0.2 (S-16); Soil ×8; Thermal ×7; SE 1.0 (S-17(6)); Ess 1.0 (S-18), 0.7 (S-24, S-25); Eo 1.6 ×3 (S-14–16); Wtw/Wtp/Wtm (S-19, S-20); Fa, Pa 1.4(11)/1.0/1.0, Ta, Ra (S-23–25); Yr (S-25) |
| **6.4-6 s2** | L1322–1331 | 64 | **T6(#1) H**, T4, T99 | 소실 22: header 20 + Yi 1.0, Ym 1.0 (S-25). 기호 `Yi (7)`은 원본 표기 |
| 6.4-6 notes (1)–(12) | L1334–1347 | 64 | T14(#3) | note (4) 약 10 token 누락 |
| **6.4-7 s1** Extraordinary Events, NSRST Substructure, Concrete | L1350–1371 | 65 | **T14(#2) caption 없음**, **T6(#1)** | 소실 17: Dead, Live 1.0(10), Hydrostatic (C-16, C-17); Crane (C-16); Ess (C-17); Fa, Pa 1.4(4)/1.0, Ta, Ra (C-16, C-17); Yr (C-17) |
| **6.4-7 s2** | L1374–1380 | 66 | T14(#2), T6(#1) | 소실 2: Yj, Ym 1.0 (C-17) |
| 6.4-7 notes (1)–(10) | L1383–1394 | 66 | T14(#3) | note (3) 3곳, note (6) `Guidanc` |
| **6.4-8 s1** Extraordinary Events, NSRST Substructure, Steel | L1397–1415 | 67 | **T14(#2)**, **T6(#1)** | 소실 12: header S-24(8), S-25; Dead, Hydrostatic, Fa, Pa (S-24, S-25) 1.0; Ess 0.7 ×2. (Equation 행 NB2-9는 보존) |
| **6.4-8 s2** | L1418–1426 | 68 | T14(#2), T6(#1) | 소실 4: header 2 + Yr, Yj 1.0 (S-25). "Accident Thermal" 행 기호 없음은 원본 그대로 |
| 6.4-8 notes (1)–(9) | L1429–1439 | 68 | T14(#3) | note (3) `fact`, note (6) `Y` |
| 6.4-9 SR Structural Stability | L1442–1457 | 69 | md=PDF / **T99-1(#4)** | 값 일치. 단 원본의 "Minimum Factors of Safety" 블록이 한 열 왼쪽으로 어긋나 인쇄됨 → md도 동일하게 오독 유발 (편집 주석 권장, 자동 이동 금지) |
| 6.4-10 Concrete Material Properties | L1469–1476 | 70 | OK | E 580,392/820,670 ksf; G 247,968/350,626 ksf; ν 0.17; density 0.150/0.212 kcf 일치. 첫 header 셀 공란은 원본 |
| **6.4-11 s1** Extraordinary Events, NSRST Superstructure, Concrete | L1479–1499 | 71 | **T14(#2)**, **T6(#1)** | 소실 15: Dead, Live 1.0(9), Soil (C-16, C-17); Ess (C-17); Fa, Pa 1.4(4)/1.0, Ta, Ra (C-16, C-17) |
| **6.4-11 s2** | L1502–1509 | 72 | T14(#2), T6(#1) | 소실 3: Yr, Yj, Ym 1.0 (C-17) |
| 6.4-11 notes (1)–(9) | L1512–1522 | 72 | T14(#3) | note (3) 2곳, note (4) "in" |
| **6.4-12 s1** Extraordinary Events, NSRST Superstructure, Steel | L1525–1545 | 73 | **T14(#2)**, **T6(#1)** | 소실 20: header S-24(8), S-25, NB2-9×2; Dead, Live 0.8, Hydrostatic, Ess 0.7, Fa, Pa, Ta, Ra (S-24, S-25). pdfplumber는 선두 빈 열 포함(9열) |
| **6.4-12 s2** | L1548–1555 | 74 | T14(#2), T6(#1) | 소실 7: header 4 + Yr, Yj, Ym 1.0 (S-25) |
| 6.4-12 notes (1)–(9) | L1558–1568 | 74 | T14(#3) | note (3) `fact`. `DC/COL ISG-007`는 원본 표기 |
| 6.4-13 Design Basis Tornado Parameters | L1571–1580 | 75 | OK | 160 mph, 32 mph, 128 mph, 150 ft, 0.6 psi, 0.2 psi/s 일치 |
| 6.4-14 Tornado Missile Spectrum | L1583–1589 | 76 | OK | 287 lb/79/53; 2,595 lb/79/53; 0.147 lb/20/14 일치 |
| 6.4-15 Tornado/Winter Precipitation Applicability | L1592–1608 | 77 | 값 OK / T6(#15), T8(#12) | 13행×4값 일치. rowspan 미충전 13셀, `SSC| | |`, `Wind3`·`Protection2`·`Yes1`·`FHB2`·`RAB2` |
| 6.4-16 Summary of Design Transients | L1618–1651 | 78 | OK | 30행 일치. `A. 9`(원본) |
| 6.4-17 Applicable Loads, ASME Class A/B | L1654–1671 | 79 | OK / T8 | 14행 일치. `Tdesign`, `Pdesign` subscript |
| 6.4-18 Load Combinations & Service Stress Limits | L1674–1686 | 80 | OK / T6(#16) | 9행 일치. L1681 `<br><br>`; notes 1–4 일치 |

집계: 28 block 중 값 손실 12 block(6 tables), caption 손실 11 block(6 tables), 내용 완전 16 block. 하중조합 표 전체 load factor 522개 중 179개(34.3 %) 손실 — 표별 6.4-5 48/125, 6.4-6 63/193, 6.4-7 19/52, 6.4-8 12/48, 6.4-11 18/52, 6.4-12 19/52.

## 3. Figure inventory

| Figure ID | md lines | raster/vector | image file | debris lines to delete | Notes |
|---|---|---|---|---|---|
| (cover) Natrium logo | L1 | raster | imageFile1.png (182,866 B, md5 6ed7…) | L1 | 장식; PSAR 7개 chapter 동일 |
| (cover) plant rendering | L3 | raster | imageFile2.png (2,236,298 B, md5 8b32…) | L3 | 장식; 동일 |
| (cover) TerraPower logo | L11 | raster | imageFile3.png (26,035 B, md5 b56e…) | L11 | 장식; 동일 |
| — | — | — | — | — | 본문 figure 0개, vector debris 0. λ = V/f(p33)는 font 문자 수식(#11) |

## 4. Heading outline check

**요약**: PDF 기준 의도 outline = chapter title 1 + 번호 heading 74 (H2 4, H3 8, H4 28, H5 34) + underlined 소제목 98 (H6) + transient 소제목 30 (H6) + References 2 (§6.1, §6.4).

| 결함 유형 | 개수 | 비고 |
|---|---|---|
| 번호 heading이 list item | 74 / 74 | 정상 `#` heading 0 |
| 번호 heading + 본문 결합 | 4 | L80 (6.1.1.2), L109 (6.1.1.4.1), L557 (6.4.2.2.4), L711 (6.4.2.4.3) |
| 번호 heading + 소제목 결합 | 6 | L415 (6.4.1.3.5 + "Effects of Parameter Variations on Floor Responses"), L517 (6.4.2.2.1 + "Dead Loads (D)"), L574 (6.4.2.2.5 + "SR Substructure Loading Combinations"), L603 (6.4.2.2.6 + "SR Substructure Foundations"), L627 (6.4.2.3.2 + "FE Model Geometry"), L1005 (6.4.4.3 + "Flexibility") |
| underlined 소제목: 자기 줄 plain / list item | 3 / 7 | L360, L733, L868 / L736, L740, L744, L751, L803, L844, L856 |
| underlined 소제목: 문단 앞 결합 | 47 | 예 L326, L335, L347, L383, L401, L435, L524, L532, L608, L632, L646, L654, L676, L749, L915, L917, L1028, L1056, L1077 |
| underlined 소제목: 문단 중간 결합 | 41 | 이 중 선행 문단 끝 결합 7: L368, L374, L475, L551, L689, L911, L1087 |
| transient 소제목 list item | 30 | L754–L891 |
| References heading 누락 | 1 | §6.4 References가 L1087 끝에 결합 (§6.1은 L232 `### References` 정상) |
| 잘못된 level | 3 | L5 `#`/L7 `##` (cover 문구), L59 `###` Chapter title (→ H1) |
| 비-heading의 heading 승격 | 12 | `### Kemmerer Unit 1 PSAR` 2 (L1257, L1322), `### (Sheet n of 2)` 10 |

**번호 heading 전체 목록 (md line : 번호 → 의도 level)**: L61:6.1→##; L67:6.1.1→###; L76:6.1.1.1→####; L80:6.1.1.2→####(glued); L87:6.1.1.3→####; L106:6.1.1.4→####; L109:6.1.1.4.1→#####(glued); L126:6.1.1.4.2→#####; L136:6.1.1.5→####; L172:6.1.1.6→####; L176:6.1.1.7→####; L181:6.1.1.8→####; L186:6.1.2→###; L190:6.1.3→###; L200:6.1.3.1→####; L227:6.1.3.2→####; L255:6.2→##; L268:6.3→##; L277:6.4→##; L280:6.4.1→###; L287:6.4.1.1→####; L302:6.4.1.2→####; L305:6.4.1.2.1→#####; L309:6.4.1.2.2→#####; L313:6.4.1.2.3→#####; L318:6.4.1.3→####; L321:6.4.1.3.1→#####; L385:6.4.1.3.2→#####; L407:6.4.1.3.3→#####; L411:6.4.1.3.4→#####; L415:6.4.1.3.5→#####(glued); L437:6.4.1.3.6→#####; L443:6.4.1.3.7→#####; L448:6.4.1.4→####; L455:6.4.1.5→####; L457:6.4.1.5.1→#####; L461:6.4.1.5.2→#####; L468:6.4.1.6→####; L497:6.4.2→###; L504:6.4.2.1→####; L512:6.4.2.2→####; L517:6.4.2.2.1→#####(glued); L544:6.4.2.2.2→#####; L549:6.4.2.2.3→#####; L557:6.4.2.2.4→#####(glued); L574:6.4.2.2.5→#####(glued); L603:6.4.2.2.6→#####(glued); L615:6.4.2.3→####; L618:6.4.2.3.1→#####; L627:6.4.2.3.2→#####(glued); L678:6.4.2.3.3→#####; L684:6.4.2.3.4→#####; L697:6.4.2.4→####; L700:6.4.2.4.1→#####; L707:6.4.2.4.2→#####; L711:6.4.2.4.3→#####(glued); L714:6.4.3→###; L721:6.4.3.1→####; L726:6.4.3.1.1→#####; L896:6.4.3.1.2→#####; L906:6.4.3.2→####; L926:6.4.3.3→####; L931:6.4.3.3.1→#####; L958:6.4.3.3.2→#####; L963:6.4.4→###; L966:6.4.4.1→####; L973:6.4.4.2→####; L975:6.4.4.2.1→#####; L994:6.4.4.2.2→#####; L998:6.4.4.2.3→#####; L1005:6.4.4.3→####(glued); L1010:6.4.5→###; L1017:6.4.5.1→####; L1070:6.4.5.2→####.

(TOC L15–31의 12개 `- 6.x` 항목은 heading 변환 대상에서 제외해야 함 — 선행 스캔의 "86 list items" = 본문 74 + TOC 12.)

## 5. File-specific observations and recommendations for the cleanup script

**권장 처리 순서**
1. frontmatter 삽입: `doc: Kemmerer Unit 1 PSAR, Chapter 6`, `title: Safety-Significant SSC Criteria and Capabilities`, `revision: Revision 1`, `applicant: US SFR Owner, LLC (TerraPower)`, `doe_agreement: DE-NE0009054`, `copyright: 2025 TerraPower, LLC`, `source_pdf`, `pdf_pages: 80`, `psar_pages: 6.1-1–6.4-67`, `tables: [6.1-1, 6.4-1A … 6.4-18]`.
2. L1–11(cover), L13–56(TOC/LOT) 삭제.
3. **표 재구성 (최우선, class B)**: Table 6.4-5/6/7/8/11/12의 12 sheet를 pdfplumber 결과로 교체 → 기호열 subscript 재결합 → 6.4-12 선두 빈 열 제거 → sheet 병합 → caption 복원(6.4-2, 6.4-4, 6.4-7, 6.4-8, 6.4-11, 6.4-12) → header 3단(group/case/equation) 합성 → 반복 header 삭제 → note 블록을 PDF text로 교체(#3) 및 표 바로 뒤에 caption ID와 함께 배치. 교체 후 셀 수 검증: load factor 비공란 522개, 표별 125/193/52/48/52/52.
4. running header 제거(`### Kemmerer Unit 1 PSAR`, caption 접두).
5. heading: TOC 제거 후 `^- (6(?:\.\d+)+)\s+` → level=depth+1; glued 10건은 PDF title 목록으로 분리; underlined 소제목 98건을 PDF underline 검출로 H6 분리(선행 문단 끝 결합 7건 우선); transient 30건 H6; §6.4 "References" heading 복원; chapter title H1.
6. 문단 복구: #9 규칙(예외 L354–355, L595–596 반드시 적용), page-break 분리 4건 결합, 이후 PDF 문단 경계로 병합 문단 분할(#10).
7. 수식·범례: IBC 조합 7행, 범례 12항목, t' 식 4행, 정의 10항목 분리; λ 블록 수작업.
8. 첨자: `1x10-7` → 지수 표기, 표 footnote 첨자 10건 규약화; 하이픈 결합 3건; `<br>`/`•` 정리.

**자동 수정 금지 (원본 결함 보존, 주석만)**
- L354–355 α 값 부재(원본 PDF에 없음) — 값을 추정·삽입하지 말 것.
- Table 6.4-9 "Minimum Factors of Safety" 열 어긋남 — 값 이동 금지, 편집 주석으로 경고.
- L577 "Table 6.4-11 and Table 6.4-12"(SR substructure) 교차참조, `Yi (7)`, `A. 9`, `DC/COL ISG-007`, `Tornado - Generated`(공백 포함 하이픈), `GT STRUDLVersion 40`, `10 CFR Appendix S`, `ACI349-13`/`AISC348-14`(원본 공백 없음), mesh 식 좌변 "L" 부재, B.3 명칭 불일치 — 모두 원문 그대로.

**Pitfalls**
- 소문자 list item 결합 규칙은 `- f1 = `, `- f2 = `(L595–596)와 `:` 뒤 하위 bullet(L354–355)을 반드시 제외.
- Table 6.4-5는 `C-9`(Normal)와 `C-9(6)`(Extreme) 두 열이 공존 → 열 key에 `(6)` 유지.
- 6.4-7 vs 6.4-11, 6.4-8 vs 6.4-12는 구조가 거의 동일하므로 caption 복원 전 병합·귀속 금지(페이지 번호로만 판별: 65–66, 71–72, 67–68, 73–74).
- note 재추출 시 subscript(`Lr`, `Ccr`, `Yj`)가 pdfplumber에서 분리되어 나오므로(`L r`, `C cr`, `Y. j`) 결합 규칙 필요.
- superscript를 `^`로 표기하면 Obsidian block reference와 충돌 가능 → `<sup>` 사용 권장.
- underline 검출: underline은 높이≈0.8 pt의 filled rect이며 rect top이 단어 bottom보다 약 1.5 pt 위에 있음(단순 "단어 아래" 조건으로는 미검출). 페이지 header rule(top≈282 pt)과 표 테두리(p11 등)는 제외.

**Retrieval용 식별자 (frontmatter/tag 후보)**
- Seismic/safety class: SCS1, SCS2, SCN1, SCN2, SCN3; SR, NSRST, NST; ASCE 43-19 Limit State B (LS-B).
- 구조물·계통: RXB, FHB, NCB, RAB, NI, EI; IAC, RAC, PSP, ISP, NSS, ESS, PHT, IHT, RES.
- Load 기호: D, L, Lr, S, R, F, H, Ro, To, Ccr, W, SE, Eo, Ess, Wtw, Wtp, Wtm, Fa, Pa, Ta, Ra, Yr, Yj, Ym, Di, Wi, F'. Load case: C-1…C-17, S-1…S-25, St-1…St-7. Equation: ACI 349-13 Eq. 9-1…9-9, AISC N690-18 NB2-1…NB2-9, IBC-2021 §1605.1.
- Design transients: A.1–A.11, B.1–B.9, C.1–C.2, D.1–D.2, Test 1–6 (본문 "Service Level X Transient n"과 alias 연결).
- 핵심 수치(검색 빈도 높음, md prose에서 온전함 확인): OBE = 1/3 SSE; basic wind 110 mph (RC III, NCB)/115 mph (RC IV); tornado 160 mph, 0.6 psi, 0.2 psi/s (RG 1.76 Region III); ground snow 35 psf; extreme winter precipitation 75 psf; groundwater 15 ft below grade; f'c 5,000 psi; missile probability screening 1×10⁻⁷/yr; NSRST stability FS 1.50/1.10/1.10.
- 참고: §6.1.2 SRDC는 Tables 5.2-1–5.2-3(ch5)을 참조할 뿐 ch6에 criterion record가 없음; §6.1.3 interaction criteria 1–3(L195–197)은 온전.

**검증 산출물 (scratchpad)**: `ch6_pages.txt`(PDF page text), `ch6_cmp.py`/`ch6_cmp_out.txt`(표 셀 대조), `ch6_cmp2.py`(6.4-12 offset 대조), `ch6_notes.py`(note 대조), `ch6_head.py`(heading), `ch6_ul.py`(underline 소제목), `ch6_splits.py`, `ch6_paras.py`, `ch6_fulldiff.py`(본문 전체 token 대조).
