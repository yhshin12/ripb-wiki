---
type: concept
aliases: []
sources: [NEI_18-04]
status: checked
verified: 2026-09-15
term:
tags: []
terms_pending: []
---
# SSC 안전 분류 (SSC Safety Classification)

> [!abstract] 요약
> Structures, Systems, and Components%%t:SSC%%는 PRA에 모델링된 기능을 기준으로 Safety-Related%%t:SR%%, Non-Safety-Related with Special Treatment%%t:NSRST%%, Non-Safety-Related with No Special Treatment%%t:NST%% 세 범주로 분류된다. 분류는 SSC%%t:SSC%% 자체가 아니라 Licensing Basis Event%%t:LBE%%에 나타나는 기능 단위로 이루어지며, SR%%t:SR%% 선정, risk significance 기준, 심층방어(Defense-in-Depth)%%t:DID%% 기준의 순서로 판정한다.

## 원문 사실
- "The purpose of this section is to define the approach to SSC safety classification and to identify potential technical concerns related to SSC safety classification and the derivation of requirements necessary to support SSC performance of safety functions in the prevention and mitigation of LBEs that are modeled in the PRA (i.e., PSFs)." [NEI_18-04 §4 p.38]
- "SSCs selected by the designer from the SSCs that are available to perform the RSFs to mitigate the consequences of DBEs to within the LBE F-C Target, and to mitigate DBAs that only rely on the SR SSCs to meet the dose limits of 10 CFR 50.34 using conservative assumptions" [NEI_18-04 §4 p.38]
- "SSCs selected by the designer and relied on to perform RSFs to prevent the frequency of BDBE with consequences greater than the 10 CFR 50.34 dose limits from increasing into the DBE region and beyond the F-C Target" [NEI_18-04 §4 p.38]
- "Non-safety-related SSCs relied on to perform risk-significant functions." [NEI_18-04 §4 p.38]
- "Non-safety-related SSCs relied on to perform functions requiring special treatment for DID adequacy" [NEI_18-04 §4 p.38]
- "All other SSCs (with no special treatment required)" [NEI_18-04 §4 p.38]
- "Non-safety-related SSCs that perform risk-significant functions or perform functions that are necessary for defense-in-depth adequacy" [NEI_18-04 §6 p.90]
- "All SSCs within a plant that are neither Safety-Related SSCs nor Non-Safety-Related SSCs with Special Treatment SSCs." [NEI_18-04 §6 p.90]
- "Safety-significant SSCs include all those SSCs classified as SR or NSRST. None of the NST SSCs are classified as safety-significant." [NEI_18-04 §4 p.38]
- "It is noted that there will be design requirements to protect all SR SSCs from any adverse impacts of any DBEHLs." [NEI_18-04 §4 p.38]
- "This may lead to design requirements to prevent any adverse impacts from failure of an SSC classified as NST or NSRST that could otherwise prevent an SR SSC from performing its RSFs." [NEI_18-04 §4 p.38]
- "The information needed to support the SSC safety classification is available when Task 10 of the LBE selection and evaluation process is completed in each phase of the design process." [NEI_18-04 §4.1 p.39]
- "This process is described as an SSC function classification process rather than an SSC classification process because only those SSC functions that prevent or mitigate events represented in the LBEs are of concern." [NEI_18-04 §4.1 p.42]
- "Although the SSCs are classified, the resulting performance and special treatment requirements are for the specific functions identified in the LBEs." [NEI_18-04 §4.1 p.42]
- "For SSCs that successfully mitigate the consequences of the IE, their capabilities and safety margins to respond to the IE are the focus of the safety classification process and resulting special treatment." [NEI_18-04 §4.1 Task 1 p.42]
- "For those SSCs that fail to respond along the LBE, their reliabilities, which serve to prevent the LBE by reducing its frequency, are the focus of the reliability targets derived from the classification and treatment process." [NEI_18-04 §4.1 Task 1 p.42]
- "The designer then selects one specific combination of available SSCs to perform each RSF that covers all the DBEs and high-consequence BDBEs. These specific SSCs are classified as SR in Task 5A and are the only ones included in the DBA analysis of the DBAs." [NEI_18-04 §4.1 Tasks 4A and 5A p.44]
- "If the SSC is classified as risk-significant and is not an SR SSC, it is classified as NSRST in Task 5B." [NEI_18-04 §4.1 Tasks 4B and 5B p.44]
- "Those that meet these criteria are classified as NSRST in Task 5B and those remaining as NST in Task 5C." [NEI_18-04 §4.1 Tasks 4C and 5C p.44]
- "For those SSCs classified as NST, the reliability and capability targets are part of the non-regulatory owner design requirements." [NEI_18-04 §4.1 Task 6 p.45]
- "The purpose of this task is to establish the specific design requirements for SSCs which include design criteria for SR classified SSCs, regulatory design and special treatment requirements for each of the safety-significant SSCs classified as SR or NSRST, and owner design requirements for NST-classified SSCs." [NEI_18-04 §4.1 Task 7 p.46]

