# Review rg: RG_1.232.md (md lines 1–1359, PDF pages 1–133)

검토 대상: `C:\Obsidian\ripb\references\RG_1.232.md` (opendataloader-pdf 2.5.7 기본 옵션 산출물) ↔ `references\pdf\RG_1.232.pdf` (133 pp., untagged, outline 없음).
검증 도구: pdfplumber 0.x (문자·폰트·색상·표 셀), pypdf, PDF 페이지 렌더링(p1, 13–18, 63–65, 81), 스크래치패드 스크립트 `rg_crit.py`(기준별 단어 수준 대조), `rg_body.py`(본문 토큰 정렬), `rg_celldiff.py`(Table 1 셀 대조), `rg_hyph.py`(줄끝 하이픈), `rg_sup.py`(각주 위첨자), `rg_colors.py`(redline 색상), `rg_blocks.py`(md 표 블록↔PDF 표 1:1 매핑).
판정 원칙: 원문 verbatim 보존. 아래 "원문 오기(誤記)" 항목은 변환 결함이 아니므로 수정 대상에서 제외한다.

## 0. 개요

| 항목 | 값 |
|---|---|
| md 규모 | 1,359 lines, 309,747 chars (파일 311,835 B), 2,000자 초과 행 18개, 빈 행 435개 |
| PDF | 133 pp.; 본문 p1–28 (쪽 번호 1–27, p20·p21이 모두 "Page 20"으로 인쇄된 원문 오류), Appendix A p29–61 (A-1–A-33), Appendix B p62–103 (B-1–B-42), Appendix C p104–133 (C-1–C-30, p105의 footer가 "Page B-2"로 오기) |
| 논리 표 | 4개: Table 1 Non-LWR Crosswalk (p13–20, 65 criteria × 5 cols), Appendix A ARDC 표 (p30–61, 55 criteria), Appendix B SFR-DC 표 (p63–103, 65 criteria), Appendix C MHTGR-DC 표 (p106–133, 58 criteria) |
| md 표 블록 | 123개 (Table 1: 10, A: 34, B: 46, C: 33) — PDF의 페이지별 표 123개와 1:1 대응, criterion ID 순서 전부 일치(행 누락 0) |
| `<br>` | 706개 (`<br><br>` 331, `<br><br><br>` 6, 셀 끝 trailing `<br>` 40) |
| 그림 | 0 (raster 1개 = 표지 NRC 휘장, 장식용) |
| 헤딩 | md 33개 (H1 1, H2 1, H3 11, H4 17, H5 1, H6 2); PDF 기준 의도된 본문 헤딩 32개 + 표 section 27개 + criterion 178개 |
| 각주 | 14개 (본문 참조 기호 14, 본문 bodies 14) |
| 약어 | 42개 (ACRONYMS/ABBREVIATIONS; p23 41 + p24 1) |
| 순수 노이즈 | ≈ 370 lines / ≈ 15,500 chars (5.0 % of chars, 27 % of lines): 반복 표 헤더 2행×123 + 구분행 (중복분 357 lines, ≈ 14,030 chars), TOC 11 lines / 1,362 chars, footer 1 line / 41 chars, 표지 이미지 1 line |
| 오배치(노이즈는 아님) | 각주 본문 14개 4,045 chars, 표지 text box 1,061 chars(메타데이터로 이동 대상), 연속행 73개(criterion key 없음) |

핵심 결론: 본문(비표) 텍스트는 단어 수준에서 거의 완전하나(누락 0, 순서 오류 2), (i) Table 1의 redline-strikeout 의미가 소실되어 29개 셀의 제목이 사실과 다르게 기록되었고, (ii) 가로(/Rotate 90) 페이지의 가장 오른쪽 열에서 줄끝 텍스트 조각 20개가 누락되었으며(16개 셀), (iii) 각주 위첨자 결합으로 `10 CFR 50.342` 같은 허위 인용 번호가 생성되었고, (iv) 줄끝 하이픈 제거로 `SFRDC 17`, `SECY-150002`, `https://www.gen4.org` 등 식별자·URL 21건이 손상되었다. 표는 페이지 단위로 123개로 쪼개져 criterion 178개 중 62개가 복수 블록에 분산(43개는 문장 중간 분할)되어 criterion 단위 검색이 불가능하다.

재변환 검증(§2.7): (ii)의 원인은 opendataloader 기본 content-safety `off-page` 필터로 확인되었다. 133쪽 중 109쪽이 /Rotate 90(MediaBox 612 × 792 pt)이며, 누락 조각 20개는 모두 폰트 전환 직후 표시 좌표 x ≥ 613.8 pt(> 612 pt)에서 시작한다. `content_safety_off="off-page"`로 재변환하면 20개가 전부 복원되고 그 외 텍스트 변화는 0이다(부록 178 criteria 단어 diff 0). `detect_strikethrough=True`를 추가하면 Table 1의 삭제어 33군(29개 셀)이 모두 `~~…~~`로 표시된다. (i)·(ii)는 재변환으로 해결되며, (iii)·(iv)와 표 분할·헤딩 결함은 재변환으로 해결되지 않는다.

## 1. Findings

