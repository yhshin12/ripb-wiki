---
type: natrium
aliases: []
sources: [SER_KU1_CP, PSAR_ch03]
status: checked
verified: 2026-10-30
term:
tags: [natrium, dba, siting, nrc-review]
terms_pending: []
---
# NRC의 주요사고 평가 (NRC Evaluation of the Major Accident)

> [!abstract] 요약
> 사업자는 `RG 1.253` Option 1에 따라 Design Basis Accident%%t:DBA%% 결과로 주요사고(Major Accident)%%t:MAJOR_ACCIDENT%%를 정하고, 용기 내 DBA%%t:DBA%%로 범위를 좁혀 core blockage and local faults DBA%%t:DBA%%를 선정했다. NRC staff는 이 사고가 출력운전 중 용기 내 DBA%%t:DBA%%는 bound하지만 용기 외 사건과 연료취급 DBA%%t:DBA%%는 bound하지 못한다고 명시했다. 그럼에도 Licensing Basis Event%%t:LBE%% 평가가 뒷받침하는 DBA%%t:DBA%% 집합이 안전·부지 해석 요건을 포괄적으로 다룬다고 판단해 선정을 수용했다.

## 원문 사실
- "Option 1: Use the DBA dose consequence results from an LMP-based approach to establish the acceptability of the EAB and LPZ" [SER_KU1_CP §3.3.1.7 p.219]
- "Option 2: Use the greater of the dose consequence results from the bounding DBA and from a bounding BDBE, as identified in the LMP-based approach, to establish the acceptability of the EAB and LPZ" [SER_KU1_CP §3.3.1.7 p.220]
- "To characterize the major accident for KU1, the PSAR states that the applicant chose to use option 1 described in RG 1.253, staff position C.3.b." [SER_KU1_CP §3.3.1.7 p.221]
- "The applicant narrowed the consideration to in-vessel DBAs to be consistent with the 10 CFR 50.34(a)(1) description of the accident analysis as evaluating the postulated fission product release from the core into the containment." [SER_KU1_CP §3.3.1.7 p.221]
- "The PSAR states that the core blockage and local faults DBA described in PSAR section 3.9.6.1 was selected as the major accident because it represents the potential hazard not exceeded by any other in-vessel DBE or in-vessel DBA." [SER_KU1_CP §3.3.1.7 p.221]
- "Review of PSAR section 3.9 shows that of the nine DBA with release scenarios that are described, only the at-power in-vessel DBAs with core damage and release into the functional containment are consistent with the 10 CFR 50.34(a)(1)(ii)(D) description of a postulated fission product release from the core into containment." [SER_KU1_CP §3.3.1.7 p.221]
- "The staff notes that although the offsite radiological consequences of the selected major accident are bounding for at-power in-vessel DBAs, that is not true for the ex-vessel and fuel handling DBAs. This means that the consequences of the major accident analyzed by USO do not bound the consequences of all DBAs as was done in reactor licensing precedents. This would necessitate additional justification as discussed in footnote 10 to RG 1.253 option 1." [SER_KU1_CP §3.3.1.7 p.221]
- "Review of the DBAs in PSAR section 3.9 shows that the offsite dose results for the selected major accident are higher than other at-power in-vessel DBAs." [SER_KU1_CP §3.3.1.7 p.221]
- "Because of the differing analysis methodologies, the LBE dose results should not be directly compared to the" [SER_KU1_CP §3.3.1.7 p.221]
- "the staff’s judgment is that the PSAR DBAs, as supported by evaluation of the LBEs, comprehensively address the safety and siting analyses consequence analysis requirement." [SER_KU1_CP §3.3.1.7 p.222]
- "Therefore, based on its assessment of the PSAR information in the context of the regulatory description of the required safety analysis, the staff determined the selection of the PSAR section 3.9.6.1 core blockage and local faults DBA as the major accident, as supported by the assessment of DBAs in the LMP methodology, appropriately addresses the purpose and intent of the 10 CFR 50.34(a)(1)(ii)(D) safety analysis of a major accident postulated from considerations of possible credible accidental events." [SER_KU1_CP §3.3.1.7 p.222]
- "The results show that the offsite dose consequences for each of the DBAs with radiological release meet the dose criteria in 10 CFR 50.34(a)(1)(ii)(D) with margin. This includes the results of the core blockage and local faults DBA selected as the major accident." [SER_KU1_CP §3.3.1.7 p.222]
- "This event was selected as the major accident, as it represents the potential hazard not exceeded by any other in-vessel design basis event or in-vessel DBA." [PSAR_ch03 §3.3.3 p.47]

