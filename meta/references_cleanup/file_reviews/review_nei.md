# Review nei: NEI_18-04_Modernization of Technical Requirements for Licensing of Advanced Non-Light Water Reactors.md (md lines 1–1921, PDF pages 1–95)

작성 범위: 파일 전체(1–1921행)를 순차 판독, PDF 95쪽 전체를 pdfplumber 텍스트/폰트/도형으로 대조, 표·그림 페이지(14, 36, 43, 52–54, 57–58, 67, 69, 73, 77–78, 84, 87)는 렌더링 이미지로 육안 확인. 재변환 실험은 scratchpad `nei/` 하위에만 출력(아래 §5.1). `references/`는 읽기만 함.

---

## 0. 개요

| 항목 | 값 |
|---|---|
| md 크기 | 1,921 lines (non-blank 1,059), 242,184 chars (243,357 bytes UTF-8) |
| PDF | 95 pages (p1 cover, p2–8 front matter = 인쇄쪽 ii–viii, p9–95 = 인쇄쪽 1–87; **인쇄쪽 = PDF쪽 − 8**), Word→Acrobat PDFMaker 17, tagged, outline 61 bookmarks |
| PDF metadata | `/AccessionNumber ML19241A472`, `/DocketNumber PROJ0689`, `/DocumentReportNumber NEI 18-04, Rev 1`, `/DocumentDate 20190829` |
| 구조 (PDF 기준) | 6 chapters, 19 x.y sections, 30 x.y.z subsections (= outline 55) + BoldItalic 소제목 68개 (Task 43 + 무번호 25) |
| 표 | 번호 표 13 (3-1, 3-2, 4-1, 5-1 … 5-10) + List of Acronyms(2열 표 형태) + Glossary(6쪽 표). md에는 table block 26개(실표 21 + phantom 5) + 표가 비표 텍스트로 풀린 부분 3곳(Table 4-1 p52, Table 5-6 p78, Acronyms p8) |
| 그림 | 11 (raster 5, vector 5, hybrid 1). image 파일 6개 (imageFile5 = 140×137 px 회색 원, 정보 없음) |
| 순수 잡음 추정 | ≈19.2 k chars (7.9 %): TOC/LoF/LoT 11,107 (L27–173, dot-leader 80행) + vector 그림 잔해 5,014 (112 non-blank행) + `<br>` 528개 2,112 + 반복 표 헤더 575 (15행) + footer/header 잔재 329 (8행) + 기타 60. 비공백행 기준 ≈215행/1,059행 (20 %) |
| 가장 심각한 문제 | ① 지수 부호 소실로 **수치 자체가 틀림** 3건 (`1×104`, `102/plant-year` ×2) ② 핵심 표 대부분이 1열로 붕괴(열 연관 소실) — Table 3-1, 3-2, 5-1, 5-3, 5-4, 5-5, 5-7, 5-8, Glossary 6블록; Table 4-1·5-9·5-10의 √ 행렬 소실 ③ Table 3-2·식 R_j 수식이 PDF text layer 단계에서 이미 깨짐 ④ outline heading 55개 중 14개가 heading 아님, 35개가 깊이 무관 `#####` |

---

## 1. Findings

