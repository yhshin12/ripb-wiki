# Review ch3: TP_Natrium_PSAR2025_ch3_Licensing Basis Events.md (md lines 1–3647, PDF pages 1–132)

검토 방법(요약): md 전체를 순차 판독(L1–3647)하고, PDF 132쪽을 pdfplumber로 전량 텍스트화(`scratchpad/ch3_pages.txt`)하여 (a) 단어 단위 정렬(difflib, PDF↔md 34,862 : 34,678 words, ratio 0.977), (b) 문서 표 36개 블록의 셀 토큰 비교(pdfplumber `extract_tables`), (c) LBE 수치 표 88개의 값·소속 섹션 정렬, (d) PDF 본문에서 추출한 번호 절 outline(458개)과 md heading 형태 비교를 수행하였다. 표·수식·그림 페이지(p9, 15–22, 27–30, 50, 59–62, 97, 127–129)는 렌더링하여 육안 확인하였다. 사용 스크립트: `scratchpad/ch3_lbe2.py`(모든 level 절 추적), `ch3_listed.py`, `ch3_tcmp.py`, `ch3_outline.py`, `ch3_wdiff.py`, `ch3_sample.py`, `ch3_stats.py`.

## 0. 개요 — lines, chars, pages, #tables, #figures, #sections; noise estimate

| 항목 | 값 |
|---|---|
| md 크기 | 3,647 lines (마지막 빈 줄 포함), 248,692 chars (UTF-8 248,958 bytes), 비공백 2,036 lines, 공백 1,611 lines |
| PDF | 132 pages: p1 cover, p2–4 TOC, p5 List of Tables, p6 List of Figures, p7–132 본문(쪽번호 3.1-1 … 3.14-6). struct tree 없음 |
| 페이지 라벨↔PDF 쪽 | 3.1-1…3.1-16 = p7–22; 3.2-1…3.2-21 = p23–43; 3.3-1…3.3-8 = p44–51; 3.4-1 = p52; 3.5-1…3.5-10 = p53–62; 3.6-1…3.6-4 = p63–66; 3.7-1…3.7-16 = p67–82; 3.8-1…3.8-25 = p83–107; 3.9-1…3.9-11 = p108–118; 3.10-1 = p119; 3.11-1 = p120; 3.12-1…3.12-4 = p121–124; 3.13-1…3.13-2 = p125–126; 3.14-1…3.14-6 = p127–132 |
| 표 (md 블록) | 124 = 문서 표 36 블록 [캡션 있는 표 25개(Table 3.1-1…3.1-3, 3.2-1…3.2-18, 3.5-1…3.5-4)가 35 블록으로 분할 + 무캡션 초기조건 표 1] + LBE 수치 mini-table 88개(30-day EAB TEDE 34, frequency 45, DBA enveloping dose 9). header 빈 셀 포함 21개(T009–T027, T035–T036) |
| 그림 | Figure 3.5-1 1개(raster `imageFile4.png`, 2318×2318 px) + cover 장식 이미지 3개(`imageFile1–3.png`; md5가 PSAR ch1/3/4/5/6/7/11의 동일 파일과 일치) |
| 절(section) | 번호 절 458개(level 2 = 3.x: 14, level 3: 40, level 4: 143, level 5: 261) + 무번호 `References` 7개. LBE 절 106개(AOO 11 / DBE 27 / BDBE 47 / DBA 21) |
| 본문 누락 | 본문 문단 누락 없음(단어 정렬 잔차는 표 캡션·표 header·하이픈·하첨자로 모두 설명됨). 누락은 표 캡션 15건(6개 표), Table 3.5-4 열 header 1종(2 sheet) |
| 수치 정확도 | source-term 표 19 블록 셀 전수 일치, LBE 표 88개 값 전수 일치. 단 LBE 표 29개(33 %)가 다른 LBE 또는 상위 절 도입부에 붙어 있음(H) |
| 샘플 문단 검사 | 12개 문단(L157, 258, 540, 1021, 1120, 1648, 1914, 2476, 2988, 3236, 3453, 3605; p7–131)을 PDF에서 공백 무시 verbatim 검색: 11개 일치, L3605는 `keff`(PDF k<sub>eff</sub>) 하첨자 차이로만 불일치. 쪽 경계 분리 문단 16개는 결합 시 모두 PDF와 일치(완결) |
| noise 추정 | cover L1–11 456 chars; TOC/LOT/LOF L13–143 비공백 82 lines, 8,929 chars; stray "." 6 lines; 연속 sheet의 반복 header 행 12행(≈1.1 k chars); 고아 기호 줄 5줄(L3508, 3531, 3553, 3557, 3561); 초과 공백줄 456줄(≥3 공백줄 run 8개). 순수 noise ≈ 10.5 k chars ≈ 4.2 % (공백줄 제외) |

## 1. Findings