| # | T-ID | Sev | Count | md lines (examples) | PDF p. | Evidence / description | Proposed fix | Fix class |
|---|---|---|---|---|---|---|---|---|
| F01 | T13+T14 | H | 29 redline 셀 (삭제어가 일반 텍스트로 잔존 22, 삽입/삭제어 누락 7) | L256, L257, L278, L287–L290, L293, L294, L306–L308, L319, L320 | 14–18 | Table 1은 "Words removed from the title are in red with a strikethrough and words that have been added are in blue and underlined"(L209). md는 이 표지를 전부 잃었다. 예: L256 ARDC `Reactor coolant pressure boundary.` ← PDF `Reactor coolant ~~pressure~~ boundary.` (실제 ARDC 14 제목 = "Reactor coolant boundary"); L257 SFR `Primary Reactor coolant system design.` ← `<ins>Primary</ins> ~~Reactor~~ coolant system design.`; L256 MHTGR `Reactor pressure boundary.` ← `Reactor <ins>helium</ins> ~~coolant~~ pressure boundary.`; L293 MHTGR `Inspection of core cooling removal system.` ← `Inspection of <ins>passive</ins> ~~emergency core cooling~~ <ins>residual heat removal</ins> system.` 전체 목록 §1.1 | 재변환(`content_safety_off="off-page"`, `detect_strikethrough=True`)으로 삭제어 33군이 `~~…~~`로 표시되고 누락어가 복원됨(§2.7 검증). 삽입어(청색 밑줄)는 표시되지 않으므로 필요하면 PDF 문자 색상(청색 (0.122,0.286,0.486))으로 `<ins>…</ins>` 추가. 이후 열을 "최종 제목(= `~~…~~` 제거) / 상태 / redline"으로 분리하고 최종 제목을 Appendix A–C italic 제목과 교차검증 | B (재변환) |
| F02 | T14 | H | 20 누락 span / 16 셀 (Table 1: 11 span / 9 셀; Appendix: 9 span / 7 셀) | L538, L821, L989, L1189, L1273, L1305, L1307; L256, L257, L278, L287–L289, L291, L293, L339 | 35, 70, 92, 115, 125, 129; 14–16, 20 | 가로(/Rotate 90) 페이지의 가장 오른쪽 열(Table 1 MHTGR-DC 열, 부록 rationale 열)에서 폰트가 바뀐 뒤 x ≥ 613.8 pt(> MediaBox 폭 612 pt)에서 시작하는 줄끝 조각이 `off-page` 필터에 의해 삭제됨(§2.7). 예: L538/L821/L1189 `…to operate the nuclear power unit<br><br>However…` ← PDF `…unit safely…” However…` (인용문 핵심어 "safely" 소실, 3회); L821 `operators must knowledge … be able to decisions` ← `must have certain knowledge … be able to make decisions`; L989 `SFR-DC 57, “Closed system isolation valves,” systems that penetrate` ← `… valves,” addresses closed systems that penetrate`; L1273/L1305/L1307 `was removed. rationale for ARDC 17` ← `was removed. Refer to the rationale for ARDC 17`; L291 MHTGR-34 `Residual heat removal. for MHTGR-DC` ← `… Modified for MHTGR-DC`; L339 MHTGR-72 `…building inspection` ← `…building inspection.` (roman 마침표) | `content_safety_off="off-page"`로 재변환 — 20개 전부 복원, 부작용 0 (§2.7). 정리 후 PDF 셀 단위 단어 diff를 회귀 검사로 유지 | B (재변환) |
| F03 | T8 | H 4 / M 10 | 14 각주 참조 기호가 앞 토큰에 결합 | L19, L123, L140, L194, L351, L355, L388, L411, L432, L440, L442, L444, L737, L1086 | 1, 7, 8, 11, 21, 25–28, 62, 104 | 위첨자(7 pt) 소실. 허위 번호 생성: L123 `Title 10 CFR 50.342 states` (= 50.34 + fn 2; 인용 목록에 "10 CFR 50.342"가 독립 인용으로 집계됨), L194 `developing PDC4.` (PDC 번호 "PDC 4"와 충돌), L444 `…/pii/S030645491500580012.` (URL = …S0306454915005800 + fn 12), L19 `(Ref. 2)1.`; 헤딩 오염 L388 `### REFERENCES7`. 전체 목록 §1.2 | 명시 목록(줄, 토큰, 각주 번호)으로 `[^n]` 치환. 일반 정규식(`[a-z]\d`) 금지 — `SFR-DC17`, `MHTGR-DC 10` 등 오탐 | A (목록 확정됨) |
| F04 | T11 | H | 21 (+ 식별자 분할 2) | L190, L409, L440, L442, L902, L903, L909, L910, L917, L929, L938, L953, L954, L962, L1081, L1225, L1299; L446–L452 | 11, 26, 28, 81–103, 119, 128 | 줄끝 하이픈 제거로 식별자·URL 손상: `SFRDC` ×13 (예 L903 `Refer to SFRDC17`, L909 `SFRDC 34`), `MHTGRDC` ×3 (L190, L1225 `MHTGRDC 15`, L1299 `MHTGRDC 34`), L409 `SECY-150002` (= SECY-15-0002), L1225 `SECY94-084`, L903 `NUREG1368`, L440 `https://www.gen4.org/…` (= gen-4.org), L442 `…NPTDSmexico/…` (= NPTDS-mexico). 또한 L446–L452 `INL/EXT-` + `- 10-17997`, `INL/EXT-` + `- 11-22708`: 보고서 번호가 줄바꿈에서 거짓 목록 항목으로 분할 | PDF 줄끝 하이픈 목록(§1.3)으로 복원: 하이픈 유지 결합(`SFR-DC 34`, `SFR-DC17`은 원문대로). INL 번호는 한 줄로 병합 | B (또는 §1.3 목록 기반 A) |
| F05 | T11 | M | 45 (21 형태) + em dash 1 | L15, L27, L127, L136, L140, L154, L164, L176, L194, L498, L681, L690, L769, L792, L800, L989, L1053, L1154, L1169, L1231 | 1, 7–11, 29–133 | 식별자 외 하이픈 결합: `nonLWR` ×18, `NonLight` ×3, `preapplication` ×3, `sodiumcooled` ×2, `fireresistant` ×2, `structurespecific` ×2, `leaktightness` ×2, `technologyspecific`, `todiameter`, `NonLWRs`, `FacilitySpecific`, `heatresistant`, `lossof`, `liquidmetal`, `pressureretaining`, `pressurizedwater`, `RadioactiveWaste`, `MHTGRspecific`, `offnormal`, `safetyrelated`; L136 `technologiesspecifically` ← `technologies—␤specifically` (em dash 소실). 주의: L123 `watercooled`, L498 `fire- resistant`는 PDF 원문 그대로(텍스트층·렌더링 확인)이므로 수정 금지 | PDF 목록 기반 복원 (§1.3). 사전 기반 추정 금지 | B/A |
| F06 | T6 | H(검색) / M | 123 블록; 헤더 오용 123; 헤더 반복 123; 연속행 73 (A 22, B 30, C 21); 분산 criteria 62/178; 문장 중간 분할 43; criterion 본문 전체가 연속행에만 있는 경우 5 | L234–L346, L488–L732, L759–L1081, L1115–L1356 | 13–133 | section group label(`\|I. Overall Requirements\| \| \|`)이 Markdown 헤더 행이 되고 실제 헤더(`Criterion\|SFR-DC Title and Content\|NRC Rationale…`)가 매 블록 본문 첫 행으로 반복. 페이지 경계에서 행이 끊겨 Criterion 셀이 빈 연속행 발생: SFR-DC 4 마지막 문단 L776, SFR-DC 11 문장 중간 L784→L790 (`the prompt inherent nuclear` / `feedback characteristics…`), SFR-DC 26은 4개 블록(L849, L855, L861, L867), MHTGR-DC 26은 5개 블록. SFR-DC 18·40, ARDC 5, MHTGR-DC 24·61은 제목+상태만 첫 행에 있고 기준 본문은 번호 없는 연속행에만 존재 | 부록별·section별로 블록 병합, 중복 헤더 제거, 연속행을 직전 criterion에 결합(문장 중간이면 공백, 문장 끝이면 문단 구분), 이후 criterion 단위 record로 변환(§5.1). md만으로 결정적 처리 가능(123 블록 ↔ 123 PDF 표, ID 순서 일치 확인) | A |
| F07 | T6+T13 | M | 178 부록 셀 + Table 1 제목·상태 결합 셀 81 (ARDC 39, SFR-DC 22, MHTGR-DC 20) | L491, L762, L770, L1118, L240 | 30–133, 13–20 | 부록 Column 2 한 셀에 italic 제목 + 상태행("Same as GDC"/"Same as ARDC"/"Not applicable to MHTGR.") + 본문이 공백으로 연결(예 L762 `Quality standards and records. Same as GDC Structures, systems, …`). PDF p63–65는 세 요소가 별도 줄이며 제목만 italic. 부록 B: 상태행 있는 33개(공백 연결 29, `<br>` 2, 셀 끝 2), 상태행 없는 32개(Modified 22, New 10; 상태는 Table 1에만 존재). Table 1 셀도 `Fire protection. Modified for ARDC`처럼 제목과 상태가 결합. PDF italic run 315개(Table 1 111, A 61, B 73, C 64, 본문 6)가 md에서 전부 소실(md에 `*`/`_` 강조 0) | 제목/상태/본문 분리. 상태 정규식 `^(Same as GDC\|Same as ARDC\.?\|Not applicable to MHTGR\.)`, 제목 = PDF italic run(단 SFR-DC 18은 상태행도 italic, SFR-DC 39·44·52·73·78 제목은 마침표 없음, 78은 Title Case) | A/B |
| F08 | T6 | L | 문단 병합 3 셀, 목록 문단→`<br>` 4 셀, 불필요한 `<br><br>` ≈ 30 셀 | L800, L903, L1299; L567, L849, L1062, L1219; L976, L996, L1030 | 67, 81, 128; 39, 74, 100, 118 | SFR-DC 34 L903 `…are not exceeded. Suitable redundancy…` ← PDF 두 문단(p81); SFR-DC 16 L800, MHTGR-DC 44 L1299 동일. 반대로 줄 머리의 "(1)"·"(3)" 앞에 `<br><br>` 삽입(L976 `shall be designed to permit<br><br>(1) appropriate…`) | record 변환 시 PDF 줄 간격(> 18 pt)으로 문단 재구성 | B |
| F09 | T9 | M | 14 (목록 항목 13, H6 헤딩 1); 문장/목록 중간 삽입 6 | L27, L131, L154, L204, L370, L371, L403, L419, L437, L458, L460, L462, L756, L1106 | 1, 7, 8, 11, 21, 25–28, 62, 104 | `- 1 While the design criteria…`(L27, Applicable Regulations 목록 사이), `###### 3 The technology-specific…`(L154, bullet L150–L156 중간), L370–L371(fn 5·6, 문장 `…compliance with the` / `underlying NRC…` 사이), L437(fn 9, Ref. 34 본문 중간), L1106(fn 14, Section 목록 중간). 원문 중복: fn 1 = fn 4, fn 3 = fn 13 = fn 14, fn 10 = fn 11 (verbatim 유지) | `[^n]:` 정의로 이동(해당 section 끝 또는 문서 끝), 본문 결합 복구 | A |
| F10 | T3 | M | 스퓨리어스 5, 순서 뒤바뀜 2, 누락/본문 결합 4, 오염 1, 캡션 누락 1, 표 section 제목 27(표 헤더에만 존재), criterion 헤딩 178 부재 | L1, L5, L7, L9, L93, L110, L154, L164, L386, L388 | 1, 5, 6, 9, 24, 25 | §4 참조 | §4의 의도된 outline 적용 | A/C |
| F11 | T16 | M | 2 | L11→L13, L87→L89 | 1, 5 | `#### Purpose`가 부모 `### A. INTRODUCTION`보다 앞, `#### Reason for Issuance`가 `### B. DISCUSSION`보다 앞 (xycut이 중앙정렬 제목보다 좌측 소제목을 먼저 배치) | 두 쌍 순서 교환 | A |
| F12 | T1 | M | 헤딩화된 표지 3줄, 장식 이미지 1, 표지 text box 2문단(1,061 chars) | L1, L3, L5, L7, L30, L32 | 1 | `# U.S. NUCLEAR REGULATORY COMMISSION`(H1), `###### Issue Date: April 2018 Technical Lead: Jan Mazza`(두 필드 병합). 표지 하단 박스(`Written suggestions…`, `Electronic copies…`)가 "Applicable Regulations" 하위 bullet 사이(L25와 L34 사이)에 삽입. 박스에 ADAMS ML17325A611 등 메타데이터 포함 | frontmatter로 이동(§5.3), 이미지 참조 삭제 | A |
| F13 | T2 | M | TOC 9 항목 / 1,362 chars; 1행에 3항목 병합 | L74–L84 (L79) | 4 | `- D. Implementation …… 20 Acronyms …… 22 References …… 24` | 삭제(헤딩이 구조 제공) | A |
| F14 | T5 | M | 본문 문장/목록 분할 13곳 | L34→L36, L99→L101, L105→L107→L110, L146→L148, L150→L152→L154→L156, L162→L164, L361→L363, L368→L374, L382→L384, L434→L440, L446→L448, L450→L452, L1103→L1109 | 2, 5–6, 8–9, 21–22, 23, 27–28, 104–105 | 예: L162 `…held on October` / L164 `- 11, 2016 (Ref. 23), to develop DG-1330…` (날짜가 목록 항목으로 분리); L105–L110 문단이 `- licensed under…`, `- 10 CFR 50.34(a)(3). NRC Policy on Advanced Reactors` 두 목록 항목으로 쪼개지고 헤딩까지 결합; L361 `…whether a` / L363 `- licensee intends…` | 명시 목록 기반 병합 | A |
| F15 | T11 | M | raw glyph 6줄, 하위 bullet 평탄화 4줄 | L23, L25, L34, L38, L150, L158; L40–L43 | 1–2, 8–9 | `•`(4), `o`(2)가 Markdown 목록으로 변환되지 않음; PDF의 `o` 하위 항목 L40–L43은 최상위 `- `로 변환되어 계층 소실; L54–L56, L170–L173, L226–L227 목록이 빈 줄로 끊김 | `•`→`- `, `o`→`    - `, 빈 줄 제거 | A |
| F16 | T6 | M | 약어 42개가 2개 문단 + H5 1개 | L382, L384, L386 | 23–24 | `AEC Atomic Energy Commission ANS American Nuclear Society …`가 한 문단; `FAUNA … (Research Facility for` / `Investigating Nuclear Aerosols)`에서 문단 분할; p24 단독 항목 `##### TRISO tristructural isotropic fuel` | PDF x좌표(약어 x = 72 pt, 풀이 x = 144 pt; 탭 정렬)로 2열 표 생성 | B |
| F17 | T6/T5 | M | 참고문헌 39개 중 구조 결함 4, 사이 삽입 각주 6 | L390–L462 (L434, L440, L446–L452) | 25–28 | Ref. 34가 fn 9에 의해 L434 / L440으로 분리, Ref. 37·38 보고서 번호 분할(F04), Ref. 38(L450)만 목록 기호 없음, fn 7–12가 참고문헌 사이에 끼어 있음 | 번호 목록 재구성 + `^ref-n` 앵커(본문 "(Ref. n)"과 연결) | A/C |
| F18 | T4 | L | 1 | L1113 | 105 | `Appendix B to RG 1.232, Rev. 0, Page B-2` (Appendix C 2쪽의 footer가 원문에서 B-2로 오기되어 header/footer 필터를 통과한 것으로 판단) | 삭제 | A |
| F19 | T14 | M | 1 | (L233 위치) | 13–20 | 표 제목 `TABLE 1: NON-LIGHT-WATER-REACTOR CROSSWALK`가 매 페이지 반복 헤더로 취급되어 전부 제거됨(md 0회). 본문 L190은 "Table 1: Non-Light-Water Reactor Crosswalk"를 참조 | 표 앞에 캡션 1회 추가 | A |
| F20 | T15 | M | — | — | 전체 | frontmatter 없음, 페이지 앵커 없음 → "B-20쪽" 같은 인용 불가. 쪽 번호 체계 4종(1–27, A-, B-, C-) | frontmatter(§5.3) + 재변환 시 `--markdown-page-separator "<!-- page %page-number% -->"`로 앵커, 인쇄 쪽 번호 매핑표 병기 | B |
| F21 | T13 | M | 15 italic run (3 × 5) | L538, L821, L1189 | 35, 70, 115 | GDC 19 rationale는 "(with emphasis added)"라고 명시하며 `actions can be taken`, `safely`, `controls`, `have certain knowledge`, `make decisions`를 italic으로 강조. md에서 강조가 사라져 "emphasis added"의 대상이 불명확(일부는 F02로 텍스트 자체도 누락) | `*…*`로 복원 | B |
| F22 | T13 | L | 5 | L15, L95, L390, L391, L444 | 1, 5, 25, 28 | "Code of Federal Regulations", "Annals of Nuclear Energy" italic 소실 | 선택적 복원 | B |
| F23 | T12 | L | 0 치명; bare URL 10, URL 내 `_` 쌍 2 | L440, L442 | 28 | `[[`, `#tag`, `$`, `==`, `%%`, `^`, HTML entity 모두 0. `2-3-_IAEAseminarMexicoCity_TSofu…`는 CommonMark 규칙상 강조로 해석될 위험 낮음 | URL을 `<…>`로 감싸기(선택) | A |
| F24 | T5 | L | 1 | L743 | 62 | Appendix B 서두의 `Column 1—Criterion Number Column 2—SFR-DC Title and Content Column 3—Staff Rationale…`가 한 문단(부록 A·C는 목록) | `Column \d—` 앞에서 목록 분리 | A |
| F25 | T99-1 | 정보 | 16 | §5.4 | — | 원문 오기(수정 금지): `(Criterion 1 – 15)` 등 | verbatim 유지, 필요 시 `<!-- sic -->` 주석만 | — |