| # | T-ID | Sev | Count | md lines (examples) | PDF p. | Evidence / description | Proposed fix | Fix class |
|---|---|---|---|---|---|---|---|---|
| F01 | T8/T11 | **H** | 3 | L347 `mean frequencies of 1×104/plant-year to 1×10-2/plant-year are classified as DBEs`; L370 `frequencies between 10-4 to 102/plant-year`; L911 `…with the SSC failed is greater than 102/plant-year.` | 14, 16, 47 | 윗첨자 지수 `-2`/`-4`가 PDF 줄바꿈 위치에서 `10-⏎2`로 끊겨 있고(pdfplumber: `1×10-\n4/plant-year`, `10-\n2/plant-year`), opendataloader가 줄끝 `-`를 hyphenation으로 보고 제거 → **값이 10²/10⁴로 뒤바뀜**. DBE 하한(10⁻⁴)과 SSC 위험중요도 기준(10⁻²/plant-year = 1/plant-year의 1 %)이 오염. 같은 정의가 L427·L1873에서는 정상이라 md 내부 모순 발생 | 3건 명시 치환: `1×104/`→`1×10-4/`, `10-4 to 102/`→`10-4 to 10-2/`, `than 102/`→`than 10-2/` (이 문서의 지수는 전부 음수·전부 `/plant-year` 앞 — §5 R6) | A |
| F02 | T6 | **H** | 1 표 (5행) | L344–350 Table 3-1 `\|Anticipated Operational Occurrences (AOOs)<br><br>“Conditions of normal operation…”<br><br>Anticipated event sequences…\| \| \|` | 14 | "Event Type / Current Definition / Guidance Document Definition" 3열 내용이 전부 1열에 `<br><br>`로 연결, 2·3열 공란(fill 0/10). 4행은 3분절이라 분할 가능하나 DBA 행(L349)은 4분절(Current Definition에 인용 2개) → 기계적 분할 불가. L347 F01 오류 포함 | struct-tree 변환본의 Table 3-1(3열 정확) 사용 + F01 수정. 대안: 분절수=3 행은 A-split, DBA 행은 seg2+seg3 병합 | B |
| F03 | T10/T6 | **H** | 8 수식 + 1 표 | L717 `\|Risk Reduction RR 𝑅𝑅(𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏) − 𝑅𝑅(𝑥𝑥𝑖𝑖 = 0)\| \| \|`; L718, L720, L723 | 36 | (a) Measure/Abbreviation/Principle 3열이 1열로 붕괴. (b) Cambria Math의 ToUnicode가 PDF 자체에서 깨져 있음: `base`→`𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏`(첫 글자 반복), 분수선 소실(분자·분모 나열). pdfplumber 텍스트도 동일하므로 **재변환으로 복구 불가**, 단순 중복제거도 `R(bbbb)`가 됨 | 렌더 이미지 기준 수동 전사(§2 Table 3-2 행에 정답 수식 기재). 열은 struct-tree본 사용 | C |
| F04 | T6/T16/T8 | **H** | 1 표 (3쪽, 데이터 19행 + 그룹 3행, √ 26) | p52 부분 L984–1041 (표 아님: `Applicability1` / `SR Available Guidance4 SSC` / `√ √ √` / `- NEI-00-04 for RISC-1 SSCs` …); p53–54 부분 L1043–1058, L1061–1064 `\|Technical Specifications √ 2 10 CFR 50.36, SRP, …\| \| \| \| \|`, `\|Seismic design basis √ 3 3 Essentially …\|` | 52–54 | Special Treatment 적용성 행렬(SR/NSRST/NST × 19 행) 소실. p52: 항목명·√·guidance가 뒤섞인 29개 단락/목록 행(√ 15개가 어느 행·열인지 판별 불가, guidance가 행 라벨보다 먼저 나옴). p53–54: 5열 표이나 √(11개)와 각주번호가 1열에 합쳐짐(fill 3/56). 각주번호 접착 `Applicability1` ×3, `Guidance4` ×3, `Process5` ×1; NSRST/NST 칸의 각주참조가 `√ 2`(×3), `√ 3 3`(×1) 형태로 값처럼 보임. `NEI-0004`(L1039, PDF `NEI-00-⏎04`). 헤더 반복(L1061–1063), 주석 1–5가 표 행으로 들어감 | struct-tree본 Table 4-1 채택(√가 열별로 정확, fill 59/116) 후: 헤더 1행으로 재구성, RISC-2 행 √를 NSRST 열로 1칸 이동(struct-tree본 오류), 반복 헤더 삭제, 주석 1–5를 표 아래 footnote로. 정답 행렬은 §2에 수록 | B + C |
| F05 | T6 | **H** | 2 표 (√ 21 + 23) | L1812 `\|Normal Operation √ √ √ AOOs √ √ √ DBEs √ √ √ √ √ BDBEs √ √ √ √ √ DBAs √ √ √ √ √<br><br>\| \| \| \| \| \|`; L1821 | 87 | Table 5-9/5-10의 5행×5열 체크 행렬 전체가 한 셀. 행(LBE 범주)·열(DID 속성) 연관 완전 소실. 2단 헤더도 분리됨(L1809–1811) | struct-tree본(행·열 정확, 2단 헤더만 1칸 밀림) 채택 후 헤더를 `Functional: Margin Adequacy` 식 단일 헤더로 평탄화. 정답 행렬 §2 | B |
| F06 | T6 | **H** | 6 블록, 35 용어 + 5 그룹행 | L1860 `\|Fundamental Safety Function<br><br>FSF<br><br>Safety functions common…<br><br>IAEA-TECDOC-1570\| \| \| \|`; L1885 `\|Plant<br><br>The collection of site…<br><br>LMP\|`; L1901 `\|Risk-Informed RI<br><br>…`; L1908 `\|Initiating Event IE<br><br>…` | 90–95 | Glossary 4열(Term/Acronym/Definition/Source)이 1열로 붕괴(fill 0/120). 대부분 4분절이지만 acronym 공란(Plant, End State) 2행은 3분절, `Risk-Informed RI`·`Initiating Event IE`는 공백으로 접착 → 분할 모호. 쪽마다 헤더 반복(6블록) | struct-tree본(46행 단일 표, fill 118/135) 채택, 그룹행("Terms Associated with …")을 `Category` 열로 전개 | B |
| F07 | T6/T16 | **H** | 1 표의 2쪽 중 1쪽 (4 행) | L1567–1628 `Operational Technical Specifications Allowable Outage` / `- 1. Are all risk-significant LBE limiting condition…` / `Times Part 21 Reporting Maintenance Rule` / `Scope` / `Compensation` / `for Unknowns (Performance Variability)` | 78 | Table 5-6 p78 부분(Compensation for Mechanical Errors, Unknowns–Performance Variability, Unknowns–Knowledge Uncertainty, Offsite Response/Emergency Response Capability)이 표 구조 없이 흩어짐: 질문 목록이 어느 Evaluation Focus에 속하는지 소실, Implementation Strategies 순서 뒤섞임. p77 부분(L1559–1564)은 3열 유지되나 셀 내부 분절 오류(`Equipment<br><br>Qualification Performance<br><br>Testing`) | struct-tree본 Table 5-6(두 쪽 병합·전 행 정확) 채택 | B |
| F08 | T6/T2 | **H** | 53 acronyms → 21 단락 조각 | L182 `Engineers BDBE* Beyond Design Basis Event CFR Code of Federal Regulations DBA* …`; L184–186 `FMEA failure modes and effects` / `analysis FSAR Final Safety Analysis Report …`; L190–192 `IDP IDPP` / `Integrated Decision-Making Process Integrated Decision-Making Process Panel` | 8 | 2단 약어표가 문단 조각으로 풀리고 정의가 조각 경계에서 잘림 → 약어→정의 매핑 불가(에이전트 용어 사전으로 쓰기 어려움). `NUREG-⏎0800`(L216–218) 분리 | struct-tree본의 2열 표(27+25행) 채택, IDP/IDPP 행 분리, 두 반쪽 병합. `*`(=Glossary 정의 용어 표시) 유지 | B |
| F09 | T6 | **H** | 1 표 | L1428 `\|5) Deploy adequate offsite protective actions and prevent adverse impact on public health and safety\| \| \| \| \|`; L1424–1427 | 69 | Table 5-2: Layer 4·5가 공유하는 Quantitative/Qualitative 지침(rowspan 2)과 Overall Guidelines 2열(rowspan 5)이 첫 행에만 기재 → Layer 5는 "지침 없음"처럼 보임. Layer 1 Layer Guideline(colspan 2)은 Quantitative 열에만. `&lt; 10-2/plant-year`. struct-tree본은 4열로 오히려 어긋남 | 수동 재작성(5행×4지침열, rowspan 값 채움, 주석 [a]–[d]는 표 아래) | C |
| F10 | T11 | **H** | 7 | L1039 `NEI-0004`; L1886 `ASME/ANS-Ra-S-1.42013`; L1396 `Elements of TIRIPB Framework`; L212 `RIPBDM*`, L1723 `the RIPBDM process`; L22/L235 `defense-indepth` | 52, 92, 67, 8, 83, 3, 9 | 줄끝 hyphen 제거로 **식별자** 훼손(문서번호·표준번호·약어). 검색 키 불일치 | PDF 줄끝 hyphen에서 도출한 사전 치환(§5 R7) | A (B-derived dictionary) |
| F11 | T10/T8 | **H** | 1 식 + 8 기호 | L1495 `𝑅𝑅𝑗𝑗 = 𝑄𝑄 × 𝐹𝐹𝐼𝐼𝐼𝐼,𝑗𝑗 × 𝑃𝑃𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴,𝑗𝑗 …`; L1497 `where: Rj = … Q = … FIE,j = … PASSC,j = … rfuel,j= …` (한 단락); L711 `the term xi represents` | 73, 35 | 식이 PDF text layer에서 깨짐(`fuel`→`𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓`, `ASSC`→`𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴`). 기호 정의 8개가 한 단락, 아래첨자 소실 | 수동: `R_j = Q × F_IE,j × P_ASSC,j × P_PSSC,j × r_fuel,j × r_PB,j × r_cont,j`; where-목록을 8행 정의 목록으로 분리(`X = ` 앞에서 분할은 A 가능) | C (+A) |
| F12 | T3 | **H** | 14 | L357 `3.2 Advanced Non-LWR LBE Selection Approach`(plain); L359 `- 3.2.1 Frequency–Consequence…`; L893/L896 `- 4.2 …`/`- 4.2.1 …`; L1103 `- 5.1 Defense-in-Depth Philosophy According to the NRC glossary, defense-in-depth is:`; L1686/L1689 `- 5.9 …`/`- 5.9.1 …` | 15, 32, 46, 56, 69, 74, 75, 82, 84, 85, 87 | outline heading 55개 중 14개가 heading 아님(list 9, list+glued 4, plain 1) → 해당 절 본문이 직전 절(예: 4.2/4.2.1 본문이 4.1 Task 7 아래, 5.9.x 본문이 5.8.2 아래)에 귀속 | pypdf outline 기반 heading 재구축(§4 목록) + glued 본문 분리 | B |
| F13 | T9/T5 | **H**(6) / M | 16 footnotes (15 `*` + 1 `†`) | 문장 중간 삽입 6: L441→L443→L445 `…and all non-` / `* Designers and applicants…` / `safety-related SSCs…`; L463–468, L499–503, L956–960, L1184–1188, L1299–1303. list item화 2: L465 `- The term “substantial”…`, L478 `- It is recognized that the PRA…`. 목록 내부 삽입: L275(각주 2개 `*`+`†`가 한 단락으로 합쳐져 목록 중간), L670 | 10, 12, 14, 21–24, 32, 37, 39, 49, 58, 62, 63, 71 | 쪽 하단 각주(9 pt, 구분선 rect 144×1 pt)가 본문 흐름에 삽입. 문장이 둘로 쪼개져 청크 경계에서 사실 절단. 본문 참조부호 16개(`following:*` L257, `event sequences†` L271, `substantial*` L453, `bands*` L468 …)는 본문과 연결 안 됨 | 각주를 `[^pNN]` Markdown footnote로 변환, 본문 조각 재결합(§5 R8) | A (페이지 마커 있으면) / B |
| F14 | T3 | M | 35 | `##### 1.1 Purpose`(L233) … `##### 3.2.2 LBE Selection Process`(L391) … `##### 5.9.7 …`(L1849) | – | x.y(15개)와 x.y.z(20개)가 모두 `#####` → 계층 평탄화. 장(H2)과 절 사이 H3/H4 결손 | outline depth 1→H3, 2→H4 | B |
| F15 | T3 | M | 68 소제목 (9 비heading) | Task: L402 `- Task 1: Propose Initial List of LBEs`, L485 `- Task 7b: Evaluate Integrated Plant Risk against QHOs and 10 CFR 20 In this task, the integrated risk…`(glued), L496 `- Task 7c: …`; 무번호: L657 `Overall Plant Risk Metrics`(plain), L970 `Purpose of Special Treatment The purpose of special treatment is reflected…`(glued), L1174(plain), L1182 `…create layers-of-defense responses to plant challenges. Programmatic Defense-in-Depth`(단락 끝에 접착), L1771, L1827(plain) | 19, 24, 32, 50, 58, 85, 87 | PDF에서 Calibri-BoldItalic 11 pt인 소제목 68개(Task 43 + 무번호 25). 59개는 `#####`(깊이 무관), 9개는 heading 아님. 동일 명칭 중복(Task 1 ×3 — LBE/SSC/DID 절차, "Margin Adequacy" ×2) | 폰트 기준 목록(§4)으로 부모 절+1 레벨 부여, glued 분리. breadcrumb 필요(§5) | B |
| F16 | T3 | M | 3 + 캡션 24 | L553 `###### Systems Engineering Inputs`(Fig 3-3 라벨); L1141 `### PRA`(Fig 5-2 라벨, 12.1 pt Bold); L791 `##### THIS PAGE INTENTIONALLY BLANK`; 캡션 H5 18개(L342, L366, …, L1706), list 5개(L399, L817 glued, L1171, L1807, L1815), plain 1개(L1419) | 28, 58, 41 | 비-heading의 heading 승격. 캡션은 PDF에서 절 제목과 같은 Calibri-Bold 11 pt라 `#####`로 오인됨 | 3건 삭제/강등; 캡션 24개를 `**Table 3-1. …**` 단락으로 통일(표/그림 바로 앞) | A |
| F17 | T7 | M | 5 그림 + 1 hybrid, 112 non-blank행, 5,014 chars, phantom table 5 | Fig 3-3 L553–600; Fig 4-2 L813–814 (1열 표 + imageFile5); Fig 4-3 L841–863; Fig 5-1 L1112–1120 (`<br><br>\|Protective measures…\|`, `res`); Fig 5-2 L1130–1169; Fig 5-4 L1211–1282 (`A`, `A A`, `Acronymns`) | 28, 43, 45, 57, 58, 61 | vector 도식이 라벨 조각·가짜 표로 분해. 일부는 본문과 구분 불가(L1130–1136 Fig 5-2 bullet이 5.2 도입문 직후 본문 목록처럼 보임) | 삭제하되 정보성 텍스트(Fig 5-2 bullet, Fig 5-1 두 설명박스, Fig 4-3 범주 정의·주석)는 캡션 아래 `> [!figure]` 블록으로 이동(§3) | A (삭제) / C (보존 블록) |
| F18 | T7 | M | 5 | L364 `![](<…imageFile1.png>)` (alt 빈칸) 등 | 15, 19, 34, 40, 59 | raster 그림 alt text 없음. Fig 3-1 F-C Target 앵커값(그래프에만), Fig 5-3 Layer 1–5 Objective/Success 문구(본문에 없음), Fig 4-1 주석 `*`/`**`(본문에 없음) | 수동 alt text/전사 | C |
| F19 | T6 | M | 5 표 | L1398 `\|Designer Development of Safety Design Approach<br><br>Selection of inherent, active, and passive design features Selection of approach…<br><br>Advanced Reactor Safety Policy…\| \|` (5-1); L1452 (5-3); L1545 (5-5); L1672 (5-7); L1711 (5-8) | 67, 70, 75, 81, 83 | 목록형 2열 표가 1열로 붕괴하고 항목 경계가 공백 연결로 사라짐(`<br><br>`는 줄바꿈 위치일 뿐 항목 경계 아님 — 분절수 불일치 [4,9,2,2,4] 등) | struct-tree본 채택 후 rowspan-shift 교정(§5 R5b) | B |
| F20 | T6 | M | 1 표 (7행, 2쪽) | L1478–1485 + L1488–1490 (헤더 반복) | 72–73 | Table 5-4: 3열이 1열로 붕괴하나 모든 행이 정확히 3분절 → 분할 가능. 쪽 분할 미병합 | `<br><br>` 3분할(A) 또는 struct-tree본(병합·정확) | A/B |
| F21 | T6 | M | 4 표 | Table 4-1 (3쪽), 5-4 (2쪽), 5-6 (2쪽), Glossary (6쪽); 반복 헤더 15행/575 chars | 52–54, 72–73, 77–78, 90–95 | 쪽 분할 표 미병합, 헤더 반복 | 병합(struct-tree본은 병합됨) | A/B |
| F22 | T6 | M | 528 `<br>`; 빈 헤더셀 표 8 | L555, L593, L1043, L1061, L1233, L1421, L1809, L1818 | – | 셀 내부 `<br><br>`는 대부분 PDF 줄바꿈 잔재. 셀 내부 항목 분절 오류(Table 5-6 `Training and<br><br>Qualification Plant Simulators Independent<br><br>Oversight…`) | 표 교체 후 `<br>` 정규화(목록 항목 경계만 `<br>` 유지) | B |
| F23 | T11 | M | 59 tokens / 26 forms (F10 식별자 7건 제외) | L750 `regarded as risksignificant`; L1900 `PerformanceBased`, `performancebased`, `decisionmaking`; L349/L1861/L1888 `SafetyRelated`; L813/L861/L1891 `SafetySignificant`; L313 `riskinformed`; L374 `10-2/plantyear`; L447 `nonLWRs`; L1851 `reevaluated`; L1908 `humancaused`, `seismicallyinduced` | 전역 | Word PDF에는 자동 hyphenation이 없고 줄끝 `-`는 모두 실제 복합어 hyphen인데, 변환기가 제거. 정의 용어("risk-significant", "Safety-Related", "performance-based")의 키워드 검색 실패. 전수(PDF 인라인에 결합형이 0회인 형태): risksignificant 10, performancebased 6, SafetyRelated 5, riskinformed 4, safetysignificant 4, SafetySignificant 4, decisionmaking 3, PerformanceBased 2, plantyear 2, nonLWRs 2, nonreactor 2, 기타 1회 15종(DecisionMaking, FrequencyConsequence, RiskSignificant, designspecific, fitfor, highconsequence, humancaused, inservice, nonrisk, nonsafety, offnormal, reevaluated, seismicallyinduced, technologyinclusive, L1898 `Defense-inDepth`) | PDF 줄끝 hyphen 사전 치환(§5 R7) 또는 `--keep-line-breaks` 재변환 후 hyphen 보존 결합 | A (B-derived) |
| F24 | T11 | M | 89 | L259 `10 Code ofFederal Regulations (CFR)50.34(a)`; L261 `aStandard`; L316 `SSCsthat`; L329 `Section3`; L489 `fatalitieswithin`; L1657 `technicalspecifications`; L1718 `Identificationof` | 10–86 | 공백 소실(pdfplumber에는 공백 존재). 주로 bullet 목록의 좁은 justified 공백 | **`--space-ratio 0.12` 재변환**: 검증 결과 89건 전부 올바른 공백 삽입, 오분할 0, 기타 변경 0 (0.08도 TOC dot-leader 외 변화 없음) | B |
| F25 | T4/T1 | M | 8 + cover 2 | L17 `- © NEI 2019. All rights reserved. nei.org ii` … L228 (`viii`) 7행; L340 `August 2019`(Table 3-1 캡션 직전); L1 `18-04`; L11 `© NEI 2019. All rights reserved. nei.org` | 1–8, 14 | 앞부속 쪽 footer가 list item으로 잔존, 본문 header 1건 | 정규식 삭제 `^- © NEI 2019\. All rights reserved\. nei\.org [ivx]+$`, `^August 2019$`(L9 표지 날짜 제외) | A |
| F26 | T2 | M | 55 + 11 + 13 항목, 80 dot-leader행, 11,107 chars | L29 (NOTICE/Abstract/LoF/LoT/LoA 5항목이 한 줄), L31–121 `- 3.2.1 Frequency–Consequence Evaluation Criteria ....... 7`, L78 footer 끼어듦 | 4–7 | TOC/LoF/LoT (인쇄쪽 번호, PDF쪽 아님) | 삭제(heading 트리로 대체). 필요 시 page 번호 없는 nav 목록 | A |
| F27 | T5 | M | 21 쪽경계 분할 + 6 각주 끼임 + 1 | L255/257 `…applicable to a` / `technology-inclusive array…`; L405/407; L549/551; L1348/1350; L1803/1805; L376/L379 `- all the LBEs is addressed…`(연속문이 list item) | 9–87 | 쪽 경계에서 단락이 2개로 분리 | 페이지 마커 기준 재결합(끝 구두점 없음 + 다음 소문자) — 줄끝 `non-`는 hyphen 유지 | A |
| F28 | T5/T3 | M | 6 | L1202 `- As explained more fully…`; L1296 `- At an early stage…`; L1309 `- As noted previously…`; L1358 `- At this task…`; L1391 `- As seen Table 5-1…`; L1638 `- At the plant level…` | 60, 62, 63, 65, 66, 79 | 본문 단락(x0 = 72 pt, bullet 없음)이 list item으로 오인 — "As/At"로 시작하는 단락에서만 발생 | `- ` 제거(PDF bullet 좌표 x0=90/108과 대조) | A (목록 지정) / B |
| F29 | T5 | M | 33 중첩항목 | L304–310 (`o` 4개), L758–770, L1733–1765 (3단: • / o / ▪) | 12, 38, 84–85 | PDF 중첩 목록(`o` CourierNew 20개 + ▪ Wingdings 13개)이 md에서 전부 0단 `- `로 평탄화, 항목 사이 빈 줄 | 들여쓰기 복원(PDF x0 108→126→144 pt 기준) | B |
| F30 | T12 | M | 14 + 1 | L226, 275, 323, 443, 501, 670, 750, 785, 859, 958, 1186, 1301, 1320, 1472 (`* …`로 시작); L1112–1117 깨진 표 문법 | – | Obsidian이 `* `로 시작하는 줄을 bullet로 렌더(각주 본문). `<br><br>\|…\|`로 시작하는 줄 | 각주 변환(F13) 시 해소; phantom table 삭제 | A |
| F31 | T8 | M | 47 | L346 `1×10-2/plant-year`; L488 `5×10-7/plant-year`; L912 `5×10-9/plant-year`; L913 `2×10-8/plant-year`; L1425 `&lt; 10-2/plant-year` | 전역 | 윗첨자 소실(27× `N×10-M`, 20× bare `10-M`; `5x10-7` 2건은 원문 표기). 모두 `/plant-year` 앞 → 오해석 가능성은 낮으나 표기 비표준 | 코퍼스 공통 규칙으로 정규화(예: `10⁻²` 또는 `10<sup>-2</sup>`), regex `(?<=10)-(\d+)(?=\s?/plant)` | A |
| F32 | T8 | M | 7 + 4 | L984/L1043/L1061 `Applicability1`; L986/L1043/L1061 `Guidance4`; L994 `Process5`; L1050 `√ 2`, L1051 `√ 3 3`, L1056–1057 `√ 2` | 52–54 | 표 각주번호가 단어에 접착되거나 셀 값처럼 보임 | 표 교체 시 `[^t4-1-1]` 등으로 변환 | A/B |
| F33 | T11 | M | 11 | `&amp;` L204, L1294, L1299, L1544, L1562, L1818; `&lt;` L745, L746, L1425, L1426, L1427 | – | HTML entity | decode (`O&M`, `<`) | A |
| F34 | T15 | M | – | 파일 전체 | – | YAML frontmatter 없음, page anchor 없음 | 재변환 `--markdown-page-separator "<!-- page %page-number% -->"`(현 md와 페이지 마커 외 동일함을 검증) + frontmatter(§5 R1) | B |
| F35 | T11 | L | 1 + 1 + 1 | L668 `• The Initiating Events (IEs)…`; L770 `…(NST): o All other SSCs…`; L1793 `in two waysfrequency uncertainty` | 32, 38, 86 | raw bullet glyph, inline `o` bullet, 줄끝 em dash 소실(PDF `two ways—⏎frequency`) | 치환 | A |
| F36 | T12 | L | 15 | L934 `- 1. Mitigate DBEs…`; L1575–1617 `- 1. Are all…` | 48, 78 | `- 1.` 이중 표지 (Table 5-6 질문은 표 교체 시 셀로 흡수) | `- ` 제거 | A |
| F37 | T13 | L | ≈3,443 italic chars | L241, L245, L249, L889, L901, L972, L1106–1108, Table 3-1 Current Definition 열 | 9, 14, 46, 47, 50, 56–57 | 인용 정의의 italic 소실(인용부호로 구분은 가능). underline/strike 없음(표 테두리 외 밑줄 rect 0) | 선택적 `*…*` 복원 | B |
| F38 | T14 | L | 0 본문 누락 | – | – | 산문 페이지 전체 PDF 행 대비 일치(28-char window, 불일치 0행). 불일치는 표/그림 다열 행뿐. 누락은 raster 그림 내용(F18)과 cover logo "NEI TECHNICAL REPORT"뿐 | – | – |
| F39 | T11 | – (보존) | 7 | L545 `industry consensus stan and regulatory guides`; L745 `The total mean -frequency`; L1493 `release s`; L1276 `Acronymns`; L468 `5x10-7/plant year`; L777/L1099 `complimentary`; L1797 `threating` | 28, 37, 73, 61, 23, 39/56, 86 | PDF 원문 자체의 오타 — 변환 결함 아님 | **수정 금지**(필요 시 `[sic]` 주석만) | – |
| F40 | T1 | L | 1 | L13–15 NOTICE 면책문 | 2 | boilerplate | frontmatter `notice:` 로 이동 또는 유지 | A |

