# Review ch11: TP_Natrium_PSAR2025_ch11_Conduct of Operations.md (md lines 1–1615, PDF pages 1–77)

## 0. 개요

| 항목 | 값 |
|---|---|
| md | 1,615 lines (newline 1,614), 151,942 chars (152,316 bytes); 최장 행 L1599 = 2,889 chars |
| PDF | 77 pages. p1 cover, p2–3 TOC, p4 LoT, p5 LoF, p6–77 본문. p17–18 은 `/Rotate 90` landscape(1224×792 pt), p60 만 612×792 pt, 나머지 792×1224 pt(cropbox 90,216–702,1008) |
| md↔PDF 대응 | p1→L1–11; p2–5→L13–82; p6–14→L84–316 (11.1); p15–18→L319–435 (Fig. 11.1-1…-4); p19–45→L437–1209 (11.2); p46–50→L1212–1262 (Table 11.2-1/-2); p51–59→L1265–1456 (11.3); p60–64→L1459 (11.4, withheld); p65–66→L1461–1509 (11.5); p67–74→L1512–1578 (Table 11.5-1/-2); p75–77→L1581–1612 (11.6) |
| Sections | 번호 heading 127개 (11.x: 6, 최대 깊이 5단 예: 11.1.4.1.1) + chapter title 1 + 번호 없는 소제목 8 (`Design Changes` bold 1, 밑줄 7) + `References` 5 |
| Tables | 논리 table 4개 (11.2-1; 11.2-2 = 4 sheets; 11.5-1 = 7 sheets; 11.5-2) → md table block 13개, `<br>` 117 |
| Figures | 4개 (11.1-1 vector + 빈 raster 9; 11.1-2 raster imageFile13; 11.1-3, 11.1-4 vector, landscape page) |
| Images | 13 refs, 전부 alt text 없음. imageFile1–3 cover logo, 4–12 단색 사각형, 13 Fig. 11.1-2 |
| 본문 누락 검사 | md 본문(L84–) 21,693 tokens vs PDF 본문(p6–77, header/footer 제외) 21,906 tokens, difflib ratio 0.974. 비일치 구간은 모두 figure page(p15/17/18), table page(p46–50, p67–74), withheld 반복(p61–64)에 국한됨 → 본문 문단 누락 0 |
| Noise 추정 (순수 삭제 대상) | cover 447 chars/6 lines + TOC·LoT·LoF 4,490/43 + 빈 image ref 678/9 + 반복 table header 708/18 + `##### .` 7/1 ≈ **6,330 chars (4.2 %), 77 non-blank lines**. 이 외 재구성 대상(삭제 금지): org-chart label 45 lines/1,029 chars, Table 11.5-1 row 5.0 파편 12 rows/693 chars |

핵심 결론: 본문 텍스트는 거의 verbatim 이지만 (1) 번호 heading 127개 중 Markdown heading 은 0개(11.4 만 `####`+glue), (2) Table 11.5-1 row 5.0 이 단어 중간에서 3열로 분해되고 문자 중복 발생, (3) Table 11.2-2·11.5-1 caption 11개 전부 누락, (4) landscape page(p17–18) 우측 org-chart label 4개가 소실, (5) glued heading/문단 병합으로 11.3 서두·11.6.2 소절 내용이 잘못된 section 에 귀속된다.

## 1. Findings