### 1.1 Table 1 redline 셀 및 우측 열 누락 전체 목록 (PDF p14–18 렌더링 + 문자 색상 대조)

표기: A = ARDC 열, S = SFR-DC 열, M = MHTGR-DC 열. `~~x~~` = 빨강 취소선(삭제), `<ins>x</ins>` = 청색 밑줄(추가). "최종 제목"은 redline 적용 후 제목(해당 부록의 italic 제목과 일치 확인).

| Row | 열 | md line | md 현재 값 | PDF redline | 최종 제목 | 결함 유형 |
|---|---|---|---|---|---|---|
| 14 | A | L256 | Reactor coolant pressure boundary. | Reactor coolant ~~pressure~~ boundary. | Reactor coolant boundary. | 삭제어 잔존 |
| 14 | S | L256 | Primary coolant pressure boundary. | <ins>Primary</ins> coolant ~~pressure~~ boundary. | Primary coolant boundary. | 삭제어 잔존 |
| 14 | M | L256 | Reactor pressure boundary. | Reactor <ins>helium</ins> ~~coolant~~ pressure boundary. | Reactor helium pressure boundary. | 추가어·삭제어 누락 |
| 15 | S | L257 | Primary Reactor coolant system design. | <ins>Primary</ins> ~~Reactor~~ coolant system design. | Primary coolant system design. | 삭제어 잔존 |
| 15 | M | L257 | Reactor boundary | Reactor <ins>helium pressure boundary</ins> ~~coolant~~ design. | Reactor helium pressure boundary design. | 누락 (`helium pressure`, `coolant design.`) |
| 26 | A | L278 | Reactivity control systems redundancy and capacity | Reactivity control system<ins>s</ins> ~~redundancy and capacity~~ | Reactivity control systems | 삭제어 잔존 |
| 26 | M | L278 | Reactivity control system | Reactivity control system<ins>s</ins> | Reactivity control systems | 추가 `s` 누락 |
| 27 | A | L279 | Combined reactivity control systems capability DELETED and incorporated into ARDC 26 | ~~Combined reactivity control systems capability~~ DELETED and incorporated into ARDC 26 | (삭제) | 삭제어 잔존 |
| 30 | A | L287 | Quality of reactor coolant pressure boundary. | … coolant ~~pressure~~ boundary. | Quality of reactor coolant boundary. | 삭제어 잔존 |
| 30 | S | L287 | Quality of reactor primary coolant pressure boundary. | Quality of ~~reactor~~ <ins>primary</ins> coolant ~~pressure~~ boundary. | Quality of primary coolant boundary. | 삭제어 잔존 |
| 30 | M | L287 | Quality of reactor pressure boundary. | Quality of reactor <ins>helium</ins> ~~coolant~~ pressure boundary. | Quality of reactor helium pressure boundary. | 누락 (`helium coolant`) |
| 31 | A | L288 | Fracture prevention of reactor coolant pressure boundary. | … coolant ~~pressure~~ boundary. | Fracture prevention of reactor coolant boundary. | 삭제어 잔존 |
| 31 | S | L288 | Fracture prevention of reactor primary coolant pressure boundary. | … of ~~reactor~~ <ins>primary</ins> coolant ~~pressure~~ boundary. | Fracture prevention of primary coolant boundary. | 삭제어 잔존 |
| 31 | M | L288 | Fracture prevention of reactor helium coolant boundary. | … reactor <ins>helium</ins> ~~coolant~~ pressure boundary. | Fracture prevention of reactor helium pressure boundary. | 누락 (`pressure`) + 삭제어 잔존 |
| 32 | A | L289 | Inspection of reactor coolant pressure boundary. | … coolant ~~pressure~~ boundary. | Inspection of reactor coolant boundary. | 삭제어 잔존 |
| 32 | S | L289 | Inspection of reactor primary coolant pressure boundary. | … of ~~reactor~~ <ins>primary</ins> coolant ~~pressure~~ boundary. | Inspection of primary coolant boundary. | 삭제어 잔존 |
| 32 | M | L289 | Inspection of reactor coolant pressure boundary. | … reactor <ins>helium</ins> ~~coolant~~ pressure boundary. | Inspection of reactor helium pressure boundary. | 누락 (`helium`) + 삭제어 잔존 |
| 33 | A | L290 | Reactor coolant inventory maintenance makeup. | Reactor coolant <ins>inventory maintenance</ins> ~~makeup~~. | Reactor coolant inventory maintenance. | 삭제어 잔존 |
| 33 | S | L290 | Reactor Primary coolant inventory maintenance makeup. | ~~Reactor~~ <ins>Primary</ins> coolant <ins>inventory maintenance</ins> ~~makeup~~. | Primary coolant inventory maintenance. | 삭제어 잔존 |
| 34 | M | L291 | Residual heat removal. for MHTGR-DC | Residual heat removal. Modified for MHTGR-DC (redline 없음) | — (상태 "Modified") | 누락 (`Modified`) |
| 36 | M | L293 | Inspection of core cooling removal system. | Inspection of <ins>passive</ins> ~~emergency core cooling~~ <ins>residual heat removal</ins> system. | Inspection of passive residual heat removal system. | 누락 (`passive emergency`, `residual heat`) |
| 37 | M | L294 | Testing of passive residual heat removal emergency core cooling system. | Testing of <ins>passive residual heat removal</ins> ~~emergency core cooling~~ system. | Testing of passive residual heat removal system. | 삭제어 잔존 |
| 44 | A | L306 | Structural and equipment cooling. Cooling water | <ins>Structural and equipment cooling.</ins> ~~Cooling water~~ | Structural and equipment cooling. | 삭제어 잔존 |
| 44 | M | L306 | Structural and equipment cooling. Cooling water | (동일) | Structural and equipment cooling. | 삭제어 잔존 |
| 45 | A | L307 | Inspection of structural and equipment cooling water systems. | Inspection of <ins>structural and equipment</ins> cooling ~~water~~ systems. | Inspection of structural and equipment cooling systems. | 삭제어 잔존 |
| 46 | A | L308 | Testing of structural and equipment cooling water systems. | Testing of <ins>structural and equipment</ins> cooling ~~water~~ systems. | Testing of structural and equipment cooling systems. | 삭제어 잔존 |
| 55 | A | L319 | Reactor coolant pressure boundary penetrating containment. | Reactor coolant ~~pressure~~ boundary penetrating containment. | Reactor coolant boundary penetrating containment. | 삭제어 잔존 |
| 55 | S | L319 | Reactor Primary coolant pressure boundary penetrating containment. | ~~Reactor~~ <ins>Primary</ins> coolant ~~pressure~~ boundary penetrating containment. | Primary coolant boundary penetrating containment. | 삭제어 잔존 |
| 56 | A | L320 | Primary Containment isolation. | ~~Primary~~ Containment isolation. | Containment isolation. | 삭제어 잔존 |
| 56 | S | L320 | Primary Containment isolation. | ~~Primary~~ Containment isolation. | Containment isolation. | 삭제어 잔존 |
| 72 | M | L339 | Provisions for periodic reactor building inspection | Provisions for periodic reactor building inspection. (redline 없음) | — | 누락 (roman `.`; 재변환 diff에서 발견) |

(주: row 36·37 ARDC 셀의 `cooling-system`에 보이는 짧은 선은 텍스트층에 없는 도형이며 md `cooling system`은 텍스트층과 일치. 미확정 사항으로 기록.)

부록 rationale 열 누락 9 span: ARDC 19 (L538, p35) `safely…”`; SFR-DC 19 (L821, p70) `safely…”`, `have certain`, `make`; SFR-DC 55 (L989, p92) `addresses closed`; MHTGR-DC 19 (L1189, p115) `safely…”`; MHTGR-DC 34 (L1273, p125) `Refer to the`; MHTGR-DC 44 (L1305, p129) `Refer to the`; MHTGR-DC 46 (L1307, p129) `Refer to the`. 공통 패턴: /Rotate 90 페이지의 오른쪽 열에서 폰트 전환(italic↔roman, Calibri 공백 등)으로 새 텍스트 청크가 시작되고 그 시작점이 x = 613.8–700 pt(표시 좌표)인 경우. 동일 위치라도 청크가 612 pt 왼쪽에서 시작한 줄끝 단어는 보존됨(예 p129 `system` x = 676.7). 즉 `off-page` 필터가 회전 전 MediaBox 폭(612 pt)을 회전 후 좌표에 적용하는 것과 합치한다. `content_safety_off="off-page"` 재변환으로 20개 모두 복원됨을 확인(§2.7).

### 1.2 각주 참조 기호 결합 전체 목록 (PDF 7 pt 위첨자 검출 14개 = md 14개)

| fn | md line | md 현재 | PDF p. | 복원 형태 | Sev |
|---|---|---|---|---|---|
| 1 | L19 | `(Ref. 2)1.` | 1 | `(Ref. 2)[^1].` | H (참조 번호처럼 읽힘) |
| 2 | L123 | `Title 10 CFR 50.342 states:` | 7 | `Title 10 CFR 50.34[^2] states:` | H (허위 CFR 조항) |
| 3 | L140 | `information available.3 DOE determined` | 8 | `available.[^3] DOE` | M |
| 4 | L194 | `for developing PDC4. Since` | 11 | `for developing PDC[^4]. Since` | H (PDC 번호 충돌) |
| 5 | L351 | `applicants and licensees5 may use` | 21 | `licensees[^5]` | M |
| 6 | L355 | `may voluntarily6 use` | 21 | `voluntarily[^6]` | M |
| 7 | L388 | `### REFERENCES7` | 25 | `## REFERENCES[^7]` | M |
| 8 | L411 | `ML14353A248)8.` | 26 | `ML14353A248)[^8].` | M |
| 9 | L432 | `download.php?doc=77089 9` | 27 | `…doc=77089[^9]` | M |
| 10 | L440 | `sdc_report_2may2013.pdf 10.` | 28 | `….pdf[^10].` | M |
| 11 | L442 | `…SFRTechnologyOverview.pdf 11.` | 28 | `….pdf[^11].` | M |
| 12 | L444 | `…/pii/S030645491500580012.` | 28 | `…/pii/S0306454915005800[^12].` | H (URL 손상) |
| 13 | L737 | `loop-type designs.13 Applicants` | 62 | `designs.[^13] Applicants` | M |
| 14 | L1086 | `(MHTGR-DC).14 These` | 104 | `(MHTGR-DC).[^14] These` | M |

### 1.3 줄끝 하이픈 결합 전체 목록 (PDF 셀·문단 내 `A-␤B` 67쌍, 31형태 → md)