| # | T-ID | Sev | Count | md lines (examples) | PDF p. | Evidence / description | Proposed fix | Fix class |
|---|---|---|---|---|---|---|---|---|
| 1 | T16/T6 | H | 29 표 / 19 LBE (freq 14, dose 10, DBA dose 5) | L1555 (DHS-ISTL-2 freq가 `- 3.7.2.4 … (DHS-RNBK-3)` 아래), L1633 (SUD-IHEL-BL freq가 `- 3.7.3 …` 도입부), L1830–1837 (RRS-RWG-2 dose+freq가 `- 3.7.4 Fuel Handling DBEs` 도입부), L1744–1751 (RRS-SPLX-BL dose+freq가 3.7.3.5 RRS-SPLA-BL 아래), L1867–1874 (RFH-FDIV-1 dose+freq가 `- 3.7.4.3.1 LBE Description`(RFH-FDIV-3) 아래), L1960–1967 (RFH-ESWR-1 dose+freq가 무방출 LBE RFH-LTCA-1 아래), L3133–3140 (RRS-CGR-CN 7.75E+00/7.77E+00 과 RRS-ISPL-CN 1.34E-01/5.30E-01 이 모두 3.9.4.3 RRS-SPLX-CN 아래), L3267 (RFH-ESWR-CN 2.01E-02/6.09E-01 이 3.9.5.4 RFH-LTCA-CN 아래) | 69–71, 74, 76–78, 80–81, 93, 96, 98, 101, 104, 112–113, 116 | PDF에서는 모든 표가 같은 쪽에서 "… are listed below." 바로 뒤에 있음(쪽 경계 아님, xycut 순서 오류). md에서는 표가 다음 heading(다음 LBE 또는 상위 3.x.y 절) 뒤로 밀려 29개 "listed below." 문장이 자기 절 안에서 표 없이 끝나고(L1535, 1585, 1624, 1737/1739, 1823/1825, 1857/1859, 1885/1887, 1951/1953, 1983, 2418/2420, 2536/2538, 2622/2624, 2739/2741, 2860/2862, 3116, 3127, 3154, 3165, 3263), 수신 LBE는 dose/freq 표를 2벌 갖게 됨. 예: RAG가 "RRS-SPLX-CN EAB dose"를 물으면 7.75E+00 rem(실제 8.13E-02 rem, 약 95배)을 반환할 위험; DHS-RNBK-3 mean frequency 3.02E-03(실제 1.84E-04). 영향 LBE 19개: DHS-ISTL-2, SUD-IACA-1, SUD-IHEL-BL, RRS-SPLX-BL, RRS-RWG-2, RFH-FDIV-1, RFH-FDIV-3, RFH-ESWR-1, RFH-LBCA-BL, SUD-CGR-1, RFH-FDSP-2, RFH-LMCA-1, RFH-FDEM-1, RFH-FDPI-1, RRS-CGR-CN, RRS-ISPL-CN, RRS-SPLX-CN, RRS-SPLA-CN, RFH-ESWR-CN. 표별 목록은 §2 T042…T123 | 3.6–3.9 범위에서 "… are listed below." 문장 88개(dose 34, freq 45, DBA 9)와 표 88개가 종류별로 같은 순서임을 확인(순서 위반 0, PDF 정렬 88/88 일치). i번째 kind-k 문장 바로 뒤로 i번째 kind-k 표를 이동. 메모리 상 적용 시뮬레이션(`scratchpad/ch3_simfix.py`) 결과 88/88 표가 PDF와 같은 LBE·하위절에 위치(불일치 0). 이동 후 각 LBE에 announced kind별 표가 정확히 1개인지 검증 | A (PDF 정렬로 검증된 결정론 규칙) |
| 2 | T6/T14 | H | 2 sheet, 21 값 | L1246, L1266: `\|DBE ID\|DBA ID\|DBA Title\|DBA 2-hour Exclusion Area Boundary TEDE (rem)\| \|` | 60–61 | 5번째 열 header "DBA 30-day Low Population Zone Boundary TEDE (rem)" 소실 → LPZ 값(예: LFF-SAO-CN 9.60E-01, RRS-ISPL-CN 5.30E-01)이 무라벨 | header를 `\|DBE ID\|DBA ID\|DBA Title\|DBA 2-hour Exclusion Area Boundary TEDE (rem)\|DBA 30-day Low Population Zone Boundary TEDE (rem)\|` 로 교체 | C (1회성) / B |
| 3 | T6 | H | 7 행 × 4 셀 | L1251 `\|DHS-ISTL-2\| \| \| \| \|`, L1253, 1257, 1259, 1260, 1272, 1275 | 60–61 | Table 3.5-4 rowspan(DBA ID, DBA Title, 두 dose)이 첫 행에만 있음 → DHS-ISTL-2, DHS-RNBK-3, RFH-ESWR-1, RFH-FDIV-1, RFH-FDIV-3, RRS-CGR-1, RRS-RWG-2 의 DBE→DBA 매핑·dose가 행 단위로 소실 | col1만 채워진 행은 col2–5를 직전 행에서 fill-down | A |
| 4 | T6 | H | 27 행 | L500–501, 503–506, 508–515, 517–524, 530–534 (예: `\|Sodium Fire\| \|`) | 21–22 | Table 3.1-3 "Analysis" 열 rowspan 미충전(5개 그룹: Volcanic 3행, seismic 5행, internal fire 9행, winds 9행, internal flood 6행). 행 단위 검색 시 "Sodium Fire"의 분석이 공란 | 직전 비공란 Analysis로 fill-down(각 그룹 첫 행이 비공란이므로 결정론적) | A |
| 5 | T14/T3 | H | 6 표 15 sheet 캡션 | L369(3.1-2 시작), L495(3.1-3), L622/L663(3.2-4), L1148/L1171(3.5-2), L1183/1209/1229(3.5-3), L1244/L1264(3.5-4는 `#### (Sheet n of 2)`만 잔존) | 17–22, 28–29, 55–61 | 캡션 부재로 heading 기반 chunking 시: Table 3.2-4(Local Fault Event DBA, 40 isotope 행)가 `#### Table 3.2-3 In-vessel Fuel Drop` 아래로, Table 3.5-2(DBE 27)·3.5-3(BDBE 47)이 `#### Table 3.5-1 Summary of AOOs` 아래로, Table 3.1-2/3.1-3이 `#### (Sheet 2 of 2)`(Table 3.1-1) 아래로 귀속 | §5의 block→caption 고정 map으로 캡션 삽입(LOT L112–140 텍스트 사용) 후 sheet 병합 | A (고정 map) |
| 6 | T16 | H | 1 표 | L1064–1078 | 50 | 3.3.4.2 "…used in the LBE analyses:"(L1066) 바로 뒤에 있어야 할 초기조건 표(Low Power 5/15/309.5; Full Power 100/100/360.1 °C)가 `- 3.3.4.3 LBE Analysis End States` heading 뒤(L1075)로 이동 | L1075–1078 블록을 L1066 뒤로 이동 | C |
| 7 | T8 | H | 10 | L348 `1x10-3 per year`, L350/351 `1x10-4`, L1291 `1x10-2 per plant-year`, L1449 `1x10-4 … 1x10-2`, L2048 `5x10-7 … 1x10-4`, L2990 `1 x 10-2/plant-year`, `1 x 10-4` | 15, 63, 67, 83, 108 | 지수 위첨자 소실. PRA 가정(Table 3.1-1)과 LBE 분류 빈도 경계(AOO ≥1×10⁻², DBE 1×10⁻⁴–1×10⁻², BDBE 5×10⁻⁷–1×10⁻⁴)에 해당 | `(\d)\s?[x×]\s?10-(\d+)` 매칭 후 지수 숫자를 superscript 문자로 매핑(`1x10-3` → `1×10⁻³`, `1 x 10-2` → `1×10⁻²`) 또는 코퍼스 공통 표기. TOC 쪽번호 `3.10-1` 같은 오검출 제외 | A |
| 8 | T10/T8/T11/T3 | H | 수식 2개, 기호 소실 9, 고아 기호 줄 5 | L3508 `### σ`, L3510 `uncertainty ( ) must`, L3512 `keff + 2σ &lt; USL`, L3514–3520 수식/번호 순서 뒤섞임, L3526–3528 `- is the uncertainty in the bias.`, L3531 `σbias ΔSM ΔAOA`, L3550 `Bias, , and are computed`, L3555 `the bias, , and for`, L3559 `the standard value of 0.05` | 128–129 | 기호 σ, σbias, ΔSM, ΔAOA가 문장에서 빠져 고아 줄로 분리, `(Equation 3.14-1)`이 Eq. 3.14-2 뒤에, `(Equation 3.14-2)`는 "defined as:" 뒤 빈자리에 위치 | §5-4의 정답 블록으로 L3508–3561 수작업 치환 | C |
| 9 | T3 | H | 1 (LBE heading 매몰) | L2388 `3.8.3.7.2 Radiological Consequences The fuel … 3.8.3.8 Reactor Scram or Spurious Scram with Alternative Shunt Trip (RPD-SS-4) 3.8.3.8.1 LBE Description The postulated…` | 92 | LBE 절 3.8.3.8(RPD-SS-4) heading이 행 중간에 매몰 → RPD-SS-4 서술이 RPD-SS-3 절로 귀속 | whitelist 제목으로 3분할 | A |
| 10 | T3 | M | 458 번호 절 중 Markdown heading 2개 | list item 416(정상 390 + body 붙음 26), plain paragraph 29(정상 15 + body 붙음 14), 앞 문장 뒤에 붙음 11, `#####` 2(L1945, L1979) | 전체 | structure-aware chunking 불가. 예 `- 3.7.4.2.3 …`(L1854 끝), `3.3.2 Licensing Methodology for AOO, DBE, and BDBE`(L983 plain) | PDF outline whitelist(458개 번호+정확한 제목)로 승격; level = 번호 성분 수(3.x→H2 … 3.x.y.z.w→H5), Chapter 제목 H1 | A (+B whitelist) |
| 11 | T3 | M | 45 lines / 52 절번호 + `References` 2 | L210, 1058, 1377, 1385, 1435, 1443, 1848, 1852, 1854, 1935, 1979, 1983, 1985, 2008, 2204, 2249, 2376, 2388, 2472, 2594, 2711, 2786, 2832, 2982, 3057, 3061, 3063, 3067, 3116, 3127, 3154, 3165, 3190, 3244, 3263, 3276, 3279, 3283, 3292, 3350, 3392, 3493, 3506; `… Revision 0 … References`(L3330), `… TP-LIC-RPT-0011. References`(L3481) | 9–127 | heading+본문, 본문+heading, heading+heading 결합. L1852(695 chars)는 3.7.4.2.1과 3.7.4.2.2 두 절을 포함, L1854는 `- per day …Table 3.2-5. 3.7.4.2.3 Radiological Consequences` | whitelist 제목 정확 일치 위치에서 줄 분리 | A |
| 12 | T3 | M | 5 | L1375+L1377 `(RPD-CW1ACS-BL) 3.6.3.1.1 LBE Description …`, L2334+L2336 `- (RPD-CW1ACS-3)`, L2347+L2349 `- (RPD-CW1ACS-4)`, L2402+L2405 `- Retain Release While Shutdown (SUD-CGR-1)`, L2422+L2425 | 65, 91, 93 | LBE 제목이 2줄로 쪼개져 ID가 heading에서 분리 | 두 줄 결합 후 heading화 | A |
| 13 | T16/T3 | M | 2 LBE | L2206–2217 (3.8.1.11.2 heading이 3.8.1.11.1 앞, 두 본문은 뒤), L2280–2292 (3.8.2.6.1 빈 heading, 3.8.2.6.2 뒤에 LBE Description 본문) | 87, 89 | 하위절 순서/본문 귀속 오류(같은 LBE 내부) | 수작업 재배열 | C |
| 14 | T3 | M | 10 (+cover 2, TOC 3) | `##### The 5th percentile, 95th percentile, and mean frequency for this BDBE are listed below.` ×3 (L2602, 2719, 2840); `### σ` (L3508); `##### *Denotes high-consequence BDBE` (L1242); `#### (Sheet 2 of 2)` (L355, 1264), `#### (Sheet 1 of 2)` (L1244), `- (Sheet 1 of 2)` (L343) | 97, 100, 103, 128, 59, 15–16, 60–61 | 일반 문장·표 주석·sheet 표시가 heading으로 승격. 3건의 "The 5th percentile…" H5는 PDF에서 평문 | 평문으로 강등; sheet 표시는 병합 시 삭제; 주석은 `\*Denotes high-consequence BDBE` 평문으로 표 바로 아래 | A |
| 15 | T6 | M | 19 블록(18 표) | L577–579 `\|Cumulative Activity Release to Environment (Ci)\| \| \| \| \| \|` + `\|Isotope\|2hr\|8hr\|…` 가 데이터 행; L622–644, 679–698, 721–740 `\|Plenum Release\|…`, `\|Non-Plenum Release\|…` | 25–43 | group label이 header 행, 실제 header가 1행 데이터로 들어감; Table 3.2-4/-5/-6은 Plenum/Non-Plenum 부분표가 한 표에 섞여 동일 isotope가 2회 등장(예 Table 3.2-5 I-131 2hr 1.22E+00 vs 4.71E+00). 값 자체는 전수 일치 | header를 `Isotope\|2hr\|…`로, "Cumulative Activity Release to Environment (Ci)"는 캡션/부제로; Plenum/Non-Plenum을 별도 표(부제 "Plenum Release"/"Non-Plenum Release")로 분리하거나 `Release` 열 추가 | A |
| 16 | T6 | M | 7 표 / 17 블록, 반복 header 10회(12행) | T001/T002 (3.1-1), T003–T006 (3.1-2), T007/T008 (3.1-3), T012/T013 (3.2-4, 3행 반복), T030/T031 (3.5-2), T032–T034 (3.5-3), T035/T036 (3.5-4) | 15–22, 28–29, 55–61 | 쪽 분할 표 미병합; group label에 `(continued)` 잔존(L403, L439) | 동일 header 연속 블록 병합, 반복 header·`(continued)` 제거 | A |
| 17 | T6 | M | 105 행 | L372–398, 404–434, 440–468, 474–492 (`\| \|Air Pollution\|`) | 17–20 | Table 3.1-2 "Screening Category" rowspan 미충전(렌더 기준 공란: Individual–Qualitatively 87(3 sheet), Coexistent–Qualitatively 9, Individual–Quantitatively 9) | fill-down | A |
| 18 | T5 | M | 16 (쪽 경계) + 8 (쪽 내부) | 쪽 경계: L988/990, 1015/1017, 1408/1410 (`- 2.5 days after …`), 1563/1565, 1761/1763, 2020/2022, 2119/2121, 2194/2196, 2227/2229, 2262/2264, 2445/2447, 2646/2648, 2763/2765, 2884/2886, 3112/3114, 3361/3363. 쪽 내부: L1852/1854 (`- per day …`), 3328/3330 (`- (Reference 3.11-1), …`), 3388/3390 (`- Section 4.1.1.5 …`), 3392/3394, 3535/3537, 3540/3542, 3544/3546, 3548/3550 | 45–122, 120–128 | 문장 중간 분리, 후반부가 list item으로 변환. 23쌍을 결합해 PDF 검색: 21쌍 verbatim 일치, L3540/3542·L3548/3550은 k_eff 하첨자·σ/Δ 기호 소실로만 불일치(내용 누락 없음). L1852/1854는 PDF p77 텍스트로 연속 확인 | 앞 줄이 종결부호 없이 끝나고 다음 비공백 줄이 소문자/`(Reference`/`Section`/`2.5 days`로 시작하면 결합(`- ` 제거) | A |
| 19 | T5 | L | 2 + 5 | L188 `- As new design baselines are approved, …`, L996 `- At the construction permit stage, BEPU …`(PDF 평문); 목록 중단: L202/205, L327/330, L1101/1104, L3422/3425; 중첩 소실 L220–223 (`At-Power Operation` 하위 `Peak Power`, `Minimum Power`) | 8, 9, 13–14, 46, 50–51, 123–124 | 평문 문단의 list화, 쪽 경계 공백으로 목록 끊김, 2단 목록 평탄화 | 목록 내부 공백줄 제거(A); L188/L996 `- ` 제거, L222–223 들여쓰기(C) | A/C |
| 20 | T2 | M | 81 dot-leader lines, 3 heading | L13–143 (`#### Chapter 3 Licensing Basis Events . . . 3.1-1`, `#### LIST OF TABLES`, `##### LIST OF FIGURES Figure 3.5-1 …`) | 2–6 | TOC/LOT/LOF 8,929 chars; TOC 순서도 뒤섞임(3.3.2–3.3.4가 L48–50에서 3.7 뒤) | 삭제(LOT는 캡션 삽입에 먼저 사용) | A |
| 21 | T1 | L | 6 비공백 줄 | L1, L3, L11 이미지; L5 `# Kemmerer Power Station Unit 1 PSAR, Chapter 3`; L7 `## US SFR Owner, LLC, …`; L9 `SUBJECT TO DOE COOPERATIVE AGREEMENT NO. DE-NE0009054 Copyright © 2025 …` | 1 | 장식 이미지·cover 문구가 H1/H2 | 삭제 후 frontmatter로 이관 | A |
| 22 | T15 | M | 1 | 파일 전체 | — | YAML frontmatter·page anchor 없음(인용 시 쪽 특정 불가) | §5-6 frontmatter; page anchor는 `--markdown-page-separator "<!-- page %page-number% -->"` 재변환 또는 위 페이지 map으로 절 단위 `page:` 부여 | A + B |
| 23 | T7 | M | 1 | L1284 `#### Figure 3.5-1 F-C Chart for LBEs with Uncertainty Bands`, L1286 `![](<…/imageFile4.png>)` | 62 | raster, alt text 없음. 축(“Event Sequence Mean Frequency (per plant year)” vs “Mean Total Effective Dose Equivalent (REM) at Exclusion Area Boundary (EAB)”)·범례(44 family) 정보가 텍스트에 없음. vector debris 없음 | 캡션을 H3로, alt text에 축명·범례 family 목록만 기재(수치 추정 금지) | C |
| 24 | T11 | M | 1 + 1 + 2 + 5 | `&lt;` L3512; `●` L1091; `Contentof-Application` L331(PDF `Content-of-Application`), `Secondary-toPrimary` L1254(PDF `Secondary-to-Primary`); group label `Individual Hazards -`/`Coexistent Hazards -`의 ` -` 소실 L371, 403, 439, 473, 483 | 128, 50, 14, 60, 17–20 | 문자 변환 오류 | `&lt;`→`<`, `● `→`- `, 두 단어 복원, ` - ` 복원 | A |
| 25 | T8 | L | 23 | `keff` ×9 (L3506, 3510, 3512, 3525×2, 3542, 3605×2, 3607); `FΔH`, `FZ`, `FXY` (L3371, 3373, 3375); `σbias/ΔSM/ΔAOA` ×11 (L3514, 3531, 3553, 3557, 3561) | 122, 127–131 | 하첨자 소실 | 토큰 map: k_eff, F_ΔH, F_Z, F_XY, σ_bias, Δ_SM, Δ_AOA (또는 `<sub>`) | A |
| 26 | T12 | L | `$` 1, `*` 3 | L3089 `approximately $0.30.`; L1212 `RFH-FDEM-2*`, L1222 `RFH-LMCA-2*`, L1242 | 110, 58–59 | 현재 `$` 짝 없음·표 셀 내부 `*`라 렌더 영향 없음. 줄 결합 후에도 안전하도록 escape 권장. `[[`, `==`, `%%`, `^`, `#tag` 0건 | `\$0.30`, 주석 `\*` escape; ID의 `*`는 유지(또는 "High-consequence" 열로 명시) | A |
| 27 | T13 | L | 140 change bar / 64 pages | 예: p21 11개, p44–45 15개, p111 6개 | 7–132 | Revision 1 변경 표시(우측 여백 세로 막대) 미반영 | 선택: bar y-범위로 변경 문단 표시(`<!-- rev1 -->`) | B (선택) |
| 28 | noise | L | 6 + 8 run | L2562, 2564, 2679, 2681, 2800, 2802 `.`; ≥3 공백줄 run L1396, 1989, 2257, 2282, 2349, 2390, 3100, 3394 | 97, 100, 103 | "."는 PDF의 2-pt 불가시 마침표(Arial 2.0 pt) | 삭제, 공백줄 1줄로 정규화 | A |
| 29 | T3 | M | 1 + 7 + 18 | L145 `#### Chapter 3 Licensing Basis Events`(H1이어야 함); `#### References` 5개(L324, 570, 1099, 3435, 3637)+glued 2; 캡션 heading `#### Table 3.2-1…3.2-18`(16), `#### Table 3.5-1`, `#### Figure 3.5-1`; Table 3.1-1 캡션은 평문(L341) | 7, 14, 25–43, 54, 62 | 캡션/References 수준 불일치 → 3.2의 표 16개가 `#### References`(3.2) 아래 자식으로 chunk됨 | References·표/그림 캡션을 해당 3.x의 H3로 통일 | A |
| 30 | T6 | L | 88 | 모든 LBE mini-table (예 L1416 `\|5th Percentile 30-day EAB TEDE [rem]\|Mean …\|`) | 66–118 | 표 자체에 LBE ID가 없어 표 단독 chunk는 어떤 LBE인지 불명(F1 수정 후에도 섹션 의존) | F1 수정 후 표 앞에 `LBE: <ID>` 캡션 또는 `LBE ID` 열 추가(원문 값 불변) | A |
| 31 | T4 | — | 0 | — | — | page header/footer residue 없음(include-header-footer=off 효과). cover의 DOE/copyright 1줄은 T1 | — | — |
| 32 | T9 | — | 0 | — | — | 각주 없음(작은 글꼴 숫자는 모두 지수/하첨자) | — | — |
| 33 | (보존) | — | — | L1308 등 | — | 반복 문장은 원문 그대로임(md = PDF): "The fuel performance acceptance criteria are satisfied." 51×, "… are listed below" 88×, "This is the most limiting DBE that mapped to the …" 20×, DL3-RR10 문장 9×. 서로 다른 LBE의 동일 값 표도 원문 그대로(예 RRS-CGR-BL/RRS-CGR-1 2.27E-03/5.75E-03/9.37E-03, RFH-FDSP-1/RFH-ESWR-1 1.20E-01/3.31E-01/5.05E-01, RFH-ESWR-3/RFH-FDBL-2/RFH-FDPI-1 1.00E+01/1.40E+01/2.10E+01) | 삭제·중복제거 금지 | — |