---

## 2. Table verification log

전 표(≤30) 검사. "default" = 현재 md, "st" = `--use-struct-tree` 재변환본(scratchpad `nei/conv_st/`). fill = 2열 이후 비어있지 않은 셀 수/전체.

| Table ID | md lines | PDF p. | Status (OK / defect IDs) | Notes (lost values, split rows, …) |
|---|---|---|---|---|
| List of Acronyms | L176–226 (비표) | 8 | F08 | 53 약어가 21 단락 조각. st: 2열 표 27+25행, fill 26/26·24/24(정확). `*` 24개는 Glossary 정의 표시 — 보존 |
| Table 3-1 Definitions of LBEs | L342 cap(H5), L344–350 | 14 | F02, F01, F31, F22 | 5행 3열 → 1열 붕괴(fill 0/10). L347 `1×104`(→1×10-4). DBA 행 4분절. 표 주석 `*SRP 15.0 …`(L353) 위치 적정. st: 3열 정확(fill 10/10) — 단 `1×104` 동일 오류 |
| Table 3-2 Risk Importance Measures | L713 cap, L715–724 | 36 | F03, F02-type | 8행 3열 → 1열(fill 0/16). 정답(렌더 기준): RR `R(base) − R(x_i = 0)`; FV `[R(base) − R(x_i = 0)] / R(base)`; RRW `R(base) / R(x_i = 0)`; CR `{[R(x_i = 1) − R(x_i = 0)] / R(base)} × x_i(base)`; RA `R(x_i = 1) − R(base)`; RAW `R(x_i = 1) / R(base)`; PD `[R(x_i + ∂x_i) − R(x_i)] / ∂x_i`; BI `R(x_i = 1) − R(x_i = 0)`. st: 열은 정확, 수식은 동일하게 깨짐 |
| Table 4-1 Special Treatments (3쪽) | L982 cap; p52 L984–1041(비표); p53 L1043–1058; p54 L1061–1064 | 52–54 | F04, F21, F32, F10 | √ 26개 개수는 보존(15+11)되나 위치 소실. 정답 행렬(SR/NSRST/NST): [Requirements Associated with SSC Safety Classification] Document basis…IDP⁵ √/√/√; Document evaluation of adequacy… (RISC-1) √/–/–, (RISC-2) –/√/–; Change control process √/√/–. [Basic Requirements for all Safety-Significant SSCs] RAP √/√/–; Design Requirements for SSC capability √/√/–; Maintenance Program √/√/–; Licensee Event Reports √/√/–. 10 CFR 50 App B QA √/–/–; User provided QA Program –/√/–. [Additional Special Treatment Requirements] RFDC √/–/–; Technical Specifications √/²/–; Seismic design basis √/³/³; Seismic qualification testing √/–/–; Protection against DB external events √/–/–; EQ testing √/–/–; Materials surveillance testing √/–/– (guidance 공란); Pre-service & RI ISI √/²/–; Pre-service & IST √/²/–. st: 행렬 정확하나 RISC-2 행 √가 SR 열로 1칸 밀림, 헤더 2행 어긋남, 주석이 표 행 |
| Table 5-1 Role of Major Elements | L1394 cap, L1396–1402 | 67 | F19 | 5행 2열 → 1열(fill 0/5), 역할 항목 경계 소실(`<br><br>`는 hanging-indent 줄바꿈). `TIRIPB`(F10). st: 2열, 항목 `<br><br>` 구분 정확(fill 5/5) |
| Table 5-2 DID Guidelines | L1419 cap(plain), L1421–1429 | 69 | F09, F33, F31, F22 | 5열·2단 헤더(빈 헤더셀). Layer 5 행 전부 공란(실제는 Layer 4와 rowspan 공유), Overall 2열은 1행에만. 수치 `&lt; 10-2/plant-year`, `&lt; 10-4/plant-year` 정확. 주석 [a]–[d] 표 행. st: 4열로 어긋남(개선 없음) → 수동 |
| Table 5-3 Plant Capability DID Attributes | L1447 cap, L1449–1454 | 70 | F19 | 4 속성×평가초점 13개가 1열 공백연결(fill 0/4). st: rowspan 연속행이 1열로 밀림(fill 4/13) → R5b로 교정 가능 |
| Table 5-4 Event Sequence Model Framework (2쪽) | L1476 cap, L1478–1485, L1488–1490 | 72–73 | F20, F21 | 7행 3열 → 1열, 전 행 3분절(분할 가능), 헤더 반복. st: 3열 정확·병합(fill 16/16) |
| Table 5-5 Programmatic DID Attributes | L1540 cap, L1542–1546 | 75 | F19, F33 | 3 속성×7 초점. `Offsite Response Emergency response capability`(L1546) 공백 접착. st: rowspan shift(fill 3/7) |
| Table 5-6 Evaluation Considerations (2쪽) | L1557 cap, L1559–1564 (p77), L1567–1628 (p78 비표) | 77–78 | F07, F22, F36 | p77: 3열 유지(fill 4/8), 셀 내부 분절 오류. p78: 표 소실, 질문 13개가 `- 1.` 목록으로 떠돌고 소속 행 불명. st: 2쪽 병합, 전 6개 Focus 행 정확(헤더 1회 반복) |
| Table 5-7 Examples of Special Treatments | L1668 cap, L1670–1681 | 81 | F19 | 10 프로그램×요소 31개 1열 연결(fill 0/10). st: rowspan shift(fill 10/31) |
| Table 5-8 RIPB-DM Attributes | L1706 cap, L1708–1713 | 83 | F19 | 4 속성×초점 8개. `Uncertainty Management Magnitude and Sources of Uncertainties`(L1712) 접착. st: rowspan shift |
| Table 5-9 Plant Capability DID Evaluation Summary | L1807 cap(list), L1809–1812 | 87 | F05 | 정답(Margin Adequacy / Multiple Protective Measures / Prevention-Mitigation Balance / Functional Reliability / No Single Feature): Normal Op √/√/–/√/–; AOOs √/√/–/√/–; DBEs, BDBEs, DBAs 전부 √. md는 1셀. st: 정확 |
| Table 5-10 Programmatic DID Evaluation Summary | L1815 cap(list), L1818–1821 | 87 | F05, F33 | 정답(Q/R: Design…O&M / Human Errors / Mechanical Failures / Unknowns / Emergency Response Capability): Normal Op √/√/√/√/–; AOOs √/√/√/√/–; DBEs, BDBEs, DBAs 전부 √. md는 1셀. st: 정확 |
| Glossary (6쪽) | L1857–1868, 1871–1880, 1883–1891, 1894–1901, 1904–1909, 1912–1918 | 90–95 | F06, F21, F23, F10 | 35 용어 + 5 그룹행, 4열 → 1열(fill 0/120). 수치(AOO ≥1×10-2, DBE 1×10-4–1×10-2, BDBE 5×10-7–1×10-4, Risk-significant LBE 95%tile·1 %·2.5 mrem) 값 자체는 정확. 결합 오류 `FrequencyConsequence`, `SafetyRelated`, `PerformanceBased`, `1.42013`. st: 단일 46행 표, 4열 정확 |
| Phantom (Fig 3-3) | L555–557, L593–595 | 28 | F17 | 삭제 |
| Phantom (Fig 4-2) | L813–814 | 43 | F17 | 1열 표 + imageFile5, 삭제/figure 블록 |
| Phantom (Fig 5-1) | L1112–1117 | 57 | F17, F30 | 깨진 3개 1열 표, 삭제(설명박스 2문장은 figure 블록 보존) |
| Phantom (Fig 5-4) | L1233–1235 | 61 | F17 | 삭제 |