- 식별자·URL 손상 (H, 21): `SFR-DC` → `SFRDC` 13회 (L902, L903 ×1 `SFRDC17`, L909 ×2, L910, L917, L929, L938, L953, L954 ×2, L962, L1081; 원문 형태는 `SFR-DC 17`/`SFR-DC17`/`SFR-DC 34`/`SFR-DC 35`), `MHTGR-DC` → `MHTGRDC` 3회 (L190, L1225, L1299), `SECY-15-0002` → `SECY-150002` (L409), `SECY-94-084` → `SECY94-084` (L1225), `NUREG-1368` → `NUREG1368` (L903), `www.gen-4.org` → `www.gen4.org` (L440), `NPTDS-mexico` → `NPTDSmexico` (L442).
- 식별자 분할 (H, 2): `INL/EXT-10-17997` (L446/L448), `INL/EXT-11-22708` (L450/L452).
- 일반 합성어 (M, 45): `nonLWR(s)` 18 (L27, L127, L194, L198, L202, L204, L567, L682, L689, L690, L691, L698, L710, L711, L855, L903, L1225, L1231), `NonLWRs` 1 (L200), `NonLight` 3 (L164, L398, L1280), `preapplication` 3 (L154, L756, L1106), `sodiumcooled` 2 (L15, L467), `structurespecific` 2 (L681, L968), `leaktightness` 2 (L690, L976), `fireresistant` 2 (L769, L1126), `technologyspecific` (L140), `todiameter` (L176), `FacilitySpecific` (L427), `heatresistant` (L498), `lossof` (L732), `liquidmetal` (L792), `pressureretaining` (L800), `pressurizedwater` (L989), `RadioactiveWaste` (L1053), `MHTGRspecific` (L1154), `offnormal` (L1169), `safetyrelated` (L1231).
- em dash 소실 (M, 1): L136 `technologiesspecifically` ← `technologies—specifically`.
- 판정 근거: PDF 전체에서 결합형(무하이픈)이 줄 중간에 나타나는 사례 0건, 하이픈형은 해당 형태 대부분이 다수 존재(예 `non-LWR` 81회). NRC 문서는 자동 음절 하이픈을 쓰지 않으므로 67쌍 전부 실제 하이픈으로 판정.
- 수정 금지(원문): L123 `watercooled`(p7 텍스트층·렌더링 모두 무하이픈), L498 `fire- resistant`(p31 원문에 공백 포함).

## 2. Table verification log

검증 범위: 논리 표 4개, md 블록 123개 전부(> 30이므로 전 다중 페이지 표를 전수 검사). 방법: (a) `rg_blocks.py` — 각 md 블록과 같은 순번의 PDF 표를 pdfplumber로 추출하여 criterion ID 순서 비교(123/123 일치, 행 누락 0, 열 누락 0); (b) `rg_crit.py` — criterion별로 페이지 분할 조각을 병합한 뒤 PDF와 md의 Column 2·3 텍스트를 단어 수준 diff(하이픈·공백 정규화); (c) `rg_celldiff.py` — Table 1 셀 diff; (d) p13–18, 63–65, 81 렌더링 육안 확인(redline, italic, 문단). 숫자 표는 없음(모든 표가 서술형 텍스트 표).

모든 123개 블록에 공통 결함: T6(section label이 헤더 행, 실제 헤더가 본문 행으로 반복). 아래 Status 열은 공통 결함 외의 추가 결함만 표시한다.

### 2.1 블록별 로그 (123)

| Table ID | md lines | PDF p. | Section / criteria | Status (추가 결함) | Notes |
|---|---|---|---|---|---|
| T1-01 | L234–241 | 13 | I. Overall Requirements / crit. 1–5 | OK | — |
| T1-02 | L244–250 | 13 | II. Multiple Barriers / crit. 10–13 | OK | — |
| T1-03 | L253–261 | 14 | II. Multiple Barriers / crit. 14–19 | T13(redline lost), T14(lost words) | redline 셀: 14(A,S,M), 15(S,M); MHTGR-14 `helium coolant` 누락; MHTGR-15 `helium pressure`, `coolant design.` 누락 |
| T1-04 | L264–269 | 14 | III. Reactivity Control / crit. 20–22 | OK | — |
| T1-05 | L272–281 | 15 | III. Reactivity Control / crit. 23–29 | T13(redline lost), T14(lost words) | redline 셀: 26(A,M), 27(A); MHTGR-26 `s` 누락 |
| T1-06 | L284–295 | 16 | IV. Fluid Systems (Heat Transport Systems for MHTGRs) / crit. 30–38 | T13(redline lost), T14(lost words) | redline 셀: 30(A,S,M), 31(A,S,M), 32(A,S,M), 33(A,S), 36(M), 37(M); MHTGR-30 `helium coolant` 누락; MHTGR-31 `pressure` 누락; MHTGR-32 `helium` 누락; MHTGR-34 `Modified` 누락; MHTGR-36 `passive emergency`, `residual heat` 누락 |
| T1-07 | L298–308 | 17 | IV. Fluid Systems (Heat Transport Systems for MHTGRs) / crit. 39–46 | T13(redline lost) | redline 셀: 44(A,M), 45(A), 46(A) |
| T1-08 | L311–321 | 18 | V. Reactor Containment / crit. 50–57 | T13(redline lost) | redline 셀: 55(A,S), 56(A,S) |
| T1-09 | L324–331 | 19 | VI. Fuel and Radioactivity Control / crit. 60–64 | OK | — |
| T1-10 | L334–346 | 20 | VII. Additional Technology-Specific Design Criteria / crit. 70–79 | T14(lost words) | MHTGR-72 마침표 `.` 누락 |
| A-01 | L488–492 | 30 | I. Overall Requirements / crit. 1–2 | OK | — |
| A-02 | L495–500 | 31 | I. Overall Requirements / crit. 3–5 | OK | — |
| A-03 | L503–506 | 32 | I. Overall Requirements / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 5의 연속 |
| A-04 | L509–514 | 32 | II. Multiple Barriers / crit. 10–12 | OK | — |
| A-05 | L517–523 | 33 | II. Multiple Barriers / crit. 13–16 | OK | — |
| A-06 | L526–530 | 34 | II. Multiple Barriers / crit. 17–17 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 16의 연속 |
| A-07 | L533–538 | 35 | II. Multiple Barriers / crit. 18–19 | T6(continuation row, empty key), T14(lost words) | cont. row = 앞 블록 criterion 17의 연속; ARDC 19 rationale `safely…”` 누락 |
| A-08 | L541–544 | 36 | II. Multiple Barriers / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 19의 연속 |
| A-09 | L547–552 | 37 | III. Reactivity Control / crit. 20–22 | OK | — |
| A-10 | L555–561 | 38 | III. Reactivity Control / crit. 23–25 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 22의 연속 |
| A-11 | L564–567 | 39 | III. Reactivity Control / crit. 26–26 | OK | — |
| A-12 | L570–573 | 40 | III. Reactivity Control / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 26의 연속 |
| A-13 | L576–579 | 41 | III. Reactivity Control / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 26의 연속 |
| A-14 | L582–587 | 42 | III. Reactivity Control / crit. 27–28 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 26의 연속 |
| A-15 | L590–594 | 43 | III. Reactivity Control / crit. 29–29 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 28의 연속 |
| A-16 | L597–601 | 43 | IV. Fluid Systems / crit. 30–31 | OK | — |
| A-17 | L604–609 | 44 | IV. Fluid Systems / crit. 32–33 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 31의 연속 |
| A-18 | L612–616 | 45 | IV. Fluid Systems / crit. 34–34 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 33의 연속 |
| A-19 | L619–623 | 46 | IV. Fluid Systems / crit. 35–35 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 34의 연속 |
| A-20 | L626–630 | 47 | IV. Fluid Systems / crit. 36–36 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 35의 연속 |
| A-21 | L633–637 | 48 | IV. Fluid Systems / crit. 37–37 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 36의 연속 |
| A-22 | L640–644 | 49 | IV. Fluid Systems / crit. 38–38 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 37의 연속 |
| A-23 | L647–652 | 50 | IV. Fluid Systems / crit. 39–41 | OK | — |
| A-24 | L655–660 | 51 | IV. Fluid Systems / crit. 42–43 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 41의 연속 |
| A-25 | L663–669 | 52 | IV. Fluid Systems / crit. 44–46 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 43의 연속 |
| A-26 | L672–675 | 53 | IV. Fluid Systems / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 46의 연속 |
| A-27 | L678–682 | 54 | V. Reactor Containment / crit. 50–51 | OK | — |
| A-28 | L685–691 | 55 | V. Reactor Containment / crit. 52–54 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 51의 연속 |
| A-29 | L694–698 | 56 | V. Reactor Containment / crit. 55–55 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 54의 연속 |
| A-30 | L701–704 | 57 | V. Reactor Containment / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 55의 연속 |
| A-31 | L707–711 | 58 | V. Reactor Containment / crit. 56–57 | OK | — |
| A-32 | L714–717 | 59 | V. Reactor Containment / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 57의 연속 |
| A-33 | L720–725 | 60 | VI. Fuel and Radioactivity Control / crit. 60–62 | OK | — |
| A-34 | L728–732 | 61 | VI. Fuel and Radioactivity Control / crit. 63–64 | OK | — |
| B-01 | L759–763 | 63 | I. Overall Requirements / crit. 1–2 | OK | — |
| B-02 | L766–770 | 64 | I. Overall Requirements / crit. 3–4 | OK | — |
| B-03 | L773–777 | 65 | I. Overall Requirements / crit. 5–5 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 4의 연속 |
| B-04 | L780–784 | 65 | II. Multiple Barriers / crit. 10–11 | OK | — |
| B-05 | L787–793 | 66 | II. Multiple Barriers / crit. 12–14 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 11의 연속 |
| B-06 | L796–800 | 67 | II. Multiple Barriers / crit. 15–16 | OK | — |
| B-07 | L803–807 | 68 | II. Multiple Barriers / crit. 17–17 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 16의 연속 |
| B-08 | L810–814 | 69 | II. Multiple Barriers / crit. 18–18 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 17의 연속 |
| B-09 | L817–821 | 70 | II. Multiple Barriers / crit. 19–19 | T6(continuation row, empty key), T14(lost words) | cont. row = 앞 블록 criterion 18의 연속; SFR-DC 19 rationale `safely…”`, `have certain`, `make` 누락 |
| B-10 | L824–827 | 71 | II. Multiple Barriers / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 19의 연속 |
| B-11 | L830–834 | 72 | III. Reactivity Control / crit. 20–21 | OK | — |
| B-12 | L837–842 | 73 | III. Reactivity Control / crit. 22–24 | OK | — |
| B-13 | L845–849 | 74 | III. Reactivity Control / crit. 25–26 | OK | — |
| B-14 | L852–855 | 75 | III. Reactivity Control / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 26의 연속 |
| B-15 | L858–861 | 76 | III. Reactivity Control / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 26의 연속 |
| B-16 | L864–867 | 77 | III. Reactivity Control / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 26의 연속 |
| B-17 | L870–875 | 78 | III. Reactivity Control / crit. 27–29 | OK | — |
| B-18 | L878–881 | 78 | IV. Fluid Systems / crit. 30–30 | OK | — |
| B-19 | L884–889 | 79 | IV. Fluid Systems / crit. 31–32 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 30의 연속 |
| B-20 | L892–896 | 80 | IV. Fluid Systems / crit. 33–33 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 32의 연속 |
| B-21 | L899–903 | 81 | IV. Fluid Systems / crit. 34–34 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 33의 연속 |
| B-22 | L906–910 | 82 | IV. Fluid Systems / crit. 35–36 | OK | — |
| B-23 | L913–917 | 83 | IV. Fluid Systems / crit. 37–37 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 36의 연속 |
| B-24 | L920–923 | 84 | IV. Fluid Systems / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 37의 연속 |
| B-25 | L926–932 | 85 | IV. Fluid Systems / crit. 38–40 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 37의 연속 |
| B-26 | L935–939 | 86 | IV. Fluid Systems / crit. 41–41 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 40의 연속 |
| B-27 | L942–947 | 87 | IV. Fluid Systems / crit. 42–43 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 41의 연속 |
| B-28 | L950–956 | 88 | IV. Fluid Systems / crit. 44–46 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 43의 연속 |
| B-29 | L959–962 | 89 | IV. Fluid Systems / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 46의 연속 |
| B-30 | L965–968 | 89 | V. Reactor Containment / crit. 50–50 | OK | — |
| B-31 | L971–977 | 90 | V. Reactor Containment / crit. 51–54 | OK | — |
| B-32 | L980–983 | 91 | V. Reactor Containment / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 54의 연속 |
| B-33 | L986–989 | 92 | V. Reactor Containment / crit. 55–55 | T14(lost words) | SFR-DC 55 rationale `addresses closed` 누락 |
| B-34 | L992–997 | 93 | V. Reactor Containment / crit. 56–57 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 55의 연속 |
| B-35 | L1000–1003 | 94 | V. Reactor Containment / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 57의 연속 |
| B-36 | L1006–1009 | 94 | VI. Fuel and Reactivity Control / crit. 60–60 | OK | — |
| B-37 | L1012–1018 | 95 | VI. Fuel and Reactivity Control / crit. 61–64 | OK | — |
| B-38 | L1021–1024 | 96 | VI. Fuel and Reactivity Control / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 64의 연속 |
| B-39 | L1027–1030 | 96 | VII. Additional SFR-DC / crit. 70–70 | OK | — |
| B-40 | L1033–1038 | 97 | VII. Additional SFR-DC / crit. 71–72 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 70의 연속 |
| B-41 | L1041–1047 | 98 | VII. Additional SFR-DC / crit. 73–75 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 72의 연속 |
| B-42 | L1050–1055 | 99 | VII. Additional SFR-DC / crit. 76–77 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 75의 연속 |
| B-43 | L1058–1062 | 100 | VII. Additional SFR-DC / crit. 78–78 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 77의 연속 |
| B-44 | L1065–1068 | 101 | VII. Additional SFR-DC / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 78의 연속 |
| B-45 | L1071–1075 | 102 | VII. Additional SFR-DC / crit. 79–79 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 78의 연속 |
| B-46 | L1078–1081 | 103 | VII. Additional SFR-DC / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 79의 연속 |
| C-01 | L1115–1119 | 106 | I. Overall Requirements / crit. 1–2 | OK | — |
| C-02 | L1122–1127 | 107 | I. Overall Requirements / crit. 3–4 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 2의 연속 |
| C-03 | L1130–1134 | 108 | I. Overall Requirements / crit. 5–5 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 4의 연속 |
| C-04 | L1137–1140 | 108 | II. Multiple Barriers / crit. 10–10 | OK | — |
| C-05 | L1143–1146 | 109 | II. Multiple Barriers / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 10의 연속 |
| C-06 | L1149–1155 | 110 | II. Multiple Barriers / crit. 11–13 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 10의 연속 |
| C-07 | L1158–1163 | 111 | II. Multiple Barriers / crit. 14–16 | OK | — |
| C-08 | L1166–1169 | 112 | II. Multiple Barriers / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 16의 연속 |
| C-09 | L1172–1176 | 113 | II. Multiple Barriers / crit. 17–17 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 16의 연속 |
| C-10 | L1179–1183 | 114 | II. Multiple Barriers / crit. 18–18 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 17의 연속 |
| C-11 | L1186–1189 | 115 | II. Multiple Barriers / crit. 19–19 | T14(lost words) | MHTGR-DC 19 rationale `safely…”` 누락 |
| C-12 | L1192–1195 | 116 | II. Multiple Barriers / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 19의 연속 |
| C-13 | L1198–1202 | 116 | III. Reactivity Control / crit. 20–21 | OK | — |
| C-14 | L1205–1211 | 117 | III. Reactivity Control / crit. 22–24 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 21의 연속 |
| C-15 | L1214–1219 | 118 | III. Reactivity Control / crit. 25–26 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 24의 연속 |
| C-16 | L1222–1225 | 119 | III. Reactivity Control / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 26의 연속 |
| C-17 | L1228–1231 | 120 | III. Reactivity Control / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 26의 연속 |
| C-18 | L1234–1237 | 121 | III. Reactivity Control / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 26의 연속 |
| C-19 | L1240–1246 | 122 | III. Reactivity Control / crit. 27–29 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 26의 연속 |
| C-20 | L1249–1252 | 123 | III. Reactivity Control / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 29의 연속 |
| C-21 | L1255–1259 | 123 | IV. Heat Transport Systems / crit. 30–31 | OK | — |
| C-22 | L1262–1267 | 124 | IV. Heat Transport Systems / crit. 32–33 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 31의 연속 |
| C-23 | L1270–1273 | 125 | IV. Heat Transport Systems / crit. 34–34 | T14(lost words) | MHTGR-DC 34 rationale `Refer to the` 누락 |
| C-24 | L1276–1281 | 126 | IV. Heat Transport Systems / crit. 35–37 | OK | — |
| C-25 | L1284–1289 | 127 | IV. Heat Transport Systems / crit. 38–39 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 37의 연속 |
| C-26 | L1292–1299 | 128 | IV. Heat Transport Systems / crit. 40–44 | OK | — |
| C-27 | L1302–1307 | 129 | IV. Heat Transport Systems / crit. 45–46 | T6(continuation row, empty key), T14(lost words) | cont. row = 앞 블록 criterion 44의 연속; MHTGR-DC 44 rationale `Refer to the` 누락; MHTGR-DC 46 rationale `Refer to the` 누락 |
| C-28 | L1310–1318 | 130 | V. Reactor Containment / crit. 50–55 | OK | — |
| C-29 | L1321–1326 | 131 | V. Reactor Containment / crit. 56–57 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 55의 연속 |
| C-30 | L1329–1333 | 131 | VI. Fuel and Reactivity Control / crit. 60–61 | OK | — |
| C-31 | L1336–1342 | 132 | VI. Fuel and Reactivity Control / crit. 62–64 | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 61의 연속 |
| C-32 | L1345–1348 | 133 | VI. Fuel and Reactivity Control / crit. — | T6(continuation row, empty key) | cont. row = 앞 블록 criterion 64의 연속 |
| C-33 | L1351–1356 | 133 | VII. Additional MHTGR-DC / crit. 70–72 | OK | — |