## 2. Table verification log

검증 방법: T001–T036은 해당 PDF 쪽의 pdfplumber 표를 셀 토큰 단위로 비교(`ch3_tcmp.py`), T037–T124는 PDF 본문 텍스트에서 추출한 표(값·소속 LBE/하위절) 88개와 md 표 88개를 순서대로 정렬 비교(`ch3_lbe2.py`, 모든 level 절 추적; 수정 시뮬레이션 `ch3_simfix.py`). 124/124 검증, 수치 불일치 0, 행/열 소실 0(열 header 1종 소실 제외).

| Table ID | md lines | PDF p. | Status (OK / defect IDs) | Notes (lost values, split rows, …) |
|---|---|---|---|---|
| T001 Table 3.1-1 (Sheet 1/2) | L341–352 | 15 | T3, T6, T8 | 5 행 셀 전수 일치. 캡션 평문(L341), `- (Sheet 1 of 2)` list item(L343). `1x10-3`, `1x10-4`×2 위첨자 소실. 셀 내부 2문단은 공백으로 결합(허용) |
| T002 Table 3.1-1 (Sheet 2/2) | L355–366 | 16 | T3, T6 | 8 행 일치. `#### (Sheet 2 of 2)` heading, header 반복 → T001과 병합(13 가정 행) |
| T003 Table 3.1-2 (1/4) | L369–398 | 17 | T14, T6, T11 | 캡션+sheet 표시 없음. 28 행 일치. Screening Category rowspan 27행 공란. `Individual Hazards -` → `Individual Hazards` |
| T004 Table 3.1-2 (2/4) | L401–434 | 18 | T14, T6 | 32 행 일치. label `… (continued)` |
| T005 Table 3.1-2 (3/4) | L437–468 | 19 | T14, T6 | 30 행 일치. label `… (continued)` |
| T006 Table 3.1-2 (4/4) | L471–492 | 20 | T14, T6, T11 | 20 행 일치(Coexistent–Qualitatively 10, Individual–Quantitatively 10). 하이픈 2개 소실 |
| T007 Table 3.1-3 (1/2) | L495–524 | 21 | T14, T6 (H) | 캡션 없음. 28 행 일치. Analysis rowspan 22행 공란 |
| T008 Table 3.1-3 (2/2) | L527–534 | 22 | T14, T6 (H) | 6 행 일치. Analysis 5행 공란, header 반복 |
| T009 Table 3.2-1 | L575–585 | 25 | T6 | 6 isotope × 5 시간 일치. header = group label + 빈 셀, 실제 header는 1행 데이터 |
| T010 Table 3.2-2 | L588–599 | 26 | T6 | 7 × 5 일치 |
| T011 Table 3.2-3 | L602–619 | 27 | T6 | 13 × 5 일치 |
| T012 Table 3.2-4 (1/2) | L622–660 | 28 | T14 (H), T6 | 캡션 없음 → Table 3.2-3 heading 아래로 귀속. Plenum 16 + Non-Plenum 16 isotope × 6 시간 일치. 부분표 header 행 내장, Non-Plenum header 첫 셀 빈칸(PDF도 빈칸) |
| T013 Table 3.2-4 (2/2) | L663–674 | 29 | T14, T6 | 8 isotope 일치. group/header 3행 반복 |
| T014 Table 3.2-5 | L677–716 | 30 | T6 | Plenum 13 + Non-Plenum 18 isotope × 8 시간 일치. 동일 isotope 7종이 두 부분표에 중복 |
| T015 Table 3.2-6 | L719–758 | 31 | T6 | 13 + 18 × 8 일치 |
| T016 Table 3.2-7 | L761–774 | 32 | T6 | 9 × 8 일치 (Pu-239/Pu-238 2hr 0.00E+00 원문) |
| T017 Table 3.2-8 | L777–796 | 33 | T6 | 15 × 8 일치 |
| T018 Table 3.2-9 | L799–812 | 34 | T6 | 9 × 4 일치 |
| T019 Table 3.2-10 | L815–823 | 35 | T6 | 4 × 7 일치 |
| T020 Table 3.2-11 | L826–834 | 36 | T6 | 4 × 7 일치 |
| T021 Table 3.2-12 | L837–848 | 37 | T6 | 7 × 6 일치 |
| T022 Table 3.2-13 | L851–861 | 38 | T6 | 6 × 6 일치 |
| T023 Table 3.2-14 | L864–875 | 39 | T6 | 7 × 4 일치 |
| T024 Table 3.2-15 | L878–889 | 40 | T6 | 7 × 5 일치 |
| T025 Table 3.2-16 | L892–904 | 41 | T6 | 8 × 5 일치 |
| T026 Table 3.2-17 | L907–920 | 42 | T6 | 9 × 5 일치 |
| T027 Table 3.2-18 | L923–928 | 43 | T6 | H-3 × 5 일치 |
| T028 (무캡션) 3.3.4.2 초기조건 | L1075–1078 | 50 | T16 (H) | 2 행 일치. 3.3.4.3 heading 뒤로 이동됨(F6) |
| T029 Table 3.5-1 | L1131–1145 | 54 | OK | 11 AOO 행 일치, 캡션 `####` |
| T030 Table 3.5-2 (1/2) | L1148–1168 | 55 | T14 (H), T6 | 캡션 없음 → "Summary of AOOs" 아래. 19 행 일치 |
| T031 Table 3.5-2 (2/2) | L1171–1180 | 56 | T14, T6 | 8 행 일치(DBE 합계 27) |
| T032 Table 3.5-3 (1/3) | L1183–1206 | 57 | T14 (H), T6 | 22 행 일치 |
| T033 Table 3.5-3 (2/3) | L1209–1226 | 58 | T14, T6 | 16 행 일치. `RFH-FDEM-2*`, `RFH-LMCA-2*`(high-consequence 표시) 유지 |
| T034 Table 3.5-3 (3/3) | L1229–1239 (+L1242) | 59 | T14, T6, T3 | 9 행 일치(BDBE 합계 47). 주석이 `##### *Denotes high-consequence BDBE` |
| T035 Table 3.5-4 (1/2) | L1244–1261 | 60 | T6 (H), T14, T11 | 5열 header 소실, rowspan 5행 공란(DHS-ISTL-2, DHS-RNBK-3, RFH-ESWR-1, RFH-FDIV-1, RFH-FDIV-3), `Secondary-toPrimary`. 값 일치 |
| T036 Table 3.5-4 (2/2) | L1264–1281 | 61 | T6 (H), T14 | 5열 header 소실, rowspan 2행 공란(RRS-CGR-1, RRS-RWG-2). 값 일치(DBA 합계 21; 3.9절 enveloping 표 9개와 값 일관) |
| T037 (RFH-OERC-BL) | L1416–1418 | 66 | OK | RFH-OERC-BL 30-day EAB TEDE 2.46E-03/3.62E-03/5.40E-03 — values match PDF, correct section |
| T038 (RFH-OERC-BL) | L1423–1425 | 66 | OK | RFH-OERC-BL Frequency 2.78E-03/2.20E-02/6.49E-02 — values match PDF, correct section |
| T039 (DHP-L1PP-2) | L1466–1468 | 67 | OK | DHP-L1PP-2 Frequency 4.15E-05/1.11E-04/2.40E-04 — values match PDF, correct section |
| T040 (DHP-LOOP-1) | L1485–1487 | 68 | OK | DHP-LOOP-1 Frequency 1.01E-05/1.80E-04/5.11E-04 — values match PDF, correct section |
| T041 (SUD-LOOP-1) | L1503–1505 | 68 | OK | SUD-LOOP-1 Frequency 2.09E-05/1.35E-04/2.87E-04 — values match PDF, correct section |
| T042 (DHS-ISTL-2) | L1555–1557 | 69 | T16/T6 H (misplaced) | DHS-ISTL-2 Frequency 1.05E-03/3.02E-03/7.45E-03 belongs to 3.7.2.2/3.7.2.2.1 but md places it under DHS-RNBK-3 (3.7.2.4 heading, before its first subsection); values match PDF |
| T043 (DHS-RNBK-3) | L1569–1571 | 70 | OK | DHS-RNBK-3 Frequency 4.39E-05/1.84E-04/4.62E-04 — values match PDF, correct section |
| T044 (SUD-IACA-1) | L1595–1597 | 70 | T16/T6 H (misplaced) | SUD-IACA-1 Frequency 1.40E-04/6.14E-04/1.49E-03 belongs to 3.7.2.5/3.7.2.5.1 but md places it under IPI-IHEL-BL (3.7.2.6 heading, before its first subsection); values match PDF |
| T045 (IPI-IHEL-BL) | L1607–1609 | 71 | OK | IPI-IHEL-BL Frequency 1.46E-04/1.59E-03/5.18E-03 — values match PDF, correct section |
| T046 (SUD-IHEL-BL) | L1633–1635 | 71 | T16/T6 H (misplaced) | SUD-IHEL-BL Frequency 1.17E-05/1.81E-04/5.81E-04 belongs to 3.7.2.7/3.7.2.7.1 but md places it under 3.7.3 section intro (after `- 3.7.3` heading); values match PDF |
| T047 (RRS-CGR-BL) | L1655–1657 | 72 | OK | RRS-CGR-BL 30-day EAB TEDE 2.27E-03/5.75E-03/9.37E-03 — values match PDF, correct section |
| T048 (RRS-CGR-BL) | L1662–1664 | 72 | OK | RRS-CGR-BL Frequency 9.47E-06/2.48E-04/8.69E-04 — values match PDF, correct section |
| T049 (RRS-CGR-1) | L1684–1686 | 73 | OK | RRS-CGR-1 30-day EAB TEDE 2.27E-03/5.75E-03/9.37E-03 — values match PDF, correct section |
| T050 (RRS-CGR-1) | L1691–1693 | 73 | OK | RRS-CGR-1 Frequency 5.23E-06/1.49E-04/5.19E-04 — values match PDF, correct section |
| T051 (RRS-ISPL-BL) | L1712–1714 | 73 | OK | RRS-ISPL-BL 30-day EAB TEDE 5.93E-03/1.04E-02/2.04E-02 — values match PDF, correct section |
| T052 (RRS-ISPL-BL) | L1719–1721 | 73 | OK | RRS-ISPL-BL Frequency 3.29E-05/8.77E-04/3.19E-03 — values match PDF, correct section |
| T053 (RRS-SPLX-BL) | L1744–1746 | 74 | T16/T6 H (misplaced) | RRS-SPLX-BL 30-day EAB TEDE 1.15E-02/1.99E-02/3.98E-02 belongs to 3.7.3.4/3.7.3.4.3 but md places it under RRS-SPLA-BL (3.7.3.5 heading, before its first subsection); values match PDF |
| T054 (RRS-SPLX-BL) | L1749–1751 | 74 | T16/T6 H (misplaced) | RRS-SPLX-BL Frequency 5.74E-06/5.33E-04/1.85E-03 belongs to 3.7.3.4/3.7.3.4.3 but md places it under RRS-SPLA-BL (3.7.3.5 heading, before its first subsection); values match PDF |
| T055 (RRS-SPLA-BL) | L1770–1772 | 75 | OK | RRS-SPLA-BL 30-day EAB TEDE 1.15E-02/1.99E-02/3.98E-02 — values match PDF, correct section |
| T056 (RRS-SPLA-BL) | L1777–1779 | 75 | OK | RRS-SPLA-BL Frequency 2.03E-04/3.68E-03/1.28E-02 — values match PDF, correct section |
| T057 (RRS-RWG-1) | L1798–1800 | 75 | OK | RRS-RWG-1 30-day EAB TEDE 2.14E-04/5.62E-04/1.03E-03 — values match PDF, correct section |
| T058 (RRS-RWG-1) | L1805–1807 | 76 | OK | RRS-RWG-1 Frequency 8.89E-04/6.33E-03/1.83E-02 — values match PDF, correct section |
| T059 (RRS-RWG-2) | L1830–1832 | 76 | T16/T6 H (misplaced) | RRS-RWG-2 30-day EAB TEDE 2.38E-04/6.39E-04/1.15E-03 belongs to 3.7.3.7/3.7.3.7.3 but md places it under 3.7.4 section intro (after `- 3.7.4` heading); values match PDF |
| T060 (RRS-RWG-2) | L1835–1837 | 76 | T16/T6 H (misplaced) | RRS-RWG-2 Frequency 1.52E-05/5.11E-04/1.58E-03 belongs to 3.7.3.7/3.7.3.7.3 but md places it under 3.7.4 section intro (after `- 3.7.4` heading); values match PDF |
| T061 (RFH-FDIV-1) | L1867–1869 | 77 | T16/T6 H (misplaced) | RFH-FDIV-1 30-day EAB TEDE 8.38E-02/1.83E-01/2.90E-01 belongs to 3.7.4.2/3.7.4.2.3 but md places it under RFH-FDIV-3 (3.7.4.3/3.7.4.3.1); values match PDF |
| T062 (RFH-FDIV-1) | L1872–1874 | 77 | T16/T6 H (misplaced) | RFH-FDIV-1 Frequency 8.32E-05/2.26E-03/8.73E-03 belongs to 3.7.4.2/3.7.4.2.3 but md places it under RFH-FDIV-3 (3.7.4.3/3.7.4.3.1); values match PDF |
| T063 (RFH-FDIV-3) | L1892–1894 | 78 | T16/T6 H (misplaced) | RFH-FDIV-3 30-day EAB TEDE 1.67E-01/3.66E-01/5.82E-01 belongs to 3.7.4.3/3.7.4.3.3 but md places it under RFH-FDSP-1 (3.7.4.4 heading, before its first subsection); values match PDF |
| T064 (RFH-FDIV-3) | L1897–1899 | 78 | T16/T6 H (misplaced) | RFH-FDIV-3 Frequency 4.33E-05/1.19E-03/4.32E-03 belongs to 3.7.4.3/3.7.4.3.3 but md places it under RFH-FDSP-1 (3.7.4.4 heading, before its first subsection); values match PDF |
| T065 (RFH-FDSP-1) | L1921–1923 | 79 | OK | RFH-FDSP-1 30-day EAB TEDE 1.20E-01/3.31E-01/5.05E-01 — values match PDF, correct section |
| T066 (RFH-FDSP-1) | L1928–1930 | 79 | OK | RFH-FDSP-1 Frequency 3.24E-05/8.77E-04/3.36E-03 — values match PDF, correct section |
| T067 (RFH-ESWR-1) | L1960–1962 | 80 | T16/T6 H (misplaced) | RFH-ESWR-1 30-day EAB TEDE 1.20E-01/3.31E-01/5.05E-01 belongs to 3.7.4.6/3.7.4.6.3 but md places it under RFH-LTCA-1 (3.7.4.7/3.7.4.7.1); values match PDF |
| T068 (RFH-ESWR-1) | L1965–1967 | 80 | T16/T6 H (misplaced) | RFH-ESWR-1 Frequency 2.44E-06/1.03E-04/4.02E-04 belongs to 3.7.4.6/3.7.4.6.3 but md places it under RFH-LTCA-1 (3.7.4.7/3.7.4.7.1); values match PDF |
| T069 (RFH-LTCA-1) | L1974–1976 | 80 | OK | RFH-LTCA-1 Frequency 5.12E-06/1.02E-04/3.72E-04 — values match PDF, correct section |
| T070 (RFH-LBCA-BL) | L1994–1996 | 81 | T16/T6 H (misplaced) | RFH-LBCA-BL Frequency 1.95E-05/5.02E-04/1.72E-03 belongs to 3.7.4.8/3.7.4.8.1 but md places it under RFH-LMCA-BL (3.7.4.9/3.7.4.9.1); values match PDF |
| T071 (RFH-LMCA-BL) | L2003–2005 | 81 | OK | RFH-LMCA-BL Frequency 7.51E-04/8.82E-03/2.46E-02 — values match PDF, correct section |
| T072 (LFF-SAO-BL) | L2033–2035 | 82 | OK | LFF-SAO-BL 30-day EAB TEDE 3.82E-03/5.70E-03/9.87E-03 — values match PDF, correct section |
| T073 (LFF-SAO-BL) | L2040–2042 | 82 | OK | LFF-SAO-BL Frequency 3.32E-05/9.10E-04/3.36E-03 — values match PDF, correct section |
| T074 (DHP-LOOP-3) | L2134–2136 | 85 | OK | DHP-LOOP-3 30-day EAB TEDE 1.12E-01/1.62E-01/4.06E-01 — values match PDF, correct section |
| T075 (DHP-LOOP-3) | L2141–2143 | 85 | OK | DHP-LOOP-3 Frequency 1.99E-07/2.26E-06/6.17E-06 — values match PDF, correct section |
| T076 (DHP-LOOP-4) | L2165–2167 | 86 | OK | DHP-LOOP-4 30-day EAB TEDE 1.12E-01/1.62E-01/4.06E-01 — values match PDF, correct section |
| T077 (DHP-LOOP-4) | L2172–2174 | 86 | OK | DHP-LOOP-4 Frequency 6.79E-08/1.52E-06/5.33E-06 — values match PDF, correct section |
| T078 (SUD-CGR-1) | L2428–2430 | 93 | T16/T6 H (misplaced) | SUD-CGR-1 30-day EAB TEDE 7.73E-03/1.77E-02/3.47E-02 belongs to 3.8.4.1/3.8.4.1.3 but md places it under SUD-CGR-2 (3.8.4.2 heading, before its first subsection); values match PDF |
| T079 (SUD-CGR-1) | L2433–2435 | 93 | T16/T6 H (misplaced) | SUD-CGR-1 Frequency 3.44E-07/1.83E-05/6.70E-05 belongs to 3.8.4.1/3.8.4.1.3 but md places it under SUD-CGR-2 (3.8.4.2 heading, before its first subsection); values match PDF |
| T080 (SUD-CGR-2) | L2454–2456 | 94 | OK | SUD-CGR-2 30-day EAB TEDE 7.73E-03/1.77E-02/3.47E-02 — values match PDF, correct section |
| T081 (SUD-CGR-2) | L2461–2463 | 94 | OK | SUD-CGR-2 Frequency 2.25E-07/1.10E-05/4.20E-05 — values match PDF, correct section |
| T082 (RFH-FDIV-2) | L2483–2485 | 95 | OK | RFH-FDIV-2 30-day EAB TEDE 3.88E-01/6.74E-01/1.62E+00 — values match PDF, correct section |
| T083 (RFH-FDIV-2) | L2490–2492 | 95 | OK | RFH-FDIV-2 Frequency 3.06E-07/2.27E-05/8.48E-05 — values match PDF, correct section |
| T084 (RFH-FDIV-4) | L2511–2513 | 95 | OK | RFH-FDIV-4 30-day EAB TEDE 3.88E-01/6.74E-01/1.62E+00 — values match PDF, correct section |
| T085 (RFH-FDIV-4) | L2518–2520 | 95 | OK | RFH-FDIV-4 Frequency 1.66E-07/1.19E-05/4.41E-05 — values match PDF, correct section |
| T086 (RFH-FDSP-2) | L2543–2545 | 96 | T16/T6 H (misplaced) | RFH-FDSP-2 30-day EAB TEDE 2.40E-01/6.62E-01/1.01E+00 belongs to 3.8.5.3/3.8.5.3.3 but md places it under RFH-ESWR-2 (3.8.5.4 heading, before its first subsection); values match PDF |
| T087 (RFH-FDSP-2) | L2548–2550 | 96 | T16/T6 H (misplaced) | RFH-FDSP-2 Frequency 2.41E-06/9.74E-05/3.72E-04 belongs to 3.8.5.3/3.8.5.3.3 but md places it under RFH-ESWR-2 (3.8.5.4 heading, before its first subsection); values match PDF |
| T088 (RFH-ESWR-2) | L2571–2573 | 97 | OK | RFH-ESWR-2 30-day EAB TEDE 1.20E+00/3.31E+00/5.05E+00 — values match PDF, correct section |
| T089 (RFH-ESWR-2) | L2578–2580 | 97 | OK | RFH-ESWR-2 Frequency 4.90E-07/3.40E-05/1.61E-04 — values match PDF, correct section |
| T090 (RFH-ESWR-3) | L2597–2599 | 97 | OK | RFH-ESWR-3 30-day EAB TEDE 1.00E+01/1.40E+01/2.10E+01 — values match PDF, correct section |
| T091 (RFH-ESWR-3) | L2604–2606 | 97 | OK | RFH-ESWR-3 Frequency 3.12E-08/1.38E-06/4.94E-06 — values match PDF, correct section |
| T092 (RFH-LMCA-1) | L2629–2631 | 98 | T16/T6 H (misplaced) | RFH-LMCA-1 30-day EAB TEDE 9.53E-02/1.40E-01/2.09E-01 belongs to 3.8.5.6/3.8.5.6.3 but md places it under RFH-LMCA-2 (3.8.5.7 heading, before its first subsection); values match PDF |
| T093 (RFH-LMCA-1) | L2634–2636 | 98 | T16/T6 H (misplaced) | RFH-LMCA-1 Frequency 1.04E-08/8.82E-07/3.43E-06 belongs to 3.8.5.6/3.8.5.6.3 but md places it under RFH-LMCA-2 (3.8.5.7 heading, before its first subsection); values match PDF |
| T094 (RFH-LMCA-2) | L2655–2657 | 99 | OK | RFH-LMCA-2 30-day EAB TEDE 3.20E+01/4.60E+01/7.00E+01 — values match PDF, correct section |
| T095 (RFH-LMCA-2) | L2662–2664 | 99 | OK | RFH-LMCA-2 Frequency 9.72E-09/8.82E-07/3.48E-06 — values match PDF, correct section |
| T096 (RFH-FDBL-1) | L2688–2690 | 100 | OK | RFH-FDBL-1 30-day EAB TEDE 2.91E-02/4.32E-02/6.36E-02 — values match PDF, correct section |
| T097 (RFH-FDBL-1) | L2695–2697 | 100 | OK | RFH-FDBL-1 Frequency 4.63E-08/6.03E-05/2.09E-04 — values match PDF, correct section |
| T098 (RFH-FDBL-2) | L2714–2716 | 100 | OK | RFH-FDBL-2 30-day EAB TEDE 1.00E+01/1.40E+01/2.10E+01 — values match PDF, correct section |
| T099 (RFH-FDBL-2) | L2721–2723 | 100 | OK | RFH-FDBL-2 Frequency 2.41E-08/6.10E-07/2.33E-06 — values match PDF, correct section |
| T100 (RFH-FDEM-1) | L2746–2748 | 101 | T16/T6 H (misplaced) | RFH-FDEM-1 30-day EAB TEDE 9.53E-02/1.40E-01/2.09E-01 belongs to 3.8.5.10/3.8.5.10.3 but md places it under RFH-FDEM-2 (3.8.5.11 heading, before its first subsection); values match PDF |
| T101 (RFH-FDEM-1) | L2751–2753 | 101 | T16/T6 H (misplaced) | RFH-FDEM-1 Frequency 3.34E-06/8.80E-05/3.27E-04 belongs to 3.8.5.10/3.8.5.10.3 but md places it under RFH-FDEM-2 (3.8.5.11 heading, before its first subsection); values match PDF |
| T102 (RFH-FDEM-2) | L2772–2774 | 102 | OK | RFH-FDEM-2 30-day EAB TEDE 3.20E+01/4.60E+01/7.00E+01 — values match PDF, correct section |
| T103 (RFH-FDEM-2) | L2779–2781 | 102 | OK | RFH-FDEM-2 Frequency 7.28E-09/5.25E-07/1.99E-06 — values match PDF, correct section |
| T104 (RFH-FDET-1) | L2809–2811 | 103 | OK | RFH-FDET-1 30-day EAB TEDE 2.91E-02/4.32E-02/6.36E-02 — values match PDF, correct section |
| T105 (RFH-FDET-1) | L2816–2818 | 103 | OK | RFH-FDET-1 Frequency 5.92E-07/1.61E-05/6.01E-05 — values match PDF, correct section |
| T106 (RFH-FDPI-BL) | L2835–2837 | 103 | OK | RFH-FDPI-BL 30-day EAB TEDE 2.91E-02/4.32E-02/6.36E-02 — values match PDF, correct section |
| T107 (RFH-FDPI-BL) | L2842–2844 | 103 | OK | RFH-FDPI-BL Frequency 1.98E-06/5.10E-05/1.93E-04 — values match PDF, correct section |
| T108 (RFH-FDPI-1) | L2867–2869 | 104 | T16/T6 H (misplaced) | RFH-FDPI-1 30-day EAB TEDE 1.00E+01/1.40E+01/2.10E+01 belongs to 3.8.5.15/3.8.5.15.3 but md places it under RFH-FDRC-1 (3.8.5.16 heading, before its first subsection); values match PDF |
| T109 (RFH-FDPI-1) | L2872–2874 | 104 | T16/T6 H (misplaced) | RFH-FDPI-1 Frequency 1.98E-08/5.10E-07/1.93E-06 belongs to 3.8.5.15/3.8.5.15.3 but md places it under RFH-FDRC-1 (3.8.5.16 heading, before its first subsection); values match PDF |
| T110 (RFH-FDRC-1) | L2893–2895 | 105 | OK | RFH-FDRC-1 30-day EAB TEDE 9.53E-02/1.40E-01/2.09E-01 — values match PDF, correct section |
| T111 (RFH-FDRC-1) | L2900–2902 | 105 | OK | RFH-FDRC-1 Frequency 2.59E-06/6.79E-05/2.50E-04 — values match PDF, correct section |
| T112 (LFF-SAO-1) | L2929–2931 | 106 | OK | LFF-SAO-1 30-day EAB TEDE 9.29E-02/1.48E-01/2.37E-01 — values match PDF, correct section |
| T113 (LFF-SAO-1) | L2936–2938 | 106 | OK | LFF-SAO-1 Frequency 1.19E-08/1.02E-06/4.21E-06 — values match PDF, correct section |
| T114 (LFF-SAO-2) | L2960–2962 | 107 | OK | LFF-SAO-2 30-day EAB TEDE 9.29E-02/1.48E-01/2.37E-01 — values match PDF, correct section |
| T115 (LFF-SAO-2) | L2967–2969 | 107 | OK | LFF-SAO-2 Frequency 1.26E-07/9.13E-06/3.71E-05 — values match PDF, correct section |
| T116 (RRS-CGR-CN) | L3133–3135 | 112 | T16/T6 H (misplaced) | RRS-CGR-CN DBA 2-h EAB/30-d LPZ TEDE 7.75E+00/7.77E+00 belongs to 3.9.4.1/3.9.4.1.3 but md places it under RRS-SPLX-CN (3.9.4.3 heading, before its first subsection); values match PDF |
| T117 (RRS-ISPL-CN) | L3138–3140 | 112 | T16/T6 H (misplaced) | RRS-ISPL-CN DBA 2-h EAB/30-d LPZ TEDE 1.34E-01/5.30E-01 belongs to 3.9.4.2/3.9.4.2.3 but md places it under RRS-SPLX-CN (3.9.4.3 heading, before its first subsection); values match PDF |
| T118 (RRS-SPLX-CN) | L3171–3173 | 113 | T16/T6 H (misplaced) | RRS-SPLX-CN DBA 2-h EAB/30-d LPZ TEDE 8.13E-02/2.78E-01 belongs to 3.9.4.3/3.9.4.3.3 but md places it under RRS-RWG-CN (3.9.4.5 heading, before its first subsection); values match PDF |
| T119 (RRS-SPLA-CN) | L3176–3178 | 113 | T16/T6 H (misplaced) | RRS-SPLA-CN DBA 2-h EAB/30-d LPZ TEDE 8.13E-02/2.78E-01 belongs to 3.9.4.4/3.9.4.4.3 but md places it under RRS-RWG-CN (3.9.4.5 heading, before its first subsection); values match PDF |
| T120 (RRS-RWG-CN) | L3193–3195 | 114 | OK | RRS-RWG-CN DBA 2-h EAB/30-d LPZ TEDE 9.59E-02/9.59E-02 — values match PDF, correct section |
| T121 (RFH-FDIV-CN) | L3219–3221 | 115 | OK | RFH-FDIV-CN DBA 2-h EAB/30-d LPZ TEDE 1.74E+00/3.19E+00 — values match PDF, correct section |
| T122 (RFH-FDSP-CN) | L3247–3249 | 116 | OK | RFH-FDSP-CN DBA 2-h EAB/30-d LPZ TEDE 7.33E+00/7.33E+00 — values match PDF, correct section |
| T123 (RFH-ESWR-CN) | L3267–3269 | 116 | T16/T6 H (misplaced) | RFH-ESWR-CN DBA 2-h EAB/30-d LPZ TEDE 2.01E-02/6.09E-01 belongs to 3.9.5.3/3.9.5.3.3 but md places it under RFH-LTCA-CN (3.9.5.4 heading, before its first subsection); values match PDF |
| T124 (LFF-SAO-CN) | L3315–3317 | 118 | OK | LFF-SAO-CN DBA 2-h EAB/30-d LPZ TEDE 1.33E-01/9.60E-01 — values match PDF, correct section |