부가 검증: `--table-method cluster` 재변환은 26개 표 블록이 default와 완전히 동일(개선 없음). `--markdown-with-html`(struct-tree와 병용)은 `&lt;td&gt;` escape 버그로 `&lt;` 804개 발생(코디네이터 보고와 일치) — 사용 불가.

---

## 3. Figure inventory

| Figure ID | md lines | raster/vector | image file | debris lines to delete | Notes |
|---|---|---|---|---|---|
| 3-1 Frequency-Consequence Target | img L364, cap L366 (H5) | raster (p15, 468×399 pt) | imageFile1.png 975×832 | – | alt 없음. 앵커(그래프): 10 CFR 20 iso-risk 선 ≥10⁻¹/yr, 1 rem @10⁻¹–10⁻², 25 rem @10⁻⁴, 750 rem @5×10⁻⁷, 이하 수평. 본문 L373–376에 값 있음(단 L370 F01) → alt text에 앵커 5점 기재 권장 |
| 3-2 Process for Selecting and Evaluating LBEs | img L397, cap L399 (list) | raster (p19) | imageFile2.png 975×1043 | – | alt 없음, 캡션 list item. 내용은 Task 1–10 소제목과 대응 |
| 3-3 Flow Chart for Initial PRA Model Development | L553–600, cap L602 | vector (p28, curves 45) | – | L553–600 (26 non-blank, 988 chars; `###### Systems Engineering Inputs`, phantom 2) | 라벨 순서 뒤섞임. 본문 L549·L616이 좌/우 흐름 설명 → 삭제 무방 |
| 3-4 Use of the F-C Target to Define Risk-Significant LBEs | img L682, cap L684 | raster (p34) | imageFile3.png 1420×1031 | – | alt 없음. 2.5 mrem 하한·1 % 선은 본문 L705에 있음 |
| 4-1 SSC Function Safety Classification Process | img L787, cap L789 | raster (p40, 가로 페이지) | imageFile4.png 1279×842 | L791 `##### THIS PAGE INTENTIONALLY BLANK`(p41) | alt 없음. 그림 주석 `*Safety-Significant functions include those classified as risk-significant or required for defense-in-depth`, `** Only those SSCs selected by designer…`은 이미지에만 존재 → 전사 권장 |
| 4-2 Definition of Risk-Significant and Safety-Significant SSCs | L813–814, cap L817 (list + 본문 접착 `…SSCs The following key points…`) | hybrid (vector Venn + 62×61 pt raster 조각) | imageFile5.png 140×137 (회색 원, 무정보) | L813–814 (266 chars) | 라벨 5개(All Plant/PRA Modeled/Safety-Significant/Risk-Significant/Safety-Related SSCs)는 본문 bullet(L820–822)과 중복 |
| 4-3 LMP SSC Safety Categories and Safety Significant SSCs | L841–863, cap L865 | vector (p45) | – | L841–863 (12 non-blank, 677 chars) | 범주 정의 + 그림 주석 L859 `* SR SSCs are also relied on during DBAs…`(L851 `F-C Target*` 참조) — figure 블록으로 보존 권장 |
| 5-1 U.S. NRC’s Defense-in-Depth Concept | L1112–1120, cap L1122 | vector (p57) | – | L1112–1120 (7 non-blank, 548 chars; 깨진 표, `res`) | 설명박스 2문장("Layers of defense are defined…", "Protective measures are defined…")은 보존 가치 |
| 5-2 Framework for Establishing DID Adequacy | L1130–1169, cap L1171 (list) | vector (p58) | – | L1130–1169 (28 non-blank, 1,401 chars; `### PRA` 포함) | bullet 3묶음(7+8+6항목)이 본문 목록처럼 보임(L1130은 5.2 도입문 바로 뒤). 보존 시 figure 블록 |
| 5-3 Framework for Evaluating LBEs Using Layers of Defense | img L1196, cap L1198 | raster (p59) | imageFile6.png 970×819 | – | alt 없음. Layer 1–5 Objective/Success 문구는 본문에 없음 → 전사 권장(DID 질의에 중요) |
| 5-4 Integrated Process for Incorporation and Evaluation of DID | L1211–1282, cap L1284 | vector (p61, curves 95) | – | L1211–1282 (37 non-blank, 1,134 chars; phantom L1233–1235, `A` 기호 7행, 그림 내 약어목록 L1276–1278) | 18 Task 상자 순서 뒤섞임. 동일 Task 1–18이 본문 소제목으로 존재 → 삭제 무방 |