### 2.2 Appendix B (SFR-DC) criterion별 무결성 표 (65 criteria 전수)

열 설명: Title = PDF italic run(제목); Status = 부록 B 상태행 또는 Table 1 SFR-DC 열(Modified = "Modified for SFR-DC", New = Additional SFR-DC 70–79); md blocks = 해당 criterion이 걸친 md 표 블록 수; Mid-sentence split = 페이지 경계에서 문장 중간 분할(text = 기준 본문, rat. = NRC rationale, ×n = 횟수); Lost text = PDF 대비 md 누락; Notes = 기준 본문 위치 및 문단 구분(PDF 문단 수 → md 문단 수).

요약: 65개 중 26개가 2개 이상 블록에 분산(3블록 2개, 4블록 1개), 15개가 문장 중간 분할(본문 11, rationale 10), 2개(SFR-DC 18, 40)는 기준 본문 전체가 번호 없는 연속행에만 존재, 2개(19, 55)에 텍스트 누락(4 span), 4개(16, 26, 34, 78)는 문단 구분 축소. 나머지 단어 내용은 PDF와 일치(하이픈 결합 제외: SFRDC 13건 등은 §1.3). 표의 Section VII은 70–79를 포함하나 서두(L753, p62)는 "Criteria 70–77"로 기재(원문 오기).

| SFR-DC | Title (PDF italic) | Status | PDF p. | md lines | md blocks | Mid-sentence split | Lost text | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | Quality standards and records. | Same as GDC | 63 | L762 | — | — | — | — |
| 2 | Design bases for protection against natural phenomena. | Same as GDC | 63 | L763 | — | — | — | — |
| 3 | Fire protection. | Same as ARDC | 64 | L769 | — | — | — | — |
| 4 | Environmental and dynamic effects design bases. | Modified | 64,65 | L770,L776 | 2 blocks | — | — | 기준 본문 마지막 문단(`Chemical consequences of accidents…`)이 연속행 L776에 분리(문단 경계) |
| 5 | Sharing of structures, systems, and components. | Same as GDC | 65 | L777 | — | — | — | — |
| 10 | Reactor design. | Same as GDC | 65 | L783 | — | — | — | — |
| 11 | Reactor inherent protection. | Same as ARDC | 65,66 | L784,L790 | 2 blocks | text×1 | — | — |
| 12 | Suppression of reactor power oscillations. | Same as ARDC | 66 | L791 | — | — | — | — |
| 13 | Instrumentation and control. | Modified | 66 | L792 | — | — | — | — |
| 14 | Primary coolant boundary. | Modified | 66 | L793 | — | — | — | — |
| 15 | Primary coolant system design. | Modified | 67 | L799 | — | — | — | — |
| 16 | Containment design. | Modified | 67,68 | L800,L806 | 2 blocks | — | — | text ¶ 2→1 |
| 17 | Electric power systems. | Same as ARDC | 68,69 | L807,L813 | 2 blocks | text×1, rat.×1 | — | — |
| 18 | Inspection and testing of electric power systems. ⟨status line also italic⟩ | Same as ARDC | 69,70 | L814,L820 | 2 blocks | — | — | criterion body only in continuation row |
| 19 | Control room. | Modified | 70,71 | L821,L827 | 2 blocks | rat.×1 | `safely…”`, `have certain`, `make` (rationale) | — |
| 20 | Protection system functions. | Same as GDC | 72 | L833 | — | — | — | — |
| 21 | Protection system reliability and testability. | Same as GDC | 72 | L834 | — | — | — | — |
| 22 | Protection system independence. | Same as GDC | 73 | L840 | — | — | — | — |
| 23 | Protection system failure modes. | Modified | 73 | L841 | — | — | — | — |
| 24 | Separation of protection and control systems. | Same as GDC | 73 | L842 | — | — | — | — |
| 25 | Protection system requirements for reactivity control malfunctions. | Same as ARDC | 74 | L848 | — | — | — | — |
| 26 | Reactivity control systems. | Same as ARDC | 74,75,76,77 | L849,L855,L861,L867 | 4 blocks | rat.×2 | — | text ¶ 5→4 |
| 27 | Combined reactivity control systems capability. | Same as ARDC | 78 | L873 | — | — | — | — |
| 28 | Reactivity limits. | Modified | 78 | L874 | — | — | — | — |
| 29 | Protection against anticipated operational occurrences. | Same as GDC | 78 | L875 | — | — | — | — |
| 30 | Quality of primary coolant boundary. | Modified | 78,79 | L881,L887 | 2 blocks | — | — | — |
| 31 | Fracture prevention of primary coolant boundary. | Modified | 79 | L888 | — | — | — | — |
| 32 | Inspection of primary coolant boundary. | Modified | 79,80 | L889,L895 | 2 blocks | — | — | — |
| 33 | Primary coolant inventory maintenance. | Modified | 80,81 | L896,L902 | 2 blocks | — | — | — |
| 34 | Residual heat removal. | Modified | 81 | L903 | — | — | — | text ¶ 2→1 |
| 35 | Emergency core cooling. | Same as ARDC | 82 | L909 | — | — | — | — |
| 36 | Inspection of emergency core cooling system. | Same as ARDC | 82,83 | L910,L916 | 2 blocks | rat.×1 | — | — |
| 37 | Testing of emergency core cooling system. | Same as ARDC | 83,84,85 | L917,L923,L929 | 3 blocks | text×1, rat.×1 | — | — |
| 38 | Containment heat removal. | Same as ARDC | 85 | L930 | — | — | — | — |
| 39 | Inspection of containment heat removal system | Same as ARDC | 85 | L931 | — | — | — | — |
| 40 | Testing of containment heat removal system. | Same as ARDC | 85,86 | L932,L938 | 2 blocks | rat.×1 | — | criterion body only in continuation row |
| 41 | Containment atmosphere cleanup. | Same as ARDC | 86,87 | L939,L945 | 2 blocks | — | — | — |
| 42 | Inspection of containment atmosphere cleanup systems. | Same as GDC | 87 | L946 | — | — | — | — |
| 43 | Testing of containment atmosphere cleanup systems. | Same as ARDC | 87,88 | L947,L953 | 2 blocks | — | — | — |
| 44 | Structural and equipment cooling | Same as ARDC | 88 | L954 | — | — | — | — |
| 45 | Inspection of structural and equipment cooling systems. | Same as ARDC | 88 | L955 | — | — | — | — |
| 46 | Testing of structural and equipment cooling systems. | Same as ARDC | 88,89 | L956,L962 | 2 blocks | — | — | — |
| 50 | Containment design basis. | Modified | 89 | L968 | — | — | — | — |
| 51 | Fracture prevention of containment pressure boundary. | Modified | 90 | L974 | — | — | — | — |
| 52 | Capability for containment leakage rate testing | Modified | 90 | L975 | — | — | — | — |
| 53 | Provisions for containment testing and inspection. | Modified | 90 | L976 | — | — | — | — |
| 54 | Piping systems penetrating containment. | Modified | 90,91 | L977,L983 | 2 blocks | text×1, rat.×1 | — | — |
| 55 | Primary coolant boundary penetrating containment. | Modified | 92,93 | L989,L995 | 2 blocks | text×1 | `addresses closed` (rationale) | — |
| 56 | Containment isolation. | Modified | 93 | L996 | — | — | — | — |
| 57 | Closed system isolation valves. | Modified | 93,94 | L997,L1003 | 2 blocks | text×1, rat.×1 | — | — |
| 60 | Control of releases of radioactive materials to the environment. | Same as GDC | 94 | L1009 | — | — | — | — |
| 61 | Fuel storage and handling and radioactivity control. | Same as ARDC | 95 | L1015 | — | — | — | — |
| 62 | Prevention of criticality in fuel storage and handling. | Same as GDC | 95 | L1016 | — | — | — | — |
| 63 | Monitoring fuel and waste storage. | Same as GDC | 95 | L1017 | — | — | — | — |
| 64 | Monitoring radioactivity releases. | Modified | 95,96 | L1018,L1024 | 2 blocks | text×1 | — | — |
| 70 | Intermediate coolant system. | New | 96,97 | L1030,L1036 | 2 blocks | — | — | — |
| 71 | Primary coolant and cover gas purity control. | New | 97 | L1037 | — | — | — | — |
| 72 | Sodium heating systems. | New | 97,98 | L1038,L1044 | 2 blocks | text×1 | — | — |
| 73 | Sodium leakage detection and reaction prevention and mitigation | New | 98 | L1045 | — | — | — | — |
| 74 | Sodium/water reaction prevention/mitigation. | New | 98 | L1046 | — | — | — | — |
| 75 | Quality of the intermediate coolant boundary. | New | 98,99 | L1047,L1053 | 2 blocks | text×1, rat.×1 | — | — |
| 76 | Fracture prevention of the intermediate coolant boundary. | New | 99 | L1054 | — | — | — | — |
| 77 | Inspection of the intermediate coolant boundary. | New | 99,100 | L1055,L1061 | 2 blocks | text×1 | — | — |
| 78 | Primary Coolant System Interfaces | New | 100,101,102 | L1062,L1068,L1074 | 3 blocks | text×1, rat.×2 | — | text ¶ 5→4 |
| 79 | Cover gas inventory maintenance. | New | 102,103 | L1075,L1081 | 2 blocks | — | — | — |

