---
type: concept
aliases: [RFDC]
sources: [NEI_18-04]
status: checked
verified: 2026-09-15
term: RFDC
tags: []
terms_pending: []
---
# Required Functional Design Criteria (RFDC)

> [!abstract] 요약
> Required Functional Design Criteria%%t:RFDC%%는 Required Safety Function%%t:RSF%%을 만족하는 데 필요충분한, 원자로 설계에 고유한 기능 기준이다. Structures, Systems, and Components%%t:SSC%% 안전 분류와 SSC%%t:SSC%% 성능·special treatment%%t:SPECIAL_TREATMENT%% 요건, Safety-Related Design Criteria%%t:SRDC%% 도출 사이의 다리가 되는 것이 그 목적 가운데 하나이며, SRDC%%t:SRDC%%는 RFDC%%t:RFDC%%마다 설계자가 식별한다.

## 원문 사실
- "Reactor design-specific functional criteria that are necessary and sufficient to meet the RSFs" [NEI_18-04 §6 p.90]
- "Design criteria for SR SSCs that are necessary and sufficient to fulfill the RFDCs for those SSCs selected to perform the RSFs" [NEI_18-04 §6 p.90]
- "As noted previously, SSCs classified as SR perform one or more safety functions that are required to perform either of the following:" [NEI_18-04 §4.4.1 p.48]
- "Mitigate DBEs within the F-C Target and DBAs within 10 CFR 50.34 dose limits" [NEI_18-04 §4.4.1 p.48]
- "Prevent any high-consequence BDBEs (those with doses exceeding 10 CFR 50.34 dose limits) from exceeding 1E-04/plant-year in frequency and thereby migrating into the DBE region of the F-C evaluation" [NEI_18-04 §4.4.1 p.48]
- "These RSFs are used within this process to define a set of reactor-specific RFDCs from which SRDCs may be derived." [NEI_18-04 §4.4.1 p.48]
- "Because the RFDCs are derived from a specific reactor technology and design, supported by a design-specific PRA, and related to a set of design specific RSFs, each non-LWR design would require the development of a unique set of RFDCs." [NEI_18-04 §4.4.1 p.48]
- "One purpose of the RFDCs is to form a bridge between the safety classification of SSCs and the derivation of SSC performance, special treatment requirements, and SRDCs." [NEI_18-04 §4.4.1 p.48]
- "The process for identifying the RSFs for a given reactor starts with a review of the safety functions modeled in the PRA for the prevention and mitigation of LBEs and identifying which of those PSFs, if not fulfilled, would likely increase the consequences of any of the DBEs beyond the F-C Target." [NEI_18-04 §4.4.1 p.49]
- "This normally involves implementation of sensitivity analyses in which the performance of each PSF that mitigates the consequences of each DBE is removed and consequences re-evaluated." [NEI_18-04 §4.4.1 p.49]
- "This is just one example of the use of sensitivity analyses in this process." [NEI_18-04 §4.4.1 p.49]
- "Sensitivity analyses are also performed in the development of the PRA and in the RIBP evaluation of DID as part of the approach to addressing uncertainties in the estimation of LBE frequencies and consequences, including uncertainties in the mechanistic source terms." [NEI_18-04 §4.4.1 p.49]
- "Requirements for performing these analyses are covered in ASME/ANS-RA-S-1.4." [NEI_18-04 §4.4.1 p.49]
- "From the RSFs, a top-down logical development is used to define the functional requirements that must be fulfilled for the reactor design to meet each RSF." [NEI_18-04 §4.4.1 p.49]
- "The RFDCs may be viewed as functional criteria that are defined in the context of the specific reactor design features that are necessary and sufficient to meet the RSF." [NEI_18-04 §4.4.1 p.49]
- "The corresponding SRDCs are then developed from the RFDCs." [NEI_18-04 §4.4.1 p.49]
- "For each of the RFDCs, each designer should identify a set of Safety-Related Design Criteria (SRDC) appropriate to the SR SSCs assigned to perform the RSFs." [NEI_18-04 §4.4.2 p.49]
- "The design requirements are performance-based and tied to RSFs, derived from the LBEs, and used to systematically select the SR SSCs." [NEI_18-04 §4.4.2 p.49]
- "SR SSCs must be capable of mitigating the DBAs within the 10 CFR 50.34 dose limits." [NEI_18-04 §4.4.5 p.56]
- "These SR SSCs shall include appropriate RFDC for such functions." [NEI_18-04 §4.4.5 p.56]
- "RFDC provide a bridge between the DBAs and the formulation of Safety Related Design Criteria (SRDC) for the SR SSCs." [NEI_18-04 §5.3 Task 14 p.65]
- "DID attributes such as redundancy, diversity, and independence, and the use of passive and inherent means of fulfilling RSFs are used in the formulation of RFDCs." [NEI_18-04 §5.3 Task 14 p.65]

| Group | Special Treatment Category | SR SSC | Available Guidance | 출처 |
|---|---|---|---|---|
| Additional Special Treatment Requirements | Required Functional Design Criteria | √ | Guidance in this guidance document, INL/EXT-14-31179 | [NEI_18-04 Table 4-1 p.52] |