요약: LBE 표 88개 중 59개 OK, 29개 misplaced(F1). 표 kind별: freq 45 중 14, dose 34 중 10, DBA 9 중 5가 오배치. 오배치 표의 수신 절: 다음 LBE의 heading 바로 뒤(대부분, 첫 하위절 앞), 다음 LBE의 `LBE Description` 하위절(T061/T062, T067/T068, T070), 또는 다음 3.x.y 절 도입부(T046 → 3.7.3, T059/T060 → 3.7.4). 주의: 3-level heading을 추적하지 않는 검사로는 T059/T060이 OK로 보임(첫 검사에서 27건으로 과소 집계됨) — 검증 스크립트는 모든 level의 절 번호를 추적해야 함.

## 3. Figure inventory

| Figure ID | md lines | raster/vector | image file | debris lines to delete | Notes |
|---|---|---|---|---|---|
| Figure 3.5-1 F-C Chart for LBEs with Uncertainty Bands | L1284 (캡션 `####`), L1286 (image) | raster | `imageFile4.png` (2318×2318, 841,965 B) | 없음 | alt text 비어 있음. PDF p62에서 캡션은 그림 위(일치). x축 "Mean Total Effective Dose Equivalent (REM) at Exclusion Area Boundary (EAB)" (Zero, 0.001–100k), y축 "Event Sequence Mean Frequency (per plant year)" (1E-07–100), 범례 44 family(이 중 12개는 이 장의 LBE ID에 없음)(DHP-L1PP … SUD-LPDC; 이 장에 없는 family: DHS-EIBY, DPI-RESL, IHR-PIPO, OTH-LPDC, RFH-EVTL, RFH-OEFH, RPD-CWAR, RPD-NGS, RPD-SCR, SUD-FACA, SUD-FAS, SUD-LPDC). 점 좌표 수치는 이미지 판독 금지(LBE 표가 원천) |
| (cover) logo | L1 | raster | `imageFile1.png` (1581×454) | L1 | 장식. 7개 PSAR 장과 md5 동일 |
| (cover) site rendering | L3 | raster | `imageFile2.png` (2472×1388) | L3 | 장식(Natrium 부지 렌더링) |
| (cover) logo | L11 | raster | `imageFile3.png` (512×176) | L11 | 장식 |