### 2.3 Appendix A (ARDC) — 결함 있는 criterion만 (55개 중 20개)

요약: 20개 분산(4블록 1개: ARDC 26), 15개 문장 중간 분할(본문 9, rationale 11), 1개(ARDC 5) 기준 본문이 연속행에만 존재, 1개(ARDC 19) 텍스트 누락. 나머지 35개는 단일 행·단어 일치. 서두 L480–L482 "(Criterion 1 – 15)", "(Criterion 10 – 20)", "(Criterion 21 – 29)"는 원문 그대로(p29).

| ARDC | Title (PDF italic) | Status | PDF p. | md lines | md blocks | Mid-sentence split | Lost text | Notes |
|---|---|---|---|---|---|---|---|---|
| 5 | Sharing of structures, systems, and components. | Same as GDC | 31,32 | L500,L506 | 2 blocks | — | — | criterion body only in continuation row |
| 16 | Containment design. | Same as GDC | 33,34 | L523,L529 | 2 blocks | rat.×1 | — | — |
| 17 | Electric power systems. | Modified | 34,35 | L530,L536 | 2 blocks | rat.×1 | — | — |
| 19 | Control room. | Modified | 35,36 | L538,L544 | 2 blocks | text×1, rat.×1 | `safely…”` (rationale quote truncated) | — |
| 22 | Protection system independence. | Same as GDC | 37,38 | L552,L558 | 2 blocks | text×1 | — | — |
| 26 | Reactivity control systems. | Modified | 39,40,41,42 | L567,L573,L579,L585 | 4 blocks | rat.×3 | — | text ¶ 5→2 |
| 28 | Reactivity limits. | Modified | 42,43 | L587,L593 | 2 blocks | text×1 | — | — |
| 31 | Fracture prevention of reactor coolant boundary. | Modified | 43,44 | L601,L607 | 2 blocks | text×1 | — | — |
| 33 | Reactor coolant inventory maintenance. | Modified | 44,45 | L609,L615 | 2 blocks | rat.×1 | — | — |
| 34 | Residual heat removal. | Modified | 45,46 | L616,L622 | 2 blocks | — | — | — |
| 35 | Emergency core cooling system. | Modified | 46,47 | L623,L629 | 2 blocks | rat.×1 | — | — |
| 36 | Inspection of emergency core cooling system. | Modified | 47,48 | L630,L636 | 2 blocks | — | — | — |
| 37 | Testing of emergency core cooling system. | Modified | 48,49 | L637,L643 | 2 blocks | — | — | — |
| 41 | Containment atmosphere cleanup. | Modified | 50,51 | L652,L658 | 2 blocks | text×1 | — | — |
| 43 | Testing of containment atmosphere cleanup systems. | Modified | 51,52 | L660,L666 | 2 blocks | — | — | — |
| 46 | Testing of structural and equipment cooling systems. | Modified | 52,53 | L669,L675 | 2 blocks | text×1, rat.×1 | — | — |
| 51 | Fracture prevention of containment pressure boundary. | Modified | 54,55 | L682,L688 | 2 blocks | rat.×1 | — | — |
| 54 | Piping systems penetrating containment. | Modified | 55,56 | L691,L697 | 2 blocks | text×1, rat.×1 | — | — |
| 55 | Reactor coolant boundary penetrating containment. | Modified | 56,57 | L698,L704 | 2 blocks | text×1, rat.×1 | — | — |
| 57 | Closed system isolation valves. | Modified | 58,59 | L711,L717 | 2 blocks | text×1, rat.×1 | — | — |

### 2.4 Appendix C (MHTGR-DC) — 결함 있는 criterion만 (58개 중 18개)

요약: 16개 분산(3블록 2개, 5블록 1개: MHTGR-DC 26), 13개 문장 중간 분할(본문 7, rationale 8), 2개(24, 61) 기준 본문이 연속행에만 존재, 4개(19, 34, 44, 46) 텍스트 누락. Status 중 34는 Table 1 셀에서 "Modified"가 누락(F02)되어 md만으로는 판정 불가였으며 PDF 기준 "Modified"로 기재.

| MHTGR-DC | Title (PDF italic) | Status | PDF p. | md lines | md blocks | Mid-sentence split | Lost text | Notes |
|---|---|---|---|---|---|---|---|---|
| 2 | Design bases for protection against natural phenomena. | Same as GDC | 106,107 | L1119,L1125 | 2 blocks | text×1 | — | — |
| 4 | Environmental and dynamic effects design bases. | Modified | 107,108 | L1127,L1133 | 2 blocks | text×1, rat.×1 | — | — |
| 10 | Reactor design. | Modified | 108,109,110 | L1140,L1146,L1152 | 3 blocks | rat.×1 | — | — |
| 16 | Containment design. | Modified | 111,112,113 | L1163,L1169,L1175 | 3 blocks | rat.×1 | — | — |
| 17 | Electric power systems. | Modified | 113,114 | L1176,L1182 | 2 blocks | rat.×1 | — | — |
| 19 | Control room. | Same as ARDC | 115,116 | L1189,L1195 | 2 blocks | — | `safely…”` | — |
| 21 | Protection system reliability and testability. | Same as GDC | 116,117 | L1202,L1208 | 2 blocks | text×1 | — | — |
| 24 | Separation of protection and control systems. | Same as GDC | 117,118 | L1211,L1217 | 2 blocks | — | — | criterion body only in continuation row |
| 26 | Reactivity control systems. | Modified | 118,119,120,121,122 | L1219,L1225,L1231,L1237,L1243 | 5 blocks | text×1, rat.×3 | — | text ¶ 6→4 |
| 29 | Protection against anticipated operational occurrences. | Same as GDC | 122,123 | L1246,L1252 | 2 blocks | text×1 | — | — |
| 31 | Fracture prevention of reactor helium pressure boundary. | Modified | 123,124 | L1259,L1265 | 2 blocks | text×1 | — | — |
| 34 | Passive residual heat removal. | Modified | 125 | L1273 | — | — | `Refer to the` | — |
| 37 | Testing of passive residual heat removal system | Modified | 126,127 | L1281,L1287 | 2 blocks | rat.×1 | — | — |
| 44 | Structural and equipment cooling. | Modified | 128,129 | L1299,L1305 | 2 blocks | text×1 | `Refer to the` | text ¶ 3→2 |
| 46 | Testing of structural and equipment cooling systems. | Same as ARDC | 129 | L1307 | — | — | `Refer to the` | — |
| 55 | Reactor coolant boundary penetrating containment. | Not applicable to MHTGR | 130,131 | L1318,L1324 | 2 blocks | rat.×1 | — | — |
| 61 | Fuel storage and handling and radioactivity control. | Same as ARDC | 131,132 | L1333,L1339 | 2 blocks | — | — | criterion body only in continuation row |
| 64 | Monitoring radioactivity releases. | Modified | 132,133 | L1342,L1348 | 2 blocks | rat.×1 | — | — |

### 2.5 Table 1 (Crosswalk) 요약

| Table ID | md lines | PDF p. | Status | Notes |
|---|---|---|---|---|
| Table 1 (10 blocks) | L234–L346 | 13–20 | T6, T13, T14 | 65 rows × 5 cols 모두 존재(행·열 누락 0). 캡션 누락(F19). redline 29 셀 오기, 우측 열 누락 9 셀 11 span(§1.1; `off-page` 재변환으로 복원). 모든 비-"Same as" 셀이 `제목. Modified for X` 한 문자열(F07). trailing `<br><br>` 17개. VII section에 78·79 행 존재(서두 L231 "Criteria 70–77"은 원문 오기) |

### 2.6 비표 본문 누락 검사

`rg_body.py`로 p1–12, 21–29, 62, 104–105의 비표 텍스트 전체(표 bbox 제외, header/footer 제외)를 md 비표 토큰과 정렬했다. 차이는 6건뿐이다: `Purpose`/`B. DISCUSSION` 순서(F11), `o` glyph 4개 제거(F15), `technologies— specifically`(F05), `INL/EXT-` 분할 2건(F04), footer 1건(F18). 즉 본문 문단 누락은 0이다. 표본 확인(정렬 결과 verbatim 일치): L15 Purpose 문단, L64 Purpose of RGs, L95 NRC Regulatory Framework, L113 Advanced Reactor Policy, L127 Role of GDC for non-LWRs 둘째 문단, L184 Harmonization, L355 Use by Applicants, L467 Appendix A 서두, L737 Appendix B 서두, L1086 Appendix C 서두(10개). 페이지 경계 문단(L99→L101, L368→L374, L162→L164)은 내용 완전·구조만 분할(F14).