---

## 4. Heading outline check

**기준 outline**: pypdf `reader.outline` 61 bookmarks = front 6 (NOTICE, Abstract, TOC, LoF, LoT, LoA) + body 55 (depth 0: 6, depth 1: 19, depth 2: 30). TOC(L31–121)의 55항목과 제목·순서 일치. 추가로 PDF 폰트 기준 BoldItalic 11 pt 소제목 68개(outline 미포함). 절 제목(Calibri-Bold 11)과 캡션(Calibri-Bold 11)은 폰트가 같아 폰트만으로는 구분 불가 → 번호/접두어로 구분.

**현재 md heading 분포**: H1 1 (L5 제목), H2 12 (front 6 + chapter 6), H3 1 (`### PRA`), H5 113 (= 절 35 + Task 40 + 무번호 소제목 19 + blank page 1 + 그림 캡션 8 + 표 캡션 10), H6 1.

**요약 수치**

| 구분 | 총수 | 올바름 | 레벨 오류 | heading 아님 | 비고 |
|---|---|---|---|---|---|
| Chapter (depth 0) | 6 | 6 (H2) | 0 | 0 | 본문 표기는 대문자(`1 INTRODUCTION`) — 원문 유지 |
| x.y (depth 1) | 19 | 0 | 15 (H5) | 4 (plain 1, list 2, list+glued 1) | 목표 H3 |
| x.y.z (depth 2) | 30 | 0 | 20 (H5) | 10 (list 7, list+glued 3) | 목표 H4 |
| Task 소제목 | 43 | – | 40 (H5, 부모 무관) | 3 (list 2, list+glued 1) | 목표 = 부모+1 (3.2.2 하위 H5, 4.1·5.3 하위 H4) |
| 무번호 BoldItalic 소제목 | 25 | – | 19 (H5) | 6 (plain 4, glued 2) | 목표 = 부모+1 |
| 비-heading 승격 | – | – | – | – | `### PRA`(L1141), `###### Systems Engineering Inputs`(L553), `##### THIS PAGE INTENTIONALLY BLANK`(L791) → 삭제/강등 |
| 캡션 | 24 | – | 18 (H5) | 6 (list 5, plain 1) | 목표: heading 아닌 굵은 캡션 단락 |