vector 도식 없음 → label debris/phantom table 없음.

## 4. Heading outline check

의도 outline(PDF 본문 추출 + TOC 대조): H1 `Chapter 3 Licensing Basis Events` 1; H2 3.1–3.14 14; H3 40; H4 143 (LBE 절 106 포함, 제목 끝에 `(ID)`); H5 261 (LBE 하위절 `LBE Description` / `Mechanistic Source Term` / `Radiological Consequences[ Results]` 대부분); 무번호 `References` 7(각 3.x의 H3 권장). 번호 성분 수 최대 5 → H5까지로 충분.

렌더 상태 요약(458 번호 절):

| 형태 | 개수 | 비고 |
|---|---|---|
| `- N.N… Title` list item (정상 제목만) | 390 | 3.10 포함. 승격 규칙으로 일괄 처리 |
| list item + 본문 결합 | 26 | 아래 (c) |
| plain paragraph (제목만) | 15 | 아래 (a) |
| plain paragraph + 본문 결합 | 14 | 아래 (b) |
| 앞 텍스트 뒤에 결합 | 11 | 아래 (d) |
| `#####` heading | 2 | 3.7.4.6.2 (L1945, 형태는 목표 H5와 일치), 3.7.4.7.2 (L1979, 본문 결합) |
| 제목 2줄 분리 | 5 | 아래 (e) (위 분류와 중복 집계) |
| 하위절 순서 오류 | 2 | 아래 (f) |