### 2.7 재변환 검증 (coordinator 요청: landscape `off-page` 필터 가설)

사실관계: pypdf 기준 133쪽 중 109쪽이 `/Rotate 90`, MediaBox (0,0,612,792) — p13–20(Table 1), p30–61, p63–103, p106–133(부록 표). 세로 24쪽(p1–12, 21–29, 62, 104, 105)에서는 누락 0.

실행(모두 스크래치패드 하위 폴더, `references/`에는 쓰지 않음; JDK 17 PATH 설정 후 Python API):

| Run | 옵션 | 출력 | 규모 |
|---|---|---|---|
| R0 (현행) | 기본 | `references/RG_1.232.md` | 1,359 lines, 309,747 chars, 표 블록 123, `<br>` 706 |
| R1 | `content_safety_off="off-page"`, `markdown_page_separator="<!-- page %page-number% -->"`, `image_output="off"` | `scratchpad/reconv_offpage/RG_1.232.md` | 1,623 lines, 312,345 chars, 표 블록 123, `<br>` 704, page separator 133 |
| R2 | R1 + `detect_strikethrough=True` | `scratchpad/reconv_offpage_strike_nohf/RG_1.232.md` | R1 대비 차이 = `~~` 표시 33군뿐 |
| R3 | R2 + `include_header_footer=True` | `scratchpad/reconv_offpage_strike/RG_1.232.md` | 2,583 lines, 325,571 chars |

결과(`rg_reconv_check.py`, `rg_mddiff.py`, `rg_crit2.py`):

| 검사 항목 | 기대 | R0 | R1 | R3 |
|---|---|---|---|---|
| GDC-19 rationale `unit safely…”` (A/B/C) | 3 | 0 | 3 | 3 |
| `have certain knowledge … able to make decisions` (A/B/C) | 3 | 2 | 3 | 3 |
| SFR-DC 55 `valves,” addresses closed` | 1 | 0 | 1 | 1 |
| MHTGR-DC 34/44/46 `removed. Refer to the rationale for ARDC 17` | 3 | 0 | 3 | 3 |
| Table 1 MHTGR 열 누락어(rows 14, 15, 26, 30, 31, 32, 34, 36, 72) | 9 셀 | 0 | 9 | 9 |
| Table 1 삭제어 `~~…~~` 표시 | 33군 | 0 | 0 | 33 (R2도 33) |
| Table 1 캡션 | 1 | 0 | 0 | 8 (페이지마다 `### TABLE 1: …`) |
| 부록 A/B/C criterion 단어 diff (PDF 대비) | 0 | 7 criteria 9 span | 0 (pdfplumber 순서 인공물 1건 제외) | — |
| R0 → R1 전체 토큰 diff | — | — | 21 ops = 20개 복원 span + 이미지 참조 제거 1 | — |
| `10 CFR 50.342` / `SFRDC` / `nonLWR` / `technologiesspecifically` | 0 / 0 / 0 / 0 | 1 / 13 / 18 / 1 | 1 / 13 / 18 / 1 | 1 / 13 / 18 / 1 |

판정:
- 현행 md에서 잘린 부록 A/B/C criterion 텍스트·rationale은 R1에서 전부 복원된다: ARDC 19, SFR-DC 19(3 span), SFR-DC 55, MHTGR-DC 19, 34, 44, 46 — 7 criteria, 9 span. Table 1의 11 span(9 셀)도 복원된다. R1은 그 밖의 텍스트를 바꾸지 않는다(표 블록 수·헤딩·`<br>` 사실상 동일, `<br>` 706→704는 복원 조각 위치 변화).
- `detect_strikethrough=True`(R2)는 부작용 없이 삭제어 33군을 표시한다. 삽입어(청색 밑줄)는 표시하지 않는다.
- `include_header_footer=True`(R3)는 이 문서에서 권장하지 않는다: 쪽 footer 132개가 `###### RG 1.232, Rev. 0, Page 2`처럼 H5/H6 헤딩으로, 부록 쪽 머리글 101개(`APPENDIX B. SODIUM-COOLED FAST REACTOR DESIGN CRITERIA`)와 Table 1 캡션 8개가 반복 삽입되어 스퓨리어스 헤딩이 약 240개 증가한다. 이득은 인쇄 쪽 번호와 Table 1 캡션뿐이며, 둘 다 PDF 쪽 매핑과 캡션 1회 삽입으로 결정적으로 대체 가능하다. (PSAR과 달리 밑줄 소제목이 머리글로 오검출되는 사례는 이 문서에 없음.)
- 재변환으로 해결되지 않는 항목: F03(각주 결합), F04/F05(하이픈), F06–F10(표 분할·헤딩·셀 결합·각주 배치), F11–F17, F19–F22.

## 3. Figure inventory

| Figure ID | md lines | raster/vector | image file | debris lines to delete | Notes |
|---|---|---|---|---|---|
| (표지 NRC 휘장, 캡션 없음) | L3 | raster | `RG_1.232_images/imageFile1.png` (23,598 B; PDF p1 bbox 74,63–146,133 pt) | L3 (선택) | 장식용 로고. 본 문서에는 Figure 캡션·vector 도식이 없음(PDF 전 페이지 이미지 1개). vector debris 0 |

## 4. Heading outline check

요약 수치: md 헤딩 33개 = 의도된 헤딩과 대응 28개(제목 L9와 삭제 대상 TOC L74 포함; 이 중 순서 오류 2, 텍스트 오염 1) + 스퓨리어스 5개(L1, L5, L7, L154, L386); 평문/목록에 묻힌 헤딩 4개(`Background`, `The NRC Regulatory Framework`, `NRC Policy on Advanced Reactors`, `Key Assumptions and Clarifications Regarding the non-LWR Design Criteria`), 캡션 누락 1개(Table 1), 표 section 제목 27개(Table 1: 7, A: 6, B: 7, C: 7)는 표 헤더 행(123회 반복)으로만 존재, criterion 헤딩 178개(ARDC 55, SFR-DC 65, MHTGR-DC 58) 부재. 수준 체계: 제목(L9)이 H2이고 기관명(L1)이 H1이어서 역전. A–D·부록이 H3, 그 하위가 H4로 일관되게 한 단계 깊음.

의도된 outline(PDF 서체 위계: Arial Bold 16 pt 제목, TNR Bold 14 pt 대단원, TNR Bold 11 pt 소제목)과 현재 형태:

| md line | 현재 형태 | 의도된 형태 / 수준 | 결함 |
|---|---|---|---|
| L1 | `# U.S. NUCLEAR REGULATORY COMMISSION` | frontmatter `issuer` | 스퓨리어스 H1 |
| L5 | `### REGULATORY GUIDE 1.232, REVISION 0` | frontmatter `doc_id`, `revision` | 스퓨리어스 |
| L7 | `###### Issue Date: April 2018 Technical Lead: Jan Mazza` | frontmatter `issue_date`, `technical_lead` | 스퓨리어스, 두 필드 병합 |
| L9 | `## GUIDANCE FOR DEVELOPING PRINCIPAL DESIGN CRITERIA FOR NON-LIGHT-WATER REACTORS` | `#` (H1) | 수준 |
| L13 / L11 | `### A. INTRODUCTION` / `#### Purpose` (역순) | `## A. INTRODUCTION` → `### Purpose` | 순서, 수준 |
| L17, L21, L46, L62, L66, L70 | `####` | `###` | 수준(일괄 −1) |
| L74 | `### TABLE OF CONTENTS` | 삭제 | 노이즈 |
| L89 / L87 | `### B. DISCUSSION` / `#### Reason for Issuance` (역순) | `## B. DISCUSSION` → `### Reason for Issuance` | 순서, 수준 |
| L93 | 평문 `Background The NRC Regulatory Framework` | `### Background` + `#### The NRC Regulatory Framework` | 평문화·병합 |
| L103 | `#### Role of the General Design Criteria in the Regulatory Framework` | `####` (Background 하위) | — |
| L110 | 목록 항목 `- 10 CFR 50.34(a)(3). NRC Policy on Advanced Reactors` | 앞 문단 끝 `10 CFR 50.34(a)(3).` + `#### NRC Policy on Advanced Reactors` | 목록에 결합 |
| L119, L134, L142 | `####` | `####` (Background 하위) | — |
| L154 | `###### 3 The technology-specific design criteria…` | 각주 `[^3]:` | 스퓨리어스(각주) |
| L164 | 문단 중간 `…public comments. Key Assumptions and Clarifications Regarding the non-LWR Design Criteria The NRC staff applied…` | `#### Key Assumptions and Clarifications Regarding the non-LWR Design Criteria` | 본문에 결합 |
| L182 | `#### Harmonization with International Standards` | `####` (Background 하위) | — |
| L188, L349 | `### C. …`, `### D. …` | `##` | 수준 |
| L192, L207, L353, L359 | `####` | `###` | 수준 |
| (L233) | 없음 | `#### Table 1: Non-Light-Water-Reactor Crosswalk` (캡션) | 누락 |
| L380 | `### ACRONYMS/ABBREVIATIONS` | `##` | 수준 |
| L386 | `##### TRISO tristructural isotropic fuel` | 약어 표의 한 행 | 스퓨리어스 |
| L388 | `### REFERENCES7` | `## REFERENCES[^7]` | 텍스트 오염 |
| L465, L735, L1084 | `### APPENDIX A ADVANCED REACTOR DESIGN CRITERIA` 등 | `## Appendix A. Advanced Reactor Design Criteria` | 수준 |
| 표 헤더 123개 | `\|I. Overall Requirements\| \| \|` 등 | `### Appendix B — Section I. Overall Requirements` 등 27개 | 헤딩 부재 |
| 표 행 178개 | `\|4\|Environmental and dynamic effects design bases. Structures, …\|…\|` | `#### SFR-DC 4 — Environmental and dynamic effects design bases` 등 | 헤딩 부재 |

주: `Background` 아래 7개 소제목(L103–L182)이 Background의 하위(H4)인지 동급(H3)인지는 PDF에서 동일 서체(TNR Bold 11 pt)라 판별 불가하다. NRC RG 서식 관례상 하위로 보는 편이 자연스러우나 판단 사항이므로 C로 분류한다.

## 5. File-specific observations and recommendations for the cleanup script

### 5.1 Criterion record 목표 구조 (vault의 `wiki/SFRDC_n.md` placeholder "(Content from RG 1.232 Appendix B)"를 채울 수 있도록)

- 단위: 부록 A–C의 criterion 1개 = H4 섹션 1개. 상위 H3 = 부록 section(I–VII), H2 = 부록. 헤딩 경로가 chunk breadcrumb가 된다(예 `Appendix B > Section I. Overall Requirements > SFR-DC 4 — …`).
- 헤딩 텍스트: `{set} {n} — {Title without final period}`. 콜론은 Obsidian 헤딩 링크에서 문제가 될 수 있으므로 em dash 사용. 블록 ID `^sfr-dc-4`를 ID 행에 부여하여 `![[RG_1.232#^sfr-dc-4]]` 전이 또는 `[[RG_1.232#SFR-DC 4 — Environmental and dynamic effects design bases]]` 링크 지원. vault 명명(`SFRDC_4`, alias "SFRDC 4")과의 어휘 일치를 위해 `Aliases` 필드에 병기.
- Status 값: 부록 상태행(Same as GDC / Same as ARDC / Not applicable to MHTGR.)이 있으면 그대로, 없으면 Table 1 해당 열(Modified for SFR-DC 등, 70번대는 "Additional SFR-DC")에서 가져온다. 부록 B 분포: Same as GDC 13, Same as ARDC 20, Modified 22, New 10.
- 본문·rationale은 verbatim, 문단 구분은 PDF 줄 간격 기준으로 복원, 페이지 경계 조각은 문장 중간이면 공백으로, 문장 끝이면 빈 줄로 결합.