| 항목 | 값 | 출처 |
|---|---|---|
| Task 1 | Identify SSC Functions in the Prevention and Mitigation of LBEs | [NEI_18-04 §4.1 p.42] |
| Task 2 | Identify and Evaluate SSC Capabilities and Programs to Support Defense-in-Depth | [NEI_18-04 §4.1 p.42] |
| Task 3 | Determine the Required and Safety-Significant Functions | [NEI_18-04 §4.1 p.42] |
| Tasks 4 and 5 | Evaluate and Classify SSC Functions | [NEI_18-04 §4.1 p.44] |
| Task 6 | SSC Reliability and Capability Targets | [NEI_18-04 §4.1 p.45] |
| Task 7 | Determine SSC Specific Design Criteria and Special Treatment Requirements | [NEI_18-04 §4.1 p.46] |

## 해설
원문은 SSC%%t:SSC%%를 세 범주로 나눈다. SR%%t:SR%%은 두 경우로, Design Basis Event%%t:DBE%%의 결말을 Frequency-Consequence Target%%t:FC_TARGET%% 안으로 완화하고 Design Basis Accident%%t:DBA%%에서 10 CFR 50.34 선량 한도를 만족시키도록 설계자가 고른 SSC%%t:SSC%%와, 결말이 그 한도를 넘는 Beyond Design Basis Event%%t:BDBE%%의 빈도가 DBE%%t:DBE%% 영역으로 올라오지 않게 하는 데 의지하는 SSC%%t:SSC%%이다. NSRST%%t:NSRST%%는 risk-significant 기능이나 심층방어%%t:DID%% 적절성에 special treatment%%t:SPECIAL_TREATMENT%%가 필요한 기능을 수행하는 비안전 등급 SSC%%t:SSC%%이고, 나머지는 모두 NST%%t:NST%%이다. §6 용어집의 NST%%t:NST%% 정의는 같은 내용이고, NSRST%%t:NSRST%% 정의는 심층방어%%t:DID%% 적절성에 필요한 기능을 special treatment%%t:SPECIAL_TREATMENT%% 조건 없이 적는다.

원문은 이 과정을 SSC%%t:SSC%% 분류가 아니라 SSC%%t:SSC%% 기능 분류라고 부른다. LBE%%t:LBE%%에 나타나는 예방하거나 완화하는 기능만 관심 대상이기 때문이다. 따라서 SSC%%t:SSC%% 단위로 등급을 매기더라도 성능 요건과 special treatment%%t:SPECIAL_TREATMENT%% 요건은 LBE%%t:LBE%%에서 식별된 특정 기능에 적용된다. 분류에 필요한 정보는 LBE%%t:LBE%% 선정 절차의 Task 10이 끝나면 갖춰진다.

기능은 두 성격으로 나뉜다. Initiating Event%%t:IE%%의 결말을 성공적으로 완화하는 SSC%%t:SSC%%에서는 대응 능력과 safety margin%%t:SAFETY_MARGIN%%이 분류와 special treatment%%t:SPECIAL_TREATMENT%%의 초점이 된다. 반대로 사건 전개 중에 고장 나는 SSC%%t:SSC%%에서는 LBE%%t:LBE%% 빈도를 낮춰 예방에 기여하는 신뢰도가 초점이 되며, 이것이 reliability target으로 이어진다.

판정 순서는 세 단계이다. 먼저 DBE%%t:DBE%%와 결말이 큰 BDBE%%t:BDBE%%마다 Required Safety Function%%t:RSF%%을 수행할 수 있는 SSC%%t:SSC%%를 찾고, 설계자가 그중 한 조합을 골라 SR%%t:SR%%로 분류한다. 이 SSC%%t:SSC%%만 DBA%%t:DBA%% 해석에 포함된다. 다음으로 나머지 비안전 등급 SSC%%t:SSC%% 가운데 risk-significant인 것을 NSRST%%t:NSRST%%로 분류한다. 마지막으로 남은 SSC%%t:SSC%% 중 심층방어%%t:DID%% 기준을 위해 special treatment%%t:SPECIAL_TREATMENT%%가 필요한 것을 NSRST%%t:NSRST%%로, 나머지를 NST%%t:NST%%로 분류한다. 판정 기준은 [[Risk_Significant_SSC]]와 [[Safety_Significant_SSC]]에 있다.

모든 SR%%t:SR%% SSC%%t:SSC%%는 Design Basis External Hazard Level%%t:DBEHL%%의 영향으로부터 보호되어야 하므로, NST%%t:NST%%나 NSRST%%t:NSRST%% SSC%%t:SSC%%의 고장이 SR%%t:SR%% SSC%%t:SSC%%의 RSF%%t:RSF%% 수행을 방해하지 않도록 하는 설계 요건이 생길 수 있다. Task 6과 Task 7은 분류 결과에서 요건을 도출한다. SR%%t:SR%%과 NSRST%%t:NSRST%% SSC%%t:SSC%%에는 설계 요건과 special treatment%%t:SPECIAL_TREATMENT%% 요건이 붙고, NST%%t:NST%% SSC%%t:SSC%%의 reliability target과 capability target은 규제 요건이 아닌 소유자 설계 요건에 속한다.

## 관련 문서
- [[Safety_Significant_SSC]]
- [[Risk_Significant_SSC]]
- [[Required_Safety_Function]]
- [[LBE_Selection_Process]]
- [[SSC_Design_Requirements]]
- [[Required_Functional_Design_Criteria]]
- [[Special_Treatment]]
- [[SSC_Reliability_And_Capability]]
- [[NEI_18-04]]