**heading이 아닌 outline 절 14개 (line, 현재 형태 → 목표)**

| md line | 현재 | 목표 |
|---|---|---|
| L357 | plain `3.2 Advanced Non-LWR LBE Selection Approach` | H3 |
| L359 | list `- 3.2.1 Frequency–Consequence Evaluation Criteria` | H4 |
| L654 | list `- 3.3.5 Selection of Risk Metrics for PRA Model Development` | H4 |
| L893 | list `- 4.2 Definition of Safety-Significant and Risk-Significant SSCs` | H3 |
| L896 | list `- 4.2.1 Safety-Significant SSCs` | H4 |
| L1103 | list+glued `- 5.1 Defense-in-Depth Philosophy According to the NRC glossary, defense-in-depth is:` | H3 + 본문 분리 |
| L1432 | list `- 5.6.2 DID Guidelines for Defining Safety-Significant SSCs` | H4 |
| L1511 | list+glued `- 5.7.2 … Focus in LBE Review The evaluation of LBEs during the IDP will focus…` | H4 + 분리 |
| L1529 | list+glued `- 5.8.1 Guidelines for Programmatic DID Adequacy The adequacy of programmatic DID is based…` | H4 + 분리 |
| L1686 | list `- 5.9 Risk-Informed and Performance-Based Evaluation of DID Adequacy` | H3 |
| L1689 | list `- 5.9.1 Purpose and Scope of Integrated Decision-Making Activities` | H4 |
| L1730 | list+glued `- 5.9.3 IDP Actions to Establish DID Adequacy Adequacy of DID is confirmed…` | H4 + 분리 |
| L1768 | list `- 5.9.4 IDP Considerations in the Evaluation of DID Adequacy` | H4 |
| L1824 | list `- 5.9.6 Considerations in Documenting Evaluation of Plant Capability and Programmatic DID` | H4 |

**레벨만 틀린 outline 절 35개 (현재 `#####`)**
- → H3 (15): L233 1.1, L237 1.2, L253 1.3, L336 3.1, L543 3.3, L781 4.1, L918 4.3, L924 4.4, L1126 5.2, L1205 5.3, L1389 5.4, L1405 5.5, L1409 5.6, L1457 5.7, L1527 5.8
- → H4 (20): L391 3.2.2, L529 3.2.3, L620 3.3.1, L630 3.3.2, L640 3.3.3, L646 3.3.4, L707 3.3.6, L903 4.2.2, L930 4.4.1, L944 4.4.2, L950 4.4.3, L954 4.4.4, L968 4.4.5, L1413 5.6.1, L1441 5.6.3, L1501 5.7.1, L1553 5.8.2, L1698 5.9.2, L1801 5.9.5, L1849 5.9.7

**Task 소제목 43개 (부모별)**
- 3.2.2 (→H5) 16개: L402 Task 1 (**list**), L409 2, L413 3, L421 4, L431 5a, L435 5b, L439 6, L457 7, L461 7a, L485 7b (**list+glued**: `…10 CFR 20 In this task, the integrated risk of all the LBEs, is evaluated against three cumulative risk targets:`), L496 7c (**list**), L505 7d, L509 7e, L517 8, L521 9, L525 10
- 4.1 (→H4) 9개: L795 Task 1, L801 2, L805 3, L825 Tasks 4 and 5, L829 4A/5A, L833 4B/5B, L837 4C/5C, L871 6, L879 7 (Tasks 4A–4C는 "Tasks 4 and 5"의 하위로 H5도 가능)
- 5.3 (→H4) 18개: L1288 Task 1 … L1383 Task 18 (전부 H5)