## 해설
원문은 Safety-Related%%t:SR%% SSC%%t:SSC%%가 수행하는 안전 기능을 두 가지로 정리한다. 하나는 Design Basis Event%%t:DBE%%를 Frequency-Consequence Target%%t:FC_TARGET%% 안으로, Design Basis Accident%%t:DBA%%를 10 CFR 50.34 선량 한도 안으로 완화하는 기능이다. 다른 하나는 선량이 그 한도를 넘는 Beyond Design Basis Event%%t:BDBE%%의 빈도가 1E-04/plant-year를 넘어 DBE%%t:DBE%% 영역으로 옮겨 가지 않게 막는 기능이다. 이 절차는 이 RSF%%t:RSF%%로부터 원자로별 RFDC%%t:RFDC%% 집합을 정의하며, SRDC%%t:SRDC%%는 그 RFDC%%t:RFDC%%에서 도출될 수 있다.

RFDC%%t:RFDC%%는 특정 원자로 기술과 설계에서 나오고 설계별 PRA의 뒷받침을 받으며 설계별 RSF%%t:RSF%%와 연결되므로, 비경수형원전(non-light-water reactor)%%t:NON_LWR%% 설계마다 고유한 RFDC%%t:RFDC%% 집합을 개발해야 한다. 원문은 RFDC%%t:RFDC%%의 목적 가운데 하나로 SSC%%t:SSC%% 안전 분류와 SSC%%t:SSC%% 성능 요건, special treatment%%t:SPECIAL_TREATMENT%% 요건, SRDC%%t:SRDC%% 도출 사이의 다리 역할을 든다. §5.3의 심층방어(Defense-in-Depth)%%t:DID%% 통합 체계에서 RFDC%%t:RFDC%%를 다루는 과업은 RFDC%%t:RFDC%%를 DBA%%t:DBA%%와 SRDC%%t:SRDC%% 작성 사이의 다리로 적고, 중복성·다양성·독립성과 피동·고유 수단의 활용 같은 심층방어%%t:DID%% 속성이 RFDC%%t:RFDC%% 작성에 쓰인다고 적는다.

RSF%%t:RSF%% 식별은 PRA에 모델링된 safety function을 검토해, 수행되지 않으면 어떤 DBE%%t:DBE%%의 결말을 F-C Target%%t:FC_TARGET%% 밖으로 키울 가능성이 큰 PRA Safety Function%%t:PSF%%을 찾는 데서 시작한다. 보통은 각 DBE%%t:DBE%%의 결말을 완화하는 PSF%%t:PSF%%의 성능을 제거하고 결말을 다시 평가하는 민감도 분석을 쓴다. 원문 각주는 이것이 이 절차에서 민감도 분석을 쓰는 한 예일 뿐이라고 적는다. 민감도 분석은 Mechanistic Source Term%%t:MST%%을 포함한 Licensing Basis Event%%t:LBE%% 빈도·결말 추정의 불확실도에 대응하는 방법의 일부로 PRA 개발과 심층방어%%t:DID%% 평가에서도 수행되며, 분석 요건은 ASME/ANS-RA-S-1.4에 있다. 이어서 RSF%%t:RSF%%에서 출발하는 하향식 논리 전개로, 원자로 설계가 각 RSF%%t:RSF%%를 만족하려면 반드시 충족해야 하는 기능 요건을 정의한다. RFDC%%t:RFDC%%는 RSF%%t:RSF%%를 만족하는 데 필요충분한 특정 원자로 설계 특성의 맥락에서 정의되는 기능 기준으로 볼 수 있고, 대응하는 SRDC%%t:SRDC%%는 그 뒤에 RFDC%%t:RFDC%%에서 개발된다.

§4.4.2는 RFDC%%t:RFDC%%마다 설계자가 RSF%%t:RSF%% 수행에 배정된 SR%%t:SR%% SSC%%t:SSC%%에 알맞은 SRDC%%t:SRDC%% 집합을 식별해야 한다고 적는다. 이 설계 요건은 성능 기반이고, RSF%%t:RSF%%에 묶여 있으며, LBE%%t:LBE%%에서 도출되어 SR%%t:SR%% SSC%%t:SSC%% 선정에 체계적으로 쓰인다. §4.4.5도 SR%%t:SR%% SSC%%t:SSC%%가 DBA%%t:DBA%%를 10 CFR 50.34 선량 한도 안으로 완화할 수 있어야 하고, 그 기능에 적절한 RFDC%%t:RFDC%%를 포함해야 한다고 적는다. 표 4-1에서 RFDC%%t:RFDC%%는 추가 special treatment%%t:SPECIAL_TREATMENT%% 요건 묶음에 들고, SR%%t:SR%% SSC%%t:SSC%%에만 적용 표시가 있다.

## 관련 문서
- [[Required_Safety_Function]]
- [[SSC_Design_Requirements]]
- [[Special_Treatment]]
- [[SSC_Safety_Classification]]
- [[PRA_Safety_Function]]
- [[NEI_18-04]]
