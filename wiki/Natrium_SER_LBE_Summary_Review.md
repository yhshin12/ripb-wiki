---
type: natrium
aliases: []
sources: [SER_KU1_CP]
status: checked
verified: 2026-10-16
term:
tags: [natrium, lbe, nrc-review]
terms_pending: []
---
# NRC의 LBE 요약 평가와 NEI 18-04 이탈 두 가지 (NRC Evaluation of the LBE Summary and Two Deviations from NEI 18-04)

> [!abstract] 요약
> NRC staff는 Kemmerer Unit 1의 Licensing Basis Event%%t:LBE%% 식별·분류가 NEI 18-04와 `RG 1.233`에 맞는다고 보면서 두 가지 이탈을 지적했다. 첫째는 Beyond Design Basis Event%%t:BDBE%% 하한을 95th percentile이 아닌 mean 빈도로 판정한 것이고, 둘째는 빈도 불확도범위(uncertainty band)%%t:UNCERTAINTY_BAND%%가 Design Basis Event%%t:DBE%% 영역에 걸치는 Anticipated Operational Occurrence%%t:AOO%%와 BDBE%%t:BDBE%%에 대해 Design Basis Accident%%t:DBA%%를 만들지 않은 것이다. 사업자는 둘째 이탈에 대해 operating license%%t:OL%% 신청에서 절차를 고쳤다.

## 원문 사실
- "Two deviations from the methodology were identified based on the staff’s review." [SER_KU1_CP §3.4.1 p.225]
- "The first deviation was in the lower range used in identifying BDBEs. RG 1.233 states, “The F-C target and related discussions in NEI 18-04 include an upper bound event sequence frequency (i.e., 95th percentile) of 5E-07/plant-year to define the lower range of BDBEs.”" [SER_KU1_CP §3.4.1 p.225]
- "While USO did use the 95th percentile frequency when determining which events to evaluate as BDBEs, mean frequency was used when determining which events would be classified and included in the CP application as BDBEs." [SER_KU1_CP §3.4.1 p.225]
- "Frequency and consequence information for the additional events that would be categorized as BDBEs if the 95th percentile were used are provided in SE table 3.4-1 below." [SER_KU1_CP §3.4.1 p.225]
- "USO confirmed these values and the intention to continue using mean frequency to determine classification of BDBEs in response to the request for confirmation (RCI)-1 (ML25259A180)." [SER_KU1_CP §3.4.1 p.225]
- "The second deviation from RG 1.233 was that USO did not generate DBAs for AOOs and BDBEs with frequency bands that extend into the DBE region when identifying and classifying LBEs." [SER_KU1_CP §3.4.1 p.225]
- "Section 3.2.2 of NEI 18-04: “The mean values of the frequencies are used to classify the LBEs into AOOs, DBEs, and BDBE categories. However, when the uncertainty bands defined by the 5th and 95th percentile of the frequency estimates straddles a frequency boundary, the LBE is evaluated in both LBE categories.”" [SER_KU1_CP §3.4.1 p.225]
- "By limiting this evaluation Task 7a, no DBAs were created for AOOs with 5th percentile frequencies or BDBEs with 95th percentile frequencies that extend into the DBE region." [SER_KU1_CP §3.4.1 p.226]
- "USO updated its process to identify DBAs for AOOs and BDBEs with uncertainty bands that extend into the DBE region for its OL application as stated in section 3.9 of the PSAR." [SER_KU1_CP §3.4.1 p.226]
- "Not unexpectedly at the CP stage, the staff found that not all event sequences had unique source terms and consequence modeling performed." [SER_KU1_CP §3.4.1 p.227]
- "Table 3.4-2 of this SE shows that there are seven LBEs where only a single event from the IE family appears in the non-DBA LBEs within the PSAR." [SER_KU1_CP §3.4.1 p.227]
- "Two of these seven LBEs, RFH-OERC-BL and RFH-FDRC-1, are related as release events both occurring in the pin removal cell (PRC)." [SER_KU1_CP §3.4.1 p.227]
- "the mean failure frequency of the PRC is 1.5E-05 per plant year and it is attributed with reducing the 30day TEDE by a factor of" [SER_KU1_CP §3.4.1 p.227]
- "This reliability and capability may not be achievable for a hot cell." [SER_KU1_CP §3.4.1 p.227]
- "the staff concluded that the treatment of the PRC is potentially non-conservative but given the preliminary nature of the design and that the PRC is currently SR for radionuclide retention, the evaluation was sufficient for the CP stage." [SER_KU1_CP §3.4.1 p.227]
- "The staff identified one event, the sodium leakage from the RV into the RV-GV annulus, that potentially needs to be updated to an LBE at the OL." [SER_KU1_CP §3.4.1 p.228]
- "during audit discussions, the applicant acknowledged that the mean frequency of an RV leak should be in the BDBE range. The staff notes that this event therefore should have been identified as an LBE in the PSAR." [SER_KU1_CP §3.4.1 p.228]
- "PSAR section 3.4 states that LBEs are selected according to the NEI 18-04 methodology without deviation." [SER_KU1_CP §3.3.1.9 p.224]
- "The staff reviewed the LBE summary information described in PSAR section 3.5 and determined that the identification and classification of LBEs was consistent with NEI 18-04 and RG 1.233, with the two exceptions noted above." [SER_KU1_CP §3.4.2 p.228]

