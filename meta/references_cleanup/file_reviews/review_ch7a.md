# Review ch7a: TP_Natrium_PSAR2025_ch7_Descriptions for Safety-Significant SSCs.md (md lines 1–2388, PDF pages 1–132)

범위 경계: L2388(`Main Aerosol Filter Skid`, Figure 7.2.3-2 debris의 마지막 줄) 다음 L2389가 `- 7.2.4 Sodium Processing System`이므로 경계를 가로지르는 표·문단은 없음. PDF p.132(= 7.2-40, Figure 7.2.3-2)가 범위의 마지막 페이지.
검증 도구(재현용, scratchpad): `ch7a_dump.py`(p.1–140 텍스트 캐시 `ch7a_pages.json`), `ch7a_scan*.py`(md 통계), `ch7a_fmt.py`/`ch7a_ul.py`(italic·underline·superscript 추출), `ch7a_pb.py`(page-break 연속성), `ch7a_split.py`, `ch7a_miss*.py`(6-/4-gram 누락 검사), `ch7a_para.py`(pdfplumber 줄간격 기반 문단 경계 대조), `ch7a_figcol.py`(block diagram 채색 → 분류).

## 0. 개요

| 항목 | 값 |
|---|---|
| md 범위 | L1–2388 = 2,388 lines, 282,379 chars, non-blank 1,289 lines, blank 1,099 lines(이 중 surplus blank 263줄, 259개 run) |
| PDF 범위 | p.1(cover), p.2–7(TOC/LoT/LoF, i–vi), p.8–92(= 7.1-1…7.1-85), p.93–132(= 7.2-1…7.2-40). 페이지 환산: 7.1-n → p.(n+7), 7.2-n → p.(n+92) |
| 회전(landscape) 페이지 | p.21, 45, 47, 50, 51, 52, 55, 56, 77, 79, 131, 132 (pypdf `/Rotate 90`) |
| 번호 section heading | 67개(7.1 … 7.2.3.5) + chapter heading 1; **md에서 `#` heading으로 렌더된 번호 heading = 0** |
| 무번호 underlined run-in subheading | 34개(PDF underline 검출) + `References` 7개 |
| 표 | captioned table 19개 + borderless PSF(Function ID) table 7개(41 rows, 10 page-parts) = 26; 그 외 vector-figure 파편 phantom table 25개 |
| 그림 | 22개 = raster 19(image ref 26개; Fig 7.1.2-11이 8 tiles) + vector 3(Fig 7.2.2-1, 7.2.3-1, 7.2.3-2); cover logo 3(imageFile1–3) |
| 본문 완전성 | PDF body line 2,989줄을 md와 6-gram 대조: body 문장 누락 0. 누락은 표 셀(회전 페이지 p.45/p.77)·그림 label에 한정(§1 #1–2, #11) |
| Noise 추정 | TOC 13,405 chars(197 lines/108 non-blank) + cover 511 chars(11/6) + vector-figure debris 2,068 chars(186/101) + caption 속 header 21 chars + PSF 반복 header 3줄 ≈165 chars ≈ **16,170 chars = 5.7 %**(chars 기준); non-blank noise lines 215/1,289 = **16.7 %**; 추가로 surplus blank 263줄 |
| 기타 통계 | lines > 2000 chars: 3(L287 2,202; L689 2,202; L1542 2,025); `&amp;` 3(L141, L488, L2154); `●` 0(PDF bullet 140개는 모두 `- `로 변환됨); `Kemmerer Unit 1 PSAR` 잔여 1(L459); `Revision 1`/footer 잔여 0; change bar 잔여 0; non-ASCII는 “ ” ° – ® © − 만 존재(PUA·NBSP·ligature 0) |

## 1. Findings

| # | T-ID | Sev | Count | md lines (examples) | PDF p. | Evidence / description | Proposed fix | Fix class |
|---|---|---|---|---|---|---|---|---|
| 1 | T6/T14 | **H** | 4 cells | L855–858 | 45 (rotated) | Table 7.1.2-4 `Notes` 열 소실/절단. PDF는 RV·Reactor Head·Rotatable Plug·Instrument Drywells 4행 모두 `Primary coolant boundary component`. md: RV `Primary coolant`(절단), `|Reactor Head|…|Argon gas, sodium vapor and aerosols| |`(통째 소실), Rotatable Plug(소실), Instrument Drywells `Primary coolant`(절단). 같은 페이지 Note 1도 `described i Section 13.2.1`(L870; PDF `described in`) 1자 절단. 회전 페이지에서만 발생(메커니즘 미확인) | pdfplumber `extract_tables()`(p.45)로 셀 재추출해 교체; L870 `i`→`in` | B |
| 2 | T6/T14 | **H** | 3 cells | L1294–1296 | 77 (rotated) | Table 7.1.3-6 `Notes`: PSP 행 빈 셀(PDF `Primary coolant boundary component`), IHX Non-Tubing·IHX − Tubing `Primary coolant`(절단). 추가로 `IHX Non-Tubing Components Tubesheet, Riser…`는 PDF `Components - Tubesheet`(` - ` 소실), Base Material `SA-965 F304H SA-240 304H`는 2줄 값이 구분 없이 병합 | #1과 동일(p.77 재추출); 2줄 셀은 `<br>` 또는 `; `로 구분(원문 보존 원칙상 `<br>` 권장) | B |
| 3 | T8 | **H**(1)/M(4) | 5 | L450, L452, L1263 | 19, 74 | `3.98 x 1015 n/cm2-s`(PDF 3.98 × 10^15 n/cm²-s → 값이 1015로 오독 가능), `5,473 W/in3 (334 W/cm3)`, `40,000 gpm (150 m3/s)`. PDF 본문 superscript(size 7.68)는 범위 전체에서 이 5개 + ®2개뿐(® 는 보존됨) | 화이트리스트 치환 `x 1015`→`x 10^15`(또는 `10<sup>15</sup>`; corpus 공통 규약 1개 선택), `cm2`→`cm²`, `in3`→`in³`, `cm3`→`cm³`, `m3`→`m³`. `150 m3/s`는 원문 값(40,000 gpm ≈ 2.52 m³/s ≈ 151 m³/min이므로 원문 오류로 보이나) **수치·단위 수정 금지**, superscript만 복원 | A(whitelist) / B(size 기반 검출) |
| 4 | T6/T16 | **H** | 7 tables / 41 rows | L328–370, L616–639, L1014–1037, L1381–1409, L1577–1585, L1766–1770, L1955–1987 | 14–15, 31–32, 63, 86, 96, 108, 122–123 | Borderless PSF 표(`Function ID | Function Description | <Sys> Functional Support`, header underline)가 표가 아닌 문단/리스트로 평탄화. (a) header 줄이 첫 row와 한 줄로 병합(L328 `Function ID Function Description RCC Functional Support DL3-RC1 Scram - Gravity Driven Absorber`); (b) **5개 row에서 description의 둘째 줄(=분류 태그 포함)이 support 문장 뒤로 밀림**: L332 `Insertion by Latch Release (SR)`, L620 `absorber insertion by latch release (SR)`, L1385 `(NSRST)`(DL2-HR2), L1581 `(SR)`(DL3-HR4), L1770 `(NSRST)`(DL4-HR1 IAC); (c) SCG DL3-RR1c support 문장 분할(L1955→L1957); (d) page-break 반복 header 3줄(L349, L635, L1973); (e) 41 row 중 16개만 `- ` 리스트, 25개는 plain(형식 불일치). row 누락은 없음(PDF ID 순서와 일치: RCC 10, RES 5, PHT 8, IHT 7, RAC 2, IAC 1, SCG 8) | 7개 표를 Markdown table로 재구성: `Function ID | Function Description | Safety Classification(SR/NSRST, 괄호에서 분리하되 원문 괄호도 유지) | <Sys> Functional Support`; 반복 header 제거; DL5-PAM1(SCG) 셀 내 bullet은 `<br>• ` 로 보존. pdfplumber words의 x0 열 경계(ID ≈162–225, Desc ≈226–400, Support ≥400 pt; 표마다 확인)로 재구성 | B(+C 검수) |
| 5 | T3 | M(→H for chunking) | 67 | L213, L218, L383, L415, L463, L930, L1151, L1523 | 8–128 | 번호 heading 67개 중 `#` heading 0; list item 63(`- 7.1.1 Reactor Core System`), plain paragraph 4(L383, L463, L930, L1523); 본문과 glued 4(L383 `7.1.1.3 Design and Performance Evaluation The core assemblies…`, L415 `7.1.1.3.2 Methods and Analyses Methods and analyses…`, L1151 `7.1.3.2.3 System Design and Performance Evaluation Preliminary design…`, L1523 `7.2 Reactor Auxiliary Systems Reactor Auxiliary Systems consist of…`) | `^(- )?(7(\.\d+)+)\s+(Title)` → `#`×(dot 수+1) (7.1→`##`, 7.1.1→`###`, 7.1.1.1→`####`, 7.1.1.3.1→`#####`). glued 4건은 TOC/§4 목록의 정확한 title 문자열 길이로 분리 | A |
| 6 | T3 | M/**H**(end-glued 6) | 34 + 7 | start-glued: L248, L263, L275, L296, L326, L379, L535, L645, L667, L710, L759, L1345, L1424, L1549, L1575, L1589, L1733 (+L287, L289 첫 항목); mid-glued: L287×3, L289, L689, L1597, L1772×2; **end-glued: L608, L737, L1060, L1373, L1413, L1758**; plain: L1010; References glued: L439(start), L2141(end) | 9–108 | PDF의 underlined 무번호 subheading 34개(Fuel/Reflector/Shield/Material Surveillance/Neutron Source/Simulated Core/Compressive/Lead Demonstration/Lead Test Assembly = 9; Regulatory Criteria ×5; Functional Requirements and Design Criteria ×6; Seismic Classification and Design Codes ×5; Regulatory Guidance ×5; Reactor Vessel and Head; Reactor Internal Structures; Guard Vessel; Reactor Support Structure)가 heading으로 인식되지 않음. 19 start-glued, 8 mid-glued, 6 end-glued(앞 문단 끝에 붙어 **이전 섹션 chunk에 귀속**: 예 L608 `…Section III, Division 5. Functional Requirements and Design Criteria`, L737 `…as described in Section 3.14. Guard Vessel`), 1 standalone plain(L1010). `References` 7개 중 5개만 `### References`, 2개 glued(L439 `References 7.1.1-1 TerraPower, …`, L2141 `…according to safety significance. References`) | 위치별(line+offset) 화이트리스트로 분리 후 heading 승격(부모 번호 heading level+1, 최대 `######`). `Guard Vessel`, `Reactor Support Structure`, `Reactor Internal Structures`는 본문·figure label에도 등장하므로 **정규식 전역 치환 금지**—§4의 line 목록으로만 적용 | A(line-specific whitelist)/C |
| 7 | T5 | M | 74 | page-break 22: L232→235, L303→306, L322→324, L523, L542, L556, L579, L606, L761, L948, L967, L987, L1210, L1440, L1542, L1554, L1571, L1630, L1895, L1908, L1926, L1939; in-page 52: L241→243 `- shown in Figure 7.1.1-1…`, L263→265, L296→298, L1632→1634 … (§5-B 전체 목록) | 8–121 | 문단 분할 74건: continuation이 list item으로 된 것 56(`- shown in…`, `- described in Section 6.4.1…`, `- Section 7.1.4)…`, `- (Reference 7.1.3-1) as endorsed…`), plain 문단 18(L235 `Intermediate Heat Exchangers enters…`, L324, L441, L523, L542, L556, L579, L761, L799, L948, L961, L967, L987, L1210, L1440, L1542, L1571, L1630). in-page 분할은 PDF 줄이 `Section N`, `described in`, `(Reference`, `Figure N`, `in Section`으로 시작할 때 체계적으로 발생. 이 중 52는 page break가 아님(PDF 동일 페이지 중간) | 재결합 규칙: 앞 블록이 종결부호 `[.:;?!)]`로 끝나지 않고 다음 블록이 소문자/`Section \d`/`Figure \d`/`(Reference`/`Division \d`로 시작 → 공백 1개로 join, 선행 `- ` 제거. 예외: 대문자 시작 page-break 2건(L235, L987)과 `)`로 끝나는 L1632→1634는 line 목록으로 처리. 진짜 소문자 bullet L472–476은 제외 | A(+line list) / B(page-break 목록) |
| 8 | T5(역방향)/T3 | M | 63 경계 / 33 lines | L287(8 경계, 2,202 chars), L289(4), L649(5: RG 1.31·1.36·1.44 제목+conformance), L689(3), L710(3), L1589(5), L1772(5: Safety classifications + Regulatory Guidance + RG 1.36 + conformance + Seismic… + Codes…), L1542(2), L400, L1422, L1597 | 11–108 | pdfplumber 줄간격(본문 14.0 pt, 문단 25.0 pt; p.11·12·94 확인)으로 얻은 PDF 문단 681개 중 63개 경계가 md에서 한 줄로 병합(±2 FP). RG 목록에서 `RG 1.xx, Revision n, <title>` 줄과 `Full/Partial Conformance.` 문단이 병합되어 RG별 record 경계 소실 | PDF 문단 경계 oracle(gap > 20 pt)로 재분할; 또는 A 규칙: run-in heading 경계, `(?<=\. )RG 1\.\d+, Revision`, `(?<=\. )(Full|Partial) [Cc]onformance\.` 앞에서 개행 | B / A(부분) |
| 9 | T5/T3 | M | 240 | L336 `- DL3-HR5…`, L303 `- Consistent with PDC 10…`, L1999–2000 `- Regulatory Guide 1.44…` | 12–125 | 범위 내(TOC 이후) list item 428개 중 PDF bullet(●, 140개)에 대응하는 진짜 list는 140+번호목록 3뿐. 가짜 list marker 240 = `- Consistent with PDC` 99(PDF는 bullet 없는 문단; 117개 PDC 문단 중 99개가 `- `, 17 plain, 1 mid-line glued L296) + 번호 heading 63 + continuation 56 + DL row 16 + RG 2 + 표 각주 4(L866, L867, L1299, L1300). reference entry 45개(`- 7.1.2-1 …`)는 PDF hanging-indent 목록이므로 list 유지 가능(L) | `^- (?=Consistent with PDC \d)` 제거 등 패턴별 제거; heading/continuation은 #5·#7에서 처리 | A |
| 10 | T7 | M | 3 figs / 186 lines / 2,068 chars | L1830–1831; L2201–2294; L2298–2387 | 113, 131, 132 | Vector diagram label 파편: Fig 7.2.2-1은 1-cell table(`|BOTTOM<br><br>DAMPER<br><br>TOP DAMPER…|`, `<br>` 30개, label 순서 scramble, `IAC HEATER BLOWER`처럼 label 병합); Fig 7.2.3-1은 phantom table 11개(`|NGA| |`, `|NHV|`, `|NST|`, `|NSRST|`, `|SR|`, `|NonSCG|`, `|Exhaust Distribution Cabinet| | |`+빈 행 2) + label 문단 23; Fig 7.2.3-2는 phantom table 13 + label 문단 16. 범위 내 phantom table 25개 = single-column 14, empty header cell 11, all-empty rows 12 전부 여기서 발생(실제 captioned table 19개에는 column mismatch·empty header·`<br>` 0) | caption heading만 남기고 debris span 삭제, `> [Figure: vector diagram – see PDF p.131]` 형태 placeholder. 필요 시 #11의 분류 목록을 C로 추가 | A(span 삭제) |
| 11 | T7/T14 | M | ≈60 boxes | L1992(본문이 그림을 분류 근거로 인용), L2199–2387 | 131, 132 | Fig 7.2.3-1/-2의 SSC 분류는 **박스 채색**(legend: NST=green, NSRST=blue, SR=red, Non-SCG=gray)으로만 표시 → md에서 완전 소실. pdfplumber fill color로 복원 가능(검증함): 7.2.3-1 SR = Primary Overpressure Protection Skid, Primary Filter Skid; NSRST = Supply Isolation Valve Skid, Gas Routing Valve Skid, Primary GFIMS Cabinet, Failed Fuel Monitoring Cabinet, Gamma Spectroscopy Analysis Cabinet, Tag Gas Analysis Cabinet, Exhaust Distribution Cabinet, Guard Vessel Leakage Detection/Recirculation Skid, Vapor Trap Cell Liner; NST = Cover Gas Main Line/CRDM Shield Port Purge/CRDM Scram Cylinder/CRDM Drive Line/CRDM Housing/PSP/Static Seal Pressure/Purge/RV-GV Annulus Module, Primary Local Accumulator Skid; Non-SCG = NGA, NHV×2, IVTM/FTL/RP, PSPs, CRDMs, Reactor Vessel Cover Gas, PSP Lube Oil Skids, RWG, RV to GV Annulus. 7.2.3-2 NSRST = Loop A/B Control Module, Sampling Aerosol Filter Skid, Expansion Tank A/B·Drain Tank A/B·Supplemental Drain Tank Overpressure Protection Skid, Main Aerosol Filter Skid(연청색 0.87/0.92/0.96도 NSRST로 판단—legend에 별도 항목 없음); NST = Intermediate Local Accumulator Skid, Purge Control Module, Intermediate GFIMS Cabinet A/B, Oil Bubbler Skid, Intermediate Overpressure Discharge Skid; Non-SCG = NGA, NHV, ISP A/B, Expansion Tank A/B, Drain Tank A/B, Supplemental Drain Tank, ISP A/B Lube Oil Skid. 추가로 md debris에 오른쪽 아래 `NHV` 1개 누락(2개 중 1개) | debris 대신 "Figure 7.2.3-1 classification legend (derived from PDF fill colour)" 목록을 명시적 표기와 함께 삽입(원문 문장이 아님을 표시) | C(B로 추출) |
| 12 | T7 | L | 26 refs | L457…L1713; L914–928 | 20–104 | raster figure 19개, image ref 26개 모두 alt text 빈 값. Fig 7.1.2-11은 raster tile 8개(imageFile16–23, L914–928: 1006×1005 등 조각)로 분할; 그림 callout 4개(`Isolation Spring Unit`, `Insulation Barrier Creates Stagnant Air Cavity Where Isolation Units are Installed`, `SIS Shielding Reduces Lifetime Dose to Isolation Units`, `Isolation Damper Unit`)는 CID-encoded font라 추출 불가 → 소실 | alt = caption 텍스트(A). tile 8개는 유지하되 한 figure block으로 묶음 표시; 필요 시 p.56 페이지 렌더를 1장 이미지로 교체(B, `--image-output`) | A/B |
| 13 | T1 | L(M) | 11 lines / 511 chars | L1–11 | 1 | cover: imageFile1(Natrium logo)·imageFile2(site rendering)·imageFile3(TerraPower logo), `# Kemmerer Power Station Unit 1 PSAR, Chapter 7`, `## US SFR Owner, LLC, …`, `SUBJECT TO DOE COOPERATIVE AGREEMENT NO. DE-NE0009054 Copyright © 2025 …` | YAML frontmatter로 이동 후 삭제 | A |
| 14 | T2 | M | 197 lines / 118 entries / 13,405 chars | L13–209; merged L92(5 entries), L144(2), L188(6) | 2–7 | TOC+LoT+LoF 전체(chapter 전체 범위, 7.3–7.8 포함; 담당). dot-leader 108줄, entry 118개(= PDF 118, 누락 없음). 한 줄에 여러 entry 병합 3줄, list가 아닌 TOC 줄 5개(L43 `7.5 Ancillary Systems…`, L52, L72, L94, L209), 첫 entry가 `### Chapter 7 …. . . 7.1-1`(L13, heading 오승격), `TABLE OF CONTENTS/LIST OF TABLES/LIST OF FIGURES` 제목 부재, `&amp;` 1(L141), 계층 들여쓰기 소실 | 삭제(heading에서 재생성 가능). 삭제 전 page 번호는 page-anchor 검증용으로 추출(§5) | A |
| 15 | T4 | L/M | 1 | L459 `### Kemmerer Unit 1 PSAR Figure 7.1.1-2 Illustration of Reactor Core Loading Pattern` | 21 (rotated) | 회전 페이지의 running header가 caption에 병합(다른 회전 페이지 p.47/50/51/52/55/56/79의 caption은 정상) | `^(#+ )Kemmerer Unit 1 PSAR\s+` → `$1` | A |
| 16 | T13 | M | 132 italic + 44 underline | PDC: L296…L1942(117 paragraphs); RG: L645, L649(3), L651, L655, L659, L663, L1418, L1422, L1589(2), L1591, L1595, L1772 | 12–121 | italic 132 span 전부 소실: PDC criterion title 117(`Consistent with PDC 2, *Design bases for protection against natural phenomena*,`), RG title 15(`RG 1.20, Revision 4, *Comprehensive Vibration…*`). underline은 run-in heading 34 + PSF header 10줄(#4, #6에서 구조로 대체) | pdfplumber italic span 목록(`ch7a_fmt.json`, 132개)을 순서대로 exact-match하여 `*…*` 적용; PDC는 A 패턴 `(Consistent with PDC \d+, )(<title>)(,)`도 가능하나 title 끝 판정이 모호하므로 B 권장 | B |
| 17 | T6/T12 | M | 5 | L866–867, L1299–1300, L2197 | 45, 77, 130 | 표 각주 marker 훼손: PDF `*ASME BPVC Section II, Part A…`/`**ASME BPVC Section III, Division 5…` → md `- ASME BPVC Section II…`(`*`가 list marker로 소비), `- *ASME BPVC Section III…`(`*` 1개만 잔존) → header `Base Material*`/`Weld Material**`와의 대응 소실. L2197 `* Classification is for integrity of the associated pressure boundary only`는 Markdown bullet로 파싱되어 `*` 의미(SR*/NSRST* 대응) 소실 | `\*ASME BPVC Section II…`, `\*\*ASME BPVC Section III…`, `\* Classification…`로 escape(목록 marker 제거) | A |
| 18 | T6 | M | 2 group rows | L2170 `|Primary SCG| |`, L2191 `|Intermediate SCG| |` | 130 | Table 7.2.3-1의 group label이 빈 분류 셀을 가진 data row로 존재 → row 단위 chunk에서 23개 row가 subsystem 문맥을 잃음. `Failed Fuel Monitoring … for PostAccident Monitoring (PAM)`(L2184; PDF `Post-`+줄바꿈+`Accident`) | `Subsystem` 열 추가(Primary SCG/Intermediate SCG) 후 group row 삭제; `PostAccident`→`Post-Accident` | A |
| 19 | T6 | L | 3 cells | L1702, L1703, L1295 | 103, 77 | 2줄 셀 값이 구분 없이 병합: `150 (inlet stack) 525 (outlet stack)`, `150 (inlet duct) 525 (outlet duct)`, `SA-965 F304H SA-240 304H` | `<br>` 삽입(원문 줄 구조 보존) | B/A(line-specific) |
| 20 | T11 | L/M | 6 | L691 `fastneutron`, L2184 `PostAccident`, L2270/L2306 `NonSCG`(debris), L488 `I&amp;C`, L2154 `Concrete &amp; Commentary` (+L141 TOC) | 35, 130, 131–132, 23, 129 | 줄끝 hyphen 제거로 인한 join(PDF `fast-`/`neutron`; 같은 문장 뒤에 `Fast-neutron` 사용), HTML entity | `fastneutron`→`fast-neutron`, `PostAccident`→`Post-Accident`; `&amp;`→`&` | A |
| 21 | T12 | L | 14 | L853, L1292(`Base Material*|Weld Material**`), L2171/2175/2180–2182/2185/2188–2190(`SR*` 2 + `NSRST*` 7 = 9 cells), L867, L1300, L2197 | 45, 77, 130 | 현재는 right-flanking이라 emphasis로 파싱되지 않지만 편집 시 쉽게 italic/bold로 오파싱. `SR*`의 `*`는 의미(각주) 보유 | `\*` escape; 의미 보존 | A |
| 22 | T15 | M | — | 파일 전체 | — | YAML frontmatter 없음, page anchor 없음(`include-header-footer=off`, page separator 미사용). PDF metadata Title: `TerraPower, LLC., - Submittal of Revisions to the Construction Permit Application for the Natrium Reactor Plant, Kemmerer Power Station, Unit 1` | frontmatter: `doc: Kemmerer Unit 1 PSAR`, `chapter: 7`, `title: Descriptions for Safety-Significant SSCs`, `revision: 1`, `owner: US SFR Owner, LLC (TerraPower)`, `doe_agreement: DE-NE0009054`, `copyright: 2025`, `source_pdf`, `pdf_pages: 372`; page anchor는 `--markdown-page-separator "<!-- page %page-number% -->"` 재변환 또는 6-gram 정렬(`ch7a_l2p.py`)로 삽입 | B |
| 23 | T3 | L | 5 + 46 | L5 `#`, L7 `##`, L13 `###`, L211 `### Chapter 7 Descriptions for Safety-Significant SSCs`; caption 41개와 `### References` 5개 | 1–132 | cover 문구가 H1/H2, TOC 첫 줄이 H3로 오승격; 실제 chapter heading L211은 `###`(→`#`). caption(19 table + 22 figure)과 References가 모두 `###`로 번호 heading보다 **상위** level이 됨 | L211 → `#`; caption·References → 소속 system section(###)의 자식 `####` | A |
| 24 | T5 | L | 3 lists / 263 blank lines | L1043/1046, L2050/2053, L2080/2083 | 64, 126, 127 | page break에서 list 사이에 blank 2줄 삽입(loose list), 문단 사이 blank 2–3줄 run 259개 | 연속 blank → 1줄; list 내부 blank 제거 | A |
| 25 | T6 | L | 3 | L824–826 `- 1. Analysis…`, `- 2. CMTRs…`, `- 3. 100% volumetric…` | 42 | Table 7.1.2-1 Note 1의 번호목록이 bullet+번호로 렌더 | `- 1.`→`1.` | A |
| 26 | T16 | M | #4의 5 rows + #10 | L332, L620, L1385, L1581, L1770; L1830 | 14, 31, 86, 96, 108, 113 | reading order 오류는 borderless 3-column 표의 첫 row(각 표의 첫 page-part)에서 반복 발생 + vector label 순서 scramble | #4, #10으로 해결 | B |
| 27 | T14 | 확인 | 0 | — | 8–130 | 본문(표·그림 제외) 누락 없음: 2,989 PDF body line 중 6-gram 무매칭 17줄은 모두 다열(table/PSF) interleave. 4-gram 부분 검사에서도 본문 문장 절단은 L870(`i`) 1건뿐 | — | — |
| 28 | (확인) | — | 7 lists | L422–425, L781–786, L1101–1106, L1474–1478, L1646–1650, L1791–1795, L2130–2135 | 17, 41, 66, 89, 99, 109, 128 | `- Design Reliability Assurance Program` 7회(범위 내)는 system별 Special Treatments 목록(RCC, RES, PHT, IHT, RAC, IAC, SCG)의 **진짜 반복**(PDF bullet로 확인). 중복 제거 금지 | 유지 | — |

## 2. Table verification log

전수 검증(26개 ≤ 30): pdfplumber `extract_tables()` + 페이지 렌더(p.19, 45, 74, 77 시각 확인). 수치 표는 모든 값을 셀 단위로 대조.

| Table ID | md lines | PDF p. | Status | Notes |
|---|---|---|---|---|
| 7.1.1-1 Reactor Core Design Parameters | L443–452 | 19 | T8(H) | 6 rows 값 일치(840 MWt; 680°F (360°C); 950°F (510°C); 0.67). `3.98 x 1015 n/cm2-s`(10^15, cm²), `5,473 W/in3 (334 W/cm3)` superscript 소실 |
| 7.1.2-1 RES Safety Classification and ASME Code Applicability | L808–826 | 42 | OK / T6-L | 8 rows·3 cols 일치(HBB/HBA/NB/HGB/HFA, GV `Section VIII, Division 1 (Note 1)`). Note 1 번호목록 `- 1.` 형식만 |
| 7.1.2-2 Applicable Codes and Standards | L829–835 | 43 | OK | 3 rows 일치(`Rules for Constructions of…`는 원문 표기) |
| 7.1.2-3 Preliminary RES Dimensions | L838–848 | 44 | OK | 415.5 / 453 / 433.5 / 797 / 2 / 1 / 12 (in) 전부 일치 |
| 7.1.2-4 Preliminary RES Design Temperature, Service Environment, and Materials | L851–870 | 45 (rotated) | **T6/T14(H)**, T12, T14 | Notes 4셀 소실/절단(§1 #1); 1050/800/650°F, SA-240 316H, SA-965 F316H, SA-213 TP316H, SA-387 Gr 22 Cl 1, SA-182 Gr F22 Cl 1 일치; 각주 `*`/`**` 훼손(L866–867); Note 1 `described i` |
| 7.1.3-1 Monitored PHT Parameters | L1234–1247 | 72 | OK | 10 rows Yes/No 일치 |
| 7.1.3-2 PSP Major Components Safety Classifications | L1250–1256 | 73 | OK | 3 rows SR |
| 7.1.3-3 PSP Preliminary Design Performance Characteristics | L1259–1267 | 74 | T8(M) | `150 m3/s`(m³) superscript 소실; 300 ft (90 m), 80%, 3.5 - 5 s, 1,050°F (566 °C) 일치; `at @`는 원문 |
| 7.1.3-4 IHX Major Components Classifications | L1270–1276 | 75 | OK | SR/SCS1 ×3 |
| 7.1.3-5 IHX Preliminary Design Performance Characteristics | L1279–1287 | 76 | OK | 1,450 MBtu/hr (425 MWth); 950/510; 680/360; 620/330; 910/490 일치 |
| 7.1.3-6 Preliminary PHT Design Temperature, Service Environment, and Materials | L1290–1300 | 77 (rotated) | **T6/T14(H)**, T12 | Notes 3셀 소실/절단(§1 #2); ` - ` 소실; 2-material 셀 병합; 각주 훼손(L1299–1300) |
| 7.1.4-1 IHT Safety and Seismic Classifications | L1496–1504 | 90 | OK | 5 rows(NSRST/SCN1 ×4, SR/SCS1 ×1) 일치 |
| 7.1.4-2 Applicable Codes and Standards | L1507–1516 | 91 | OK | 6 rows 일치 |
| 7.2.1-1 RAC Safety Classifications | L1669–1682 | 101 | OK | 10 rows(SR 7, NSRST 3) 일치 |
| 7.2.1-2 Applicable Codes and Standards | L1685–1693 | 102 | OK | 5 rows 일치(md가 PDF text layer의 `ANSI/AISCN690` 공백 누락을 오히려 정상화) |
| 7.2.1-3 Preliminary Material Selection and Design Temperatures for RAC | L1696–1709 | 103 | T6-L | 7 rows 값 일치(525/150); 2줄 값 병합 2셀(L1702–1703) |
| 7.2.2-1 IAC Safety and Seismic Classifications | L1810–1816 | 111 | OK | 3 rows NSRST/SCN1 |
| 7.2.2-2 Applicable Codes and Standards | L1819–1825 | 112 | OK | 3 rows |
| 7.2.3-1 SCG Major Equipment Safety Classifications | L2166–2197 | 130 | T6-M, T11, T12 | 25 rows(= PDF) 분류값 전부 일치(SR* 2, SR 3, NSRST* 7, NSRST 11, group 2). group row 2(L2170, L2191), `PostAccident`, 각주 `* Classification…` bullet화 |
| PSF table RCC (Function ID / Description / RCC Functional Support) | L326–370 | 14–15 | **T6/T16(H)** | 10 rows(DL3-RC1, RR2, HR5, HR6, HR7, HR8, HR9, HR10, HR13, DL4-RC3) 존재; DL3-RC1 description 분할(L328/L332); 반복 header L349; list/plain 혼재(6/4) |
| PSF table RES | L611–639 | 31–32 | **T6/T16(H)** | 5 rows(DL3-RC1, HR4, HR5, RR1, DL4-RR1); DL3-RC1 분할(L616/L620); 반복 header L635 |
| PSF table PHT | L1012–1037 | 63 | T6(M) | 8 rows(DL3-HR1, HR2, HR5, RR1a, RR1d, DL4-HR1, HR2, HR6) 내용 완전, 표 구조 없음. DL4-HR1 support가 DL3-HR5와 동일 문장인 것은 원문 |
| PSF table IHT | L1376–1409 | 86 | **T6/T16(H)** | 7 rows(DL2-HR2, DL4-HR7, DL3-HR3, DL3-HR12, DL4-HR1, DL4-HR3, DL4-DID1; PDF 순서 동일); DL2-HR2 `(NSRST)` 분리(L1385) |
| PSF table RAC | L1575–1585 | 96 | **T6/T16(H)** | 2 rows; DL3-HR4 `(SR)` 분리(L1581) |
| PSF table IAC | L1761–1770 | 108 | **T6/T16(H)** | 1 row; DL4-HR1 `(NSRST)` 분리(L1770) |
| PSF table SCG | L1953–1987 | 122–123 | T6/T16(M) | 8 rows(DL3-RR1c, RR7, DL4-HR1, DL2-RR10, DL4-RR4, RR4a, RR4c, DL5-PAM1); DL3-RR1c support 분할(L1955/L1957); 반복 header L1973; DL5-PAM1 셀 내 bullet 5개(L1983–1987) 보존됨 |

요약: captioned table 19개 중 column 누락·행 누락·column 밀림 0; 값 소실 7셀(2개 회전 페이지 표), superscript 소실 5, 셀 병합 3, 각주 marker 훼손 3표. PSF table 7개(41 rows)는 row 누락 0이나 표 구조 0, 분류 태그 분리 5 rows.

## 3. Figure inventory

| Figure ID | md lines | raster/vector | image file | debris lines to delete | Notes |
|---|---|---|---|---|---|
| 7.1.1-1 Core Assembly Configuration | L455–457 | raster | imageFile4 | — | labels는 raster 내부; alt 빈 값 |
| 7.1.1-2 Illustration of Reactor Core Loading Pattern | L459–461 | raster | imageFile5 | — | caption에 header 병합(T4, p.21 rotated) |
| 7.1.2-1 Simplified RES General Arrangement | L872–874 | raster | imageFile6 | — | |
| 7.1.2-2 Simplified Reactor Head Configuration | L876–878 | raster | imageFile7 | — | p.47 rotated, caption 정상 |
| 7.1.2-3 Simplified Rotatable Plug Assembly GA | L880–882 | raster | imageFile8 | — | |
| 7.1.2-4 Simplified Reactor Fixed Internals GA | L884–886 | raster | imageFile9 | — | |
| 7.1.2-5 Simplified Core Barrel Structures GA | L888–890 | raster | imageFile10 | — | p.50 rotated |
| 7.1.2-6 Simplified Guard Vessel GA | L892–894 | raster | imageFile11 | — | p.51 rotated |
| 7.1.2-7 Simplified Reactor Support Structure Arrangement | L896–898 | raster | imageFile12 | — | p.52 rotated |
| 7.1.2-8 Primary Coolant Flowpath | L900–902 | raster | imageFile13 | — | |
| 7.1.2-9 Sodium Pool Regions | L904–906 | raster | imageFile14 | — | |
| 7.1.2-10 Simplified Diagram of Well Seal and HAA Seal | L908–910 | raster | imageFile15 | — | p.55 rotated |
| 7.1.2-11 Simplified Seismic Isolation System Arrangement | L912–928 | raster (8 tiles) | imageFile16–23 | — (image ref 7개는 중복성 noise, 그룹화 권장) | callout 4개 CID font → 추출 불가, 소실; p.56 rotated |
| 7.1.3-1 Simplified PHT Flow Diagram | L1303–1305 | raster | imageFile24 | — | |
| 7.1.3-2 Simplified RAC and PHT Process Flow Diagram | L1307–1309 | raster | imageFile25 | — | p.79 rotated |
| 7.1.3-3 Sectional View of Installed PSP | L1311–1313 | raster | imageFile26 | — | |
| 7.1.3-4 Intermediate Heat Exchangers | L1315–1317 | raster | imageFile27 | — | |
| 7.1.4-1 Intermediate Loop Simplified Diagram | L1519–1521 | raster | imageFile28 | — | |
| 7.2.1-1 Simplified RAC Airflow Diagram | L1711–1713 | raster | imageFile29 | — | |
| 7.2.2-1 IAC Simplified Arrangement | L1828–1831 | **vector** | — | **L1830–1831** (1-cell table, 287 chars) | labels 20여 개 순서 scramble |
| 7.2.3-1 Primary Cover Gas System Block Diagram | L2199–2294 | **vector** | — | **L2201–2294** (94 lines, 891 chars; phantom table 11, label 문단 23) | 채색 분류 소실(§1 #11), `NHV` 1개 누락, `Non- SCG`→`NonSCG` |
| 7.2.3-2 Intermediate Cover Gas System Block Diagram | L2296–2387 | **vector** | — | **L2298–2387** (90 lines, 890 chars; phantom table 13, label 문단 16) | 채색 분류 소실; label 전부 존재 |
| (cover) | L1, L3, L11 | raster | imageFile1–3 | L1–11 전체 | T1; 전 PSAR chapter 공통 logo |

## 4. Heading outline check

요약 수치
- 번호 heading 67개(TOC와 PDF 본문 일치): Markdown heading 0 / list item 63 / plain paragraph 4 / 본문 glued 4(list 2 + plain 2) / 누락 0 / 잘못된 level(= 번호 heading보다 상위 `###` caption) 구조적 전부.
- 무번호 underlined subheading 34개: heading 0 / start-glued 19 / mid-glued 8 / end-glued 6 / standalone plain 1.
- `References` 7개: `###` 5 / glued 2.
- 비-heading의 heading 승격: L5 `#`(cover title), L7 `##`(subtitle), L13 `###`(TOC entry). Chapter heading L211은 `###`(→ `#`).
- PDF 번호 체계 특이점(원문 그대로 유지): 7.1.3에서는 Design Basis 등이 `7.1.3.1.1–7.1.3.1.4`(Summary Description의 하위)로 번호가 매겨짐; TOC 제목 `Chapter 7 Descriptions for Safety-Significant SSCs`.

의도 level 규칙: `#` Chapter 7; `##` 7.1, 7.2; `###` 7.1.x/7.2.x; `####` n.n.n.n; `#####` n.n.n.n.n; run-in subheading = 부모 번호 heading +1(최대 `######`); References·Table/Figure caption = system section(###)의 자식 `####`.

번호 heading 목록(line, 현재 형태 → 의도 level)

| md L | 번호 / title | 현재 | 의도 |
|---|---|---|---|
| 213 | 7.1 Nuclear Heat Supply Systems | list | ## |
| 218 | 7.1.1 Reactor Core System | list | ### |
| 221 | 7.1.1.1 Summary Description | list | #### |
| 291 | 7.1.1.2 Design Basis | list | #### |
| 383 | 7.1.1.3 Design and Performance Evaluation | **plain+glued** | #### + 본문 분리 |
| 402 | 7.1.1.3.1 Reactivity Control | list | ##### |
| 415 | 7.1.1.3.2 Methods and Analyses | **list+glued** | ##### + 본문 분리 |
| 418 / 430 | 7.1.1.4 Special Treatments / 7.1.1.5 Instrumentation Requirements | list | #### |
| 463 | 7.1.2 Reactor Enclosure System | **plain** | ### |
| 465 | 7.1.2.1 Summary Description | list | #### |
| 490 / 506 / 518 / 525 | 7.1.2.1.1 Reactor Vessel and Head / .2 Reactor Internal Structures / .3 Guard Vessel / .4 Reactor Support Structure | list | ##### |
| 530 / 674 / 774 / 789 | 7.1.2.2 Design Basis / 7.1.2.3 System Design and Performance Evaluation / 7.1.2.4 Special Treatments / 7.1.2.5 Instrumentation Requirements | list | #### |
| 930 | 7.1.3 Primary Heat Transport System | **plain** | ### |
| 932 | 7.1.3.1 Summary Description | list | #### |
| 954 / 1075 / 1097 / 1109 | 7.1.3.1.1 Design Basis / .2 System Design and Performance Evaluation / .3 Special Treatments / .4 Instrumentation Requirements | list | ##### |
| 1114 | 7.1.3.2 Primary Sodium Pump | list | #### |
| 1117 / 1137 / 1151 / 1174 / 1178 | 7.1.3.2.1 Summary Description / .2 Design Basis / **.3 System Design and Performance Evaluation(list+glued)** / .4 Special Treatments / .5 Instrumentation Requirements | list | ##### |
| 1183 | 7.1.3.3 Intermediate Heat Exchanger | list | #### |
| 1186 / 1197 / 1201 / 1216 / 1220 | 7.1.3.3.1–7.1.3.3.5 | list | ##### |
| 1319 | 7.1.4 Intermediate Heat Transport System | list | ### |
| 1322 / 1340 / 1431 / 1467 / 1481 | 7.1.4.1–7.1.4.5 | list | #### |
| 1523 | 7.2 Reactor Auxiliary Systems | **plain+glued** | ## + 본문 분리 |
| 1528 | 7.2.1 Reactor Air Cooling System | list | ### |
| 1531 / 1544 / 1607 / 1639 / 1653 | 7.2.1.1–7.2.1.5 | list | #### |
| 1715 | 7.2.2 Intermediate Air Cooling System | list | ### |
| 1718 / 1728 / 1774 / 1787 / 1798 | 7.2.2.1–7.2.2.5 | list | #### |
| 1834 | 7.2.3 Sodium Cover Gas System | list | ### |
| 1837 / 1874 / 2032 / 2108 / 2138 | 7.2.3.1 Summary Description / 7.2.3.2 Design Basis / 7.2.3.3 System Design and Performance Evaluation / 7.2.3.4 Special Treatments / 7.2.3.5 Instrumentation Requirements | list | #### |
| 1842 / 1855 | 7.2.3.1.1 Primary Sodium Cover Gas / 7.2.3.1.2 Intermediate Sodium Cover Gas | list | ##### |
| 1879 / 1950 / 1994 | 7.2.3.2.1 Compliance with Principal Design Criteria / 7.2.3.2.2 Functional Requirements and Design Criteria / 7.2.3.2.3 Regulatory Guidance | list | ##### |

무번호 underlined subheading(34) — line, 현재 형태, 부모 → 의도 level

| md L | title | 현재 | 부모(level) → 의도 |
|---|---|---|---|
| 248 | Fuel Assembly | start-glued | 7.1.1.1 (####) → ##### |
| 263 | Reflector Assembly | start-glued(+ 다음 문단 L265 병합) | ##### |
| 275 | Shield Assembly | start-glued(+ L277 병합) | ##### |
| 287 | Material Surveillance Assembly | start-glued | ##### |
| 287 | Neutron Source Assembly / Simulated Core Assembly / Compressive Assembly | mid-glued ×3 | ##### |
| 289 | Lead Demonstration Assembly | start-glued | ##### |
| 289 | Lead Test Assembly | mid-glued | ##### |
| 296 / 535 / 1345 / 1549 / 1733 | Regulatory Criteria (RCC/RES/IHT/RAC/IAC) | start-glued | 7.x.x.2 (####) → ##### |
| 326 / 1575 | Functional Requirements and Design Criteria (RCC/RAC) | start-glued | ##### |
| 608 / 1373 / 1758 | Functional Requirements and Design Criteria (RES/IHT/IAC) | **end-glued**(앞 PDC 문단 끝) | ##### |
| 1010 | Functional Requirements and Design Criteria (PHT) | plain standalone | 7.1.3.1.1 (#####) → ###### |
| 379 / 667 / 1424 | Seismic Classification and Design Codes (RCC/RES/IHT) | start-glued | ##### |
| 1597 | Seismic Classification and Design Codes (RAC) | mid-glued | ##### |
| 1772 | Seismic Classification and Design Codes (IAC) | mid-glued | ##### |
| 645 / 1589 | Regulatory Guidance (RES/RAC) | start-glued | ##### |
| 1060 | Regulatory Guidance (PHT) | **end-glued** | ###### |
| 1413 | Regulatory Guidance (IHT) | **end-glued** | ##### |
| 1772 | Regulatory Guidance (IAC) | mid-glued | ##### |
| 689 | Reactor Vessel and Head | mid-glued | 7.1.2.3 (####) → ##### |
| 710 | Reactor Internal Structures | start-glued | ##### |
| 737 | Guard Vessel | **end-glued** | ##### |
| 759 | Reactor Support Structure | start-glued | ##### |

`References`: L439(glued: `References 7.1.1-1 TerraPower, …` + entry 분할 L441), L794, L1225, L1486, L1660, L1803(`###`), L2141(end-glued) → 모두 `####`.

## 5. File-specific observations and recommendations for the cleanup script

### A. 권장 처리 순서(이 범위 기준)
1. **Frontmatter 생성 + cover 삭제**(L1–11). imageFile1–3은 전 PSAR chapter 공통이므로 corpus 규칙으로 일괄 제거.
2. **TOC 삭제**(L13–209). 삭제 전 118 entry의 `(번호, title, printed page)`를 추출해 (a) heading 승격 시 정확한 title 문자열(glued heading 분리용), (b) page-anchor 검증(7.1-n → p.n+7, 7.2-n → p.n+92)에 재사용.
3. **Vector-figure debris 삭제**: L1830–1831, L2201–2294, L2298–2387(caption heading L1828/L2199/L2296은 유지). span은 "caption heading 다음 줄 ~ 다음 번호 heading 직전"으로 정의 가능하나 Fig 7.2.3-2 → `- 7.2.4` 경계(L2389)는 다른 리뷰 범위이므로 file-level 규칙 사용 시 동일 정의로 통일.
4. **Caption header 제거**: L459 `Kemmerer Unit 1 PSAR ` prefix.
5. **회전 페이지 표 재추출(B)**: p.45(Table 7.1.2-4), p.77(Table 7.1.3-6)을 pdfplumber 결과로 교체(Notes 7셀), L870 `described i`→`described in`. 회전 페이지 12개 중 추출 가능 텍스트가 있는 p.45/77/131에서만 손실 확인—다른 chapter의 회전 표도 동일 점검 권장.
6. **Heading 승격**: 번호 heading 67(§4 표), glued 4건 분리(L383, L415, L1151, L1523: TOC title 길이로 split). L211 → `#`.
7. **Run-in subheading 분리·승격**: §4의 34개를 (line, title) 목록으로 적용. end-glued 6건은 앞 문단 끝의 `. <Title>`을 잘라 새 heading 줄로 이동해야 이전 section chunk 오염이 사라짐.
8. **PSF 표 재구성(B/C)**: 7개 표(41 rows)를 4열 Markdown table로. 반복 header 3줄 제거. 분리된 분류 태그 5건(L332, L620, L1385, L1581, L1770) 재결합, L1955/L1957 support 결합.
9. **문단 재결합(T5, 74건)** 후 **과병합 재분할(63 경계/33 lines)**. 가장 확실한 방법은 pdfplumber `extract_text_lines()`의 gap(본문 14.0 pt / 문단 25.0 pt, 임계 20 pt)을 oracle로 삼아 md 블록 경계를 PDF 문단 경계에 맞추는 것(B). A-only 규칙을 쓸 경우 §1 #7의 조건 + 예외 목록(L235, L987, L1634)과 #8의 RG 패턴.
10. **가짜 list marker 제거**: `- Consistent with PDC` 99, DL row 16(표 재구성 시 자동 해소), `- Regulatory Guide` 2(L1999–2000), 표 각주 4.
11. **Superscript 복원**(L450, L452, L1263) — 화이트리스트.
12. **Italic 복원**(PDC 117 + RG 15) — `ch7a_fmt.json`의 italic span을 문서 순서대로 exact-match.
13. **표 세부**: Table 7.2.3-1 Subsystem 열 추가·group row 제거; 각주 `\*`/`\*\*` escape(L866–867, L1299–1300, L2197); `<br>`로 2줄 셀 구분(L1295, L1702, L1703); `- 1.`→`1.`(L824–826).
14. **문자 정규화**: `&amp;`→`&`(L488, L2154), `fastneutron`→`fast-neutron`(L691), `PostAccident`→`Post-Accident`(L2184).
15. **이미지**: alt text = caption; Fig 7.1.2-11 tile 8개 그룹화.
16. **Blank line 정규화**(surplus 263줄) 및 list 내부 blank 제거(L1044–1045, L2051–2052, L2081–2082).
17. **Page anchor 삽입**(재변환 `--markdown-page-separator` 권장; 대안 `ch7a_l2p.py`식 6-gram 정렬).

### B. T5 분할 전체 목록(74; A→B, B가 continuation)
- page-break 22: 232→235(p.8/9), 303→306(12/13), 322→324(13/14), 521→523(24/25), 539→542(25/26), 553→556(26/27), 577→579(28/29), 603→606(30/31), 759→761(39/40), 946→948(57/58), 964→967(58/59), 984→987(60/61), 1208→1210(70/71), 1438→1440(87/88), 1540→1542(93/94), 1551→1554(94/95), 1568→1571(95/96), 1628→1630(98/99), 1892→1895(116/117), 1905→1908(117/118), 1923→1926(119/120), 1936→1939(120/121).
- in-page 52: 230→232, 241→243, 263→265, 275→277, 296→298, 372→374, 379→381, 383→385, 439→441, 483→485, 497→499, 582→584, 611→613, 667→669, 679→681, 681→684, 697→699, 724→726, 735→737, 740→742, 769→771, 776→778, 797→799, 935→937, 940→942, 942→943, 959→961, 967→969, 987→989, 1058→1060, 1078→1080, 1120→1122, 1141→1143, 1143→1146, 1327→1329, 1360→1362, 1376→1378, 1411→1413, 1424→1426, 1469→1471, 1523→1525, 1597→1599, 1599→1602, 1632→1634, 1641→1643, 1744→1746, 1761→1763, 1917→1919, 2009→2011, 2016→2018, 2025→2027, 2110→2112.
- 참고: 예비 스캔 기준(`analyze_md.py` 조건)으로는 이 범위에서 suspected split 35, lowercase list item 29(파일 전체 97/71 중). 대문자·`Section`·`(Reference` 시작 continuation과 page-break 대문자 연속이 누락되므로 위 목록(74)이 정확한 값.

### C. 자동 수정 금지(원문 그대로 유지)
- 원문 오탈자/표기: `metallic metallic`(L689, p.34), `Rules for Constructions`(Table 7.1.2-2), `Minimum Hydraulic Efficiency at @`(Table 7.1.3-3), `150 m3/s`의 값·단위(superscript만 복원), `flourides`(L1997), `AMSE BPVC`(L2021), `250F`(L1849), `15kGy`(L767), `(N872)`(L657), `Specified Acceptable Radionuclide Release Limits (SARRDLs)`(L1742), `Aluminium`, `noncondensible`, `several part per million`, RG 1.87 연도 불일치(L1067 `2023` vs L2009 `2021`), `Scram - Gravity Driven` vs `Scram – Gravity driven`(RCC/RES 표 차이).
- 진짜 lowercase bullet L472–476(RES enhanced safety features) — continuation join 규칙에서 제외.
- 반복 special-treatment bullet(system별 7개 목록) — 중복 제거 금지.
- `SR*`, `NSRST*`의 `*`(각주 의미) — escape만, 삭제 금지.
- PHT 표 DL4-HR1 support가 DL3-HR5와 동일 문장인 것은 원문(p.63 확인).
- run-in title과 동일 문자열이 본문·그림에 등장(`Guard Vessel Leakage Detection/…` L2286, `Reactor Internal Structures` 본문 다수) → 전역 정규식 금지, line 목록 기반만 허용.
- vector 그림 분류 목록(§1 #11)은 원문 문장이 아니므로 삽입 시 "derived from figure colour legend" 등 출처 표시 필수.

### D. Retrieval용 식별자(frontmatter/tag 후보)
- DL function ID(33 unique): DL2-HR2, DL2-RR10, DL3-HR1, DL3-HR2, DL3-HR3, DL3-HR4, DL3-HR5, DL3-HR6, DL3-HR7, DL3-HR8, DL3-HR9, DL3-HR10, DL3-HR12, DL3-HR13, DL3-RC1, DL3-RR1, DL3-RR1a, DL3-RR1c, DL3-RR1d, DL3-RR2, DL3-RR7, DL4-DID1, DL4-HR1, DL4-HR2, DL4-HR3, DL4-HR6, DL4-HR7, DL4-RC3, DL4-RR1, DL4-RR4, DL4-RR4a, DL4-RR4c, DL5-PAM1 (system별: RCC 10, RES 5, PHT 8, IHT 7, RAC 2, IAC 1, SCG 8).
- System/SSC 약어: RCC, RES, PHT, IHT, NSS, RAC, IAC, SCG, SPS, CRD, NGA, NHV, RWG, NFP, RMS, NIC, RPS, RXB, RAB, FHB, HAA, RV, GV, RPA, UIS, RFI, CBS, IVS, FIVS, RSS, RSB, MIRSS, PSP, IHX, ISP, SHX, AHX, ASE, CCA, CRDM, IVTM, FTL, GFIMS.
- 분류: safety SR / NSRST / NST; seismic SCS1 / SCN1 / SCN3.
- PDC(system별 적용 목록): RCC 2,4,10,11,12,16,26,28,29,80; RES 2–4,10–12,14–16,26,28–37,61,62,72–74,78–80; PHT 2–4,10–16,30–37,71,72,74,78; IHT 2–4,10,34,35,70,72–78; RAC 2–4,13,35–37,64; IAC 2–4,10,34,70,72–77; SCG 2–4,10,13–16,30–32,60,63,70–79.
- RG: 1.20, 1.22, 1.31, 1.36, 1.44, 1.45, 1.61, 1.68(.3), 1.69, 1.76, 1.84, 1.87, 1.97, 1.100, 1.124, 1.130, 1.147, 1.153, 1.189, 1.192, 1.199, 1.243, 1.246. Codes: ASME BPVC III Div 5(HBB/HBA/HGB/HFA), III Div 1 NB/NF, VIII Div 1, XI Div 2, II Part A/D, V; B31.1, B31.3, B36.19M, B16.34, PTC-25, AG-1, STS-1, QME-1; ANSI/AISC N690; IEEE 308/323/344/382/497/603; SMACNA 1108; ACI 355.2-07; ASTM E488/E488M-15. Topical reports: NAT-2806-A, NAT-8922.
- Cross-reference 패턴: `Section \d+(\.\d+)*`, `Table 7\.\d\.\d-\d+`, `Figure 7\.\d\.\d-\d+`, `\(Reference 7\.\d\.\d-\d+\)`, `PDC \d+`, `RG 1\.\d+`, `10 CFR 50\.\d+[a-z]?(\([^)]+\))*`.