결함 heading 목록(line, 현재 형태 → 의도 형태/수준):

(a) plain paragraph(15): 3.3.2 L983 →H3; 3.6.3.1 L1375 →H4(+ID 결합); 3.6.4 L1391 →H3; 3.7.1.3 L1494 →H4; 3.7.4.7 L1955 →H4; 3.7.4.9 L1987 →H4; 3.8.2 L2219 →H3; 3.8.2.4 L2255 →H4; 3.8.2.5.1 L2272 →H5; 3.8.2.6 L2280 →H4; 3.8.3.4 L2347 →H4(+ID 결합); 3.8.3.5 L2363 →H4; 3.8.3.7 L2382 →H4; 3.9.2 L3032 →H3; 3.9.4 L3098 →H3.

(b) plain + 본문 결합(14): 3.6.3.2.1 L1385; 3.7.4.2.1 L1852; 3.7.4.5.1 L1935; 3.7.4.8.1 L1983; 3.8.1.10.1 L2204; 3.8.2.3.1 L2249; 3.8.3.6.1 L2376; 3.8.3.7.2 L2388; 3.8.5.12.1 L2786; 3.9.2.3.2 L3061; 3.9.2.4.2 L3067; 3.9.5.5.2 L3283 (이상 H5); 3.12.1.5 L3392 →H4; 3.14.2 L3506 →H3.