**무번호 BoldItalic 소제목 25개 (부모별)**
- 3.3.5 (→H5): L657 Overall Plant Risk Metrics (**plain**), L678 Risk Significance Evaluations
- 4.4.5 (→H5): L970 Purpose of Special Treatment (**glued**: `Purpose of Special Treatment The purpose of special treatment is reflected…`), L1067 Relationship Between SSC Capability, Reliability, Mitigation, and Prevention, L1073 Role of SSC Safety Margins, L1081 Specific Special Treatment Requirements for SR and NSRST SSCs, L1087 Reliability Assurance for SSCs, L1091 Capability Targets for SSCs
- 5.2 (→H4): L1174 Plant Capability Defense-in-Depth (**plain**), L1182 Programmatic Defense-in-Depth (**단락 끝 접착** `…plant challenges. Programmatic Defense-in-Depth`), L1190 Risk-Informed Evaluation of Defense-in-Depth
- 5.8.2 (→H5): L1630 Quality and Reliability, L1636 Margin Adequacy, L1641 Treatment of Uncertainty in Programmatic DID, L1645 Compensation for Unknowns, L1653 Programmatic DID in Design
- 5.9.4 (→H5): L1771 Risk Triplet Examination (**plain**), L1775 State of Knowledge, L1779 Margin Adequacy, L1783 Sources of Uncertainties, L1791 Magnitude of Uncertainties, L1795 Compensatory Action Adequacy
- 5.9.6 (→H5): L1827 Simplify Change Evaluation (**plain**), L1841 Quantification of LBE Margins Against F-C Target, L1845 Summary Evaluation of DID Adequacy Baseline

---

## 5. File-specific observations and recommendations

### 5.1 `--use-struct-tree` 재변환 및 outline 재구축 평가 (요청 사항)

실행: JDK 17(`C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot\bin\java.exe`)로 opendataloader-pdf 2.5.7 jar 직접 호출, 출력은 `scratchpad\nei\conv_{base,st,sthtml,cluster,sr0.12,sr0.08,klb}\`. `conv_base`(default + page separator)는 현재 md와 **페이지 마커·빈 줄 외 완전히 동일**(결정적)함을 확인.

| 지표 | default (현 md) | struct-tree | 판정 |
|---|---|---|---|
| outline 55절 중 Markdown heading | 41 (전부 H5/H2, 레벨 오류 35) | **3** (3.3.3, 5.9, 5.9.3) | st 악화 |
| 잘못 승격된 heading | 3 + 캡션 18 | **23 본문 단락**을 H1/H3로 승격(예: `# analyses. Decisions to defer…`, `# Quantification of the frequencies…`, `# For each of the SSC functions…`, `### Given the simple systems…`), 캡션 2, Fig 5-4 전체가 `###` 한 줄 | st 크게 악화 |
| 표 (열 분리) | 14 블록 완전 붕괴, 4-1·5-9·5-10 √ 소실 | 3-1, 3-2, 4-1, 5-1, 5-4, 5-6, 5-9, 5-10, Acronyms, Glossary 정확; 5-3/5-5/5-7/5-8은 rowspan 연속행이 1열로 밀림(규칙 교정 가능); 4-1 RISC-2 행 1칸 밀림; 5-2는 4열로 어긋남 | **st 우수** |
| 쪽 분할 표 병합 | 안 됨 | 4-1, 5-4, 5-6, Glossary 병합 | st 우수 |
| `<br>` | 528 | 186 | st 우수 |
| 공백 소실 | 89 | 0 | st 우수 (단 `--space-ratio 0.12`로도 0) |
| 줄끝 hyphen/지수 부호 소실 | 62+ / 3 | 동일(`1×104`, `102/` 그대로) | 차이 없음 |
| 각주 | 본문 삽입(6 문장 분할) | 동일하게 쪽 끝 단락으로 삽입(† 분리만 개선) | 차이 없음 |
| 윗첨자 표지 | 0 | 0 (`<sup>` 없음) | 차이 없음 |
| st 고유 신규 오류 | – | 윗첨자 위치 이탈: `frequencies of 10 4.   -1/plant-year … Section`(원문 `of 10-1/plant-year … Section 4.`), `(at the 5 Figure 3-4 illustrates … th …`; bullet 이중화 `- • ` 110행; 단락 위치 이동 2건; 다쪽 표에서 `<!-- page 53 -->`, `54`, `78` 마커가 빈 채 뒤로 밀림 | 주의 |

**결론**
1. `--use-struct-tree`는 heading 계층과 각주를 **해결하지 못함**(오히려 heading 악화). 이 PDF의 H2/H3 태그는 Word 스타일과 대응하지 않음.
2. 반면 **표는 struct-tree본이 대부분 정확** → 표 블록만 캡션 매칭으로 이식하는 hybrid가 최선.
3. heading은 **pypdf outline(55, 제목·순서·depth 정확)** 으로 결정적 재구축 가능, 소제목 68개는 pdfplumber 폰트(`Calibri-BoldItalic`, 11 pt, 단독 행)로 결정적 추출 가능. 둘을 합치면 heading 결함 100 %를 B-class로 해결.
4. 공백 소실은 `--space-ratio 0.12`(89건 전부 정확, 부작용 0) 재변환으로 해결. 줄끝 hyphen은 `--keep-line-breaks`(검증: `risk-⏎`, `10-⏎2`, `NEI-00-⏎04`, `ways—⏎` 보존) 후 "hyphen 유지 결합" 또는 PDF-유래 사전 치환으로 해결.

**5.1b 가로 페이지 / `content_safety_off="off-page"` / `include_header_footer` 점검 (코디네이터 요청)**
- 가로 페이지: p14 (Table 3-1), p40–41 (Fig 4-1 + blank), p52–54 (Table 4-1), p89–95 (Glossary) — 모두 `/Rotate` 없이 MediaBox 792×612 pt. 텍스트 최대 x1 = 734 pt(< 792).
- 절단 여부: 위 13쪽에서 x1 > 612 pt인 단어 행(총 140행)을 md와 대조 → footer `nei.org N`(의도적 제거)을 제외하면 **누락 0**. 즉 이 파일에는 off-page 절단이 없음.
- 재변환 비교(scratchpad `conv_base_os`, `conv_st_os`, `conv_base_osf`, `conv_st_osf`): `--content-safety-off off-page`는 default·struct-tree 모두 **바이트 단위 동일**. `--include-header-footer`는 default에서 `###### August 2019` 93행 + `###### © NEI 2019. All rights reserved. nei.org N` 87행(H6, 순수 잡음)만 추가하고 복원되는 소제목은 0; struct-tree에서는 빈 줄 360개만 추가. → NEI 18-04에는 두 옵션 모두 **불필요**(소제목 68개·outline 55절은 이미 md 텍스트에 전부 존재).

### 5.2 권장 정리 규칙 (적용 순서)