예시 (SFR-DC 4; 텍스트는 md L770 + L776 + PDF p64–65 대조 결과):

```markdown
### Appendix B — Section I. Overall Requirements (SFR-DC 1–5)

#### SFR-DC 4 — Environmental and dynamic effects design bases
- **ID:** SFR-DC 4 ^sfr-dc-4
- **Aliases:** SFRDC 4
- **GDC counterpart (Table 1):** GDC 4 — Environmental and dynamic effects design bases.
- **Title:** Environmental and dynamic effects design bases.
- **Status:** Modified for SFR-DC (source: Table 1; Appendix B cell has no status line)
- **Source:** RG 1.232 Rev. 0, Appendix B, pp. B-3–B-4 (PDF p. 64–65)

##### Criterion text
Structures, systems, and components important to safety shall be designed to accommodate the effects of, and to be compatible with, the environmental conditions associated with normal operation, maintenance, testing, anticipated operational occurrences, and postulated accidents, including the effects of liquid sodium and its aerosols and oxidation products. These structures, systems, and components shall be appropriately protected against dynamic effects, including the effects of missiles, pipe whipping, and discharging fluids that may result from equipment failures and from events and conditions outside the nuclear power unit. However, dynamic effects associated with postulated pipe ruptures in nuclear power units may be excluded from the design basis when analyses reviewed and approved by the Commission demonstrate that the probability of fluid system piping rupture is extremely low under conditions consistent with the design basis for the piping.

Chemical consequences of accidents, such as sodium leakage, shall be appropriately considered for the design of structures, systems, and components important to safety, which must be protected.

##### NRC rationale for adaption to GDC
This change removes the light-water reactor (LWR) emphasis on loss-of-coolant accidents (LOCAs) … if relevant to the design.

The phrase “the environmental conditions associated with anticipated operational occurrences” has been added … as suggested in NUREG-1368.

A new sentence is added to ensure the designer considers the effects of sodium leakage and associated chemical reactions with SSCs important to safety, which must be protected.
```

(예시의 "…"는 이 리뷰에서의 생략 표기이며, 실제 출력에서는 전문을 둔다.) "Same as GDC/ARDC"이고 rationale이 비어 있는 criterion(부록 B 14개)은 `##### NRC rationale for adaption to GDC` 아래에 `(none in source)`를 두어 빈 셀과 누락을 구분한다. SFR-DC 27은 Criterion text에 `DELETED—Information incorporated into SFR-DC 26`을 verbatim으로 둔다. 가장 긴 record는 SFR-DC 26(≈ 9,000 chars, 4 블록)과 MHTGR-DC 26(5 블록)이며, H5 소제목으로 기준 본문과 rationale을 분리하면 chunk 크기를 제어할 수 있다.

Table 1 목표 구조: 단일 표, 열 = `Section | Criterion | GDC title | ARDC title | ARDC status | SFR-DC title | SFR-DC status | MHTGR-DC title | MHTGR-DC status`, 제목은 redline 적용 후 최종 제목, redline 원형은 별도 열 또는 각주에 `~~…~~`/`<ins>…</ins>`로 보존. "Same as GDC"는 status 열에만 두고 title 열에는 해당 GDC 제목을 채우지 않는다(원문에 없는 텍스트 생성 금지).

### 5.2 권장 정리 순서 (ordered rules)

1. (필수) 재변환: `content_safety_off="off-page"`, `detect_strikethrough=True`, `markdown_page_separator="<!-- page %page-number% -->"`, `include_header_footer=False`(§2.7 R2). 이것만으로 F01(삭제어 표시)·F02(누락 20 span)·F20(페이지 앵커)의 대부분이 해결된다. PDF 쪽↔인쇄 쪽 번호 매핑(1–27, A-1–A-33, B-1–B-42, C-1–C-30; p21 "20" 중복, p105 "B-2" 오기)은 frontmatter에 기록한다. 이하 규칙의 줄 번호는 현행 md 기준이므로 재변환 후에는 패턴(텍스트 앵커)으로 찾아 적용한다.
2. frontmatter 삽입(§5.3). L1, L3, L5, L7 제거. 표지 박스 L30–L32는 frontmatter의 ADAMS 필드로 옮기고 원문은 문서 끝 "Document information" 절에 verbatim 보존(삭제하지 않음).
3. TOC(L74–L84)와 footer(L1113) 삭제.
4. 헤딩 수술: L11↔L13, L87↔L89 순서 교환; L93 분리; L110·L164에서 헤딩 추출; L154·L386 비헤딩화; L388 `REFERENCES7` 정정; 전체 수준 −1 조정(제목 H1); Table 1 캡션 삽입.
5. 각주: §1.2 목록 14건만 `[^n]`로 치환하고, 본문 14개를 `[^n]:` 정의로 이동한 뒤 끊긴 문장(L368↔L374, L150–L156, L434↔L440, L1103↔L1109, L25↔L34)을 재결합.
6. 하이픈: §1.3의 명시 목록(67 결합 + em dash 1 + INL 분할 2)만 복원. `SFR-DC17`은 원문대로 공백 없이.
7. 본문 분할 13곳(F14) 병합, raw bullet 변환(F15).
8. Table 1: R2 출력의 `~~…~~`를 이용해 최종 제목과 redline 열 생성(F01), 필요 시 청색 삽입어에 `<ins>` 부여(PDF 색상), 제목/상태 분리, 10개 블록을 단일 표로 병합.
9. 부록 A–C: (a) 블록 병합·중복 헤더 제거, (b) 연속행 73개를 직전 criterion에 결합, (c) 제목/상태/본문 분리, (d) 누락 9 span이 R2에서 복원되었는지 확인(§2.7), (e) 문단 구분 복원(F08), (f) criterion record로 출력(§5.1).
10. 약어 42개를 2열 표로(PDF x좌표), 참고문헌 39개를 `^ref-n` 앵커가 있는 번호 목록으로 재구성(Ref. 34, 37, 38 수리).
11. 선택: GDC 19 rationale italic 강조 복원(F21).
12. 회귀 검사: PDF 셀·문단 단위 단어 diff(`rg_crit.py`, `rg_body.py` 방식) 결과가 원문 오기 목록 외 차이 0이 되어야 한다.

### 5.3 frontmatter 제안

```yaml
doc_id: RG 1.232
revision: 0
title: Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors
issuer: U.S. Nuclear Regulatory Commission
issue_date: 2018-04
technical_lead: Jan Mazza
adams_accession: ML17325A611
related_adams: {regulatory_analysis: ML16330A179, draft_guide_DG-1330: ML16301A307, public_comment_responses: ML17325A616}
source_pdf: references/pdf/RG_1.232.pdf
pdf_pages: 133
page_labels: {body: "PDF p1-28 = 1-27 (p20 and p21 both printed 20)", appendix_A: "p29-61 = A-1..A-33", appendix_B: "p62-103 = B-1..B-42", appendix_C: "p104-133 = C-1..C-30 (p105 printed B-2)"}
criteria_sets: {ARDC: 55, SFR-DC: 65, MHTGR-DC: 58, crosswalk_rows: 65}
```

검색용 식별자(태그·필드 후보, 간략): criterion ID `GDC n`/`ARDC n`/`SFR-DC n`/`MHTGR-DC n`(번호대 1–5, 10–46, 50–57, 60–64, 70–79/70–72); 10 CFR 인용(50.34(a)(3)(i), 52.47(a)(3)(i), 52.79(a)(4)(i), 52.137(a)(3)(i), 52.157(a), 50.2, 50.55a 15회, 50.34(f)(2)(iii), 20.1301 등); ADAMS 번호 42종; NUREG-0968/1338/1368/1369/1409; SECY-93-092, SECY-03-0047, SECY-15-0002, SECY-94-084; "Ref. n" 교차참조(1–39); 핵심 용어 SARRDL, functional containment, primary coolant boundary, reactor helium pressure boundary, intermediate coolant boundary; 약어 42. vault의 wiki에는 SFRDC_25, 73, 78 노트가 없다(참고).

### 5.4 자동 수정 금지 항목 (원문 오기·원문 중복; verbatim 유지)

`Section I—Overall Requirements (Criterion 1 – 15)`, `(Criterion 10 – 20)`, `(Criterion 21 – 29)` (L480–L482, p29); `Section VII—Additional SFR-DC (Criteria 70–77)` (L231, L753; 실제 70–79); `SFR-DFC` (L198, p11); `watercooled` (L123, p7); `fire- resistant` (L498, p31); `SFR-DC17` (공백 없음, p81 등 7회); `anticipated occupational occurrences` (L1030, p96); `August 2017 2017` (L424, p27); `on material properties,,` (L607, p44); `there is a need to for operators` (L538, L821, L1189); `SARRDLS` (L1146, p109); `VI. Fuel and Reactivity Control` (부록 B·C section label; 서두는 "Radioactivity"); `(MHTGR)-DC` (L737, p62); 헤더 `Adaption`/`Adaptions` vs 서두 `Adaptations`; footer `Page B-2` on p105; 각주 중복(fn 1 = 4, fn 3 = 13 = 14, fn 10 = 11); 부록 간 반복 rationale 문단(원문 내용, 중복 제거 금지).

### 5.5 스크립트 구현 시 함정

- Table 1의 삭제어는 텍스트층에 그대로 존재하므로 기본 옵션 md만으로는 판별 불가하다. `detect_strikethrough=True` 재변환 출력 또는 PDF 문자 색상(빨강 = 삭제, 청색 = 추가)을 사용할 것. 사전 기반 "교정" 금지.
- 각주 결합 정규식(`[A-Za-z)\.]\d{1,2}\b`)은 `SFR-DC17`, `MHTGR-DC 10`, `Ref. 29)`, 날짜 등을 오탐한다. §1.2의 14건 목록만 적용한다.
- 하이픈 복원을 사전·패턴으로 일반화하면 원문 `watercooled`, `nonbrittle`(6회), `leaktight`(20회; 원문에 `leak-tight` 1회도 공존) 등을 잘못 바꾼다. PDF 줄끝 하이픈 목록만 사용한다.
- italic = 제목 규칙은 SFR-DC 18(상태행도 italic)에서 깨진다. 상태 정규식을 먼저 적용한다.
- 연속행 결합 시 PDF 페이지 경계가 문단 경계와 일치하는 경우(SFR-DC 4 L776)는 빈 줄로, 문장 중간(43건)은 공백으로 결합해야 원문 문단 구조가 보존된다. 판정은 앞 조각 끝 문자(`.`, `:`, `;`, `”`, `)`)로 가능하나, 목록 항목 `(4)` 시작(SFR-DC 26 L855) 등은 줄바꿈으로 둔다.
- F02 유형의 누락은 `off-page` 필터가 /Rotate 90 페이지에서 회전 전 폭(612 pt)을 적용한 결과로 판단된다. `content_safety_off="off-page"` 없이 재변환하면 재발하므로, 재변환 후에도 PDF 대비 단어 diff를 반드시 재실행한다.
- `include_header_footer=True`는 이 문서에서 스퓨리어스 헤딩 약 240개를 만든다(§2.7). 사용할 경우 footer를 페이지 앵커로 변환하고 머리글을 삭제하는 후처리가 필수다.
- 부록 제목행의 `Same as ARDC.`(SFR-DC 18) 등 마침표 유무 차이는 원문이다.