| DBE ID | DBA ID | DBA Title | DBA 2-hour Exclusion Area Boundary TEDE (rem) | DBA 30-day Low Population Zone Boundary TEDE (rem) | 출처 |
|---|---|---|---|---|---|
| LFF-SAO-BL | LFF-SAO-CN | Core Blockage and Local Faults | 1.33E-01 | 9.60E-01 | [PSAR_ch03 Table 3.5-4 p.60-61] |
| RFH-FDIV-1 | RFH-FDIV-CN | Fuel Handling Event Occurs While Moving Fuel Assembly in the Reactor Vessel | 1.74E+00 | 3.19E+00 | [PSAR_ch03 Table 3.5-4 p.60-61] |

## 해설
`RG 1.253`은 주요사고%%t:MAJOR_ACCIDENT%% 평가에 두 방법을 둔다.
- Option 1: Licensing Modernization Project%%t:LMP%% 기반 DBA%%t:DBA%% 선량 결과로 `EAB`와 `LPZ`의 적합성을 보인다.
- Option 2: bounding DBA%%t:DBA%%와 bounding Beyond Design Basis Event%%t:BDBE%% 중 큰 선량을 쓴다.

사업자는 Option 1을 택했다. 그리고 10 CFR 50.34(a)(1)의 "노심에서 격납으로의 핵분열생성물 방출"이라는 서술에 맞추어 용기 내 DBA%%t:DBA%%로 범위를 좁혔다. staff는 방출이 있는 DBA%%t:DBA%% 아홉 건 가운데 이 서술에 맞는 것은 노심 손상과 기능적 격납 내 방출이 있는 출력운전 중 용기 내 DBA%%t:DBA%%뿐이라고 확인했다.

staff는 선정된 사고의 부지 외 선량이 출력운전 중 용기 내 DBA%%t:DBA%%를 bound하지만, 용기 외 사건과 연료취급 DBA%%t:DBA%%는 bound하지 못한다고 명시했다. 따라서 과거 원자로 인허가 선례처럼 모든 DBA%%t:DBA%%를 bound하지는 않으며, `RG 1.253` Option 1의 각주 10에 따른 추가 정당화가 필요하다고 보았다. 그럼에도 LBE%%t:LBE%% 평가가 뒷받침하는 `PSAR` DBA%%t:DBA%% 집합이 안전·부지 해석의 선량 요건을 포괄적으로 다룬다고 판단해 선정을 수용했다. 방출이 있는 모든 DBA%%t:DBA%%는 여유를 두고 선량 기준을 충족한다.

C58과의 관계는 다음과 같다. `PSAR` §3.3.3은 선정 사고가 다른 어떤 "in-vessel" DBA%%t:DBA%%에도 넘어서지 않는다고 적는다. 그러나 용기 내 연료취급 DBA%%t:DBA%%인 RFH-FDIV-CN의 low-population zone%%t:LPZ%% 선량(3.19E+00 rem)은 선정 사고(9.60E-01 rem)보다 크다. staff는 bound 범위를 "at-power in-vessel" DBA%%t:DBA%%로 한정하고, 연료취급 DBA%%t:DBA%%는 bound되지 않는다고 따로 적었다. 다만 `SER`은 `PSAR` §3.3.3 문장의 범위 자체를 판정하지 않는다. `PSAR`이 함께 든 "maximum core damage" 기준이 이 차이를 해소하는지도 원문에서 판단할 수 없으므로, C58은 기록된 상태로 둔다.

## 관련 문서
- [[SER_KU1_CP]]
- [[PSAR_ch03]]
- [[Natrium_DBA_List]]
- [[Natrium_SER_LBE_Methodologies_Review]]