- **R0 재변환(스크래치 → 검토 후 반영)**: `--markdown-page-separator "<!-- page %page-number% -->" --space-ratio 0.12` (+ 선택 `--keep-line-breaks`). 표 이식용으로 `--use-struct-tree` 변환본 병행.
- **R1 frontmatter**: `doc_id: NEI 18-04`, `revision: 1`, `title: Risk-Informed Performance-Based Technology Inclusive Guidance for Non-Light Water Reactor Licensing Basis Development`, `series_title: Modernization of Technical Requirements for Licensing of Advanced Non-Light Water Reactors`, `date: 2019-08`, `adams: ML19241A472`, `docket: PROJ0689`, `publisher: NEI`, `source_pdf`, `pages: 95`, `page_label_offset: body printed page = pdf page − 8`.
- **R2 삭제**: L1 `18-04`(frontmatter로), L11, footer 7행, L340 `August 2019`, TOC/LoF/LoT(L27–173), `THIS PAGE INTENTIONALLY BLANK`(L791), (선택) `SEE TABLES FOLLOWING PAGES`(L1855).
- **R3 heading**: outline 55절 매칭(정규화 제목 선두 일치, 형태 무관: `#####`/`- `/plain) → depth 0/1/2 = H2/H3/H4, glued 본문은 제목 뒤에서 분리(L1103, L1511, L1529, L1730). 소제목 68개 → 부모+1, glued 분리(L485, L970), L1182는 단락 끝의 `Programmatic Defense-in-Depth`를 떼어 다음 줄 heading으로. 비-heading 3건 삭제·강등, 캡션 24개를 `**Figure/Table N-M. …**` 단락으로 통일.
- **R4 그림**: vector 잔해 6 span 삭제(§3), 정보성 텍스트는 `> [!figure]- Figure N-M text` 블록으로; raster 5개 alt text 작성(C); imageFile5 참조 삭제.
- **R5 표**: (a) 13개 번호 표·Acronyms·Glossary를 st본으로 교체(캡션 앵커). (b) rowspan-shift 교정: 2열 표(5-3, 5-5, 5-7, 5-8)에서 "col2 공란 & col1 비공란 & 앞 행이 속성행"이면 col1→col2 이동, col1은 직전 속성으로 채움. (c) 4-1: 단일 헤더(`Special Treatment Category | SR SSC | NSRST SSC | NST SSC | Available Guidance`), RISC-2 행 √ 이동, 그룹행을 `Group` 열로, 반복 헤더 삭제, 주석 1–5 footnote화. (d) 5-9/5-10 헤더 평탄화. (e) 5-2 수동 재작성. (f) 3-2 수식 수동 전사. (g) `<br>` 정규화.
- **R6 수치**: F01 3건 복원 → 지수 50건 표기 통일(코퍼스 공통 규칙) → entity decode 11건.
- **R7 hyphen 사전**: PDF 줄끝 `a-⏎b`에서 결합형 `ab`를 수집하고, PDF 인라인에 `ab`가 0회인 형태만 md에서 `a-b`로 치환(28종/62건 + `defense-indepth`→`defense-in-depth` 2, `Defense-inDepth` 1, `NEI-0004`→`NEI-00-04`, `1.42013`→`1.4-2013`), em dash 1건(L1793 `ways—frequency`).
- **R8 각주**: 페이지 마커 기준으로 쪽마다 본문 `*`/`†` 참조(15+1) ↔ 각주 본문(16) 1:1 매핑 → `[^pNN]`; 각주 본문을 문서 끝(또는 절 끝)으로 이동하고 끊긴 문장 6건 재결합.
- **R9 목록**: false list item 6건 `- ` 제거, 중첩 목록 33항목 들여쓰기 복원, `- 1.` 이중 표지 제거, `•`/inline `o` 정리, 쪽 경계 분할 단락 21건 재결합.

### 5.3 자동 수정 금지 / 함정

- **원문 오타 보존**: `stan`(L545), `mean -frequency`(L745), `release s`(L1493), `Acronymns`(L1276), `5x10-7/plant year`(L468), `complimentary`(L777, L1099), `threating`(L1797). 변환 결함이 아님.
- **줄끝 hyphen 일괄 제거 금지**: 이 PDF(Word 원본)에는 자동 hyphenation이 없음 — 줄끝 `-`는 전부 실제 hyphen. 쪽 경계 재결합 시 L441 `all non-` + L445 `safety-related`는 `non-safety-related`로(hyphen 유지).
- **`10-2` 형태는 범위가 아니라 지수**(47건 모두 `/plant-year` 앞). 반대로 `10 CFR 50.34`, `NUREG-1855`, `SECY-16-0012` 등은 치환 대상 아님 — 지수 regex는 `/plant` lookahead로 한정.
- **Acronym 목록의 `*`(24개)는 "Glossary 정의 용어" 표시** — 각주 변환 대상 아님. 각주 참조는 본문 15개 `*` + 1개 `†`만. L851 `F-C Target*`은 Fig 4-3 그림 주석(L859) 참조.
- **Table 4-1 `√ 2`, `√ 3 3`의 `2`/`3`은 각주 참조**(NSRST/NST 칸) — 값으로 해석 금지.
- **Table 5-2 Layer 5 공란은 rowspan 누락** — Layer 4의 Quantitative/Qualitative 지침을 공유하므로 채워야 함(비워두면 오답).
- **Table 3-2·식 R_j는 text layer 자체가 손상** — 문자 중복 제거 스크립트로 복구 불가(`base`→`bbbb`), 반드시 이미지 기준 수동.
- **동일 소제목명 중복**: `Task 1`~`Task 7`이 LBE(3.2.2)·SSC(4.1)·DID(5.3) 절차에 각각 존재, `Margin Adequacy` ×2 — 중복 제거/병합 금지, chunk에 breadcrumb(절 경로) 포함 필요.
- struct-tree본 채택 시 페이지 마커 위치가 다쪽 표에서 어긋나므로 page anchor는 default 재변환본 기준으로 부여.
- `--markdown-with-html`은 2.5.7에서 `&lt;td&gt;` escape 버그(804건) — 사용 금지. `--table-method cluster`는 이 파일에 효과 없음.

### 5.4 에이전트 질의 대상 데이터 상태 (요청 초점)

- **F-C Target**: 본문 L373–376 값 정확(단 L374 `of10-1`, `plantyear` 형태 결함), L370 DBE 범위 `102` 오류(F01), Fig 3-1 raster(alt 없음).
- **LBE 빈도 정의**: Table 3-1 붕괴 + `1×104` 오류; Glossary L1868/L1873/L1874 값 정확(1열 붕괴); 본문 L427·L468 정확 → 현재 md 안에서 DBE 하한이 10⁻⁴와 10⁴로 상충.
- **Risk importance measures (Table 3-2)**: 8개 수식 모두 판독 불가 — 최우선 수동 수정.
- **Special treatments (Table 4-1)**: 적용성 행렬 소실 — st본 + 2건 교정.
- **DID 표(Ch.5)**: 5-2 rowspan, 5-6 p78 구조 소실, 5-9/5-10 행렬 소실, 나머지 목록형 붕괴.
- **Cumulative risk targets**: L487–489, L700–702, L745–747(`&lt;`), L911–913 — 1/plant-year(100 mrem), 5×10-7(early fatality, 1 mile), 2×10-6(latent cancer, 10 miles) 정확; SSC 기여 1 % 기준 5×10-9·2×10-8 정확, **10-2만 L911에서 `102`로 오류**.

### 5.5 frontmatter/tag 후보 식별자 (간략)

- LBE 범주·지표: AOO, DBE, BDBE, DBA, LBE, F-C Target, TLST, QHO, MST, POS, ES; 빈도 경계 1×10-2, 1×10-4, 5×10-7 /plant-year; F-C 앵커 100 mrem, 1 rem, 25 rem, 750 rem; risk-significant LBE 기준 2.5 mrem·1 %.
- 기능·분류: FSF, PSF, RSF, RFDC, SRDC, SR / NSRST / NST, safety-significant, risk-significant, DBEHL, RAP.
- DID·의사결정: DID, IDP, IDPP, RIPB-DM, layers of defense 1–5, plant capability DID, programmatic DID.
- 절차 Task ID(중복 방지 접두어 권장): `LBE-Task-1…10 (5a,5b,7a–7e)`, `SSC-Task-1…7 (4A/5A–4C/5C)`, `DID-Task-1…18`.
- 규제/표준 교차참조 패턴: `10 CFR 20/50.34/50.69/50.155/52.47/52.79/52.137/52.157/73/100`, `RG 1.174/1.201/1.203/1.232/1.100/1.178`, `SRP 15.0/17.4/17.5/19.3`, `NUREG-1855/2122`, `NUREG/KM-0009`, `SECY-16-0012`, `IAEA-TECDOC-1570`, `ASME/ANS RA-S-1.4-2013`, `NEI 00-04`, `INL/EXT-14-31179`; 내부 참조 `Figure N-M`, `Table N-M`, `Section N.N`, `Task Nx`.