| LBE | 5th Percentile Frequency | Mean Frequency | 95th Percentile Frequency | 5th Percentile 30day EAB TEDE [rem] | Mean 30-day EAB TEDE [rem] | 95th Percentile 30day EAB TEDE [rem] | 출처 |
|---|---|---|---|---|---|---|---|
| RFH-OERC-EX1 | 4.81E-09 | 3.30E-07 | 1.19E-06 | 1.20 | 3.31 | 5.05 | [SER_KU1_CP Table 3.4-1 p.229] |
| IPI-IHEL-EX1 | 1.41E-08 | 1.57E-07 | 5.28E-07 | no release | no release | no release | [SER_KU1_CP Table 3.4-1 p.229] |

## 해설
staff가 지적한 첫째 이탈은 BDBE%%t:BDBE%% 하한의 판정 기준이다. `RG 1.233`은 BDBE%%t:BDBE%% 하한을 95th percentile 5E-07/plant-year로 정의한다고 인용된다. 사업자는 어떤 사건을 BDBE%%t:BDBE%%로 평가할지는 95th percentile로 정했지만, `CP` 신청서에 BDBE%%t:BDBE%%로 분류해 싣는 기준은 mean 빈도로 했다. 이 기준으로 빠진 사건은 Table 3.4-1의 두 건이다. RFH-OERC-EX1은 mean 3.30E-07, 95th 1.19E-06/plant-year이고, IPI-IHEL-EX1은 mean 1.57E-07, 95th 5.28E-07/plant-year이다. 사업자는 RCI-1 답변에서 mean 사용을 유지하겠다고 확인했다.

staff가 인용한 NEI 18-04 문장은 mean으로 LBE%%t:LBE%%를 분류하되, 불확도범위%%t:UNCERTAINTY_BAND%%가 경계에 걸치면 두 범주 모두에서 평가하라고 한다. 둘째 이탈은 이 처리를 Task 7a 평가에만 적용하고 DBA%%t:DBA%%를 만드는 데는 적용하지 않은 것이다. 사업자는 OL%%t:OL%% 신청에서 이 절차를 고쳤다고 적혀 있다.

그 밖의 지적은 다음과 같다.
- **대표 선원항(source term)%%t:SOURCE_TERM%% 사용:** `CP` 단계에서 모든 사건열에 고유한 선원항%%t:SOURCE_TERM%%과 선량 해석이 있지는 않았다.
- **사건 하나뿐인 `IE` family:** non-DBA LBE%%t:LBE%%에 사건이 하나만 나오는 Initiating Event%%t:IE%% family가 일곱 개이다. 그 가운데 `PRC` 관련 사건 둘이 있다. staff는 `PRC`의 mean 고장 빈도(1.5E-05/plant-year)와 선량 저감 능력이 hot cell로는 달성되지 않을 수 있어 처리가 잠재적으로 비보수적이라고 보았다. 다만 `PRC`가 현재 Safety-Related%%t:SR%%이므로 `CP` 단계에는 충분하다고 판단했다.
- **누락 가능 LBE%%t:LBE%%:** 원자로 용기에서 RV-GV annulus로의 소듐 누설은 mean 빈도가 BDBE%%t:BDBE%% 범위라는 점을 사업자가 audit에서 인정했다. staff는 이 사건이 `PSAR`에서 LBE%%t:LBE%%로 식별되었어야 한다고 적었다.

`PSAR` §3.4가 NEI 18-04를 "without deviation" 따른다고 적은 것과 달리, staff는 이탈 두 가지를 찾았다([[Natrium_SER_LBE_Methodologies_Review]]). 하한 판정이 mean과 95th percentile 중 무엇이냐는 문제는 공개 노트 [[LBE_Frequency_Categories]]의 disputed 판정과 관련된 쟁점이며, [[RG_1233_LBE_Staff_Position]]과도 관련된다.

## 관련 문서
- [[SER_KU1_CP]]
- [[LBE_Frequency_Categories]]
- [[Natrium_LBE_Selection]]
- [[Natrium_BDBE_List]]
- [[Natrium_SER_LBE_Methodologies_Review]]
- [[RG_1233_LBE_Staff_Position]]