(c) list item + 본문 결합(26): 3.1.1.4 L210 →H4; 3.3.4.1.6 L1058; 3.6.4.2.2 L1435; 3.6.4.3.2 L1443; 3.7.4.1.2 L1848; 3.7.4.8.2 L1985; 3.7.4.9.2 L2008; 3.8.5.1.1 L2472; 3.8.5.5.3 L2594; 3.8.5.9.3 L2711; 3.8.5.14.3 L2832; 3.8.7.1.2 L2982; 3.9.4.1.3 L3116; 3.9.4.2.3 L3127; 3.9.4.3.3 L3154; 3.9.4.4.3 L3165; 3.9.4.5.3 L3190; 3.9.5.2.3 L3244; 3.9.5.3.3 L3263; 3.9.5.4.2 L3276; 3.9.5.6.2 L3292 (이상 H5); 3.9.2.3 L3057, 3.9.2.4 L3063, 3.9.5.5 L3279 (→H4, 뒤에 다음 H5 heading 결합); 3.12.1.2 L3350 →H4; 3.14.1 L3493 →H3.

(d) 앞 텍스트 뒤에 결합(11): 3.6.3.1.1 L1377 (앞에 `(RPD-CW1ACS-BL)`); 3.7.4.2.2 L1852; 3.7.4.2.3 L1854; 3.7.4.5.2 L1935; 3.8.1.10.2 L2204; 3.8.3.8 L2388 (→H4, LBE 매몰, H); 3.8.3.8.1 L2388; 3.8.5.12.2 L2786; 3.9.2.3.1 L3057; 3.9.2.4.1 L3063; 3.9.5.5.1 L3279 (이상 H5, 3.8.3.8 제외).

(e) 제목 분리(5): 3.6.3.1 L1375+L1377; 3.8.3.3 L2334+L2336; 3.8.3.4 L2347+L2349; 3.8.4.1 L2402+L2405; 3.8.4.2 L2422+L2425.

(f) 순서 오류(2): 3.8.1.11.2(L2209)가 3.8.1.11.1(L2212) 앞, 본문 L2215/L2217은 둘 다 뒤; 3.8.2.6.1(L2282) 빈 heading, 3.8.2.6.2(L2287) 뒤에 LBE Description(L2290)과 Radiological Consequences(L2292) 본문.

(g) heading이 아닌데 heading인 것: L2602, L2719, L2840 (`#####` 일반 문장), L3508 (`### σ`), L1242 (`#####` 표 주석), L355/L1244/L1264 (`####` sheet 표시), L5/L7 (cover H1/H2), L13/L110/L143 (TOC/LOT/LOF). 수준 오류: L145 Chapter 제목 H4→H1; `#### References` 5개 →H3; 캡션 `#### Table …` 17개 + `#### Figure 3.5-1` →H3(권장).

(h) 본문 끝에 결합된 무번호 heading: `References` L3330(3.11), L3481(3.13).

## 5. File-specific observations and recommendations for the cleanup script

### 5-1. 권장 처리 순서

1. **whitelist 생성(B, 1회)**: PDF p7–132에서 `^(3\.\d+(\.\d+)*)\s+(title)` 추출 → 458개(3.10은 제목이 숫자 `10 CFR`로 시작하므로 정규식에 숫자 허용). 제목이 2–3줄로 wrap되는 LBE(예 3.7.4.2, 3.7.4.3, 3.8.5.1, 3.8.5.2, 3.8.5.6, 3.8.5.7, 3.8.4.1, 3.8.4.2)는 `(ID)`까지 이어 붙여 저장.
2. **캡션 확보 후 cover·TOC 삭제**: LOT(L112–140)에서 캡션 문자열 확보 → L1–143 삭제(메타데이터는 frontmatter로).
3. **표 블록 캡션 map(고정)**: T001–T002 = Table 3.1-1; T003–T006 = 3.1-2; T007–T008 = 3.1-3; T009 = 3.2-1; T010 = 3.2-2; T011 = 3.2-3; T012–T013 = 3.2-4; T014…T027 = 3.2-5…3.2-18; T028 = 캡션 없음(3.3.4.2 본문 표); T029 = 3.5-1; T030–T031 = 3.5-2; T032–T034 = 3.5-3; T035–T036 = 3.5-4. 캡션을 H3(`### Table 3.x-y Title`)로 통일하고 연속 sheet 병합(동일 header 행·반복 group/header 행·`(Sheet n of m)`·`(continued)` 제거).
4. **표 내용 정규화**: source-term 표 header 교체와 Plenum/Non-Plenum 분리(F15), rowspan fill-down(Table 3.1-2 group, 3.1-3 Analysis, 3.5-4 col2–5), Table 3.5-4 5열 header 삽입(F2), group label ` - ` 복원, `Secondary-to-Primary` 복원.
5. **LBE 표 재배치(F1)**: 3.6–3.9 범위에서 문장 정규식 `[^.]*?(frequency|TEDE|dose)[^.]*?are listed below\.`(문장 시작부터 매칭; 행 중간·heading 결합 행 포함; `enveloping` 포함 시 DBA)과 표(header에 `Frequency` / `Enveloping` / 그 외 TEDE)를 kind별 FIFO로 짝지어 표를 문장 직후로 이동. 기대값: dose 34, freq 45, DBA 9, 짝 88. 값으로 짝짓지 말 것(동일 값 표 다수).
6. **heading 복원**: (i) 결합 행 분리 — whitelist의 `번호 + 정확한 제목`이 나타나는 위치 앞뒤로 줄바꿈; (ii) 분리된 제목 결합(F12); (iii) `- ` 또는 평문 번호 줄을 whitelist와 대조 후 `#`×(성분 수) heading으로 변환; (iv) 비-heading 강등(F14); (v) Chapter H1, References H3.
7. **수작업(C)**: 초기조건 표 이동(F6), 3.8.1.11/3.8.2.6 순서(F13), 3.14 수식 블록(5-4), L220–223 중첩, L188/L996 list 표지 제거, Figure 3.5-1 alt text.
8. **문단 결합**(F18) → **문자 수정**(sci-notation, `&lt;`, `●`, stray `.`, 하첨자, `$`/`*` escape) → **공백줄 정규화**.
9. **검증**: heading 458 + References 7, LBE heading 106(ID 포함), 캡션 25, "listed below" 88 = 표 88, 각 LBE의 kind별 표 ≤1, PDF 단어 정렬 ratio 재측정(≥0.99 기대).

### 5-2. 함정(pitfalls)

- `- 2.5 days after the reactor is shutdown …`(L1410)은 `^- \d+\.\d+ ` 형태라 "2.5 절"로 오인될 수 있음 → 반드시 whitelist 대조. 참고문헌 `- 3.1-1 …`, `- 3.12-1 …`(하이픈 번호)과 번호 목록 `- 1. A means …`(L3422–3427)도 heading 아님.
- 본문 속 절 번호 참조("described in Section 3.8.1.6", "Sections 3.2, 3.3, and 5")는 분리 대상이 아님 → 분리는 whitelist 제목까지 정확히 일치할 때만.
- 제목 변형 주의: `Radiological Consequences Results`(3.7.4.3.3, 3.8.4.2.3, 3.9.5.2.3), `Radiological Consequence Results`(3.8.6.2.3), `Intermediate Heat Exchanger Secondary-to-Primary Leak with Passive IAC, (IPI-IHEL-1)`(쉼표 원문), `Release From Ex-Vessel Systems`(3.3.4.1.6, 대문자 From 원문). 일반형 "Radiological Consequences"로 자르면 "Results"가 본문으로 떨어짐.
- "listed below" 문장이 heading과 같은 줄에 있는 경우(L2594, 2711, 2832, 3116, 3127, 3154, 3165, 3190, 3244, 3263)를 누락하지 말 것. 문장 kind 판정은 문장 시작부터 봐야 함: DBA 문장 "The enveloping 2-hour … TEDE … are listed below."를 `TEDE`부터 매칭하면 "enveloping"을 놓쳐 dose로 오분류됨(시뮬레이션에서 실제 발생). 권장 정규식 `[^.]*?(frequency|TEDE|dose)[^.]*?are listed below\.` 후 `enveloping` 포함 여부로 DBA 판정.
- 절 추적은 모든 level(3.x, 3.x.y 포함)로 할 것: T046·T059/T060은 상위 3.x.y heading 뒤로 밀린 경우라 4–5 level만 추적하면 정상으로 보임.
- 3.9.6.1(LFF-SAO-CN)은 PDF에도 `LBE Description` 하위절이 없음(L3301 본문 → 3.9.6.1.1 Mechanistic Source Term). 누락으로 오판 금지.
- Table 3.5-3의 `*`는 "high-consequence BDBE" 표시(주석 L1242). 제거 금지; 주석은 표 직후 평문으로.
- 반복 header를 지울 때 Table 3.2-4 sheet 2의 `|Non-Plenum Release|`, ` |Cumulative …|`, `|Isotope|…|` 3행을 모두 제거해야 병합이 맞음.