| # | T-ID | Sev | Count | md lines (examples) | PDF p. | Evidence / description | Proposed fix | Fix class |
|---|---|---|---|---|---|---|---|---|
| 1 | T6 | H | 1 row → 12 md rows; 14 단어 분절, 3 문자 중복 | L1553–1564 | p73 | Table 11.5-1 Sheet 7 row 5.0 의 spanning cell 이 header column 경계에서 절단: `\|5.0\|Administrative Con\|trols are the provisions relating to organiza\|tion and management,\|`, `\| \|• delineation of res\|sponsibility\| \|` (→ "ressponsibility"), `• description of org\|ganization` (→ "orgganization"), `setpoint control program\|m consistent with` (→ "programm"). pdfplumber 는 p73 cell 을 정상 추출(1 cell). TS Administrative Controls 목록이 검색 불가/오염 | L1553–1564 를 pdfplumber p73 cell 로 1행 재구성: `\|5.0\|Administrative Controls are the provisions … OL stage.<br><br>Probable administrative controls include:<br><br>• delineation of responsibility<br>• …<br>• reporting requirements, to include a COLR\| \| \|` (row 4.0 과 동일 형식) | B |
| 2 | T6 / T14 | H | 2 tables, sheet caption 11개 (4+7) 누락 | L1231, L1241, L1249, L1260 (11.2-2); L1512, L1521, L1527, L1532, L1538, L1545, L1551 (11.5-1) | p47–50, p67–73 | PDF caption `Table 11.2-2 Development of HFE Review Guidance for Advanced Reactors (Sheet n of 4)` 및 `Table 11.5-1 Proposed Variables and Conditions for Technical Specifications (Sheet n of 7)` 가 md 에 전혀 없음(full diff 에서 이 caption token 만 누락). 결과: Table 11.2-2 가 `### Table 11.2-1 …`(L1212) 바로 아래에 이어져 11.2-1 의 행으로 오귀속; Table 11.5-1 은 11.5 References/“Mode-4” 문단 뒤에 caption 없이 위치 → 본문 L1466 “provided in Table 11.5-1” 의 대상이 검색 불가 | LoT(L68–72)에서 caption 을 취해 첫 sheet 앞에 삽입; sheet 병합(11.2-2: 4 blocks, 11.5-1: 7 blocks), 반복 header 9쌍(708 chars) 삭제 | A |
| 3 | T3 | H | 번호 heading glued 8 (list+body 4, plain+body 2, 본문 중간 1, `####`+withheld 1) | L287, L534, L1135, L1371; L1265, L1366; L1447; L1459 | p13, 22, 43, 55, 51, 55, 58, 60 | `- 11.1.5.1 Qualification of Nuclear Personnel Qualifications of managers, supervisors…` (L287); `11.3 Emergency Preparedness This section provides a description of the preliminary plans…` (L1265, 1,684 chars; plain paragraph → chunker 가 11.3 서두를 11.2 에 귀속); `…further discussed in Section 1.1.4.3. 11.3.10 Performance Monitoring A performance monitoring program will be developed…` (L1447, 1,004 chars, 앞·뒤 모두 glue); `#### 11.4 Aircraft Impact Assessment [[ This information is withheld … ]]SRI` (L1459) | §4 whitelist 의 정확한 title 로 분리 → heading 행 + 본문 문단. heuristic(대문자 단어 경계)로 분리 금지(예: L287 title 뒤 “Qualifications…”) | A (whitelist 필요) |
| 4 | T3 / T5 | H | 번호 없는 소제목 glued 7 + `References` glued 2 | L943 끝 `Objectives and Scope`, L948 앞 `Methodology`; L1597 `Geography and Demography`, L1599 `Nearby Industrial, Transportation, and Military Facilities` / `Meteorology and Meteorological Dispersion` / `Hydrology`, L1609 `Geology, Seismology, and Geotechnical`; L1502 `…support testing. References`, L1609 `…security operations. References` | p36–37, 75–77, 66, 77 | PDF 에서 밑줄 소제목(underline stroke 확인 7건)·`References`. L1599(2,889 chars) = 소제목 3개 + PDF 문단 6개 병합 → “Hydrology”·“Meteorology” 내용이 “Nearby Industrial…” 소절에 귀속. L943 은 11.2.3 본문 문단(+잘못된 `- `) 끝에 다음 소제목이 붙음 | 소제목을 H4(11.2.3 하위: Objectives and Scope, Methodology; 11.6.2 하위 5개)로 분리; L1599 는 PDF p76 문단 경계 6곳에서 분할; `References` 를 H3 로 분리 | A (문자열 고정) + B (L1599 문단 경계) |
| 5 | T3 | M | 번호 heading 127 중 list item 115, plain 4, 정상 heading 0 | L86 `- 11.1 Organization`, L105, L227 `- 11.1.4.1.1 Director of Operations- USO`, L1305 `11.3.2 Physical Site Characteristics`, L1390, L1488 `11.5.2.2 Mode-2: Low Power Operation`, L1500 `11.5.2.4 Mode-4: Refuel` | 전 범위 | TOC 32 항목도 list item(TOC 삭제 대상). 구조 기반 chunking 불가 | 번호 depth → level (11.x=H2, 11.x.y=H3, …, 5단=H5), chapter title H1 | A |
| 6 | T3 | M | 비-heading 승격 9 / level 오류 2 | L13 `### Chapter 11 Conduct of Operations . . . . 11.1-1`, L66 `### LIST OF TABLES`, L76 `### LIST OF FIGURES`; caption `###` L349, L353, L391, L1212, L1567; L1519 `##### .`; L84 `### Chapter 11 …`(→H1); L677 `### Design Changes`(→H5, 11.2.1.9 하위, PDF bold) | p2–5, 16–18, 46, 74, 67, 6, 28 | TOC 행이 H3 로 승격되어 chapter title 과 중복 | TOC 계열 삭제; caption 은 heading 이 아닌 caption 행(코퍼스 통일 규칙)으로; `##### .` 삭제 | A |
| 7 | T5 | M | page-break 문단 분할 9 | L125/127, L295/297, L457/459, L783/785, L817/819, L1029/1031, L1117/1119, L1325/1327, L1490/1495 | p7→8, 13→14, 19→20, 31→32, 32→33, 39→40, 42→43, 53→54, 65→66 | `…The executive responsible for` ∥ `regulatory affairs is assisted…`; L1490→L1495 사이 blank 4행 + 소문자 list item `- downpower when reactor power is lowered to within the capability of the IAC…` (Mode-2 정의가 2 chunk 로 분리) | 앞 행이 종결부호 없이 끝나고 다음 비공백 행이 소문자(또는 `- ` + 소문자)면 공백 1개로 결합 | A |
| 8 | T5 | M | 문단 중간 행이 list item 화 6 | L177 `- Section 11.1.3.1 through Section 11.1.3.3.`, L219, L480 `- Section 5.4 of the HFEPP. The staff members…`, L553, L604 `- Section 11.2.6.4) and HFEPP (Section 5.11).`, L608 `- Section 11.2.7).` | p10, 11, 20, 23, 25 | PDF 에서 줄머리가 `Section N.N…` 인 continuation 행이 list 로 오인됨 | 직전 비공백 행이 종결부호 없이 끝나면 `- ` 제거 후 결합 | A |
| 9 | T5 | M | 문단 전체가 잘못된 list item 10 | L448, L943, L1107, L1272, L1486, L1490, L1498, L1502, L1601, L1604 | p19, 36, 42, 51, 65–66, 76–77 | PDF x0=162 pt(본문 들여쓰기, bullet 없음). 운전 모드 정의 4문단 `- Mode-1 is entered from Mode-2 during startup…`, `- The purpose of Mode-3 …`, `- The purpose of Mode-4 …` 전부 list 화. L1272 는 PDF 문단 2개(`…scalable PEP EPZ size.` / `The key elements of the emergency preparedness plan…`)가 병합된 상태 | `- ` 제거(10행 명시 목록 또는 PDF x0 대조); L1272 는 “size. The key elements” 에서 분할 | A (목록) / B (x0 대조) |
| 10 | T5 | L | list nesting 소실 2곳 + 번호 누락 1 | L565–567, L575–600 (11.2.1.4 item 7·10 하위), L1280–1286 (11.3.1 dash 하위 7항목), L606 | p23–25, 52 | PDF 에서 item 7 하위 bullet·item 10 하위 문단/bullet 은 x0=275/325 px 들여쓰기; 11.3.1 의 `- Emergency Response Performance …` 등 7항목은 x0=198 pt 로 `● Performance Objectives` 하위. md 는 모두 top level. L606 `12. Human Performance Monitoring – …`(PDF “12.Human”) 은 `- ` 없음 | 선택: 하위 항목 4 space 들여쓰기; `- N. ` → `N. ` 통일 | B / C |
| 11 | T14 / T7 | M (코퍼스 차원 H) | org-chart label 4개 소실 | Fig. 11.1-3 L353–389, Fig. 11.1-4 L391–435 | p17, p18 | PDF text layer 에 존재하나 md 에 없음: `Quality Control Manager`, `QC Personnel` (p17 x0≈851–884 pt), `Director of NOS`, `Quality Assurance Manager` (p18 x0≈858–895 pt). 같은 page 의 x0≤816 pt label 은 추출됨 → rotated page 우측 영역 텍스트 소실(opendataloader 좌표 처리 결함 추정). QC Manager/QC Personnel 은 본문에 없는 정보 | figure transcription(§3)에 포함; 다른 chapter 의 `/Rotate 90` page 도 동일 결함 점검 | B / C |
| 12 | T7 / T14 | M | 1 figure, box 22개 | L349–351 | p16 | Fig. 11.1-2 는 raster(imageFile13, 3920×2565 px) 뿐이며 text layer 없음 → Natrium Project Organization 의 22개 직위(예: `Sr Manager, Core Design and Methods`, `Manager, Digital Engineering`)가 RAG 에 부재. alt text 없음 | alt text + 중첩 list transcription(§3) 추가 | C |
| 13 | T7 / T16 | M | vector label 45행(3 figure), 빈 image 9 | L319–347, L353–389, L391–435; blank images L321, 323, 327, 333, 335, 339, 341, 345, 347 | p15, 17, 18 | 계층 정보 소실·순서 뒤섞임; `Security Manager Station Sciences Manager`(L403, 2 box 병합), `Commissioning`/`Manager`(L411/413, 1 box 분할), `ChiefNuclear Officer`(L329; text layer 원문, 렌더링은 “Chief Nuclear”). imageFile4–12 = 단색(white 5, black 4) 404×201–277 px 사각형(box fill/mask), 정보 0. Fig. 11.1-1 caption 은 plain(L319) | 빈 image ref 9행 삭제; label 파편을 §3 의 계층 list 로 교체 | A (삭제) + C (transcription) |
| 14 | T2 | M | dot-leader 41행; TOC·LoT·LoF 43 non-blank lines, 4,490 chars | L13–82 | p2–5 | `- 11.1.1 Executive Management Organization- TerraPower/USO. . . . . 11.1-2`; L44 는 2행 entry 병합; L73 `11.5-10P` 는 PDF 원문 오기 | outline/caption whitelist 로 수확 후 삭제 | A |
| 15 | T1 | L | 6 non-blank lines, 447 chars | L1–11 | p1 | imageFile1–3(전 PSAR chapter 공통 logo), `# Kemmerer Power Station Unit 1 PSAR, Chapter 11`, `## US SFR Owner, LLC, a wholly owned subsidiary of TerraPower, LLC`, `SUBJECT TO DOE COOPERATIVE AGREEMENT NO. DE-NE0009054 Copyright © 2025 TerraPower, LLC. All rights reserved.` | YAML frontmatter 로 이전 후 삭제 | A |
| 16 | T6 | M | cell 내부 구조 결함 9 | L1514, L1524, L1540, L1541, L1244, L1245, L1246, L1252, L1226 | p67–68, 71, 48–49, 46 | spanning cell 에서 title 과 설명 결합: `Use and Application The Use and Application section…`, `Limiting Conditions for Operation and Surveillance Requirements LCOs are…`; bullet 과 다음 문장 결합: `• PSP leakage The PHT is described in Section 7.1.3.<br>`, `• intake/exhaust flow rates The RAC is described in Section 7.2.1.<br>`; Table 11.2-2 2개 sub-row 병합 `11.2.5<br><br>11.2.1.10\|Design of the Human-system Interface Design Goals and Design Bases` (허구의 title 생성); italic stage 문단 구분 소실 `…identification of scenarios for analysis HF in Preliminary Design: participation…`; Table 11.2-1 row 11 의 Procedures/Training/V&V ↔ 11.2.6.1/.2/.3 행 대응 소실 | 해당 위치에 `<br><br>` 삽입(PDF 행 구조 기준) | B |
| 17 | T6 | L | `<br>` 117, trailing `<br>` 다수, 빈 header cell 1 | L1226 `11.2.6.1<br>11.2.6.2<br>11.2.6.3<br>`, L1529 `<br><br><br>` | p46–74 | 빈 header cell(Table 11.2-1 첫 열)은 원문과 동일; `(postconstruction)`(L1257) ↔ PDF `(post-`/`construction)` | trailing `<br>` 제거, 연속 `<br>` ≤2 로 정규화; `postconstruction` 은 판단 필요 | A / C |
| 18 | T11 | M | `&amp;` 23 (18 lines), `&gt;` 1, `●` 1 | L502 `(I&amp;C)`, L572 `(V&amp;V)`, L387 `ES&amp;H Manager`, L1243 `Staffing &amp; Minimum Shift Complement`, L1573 `\|&gt; 400 °F (204°C)\|`, L1364 `● Federal resources are available…` | p21, 23, 17, 48, 74, 55 | Table 11.5-2 Mode-3 온도 조건 `> 400 °F` 가 entity 로 저장되어 수치 검색 저해 | html.unescape; `●` → `- ` (PDF 에서 단일 bullet) | A |
| 19 | T12 | M | wikilink 1, 이중 list marker 11, ordered-list 시작 1 | L1459 `[[ This information is withheld in accordance with 10 CFR 2.390. ]]SRI`; L556–572, L602 `- 1. Operating experience review (OER) – …`; L606 `12. Human…` | p60, 23–25 | Obsidian 이 withheld marker 를 note link 로 해석 | `\[\[ … \]\]` escape(또는 코퍼스 규칙에 따른 치환); `- N. ` → `N. ` | A |
| 20 | T13 | L | italic 23, 밑줄 소제목 7(→#4), change bar 48 (24 pages) | L1233–1256 (italic `HF Planning`, `HF in Concept Design` … 18), L472–483 (run-in italic `Assumptions and Constraints -` 등 5) | p47–49, 20; bars p6–14, 19, 26–27, 37, 39, 43, 45, 53–54, 58–59, 65–67, 75–77 | Rev. 1 revision bar(x=691 pt 세로선)가 표시한 변경 구간 정보 소실(예: 11.6.2 전체 p75–77) | italic 은 `*…*` 로 복원 가능(선택); revision bar 는 frontmatter/주석으로 기록(선택) | B |
| 21 | T8 | L | 3 | L1459 `]]SRI`(SRI 는 7.7 pt 위첨자), L1571–1572 `NSS (1)`, `IAC (2)`, L1577–1578 `(1)`, `(2)` | p60–64, 74 | 의미 보존됨. 과학적 표기·각주 glue 없음; `TWR®` 유지 | 선택: `NSS<sup>(1)</sup>` | A |
| 22 | T99-1 | L | 1 | L1519 `##### .` | p67 | p67 우측 여백 7.0 pt “.” 1자(x=680, y=869 pt)가 H5 로 승격 | 삭제 | A |
| 23 | T99-2 | L | 4 marker 소실 | L1459 | p60–64 | 11.4 withheld 가 PDF 5 pages(11.4-1…11.4-5)에 걸침; md 는 1회만 보존(p61–64 page-top 반복분은 header 로 제거된 것으로 추정). 정보 손실은 page 범위뿐 | frontmatter 에 `withheld: 11.4 (PDF p60–64)` 기록 | A |
| 24 | T5 | L | page-break 로 끊긴 bullet list 9, ≥3 blank-line run 4, 2-blank run 167 | L666/669, L695/698, L725/728, L1062/1065, L1088/1091, L1151/1154, L1187/1190, L1275/1278, L1297/1300; runs L609–612, L1420–1423, L1491–1494, L1503–1506 | 해당 page break | list 가 여러 개로 분할(chunker 경계 오판 가능) | 연속 blank 를 1행으로, 인접 list item 사이 blank 제거 | A |
| 25 | T15 | M | 0 frontmatter, 0 page anchor | 전체 | — | page label: p6=11.1-1, p19=11.2-1, p51=11.3-1, p60=11.4-1, p65=11.5-1, p75=11.6-1 (각 section 연속 번호) | YAML frontmatter + `<!-- page 11.x-y -->` anchor(재변환 시 `--markdown-page-separator` 또는 token 정렬로 삽입) | B |
| 26 | T4 | — | 0 | — | — | 본문 내 `Kemmerer Unit 1 PSAR`/`SUBJECT TO DOE…`/`Revision 1` 쪽 번호 잔재 없음(`Revision 1` 5회는 모두 참고문헌·RG 판번호) | 없음 | — |
| 27 | T9, T10 | — | 0 | — | — | 각주·수식 없음 | 없음 | — |

원문(PDF) 자체의 오기로 확인된 항목(수정 금지, §5 참조): `Program Plant and Methodologies`(L444), Table 11.2-2 `11.2.2.2`(L1237, 실제 11.2.3.2), `NRSRT`(L1599) vs `NSRST`, `Section 2.3.3 Based upon`(마침표 없음), `responsibilities.The`(L1405), `through designated channels. for problems`(L791), heading 의 `Organization- TerraPower/USO` 표기, TOC `11.5-10P`.

## 2. Table verification log

전 table(4 논리 table, 13 md block)을 pdfplumber `extract_tables` 와 token 단위 difflib 로 대조하고, p46–50·p67–74 를 렌더링하여 cell 배치를 육안 확인하였다.

| Table ID | md lines | PDF p. | Status (OK / defect IDs) | Notes (lost values, split rows, …) |
|---|---|---|---|---|
| Table 11.2-1 NUREG-0711 Technical Elements Compared to Section 11.2 | L1212–1228 | p46 | OK (token 110/110) ; #16, #17 | 13 rows 전부 일치. row 11 의 3개 하위 항목(Procedures,/Training,/Verification and Validation)과 11.2.6.1/.2/.3 의 행 대응이 한 cell 로 합쳐짐. 첫 header cell 공백은 원문 동일. **원문 특성**: 2열(NUREG-0711)과 3–4열(Chapter 11 Section 2/Section #)은 행 단위로 대응하지 않는 독립 목록(예: row 5 `TA` ↔ `Functional Requirements Analysis 11.2.3.1`) — 교정 금지 |
| Table 11.2-2 Sheet 1 of 4 | L1231–1238 | p47 | #2 (caption 없음), #20 (italic 5) | token 174/174. `11.2.2.2 Allocation of Function` 는 원문 오기(11.2.3.2). bullet 목록 `<br>• …` 정상 |
| Table 11.2-2 Sheet 2 of 4 | L1241–1246 | p48 | #2 (반복 header), #16, #20 (italic 6) | token 221/221. L1245 sub-row 2개(11.2.5 Design of the Human-system Interface / 11.2.1.10 Design Goals and Design Bases) 병합; L1244, L1246 stage 문단 구분 소실 |
| Table 11.2-2 Sheet 3 of 4 | L1249–1257 | p49 | #2, #16, #17, #20 (italic 7) | token 177/178: `(postconstruction)` ↔ `(post-`/`construction)`. L1252 `…procurement procedures. HF in Detailed Design: Usability testing` 구분 소실 |
| Table 11.2-2 Sheet 4 of 4 | L1260–1262 | p50 | #2 | token 30/30, 1 row |
| Table 11.5-1 Sheet 1 of 7 | L1512–1516 | p67 | #2, #16 | token 300/299(pdfplumber 측 `10CFR` 결합 차이). row 1.0 title+설명 결합. 직후 L1519 `##### .` (#22) |
| Table 11.5-1 Sheet 2 of 7 | L1521–1524 | p68 | #2, #16 | token 165/165. row 3.0 title+설명 결합(PDF 는 title 행 + 문단 3개) |
| Table 11.5-1 Sheet 3 of 7 | L1527–1529 | p69 | #2 | token 178/178. row 3.1 bullet 3개 정상 |
| Table 11.5-1 Sheet 4 of 7 | L1532–1535 | p70 | #2 | token 223/223. rows 3.2, 3.3 정상(3.3 Basis bullet 3개 보존) |
| Table 11.5-1 Sheet 5 of 7 | L1538–1542 | p71 | #2, #16 | token 242/242. 3.4 `• PSP leakage The PHT is described in Section 7.1.3.`, 3.5 `• intake/exhaust flow rates The RAC is described in Section 7.2.1.` 결합 |
| Table 11.5-1 Sheet 6 of 7 | L1545–1548 | p72 | #2 | token 211/211. rows 3.7, 4.0 정상 |
| Table 11.5-1 Sheet 7 of 7 | L1551–1564 | p73 | **#1 (H)**, #2 | row 5.0 가 12 md rows × 3 cols 로 분해, 14 단어 분절(`Con\|trols`, `organiza\|tion`, `n\|ecessary`, `fac\|ility`, `c\|ontrols`, `speci\|fications`, `administr\|ative`, `res\|sponsibility`, `org\|ganization`, `qualific\|ations`, `m\|anuals`, `program\|m`, `TST\|F-493`, `require\|ments`), 중복 문자 3(s, g, m) |
| Table 11.5-2 Operating Modes | L1567–1578 | p74 | OK (token 71/71); #18, #21 | 4 modes × 5 cols 전부 일치: Mode 1 High Power Operation / More than one CRA coupled to CRDM driveline / NSS (1) / N/A; Mode 2 … / IAC (2) / N/A; Mode 3 Shutdown / No more than one CRA … / N/A / `&gt; 400 °F (204°C)`; Mode 4 Refuel / … / N/A / `≤ 400 °F (204°C)`. 주 (1) Mode-2→1 전환(IAC blower off, top/bottom dampers closed and latched), (2) Mode-1→2 전환(NSS isolation valves closed) verbatim 보존 |

참고: wiki `Natrium_Reactor_Operating_Modes.md` 의 Mode 표·전환 주석 값은 PDF Table 11.5-2 와 일치함을 확인(단, Mode-1 “Power ascension beyond IAC capacity” 는 원문 표현이 아닌 요약).

## 3. Figure inventory

| Figure ID | md lines | raster/vector | image file | debris lines to delete | Notes |
|---|---|---|---|---|---|
| Figure 11.1-1 Executive Management Organization | L319–347 | vector box + 빈 raster fill | imageFile4–12 (white 404×201/201/216/268/277 px, black 404×201/216/268/277 px; 4 = 6 동일) | image ref 9행: L321, 323, 327, 333, 335, 339, 341, 345, 347 | label 5개 모두 존재(L325, 329, 331, 337, 343). `ChiefNuclear Officer` → 렌더링상 “Chief Nuclear Officer”. caption L319 이 plain paragraph |
| Figure 11.1-2 Natrium Project Organization | L349–351 | raster | imageFile13 (3920×2565 px, 733 KB) | 없음 | text layer 없음 → box 22개 transcription 필요 |
| Figure 11.1-3 Construction Organization | L353–389 | vector (p17, Rotate 90) | 없음 | label 18행 L355–389(교체) | 20 box 중 18 추출. 소실: `Quality Control Manager`, `QC Personnel`. 순서 뒤섞임 |
| Figure 11.1-4 Operating Organization and Technical Support | L391–435 | vector (p18, Rotate 90) | 없음 | label 22행 L393–435(교체) | 24 box 중 22 추출(1 병합, 1 분할). 소실: `Director of NOS`, `Quality Assurance Manager` |

Transcription 초안(렌더링 p15–18 및 imageFile13 판독 기준; 연결선 해석은 cleanup 시 재확인 요망):

- Fig. 11.1-1: President/CEO TerraPower → { Chief Nuclear Officer; Director responsible for quality; Executive responsible for project execution; Executive responsible for regulatory affairs }.
- Fig. 11.1-2: Executive responsible for project execution → Deputy Project Director { Sr Manager, Procurement; Sr Manager, Project Planning; Manager, Subcontractor Oversight } / Director, Plant Delivery { Sr Manager, Instrument Controls & Electrical; Sr Manager, Reactor Systems &System Integration; Sr Manager, Nuclear Island Fluid Systems; Sr Manager, Fuel Handling Systems } / Director Nuclear Fuel and Equipment Qualification { Sr Manager, Materials Development & Qualification; Sr Manager, Fuel Development & Qualification; Sr Manager, Equipment Qualification & Testing } / Executive responsible for design { Manager, Digital Engineering; Manager, Engineering Process } / Director, Safety and Engineering Analysis { Sr Manager, Safety Analysis & Risk; Sr Manager, System Analysis; Sr Manager, Core Design and Methods; Sr Manager, Engineering Analysis }.
- Fig. 11.1-3: Project Manager (staff: Resident Engineering; Quality Assurance Manager) → Project Controls Manager; Startup Manager; Site Manager → { Project Superintendent → Construction Supervision; Project Field Engineer → { Construction Field Engineers; Advanced Work Packaging; Turnover Coordinator; Site Admin Manager → Document Control }; Project Subcontracts Manager; Project Procurement Manager; ES&H Manager → ES&H Staff; Quality Control Manager → QC Personnel }.
- Fig. 11.1-4: CNO → PGM { Director of Operations → { Shift Operations Manager; Fire Protection Manager }; Director of Training → { Ops Training Manager; Maintenance & Technical Training Manager }; Security Manager; Station Sciences Manager → RP Supervisor → Station Sciences Tech; Director of Maintenance → { Maintenance Execution Manager; Work Management Manager }; Director of Org Effectiveness → EP & Licensing Manager } / Procurement Manager (USO) / Director Engineering Support Services → { Commissioning Manager; Plant Support Engineering; Design Support Engineering } / Director of NOS → Quality Assurance Manager.

## 4. Heading outline check

의도 outline 은 PDF 본문 행(`^\d+\.\d+(\.\d+)* Title`)에서 추출하였고 TOC(3단까지)와 대조하였다. level 규칙: `Chapter 11 Conduct of Operations` = H1, 11.x = H2, 11.x.y = H3, 11.x.y.z = H4, 11.x.y.z.w = H5.

요약 (번호 heading 127):

| md 형태 | 개수 | 비고 |
|---|---|---|
| list item `- 11.x… Title` (clean) | 115 | A 규칙으로 변환 가능 |
| list item + 본문 glue | 4 | L287 (11.1.5.1), L534 (11.2.1.3), L1135 (11.2.7.1), L1371 (11.3.6.1) |
| plain paragraph | 4 | L1305 (11.3.2), L1390 (11.3.6.3), L1488 (11.5.2.2), L1500 (11.5.2.4) |
| plain + 본문 glue | 2 | L1265 (11.3), L1366 (11.3.5.2) |
| 본문 중간 glue | 1 | L1447 (11.3.10) |
| `####` + withheld marker glue | 1 | L1459 (11.4, 의도 H2) |
| 정상 Markdown heading | 0 | — |

번호 없는 heading (13): `Chapter 11 Conduct of Operations` L84 `###`→H1; `Design Changes` L677 `###`→H5; `Objectives and Scope` L943 끝 glue→H4; `Methodology` L948 앞 glue→H4; 11.6.2 하위 5개(L1597 앞, L1599 앞·중간·중간, L1609 앞) glue→H4; `References` ×5: L313, L1199, L1451 `###`(H3 유지), L1502·L1609 끝 glue→H3.

비-heading 승격: L13 (TOC 행), L66, L76, L349, L353, L391, L1212, L1567 (caption), L1519 (`.`).

전체 whitelist (번호(md line, 의도 level, 현재 형태: LI=list item, LI+G=list+glue, P=plain, P+G=plain+glue, MID=본문 중간, H4+G=`####`+glue)):

```
11.1(L86,H2,LI); 11.1.1(L105,H3,LI); 11.1.1.1(L110,H4,LI); 11.1.1.2(L116,H4,LI); 11.1.1.3(L122,H4,LI); 11.1.1.4(L129,H4,LI)
11.1.1.5(L135,H4,LI); 11.1.2(L140,H3,LI); 11.1.2.1(L147,H4,LI); 11.1.2.2(L151,H4,LI); 11.1.2.3(L155,H4,LI); 11.1.2.4(L159,H4,LI)
11.1.2.5(L163,H4,LI); 11.1.3(L170,H3,LI); 11.1.3.1(L180,H4,LI); 11.1.3.2(L184,H4,LI); 11.1.3.3(L188,H4,LI); 11.1.4(L192,H3,LI)
11.1.4.1(L222,H4,LI); 11.1.4.1.1(L227,H5,LI); 11.1.4.1.2(L231,H5,LI); 11.1.4.1.3(L235,H5,LI); 11.1.4.1.4(L240,H5,LI); 11.1.4.1.5(L244,H5,LI)
11.1.4.1.6(L248,H5,LI); 11.1.4.2(L253,H4,LI); 11.1.4.2.1(L257,H5,LI); 11.1.4.3(L262,H4,LI); 11.1.4.4(L266,H4,LI); 11.1.4.4.1(L271,H5,LI)
11.1.4.4.2(L275,H5,LI); 11.1.4.4.3(L279,H5,LI); 11.1.5(L284,H3,LI); 11.1.5.1(L287,H4,LI+G); 11.1.5.2(L288,H4,LI); 11.1.5.3(L292,H4,LI)
11.2(L437,H2,LI); 11.2.1(L451,H3,LI); 11.2.1.1(L454,H4,LI); 11.2.1.2(L499,H4,LI); 11.2.1.3(L534,H4,LI+G); 11.2.1.4(L548,H4,LI)
11.2.1.5(L621,H4,LI); 11.2.1.6(L625,H4,LI); 11.2.1.7(L629,H4,LI); 11.2.1.7.1(L634,H5,LI); 11.2.1.7.2(L645,H5,LI); 11.2.1.7.3(L649,H5,LI)
11.2.1.8(L654,H4,LI); 11.2.1.9(L658,H4,LI); 11.2.1.10(L688,H4,LI); 11.2.1.11(L701,H4,LI); 11.2.1.12(L713,H4,LI); 11.2.1.13(L717,H4,LI)
11.2.1.14(L735,H4,LI); 11.2.1.15(L739,H4,LI); 11.2.1.16(L745,H4,LI); 11.2.2(L804,H3,LI); 11.2.2.1(L825,H4,LI); 11.2.2.2(L838,H4,LI)
11.2.2.2.1(L861,H5,LI); 11.2.2.2.2(L865,H5,LI); 11.2.2.2.3(L878,H5,LI); 11.2.2.2.4(L883,H5,LI); 11.2.2.2.5(L895,H5,LI); 11.2.2.3(L913,H4,LI)
11.2.3(L926,H3,LI); 11.2.3.1(L950,H4,LI); 11.2.3.2(L954,H4,LI); 11.2.3.3(L958,H4,LI); 11.2.4(L964,H3,LI); 11.2.4.1(L969,H4,LI)
11.2.4.1.1(L976,H5,LI); 11.2.4.1.2(L980,H5,LI); 11.2.4.1.3(L994,H5,LI); 11.2.5(L1013,H3,LI); 11.2.6(L1017,H3,LI); 11.2.6.1(L1020,H4,LI)
11.2.6.2(L1024,H4,LI); 11.2.6.2.1(L1033,H5,LI); 11.2.6.2.2(L1072,H5,LI); 11.2.6.2.3(L1114,H5,LI); 11.2.6.3(L1121,H4,LI); 11.2.6.4(L1125,H4,LI)
11.2.7(L1130,H3,LI); 11.2.7.1(L1135,H4,LI+G); 11.2.7.2(L1161,H4,LI); 11.2.7.3(L1194,H4,LI); 11.3(L1265,H2,P+G); 11.3.1(L1267,H3,LI)
11.3.2(L1305,H3,P); 11.3.2.1(L1307,H4,LI); 11.3.2.2(L1311,H4,LI); 11.3.3(L1315,H3,LI); 11.3.3.1(L1318,H4,LI); 11.3.3.2(L1329,H4,LI)
11.3.4(L1334,H3,LI); 11.3.4.1(L1339,H4,LI); 11.3.4.2(L1344,H4,LI); 11.3.5(L1355,H3,LI); 11.3.5.1(L1357,H4,LI); 11.3.5.2(L1366,H4,P+G)
11.3.6(L1368,H3,LI); 11.3.6.1(L1371,H4,LI+G); 11.3.6.2(L1385,H4,LI); 11.3.6.3(L1390,H4,P); 11.3.7(L1396,H3,LI); 11.3.8(L1402,H3,LI)
11.3.9(L1409,H3,LI); 11.3.9.1(L1411,H4,LI); 11.3.9.2(L1419,H4,LI); 11.3.9.2.1(L1424,H5,LI); 11.3.9.2.2(L1428,H5,LI); 11.3.9.2.3(L1433,H5,LI)
11.3.9.3(L1438,H4,LI); 11.3.10(L1447,H3,MID); 11.4(L1459,H2,H4+G); 11.5(L1461,H2,LI); 11.5.1(L1464,H3,LI); 11.5.2(L1479,H3,LI)
11.5.2.1(L1484,H4,LI); 11.5.2.2(L1488,H4,P); 11.5.2.3(L1496,H4,LI); 11.5.2.4(L1500,H4,P); 11.6(L1581,H2,LI); 11.6.1(L1584,H3,LI)
11.6.2(L1590,H3,LI)
```

Glued heading 의 정확한 title (분리 기준 문자열):
- L287 `11.1.5.1 Qualification of Nuclear Personnel` | 본문 `Qualifications of managers, …`
- L534 `11.2.1.3 Overview of the Human Factors Engineering Program` | `The HFE program describes goals …`
- L1135 `11.2.7.1 Objectives and Scope` | `The purposes of HPM are to:`
- L1265 `11.3 Emergency Preparedness` | `This section provides a description …`
- L1366 `11.3.5.2 State and Local Governmental Agencies` | `Notification requirements, protocols, …`
- L1371 `11.3.6.1 Response to Emergency Situation` | `The steps for taking protective measures …`
- L1447 `…discussed further in Section 1.1.4.3.` | `11.3.10 Performance Monitoring` | `A performance monitoring program …`
- L1459 `11.4 Aircraft Impact Assessment` | `[[ This information is withheld in accordance with 10 CFR 2.390. ]]SRI`
- L943 `…found in OERs, TA, HSI design, and V&amp;V.` | `Objectives and Scope`; L948 `Methodology` | `Human reliability analysis is conducted …`
- L1502 `…manipulated to support testing.` | `References`; L1609 `…response activities related to security operations.` | `References`
- L1599 분할점: `Nearby Industrial, Transportation, and Military Facilities` | `Potential hazards …`; `…related to security operations.` | `Meteorology and Meteorological Dispersion` | `Regional climatology …`; `…in the presence of these hazards.` ¶ `As described in Section 5.2.1, …`; `…defense-in-depth (DID) adequacy.` ¶ `Since safety-significant structures …`; `…related to security operations.` | `Hydrology` | `The site characteristic of hydrology …`; `…pursuant to 10 CFR 73.` ¶ `Section 2.5.1 describes …`

## 5. File-specific observations and recommendations for the cleanup script

권장 적용 순서:
1. 원본 보존용으로 PDF 기반 보조 데이터 생성: (a) §4 outline whitelist(127 + 번호 없는 13), (b) caption 목록(LoT/LoF L68–81), (c) pdfplumber p73 row 5.0 cell, (d) p76 문단 경계.
2. Frontmatter 생성 후 cover L1–11 삭제. 제안 key: `doc_id: TP_Natrium_PSAR2025_ch11`, `title: "Kemmerer Unit 1 PSAR Chapter 11 Conduct of Operations"`, `applicant: US SFR Owner, LLC (TerraPower, LLC)`, `revision: 1`, `year: 2025`, `doe_agreement: DE-NE0009054`, `source_pdf`, `pdf_pages: 77`, `page_labels: {11.1: p6–18, 11.2: p19–50, 11.3: p51–59, 11.4: p60–64 (withheld), 11.5: p65–74, 11.6: p75–77}`, `withheld: ["11.4 Aircraft Impact Assessment (10 CFR 2.390, SRI)"]`, `tables`, `figures`.
3. TOC·LoT·LoF 블록 L13–82 삭제(whitelist 수확 후).
4. `### Chapter 11 Conduct of Operations`(L84) → `# …`.
5. Heading 변환: whitelist 번호와 일치하는 `^- (11\.\d+(?:\.\d+)*) ` 행 및 plain 행 → `#`×depth. glued 8건은 §4 title 문자열로 분리. 번호 없는 소제목·`References` 분리(§4).
6. `##### .`(L1519) 삭제, figure caption 형식 통일(caption 은 heading 이 아닌 형태 권장, 코퍼스 규칙에 따름), Fig. 11.1-1 caption(L319) 동일 형식화.
7. Figure: 빈 image ref 9행(imageFile4–12) 삭제; label 파편(L325–343, L355–389, L393–435)을 §3 transcription 으로 교체(누락 label 4개 포함); imageFile13 에 alt text 부여; imageFile1–3 ref 제거.
8. List 정리: false list item 17행(§1 #8 6행 결합, #9 10행 unbullet, L1495 결합), `●`(L1364)→`- `, `- N. `→`N. `, L606 형식 통일; page-break 문단 결합 9건; blank-line 정규화.
9. L1272 분할(`…scalable PEP EPZ size.` ¶ `The key elements of the emergency preparedness plan to meet 10 CFR 50.160 will include:`), L1599 분할(§4).
10. Table: caption 삽입(11.2-2, 11.5-1), sheet 병합과 반복 header 9개 삭제, row 5.0 재구성(#1), cell 내부 `<br><br>` 보정(#16), trailing `<br>` 정리.
11. HTML entity unescape(`&amp;` 23, `&gt;` 1), withheld marker escape(L1459).
12. (선택) italic 23건 복원, revision-bar 구간과 page anchor 삽입.

주의사항(pitfalls):
- 참고문헌 항목 `- 11.1-1 ANSI/ANS-3.1-2014 …`(20개: 11.1 ×2, 11.2 ×9, 11.3 ×4, 11.5 ×3, 11.6 ×2)은 `11.1-1`(hyphen) 형식이므로 heading regex(`11\.\d+(\.\d+)*\s`)에서 제외되어야 함.
- `- Section …` 행 처리 시 직전 행 종결 여부로 분기: L177/219/480/553/604/608 은 결합, L448/L1601/L1604 는 `- ` 만 제거(직전 행이 `.` 로 끝남).
- L943·L1107·L1272·L1486·L1490·L1498·L1502 은 텍스트 패턴이 제각각이므로 줄 목록 또는 PDF x0(=162 pt) 대조로 처리. 운전 모드 정의(L1486–1502)는 retrieval 가치가 높으므로 결합·분리 결과를 반드시 PDF p65–66 과 대조.
- L1490→L1495 결합 시 사이 blank 4행과 `- ` 를 함께 제거해야 “…during a shutdown or downpower when reactor power is lowered…” 가 복원됨.
- Table 11.5-2 의 `&gt;` 를 unescape 하면 `>` 가 cell 선두에 오지만 table 행 내부이므로 blockquote 로 해석되지 않음. table 밖으로 옮기지 말 것.
- heading 분리 시 heuristic(대문자 단어 경계)을 쓰면 L287 처럼 title 과 본문 첫 단어가 모두 대문자인 경우 잘못 분할됨 → whitelist 필수.
- landscape(`/Rotate 90`) page 의 우측 텍스트 소실은 opendataloader 측 결함으로 판단됨. 재변환 옵션만으로 복구된다는 근거는 확인되지 않았음(미검증); pdfplumber words 로 보완 권장. 다른 PSAR chapter 의 rotated page 도 동일 점검 필요.
- md 파일명 변경 금지: `wiki/Natrium_Reactor_Operating_Modes.md` 가 `[[TP_Natrium_PSAR2025_ch11_Conduct of Operations]]` 로 참조(heading anchor 참조는 없음).

자동 수정 금지(원문 verbatim 보존 대상):
- 원문 오기: `Natrium Human Factors Engineering Program Plant and Methodologies`(L444; 다른 곳은 “Plan”), Table 11.2-2 `11.2.2.2`, `NRSRT`/`NSRST` 불일치, `Section 2.3.3 Based upon`, `responsibilities.The`, `through designated channels. for problems`, `Organization- TerraPower/USO` 식 hyphen 표기, `Reactor Systems &System Integration`(Fig. 11.1-2 raster 원문).
- Table 11.2-1 의 행 대응(독립 목록) 재배열 금지.
- `ChiefNuclear` 는 text layer 원문이나 렌더링은 “Chief Nuclear” → 교정은 C(판단)로만.
- `(postconstruction)` 의 hyphen 복원 여부는 원문 줄바꿈 hyphen 이라 판단 필요(C).
- Table 11.5-2 주 표시 `(1)`, `(2)` 삭제 금지(Mode 전환 조건과 연결).

검색용 식별자(frontmatter/tag 후보, 요약):
- 문서/규제: NAT-2965-A (HFEPP LTR, IBR), NAT-3056-A (PEP EPZ TR, ML25104A001), TP-LIC-RPT-0012 (IBR), DANU-ISG-2022-05, DANU-ISG-2022-08, TSTF-493 Option B, NUREG-0711/-0700/-0737 Suppl. 1/-0800 §17.5/-1764/-1275/-1431/-0696/-0654 (FEMA-REP-1), NUREG/CR-6400, TLR F0028-04 (ML21287A088), RG 1.8 R4, 1.33 R3, 1.114 R3, 1.233 R0, 1.242 R0, 5.84 R0, NEI 91-04/18-04/21-07/06-06/09-01, ANSI/ANS-3.1-2014, ANSI/ANS-3.2-2012, IAEA INSAG-7, SSG-51; 10 CFR 50.160(b)(1)(iii)(A)–(H), 50.33(g)(2)(i), 50.34(a)(5)/(b)(6)(vi)/(b)(8)/(c)/(d)/(f)(2)/(f)(3)(i), 50.36(c)(1)(ii)(A)/(c)(2)(ii), 50.54(k)/(m)/(q)/(t), 50.120, Part 26 Subpart I, Part 55, 73.54, 100.20, 100.21(f)/(g), 2.390.
- 운전 모드: Mode-1 High Power Operation, Mode-2 Low Power Operation, Mode-3 Shutdown (>400 °F/204 °C), Mode-4 Refuel (≤400 °F/204 °C); TS 절 1.0–5.0, LCO 3.1–3.7.
- 계통 약어: PHT, IHT, NSS, IAC, SHX, CRA, CRD, CRDM, PSP, IHX, RAC, RPS, XIS, RIS, FHI, FHE, FHP, COLR, LSSS, SL, LCO.
- HFE/EP 약어: OER, FRA, AOF, TA, HSI, HA, V&V, ISV, TSV, HPM, HFEITS, HED, DIF, RSR, MCR, RSC, LCS, ERF/ERFP/ERFB, ERO, ED, PEP EPZ, EAB, LPZ (Emergency Classification Levels / Emergency Action Levels 는 원문에 약어 없이 기재).
- 조직 직위(11.1): CNO, PGM, Director of Nuclear Oversight (NOS), QA Manager, Station Sciences Manager, Director Engineering Support Services 등.
- 교차참조 패턴: `Section 11.x.y`, `Table 11.x-y`, `Figure 11.1-n`, `Reference 11.x-n`, `Sections a through b`.