### 5-3. 자동 수정 금지(원문 그대로 유지)

- 반복 boilerplate(§1 #33)와 동일 값 LBE 표 — 원문 사실이며 LBE별 레코드임.
- `K-effective 1.0 (for BDBE only) or less`, `K-effective 1.0`(L1086, L1095): PDF에도 관계 기호 없음(p50 확인) → `≤`/`=` 삽입 금지.
- 원문 불일치/오타(보고만): Table 3.5-2 `RRS-ISPL-BL` 제목 "SPS-I Leak at the Cold Trap with Reactor Auxiliary Building Barrier Fails to Retain Release" vs §3.7.3.3 제목 "SPS Leak at the Cold Trap with RAB Barrier Successfully Retains Release"; Table 3.5-2 RFH-LTCA-1 "…Fuel Assemblies…" vs §3.7.4.7 "…Fuel Assembly…"; `TP-LIC-RP-0011`(L3346); `NEI 12-16.The`(L3576); `RFH-FDSP-CN DBA The 5th`(L1926); `IAC, (IPI-IHEL-1)`(L2270). 모두 PDF와 동일.
- 3개 dose 표의 header 변형 `… TEDE Dose [rem]`(L2597, 2714, 2835)은 원문.
- `Pu-239`/`Pu-238`의 `0.00E+00`(Table 3.2-7/3.2-8 2hr)은 원문 값.

### 5-4. 수작업 정답 블록

**3.14.2 수식부(L3506–3561 대체용, PDF p127–129 기준)**

```
### 3.14.2 Methodology

The methodology used to evaluate criticality safety of fresh and spent fuel is described below. Subcriticality is determined by the calculation of k_eff and assuring it is below the Upper Subcritical Limit (USL), while considering additional margin for uncertainty.

The USLs are developed … moderated by water.

The computed k_eff for the system plus twice the Monte Carlo uncertainty (σ) must be less than the USL:

k_eff + 2σ < USL    (Equation 3.14-1)

This ensures that the USL is met at a 95 percent probability and 95 percent confidence level.

The USL is defined as:

USL = 1 + bias – σ_bias – Δ_SM – Δ_AOA    (Equation 3.14-2)

Where,

- Bias is calculated as the difference between the calculated k_eff and the critical experiment model. Because a positive bias can be non-conservative, the bias is set to zero when the calculated average k_eff is greater than 1.0.
- σ_bias is the uncertainty in the bias.
- Δ_SM is an administrative margin, typically 0.05.
- Δ_AOA is an additional subcritical margin to account for extensions in the area of applicability if the available benchmarks are not sufficiently similar to the fuel storage systems.
```
이어서: L3548+L3550 → "… “MCNP User's Manual, Code Version 6.2,” 2017 (Reference 3.14-6). Bias, σ_bias, and Δ_AOA are computed using the guidance provided in NUREG/CR-6698."; L3555 → "… to calculate the bias, σ_bias, and Δ_AOA for an input application. …"; L3559 → "… generally much less than the standard Δ_SM value of 0.05 applied as a general administrative margin. …"; 고아 줄 L3531, 3553, 3557, 3561 삭제. (Obsidian 수식 렌더가 필요하면 두 식을 `$$k_{eff} + 2\sigma < \mathrm{USL}$$`, `$$\mathrm{USL} = 1 + \mathrm{bias} - \sigma_{bias} - \Delta_{SM} - \Delta_{AOA}$$` 로 두고 식 번호는 식 뒤 평문 유지. 코퍼스 공통 규칙으로 결정.)

**L1850–1874 재구성 예(RFH-FDIV-1, PDF p77)**: `#### 3.7.4.2 … (RFH-FDIV-1)` → `##### 3.7.4.2.1 LBE Description` + 본문 → `##### 3.7.4.2.2 Mechanistic Source Term` + "… at an assumed rate of one percent of cover gas volume per day to the environment. The mechanistic source term is summarized in Table 3.2-5." → `##### 3.7.4.2.3 Radiological Consequences` + dose 문장 + 표 `8.38E-02 | 1.83E-01 | 2.90E-01` + freq 문장 + 표 `8.32E-05 | 2.26E-03 | 8.73E-03` → `#### 3.7.4.3 … (RFH-FDIV-3)`.

### 5-5. 재변환 옵션 관련

- LBE 표 오배치(F1)·초기조건 표(F6)는 xycut 순서 문제로 보이며, `--table-method cluster`나 `--markdown-with-html`로 해결되는지는 **검증하지 않았음**. md 단독 결정론 규칙(F1)이 PDF 88/88 정렬로 검증되어 있으므로 우선 적용 권장.
- rowspan(F3, F4, F17)은 `--markdown-with-html`로 보존 가능성이 있으나 미검증. fill-down(A)이 단순함.
- page anchor는 `--markdown-page-separator` 재변환이 가장 확실(B). 대안으로 §0 페이지 map을 절 heading에 부여.

### 5-6. frontmatter 제안 및 추출 가치가 있는 식별자

```yaml
doc_id: Kemmerer-Unit-1-PSAR-Ch3
title: "Kemmerer Power Station Unit 1 PSAR, Chapter 3 — Licensing Basis Events"
applicant: "US SFR Owner, LLC (wholly owned subsidiary of TerraPower, LLC)"
revision: "Revision 1"
copyright_year: 2025
doe_agreement: DE-NE0009054
source_pdf: "references/pdf/TP_Natrium_PSAR2025_ch3_Licensing Basis Events.pdf"
pdf_pages: 132
page_label_offset: "3.1-1 = PDF p7 (map in review §0)"
lbe_counts: {AOO: 11, DBE: 27, BDBE: 47, DBA: 21}
```
(ADAMS Accession No.는 문서에 없음 — 기입하지 말 것.)

- LBE ID(106, 정규식 `[A-Z]{3}-[A-Z0-9]{2,6}-(BL|CN|\d)`; `-BL` baseline, `-CN` DBA): AOO 3.6 — DHP-L1PP-BL, DHP-LOOP-BL, SUD-LOOP-BL, OTH-LMAC-BL, DHS-ISTL-BL, SUD-IACA-BL, RPD-CW1ACS-BL, RPD-SS-BL, RFH-OERC-BL, RFH-LSPC-BL, RFH-LTCA-BL. DBE 3.7 — DHP-L1PP-2, DHP-LOOP-1, SUD-LOOP-1, DHS-ISTL-1/-2, DHS-RNBK-1/-3, SUD-IACA-1, IPI-IHEL-BL, SUD-IHEL-BL, RRS-CGR-BL/-1, RRS-ISPL-BL, RRS-SPLX-BL, RRS-SPLA-BL, RRS-RWG-1/-2, RFH-FDIV-BL/-1/-3, RFH-FDSP-1, RFH-ESWR-BL/-1, RFH-LTCA-1, RFH-LBCA-BL, RFH-LMCA-BL, LFF-SAO-BL. BDBE 3.8 — DHP-L1PP-1/-3/-4, DHP-LAPP-BL, DHP-LOOP-2/-3/-4, OTH-LMAC-1…-4, DHS-ISTL-3/-4, DHS-RNBK-2, SUD-IACA-2, IPI-IHEL-1/-2, SUD-IHEL-1, RPD-CW1ACS-1…-4, RPD-SS-1…-4, SUD-CGR-1/-2, RFH-FDIV-2/-4, RFH-FDSP-2, RFH-ESWR-2/-3, RFH-LMCA-1/-2, RFH-FDBL-1/-2, RFH-FDEM-1/-2, RFH-FDET-BL/-1, RFH-FDPI-BL/-1, RFH-FDRC-1, LFF-SAO-1/-2, RFH-LSPC-1. DBA 3.9 — 21개 `-CN`(SEV-SSE-CN은 DBE 없음 "N/A"). Table 3.5-1…3.5-4 ID 집합과 절 ID 집합 106/106 일치.
- DBE→DBA 매핑: 문장 "This is the most limiting DBE that mapped to the <ID>-CN DBA"(20회) + Table 3.5-4.
- Risk-significant: RFH-FDIV-1, RFH-FDIV-3, RFH-FDSP-1(DBE); RFH-ESWR-2/-3, RFH-FDBL-2, RFH-FDEM-2*, RFH-FDIV-2, RFH-FDPI-1, RFH-FDSP-2, RFH-LMCA-2*(BDBE, * high-consequence).
- 기타: DL function `DL3-RR10`(9회, Table 5.2-3 참조); PDC 10/11/12/15/26/34/62; topical reports NAT-9390-A, NAT-9391-A, NAT-9392-A, NAT-9393-A, NAT-9394-A, NAT-9395-A, NAT-2806-A, NAT-3226-A, TP-LIC-RPT-0011; RG 1.145/1.183/1.233/1.240/1.247/1.249/1.253; 10 CFR 50.34(a)(1)(ii)(D), 50.68(b)(7), 50.155; NEI 18-04/20-09/12-16; ASME/ANS RA-S-1.4-2021; DG-1404; 교차참조 패턴 `Section \d+(\.\d+)+`, `Table \d+\.\d+-\d+`, `Reference 3\.\d+-\d+`.
- 계통 약어(태그 후보): IAC, RAC, PSP, ISP, SCG, SPS(-P/-I), RWG, NHV, NIC, CRD, PHT, IHT, IHX, EVHM, EVST, BLTC, PIC, PRC, SFP, FHB, RXB, RAB, HAA, IVS, NAPS, ARIS, LTA/LDA, EAB/LPZ, TEDE, MST, BEPU, F-C.
