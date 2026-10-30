---
type: concept
aliases: []
sources: [NEI_18-04, SER_KU1_CP, RG_1.233]
status: disputed
verified: 2026-10-17
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
- "Although the SSCs are classified, the resulting performance and special treatment requirements are for the specific functions identified in the LBEs." [NEI_18-04 §4.1 p.39]
- "For SSCs that successfully mitigate the consequences of the IE, their capabilities and safety margins to respond to the IE are the focus of the safety classification process and resulting special treatment." [NEI_18-04 §4.1 Task 1 p.42]
- "For those SSCs that fail to respond along the LBE, their reliabilities, which serve to prevent the LBE by reducing its frequency, are the focus of the reliability targets derived from the classification and treatment process." [NEI_18-04 §4.1 Task 1 p.42]
- "The designer then selects one specific combination of available SSCs to perform each RSF that covers all the DBEs and high-consequence BDBEs. These specific SSCs are classified as SR in Task 5A and are the only ones included in the DBA analysis of the DBAs." [NEI_18-04 §4.1 Tasks 4A and 5A p.44]
- "If the SSC is classified as risk-significant and is not an SR SSC, it is classified as NSRST in Task 5B." [NEI_18-04 §4.1 Tasks 4B and 5B p.44]
- "Those that meet these criteria are classified as NSRST in Task 5B and those remaining as NST in Task 5C." [NEI_18-04 §4.1 Tasks 4C and 5C p.44]
- "For those SSCs classified as NST, the reliability and capability targets are part of the non-regulatory owner design requirements." [NEI_18-04 §4.1 Task 6 p.45]
- "The purpose of this task is to establish the specific design requirements for SSCs which include design criteria for SR classified SSCs, regulatory design and special treatment requirements for each of the safety-significant SSCs classified as SR or NSRST, and owner design requirements for NST-classified SSCs." [NEI_18-04 §4.1 Task 7 p.46]
- "However, based on USO’s interpretation of statement (a) that NSRST SSCs may continue to function but not perform RSFs, and statement (b), USO incorporated some passive NSRST SSCs performing at a degraded level in their DBA source term analyses." [SER_KU1_CP §5.1 p.339]
- "The staff determined that USO’s interpretation of the guidance and approach to ascribing some amount of degraded performance to passive NSRST SSCs in DBA source term analyses was reasonable, but acceptability is dependent on the design aspects of the SSCs and the level of degraded performance credited." [SER_KU1_CP §5.1 p.339]
- "It is appropriate that for the inherent capabilities of passive functions, degradation of the passive function is considered, as opposed to complete failure" [SER_KU1_CP §5.1 p.339]
- "Since the design is preliminary, a final determination on the acceptability of this approach to DBA source term analysis will be made at the OL stage when the methodology and complete scope of SSCs credited with degraded performance will be available for review." [SER_KU1_CP §5.1 p.339]
- "NEI 18-04 contains the following statements in sections 5.3 and 5.6.2:" [SER_KU1_CP §5.1 p.339]
- "DBAs are then constructed, starting with each DBE, and then assuming that only the SR SSCs perform their associated RSFs." [NEI_18-04 §5.3 Task 10 p.64]
- "The guidelines in Table 5-2 require that two or more independent plant design or operational features be provided to meet the plant capability requirements." [NEI_18-04 §5.6.2 p.69]
- "It is appropriate that for the inherent capabilities of passive functions, degradation of the passive function is considered, as opposed to complete failure (i.e., a physical non-existence of that function)." [NEI_18-04 §5.6.2 p.69]
- "DBAs are derived from the DBEs by prescriptively assuming that only Safety Related SSCs are available to mitigate postulated event sequence consequences to within the 10 CFR 50.34 dose limits." [NEI_18-04 Table 3-1 p.14]
- "Design-basis accidents (DBAs) are derived from DBEs by assuming that only safety-related (SR) SSCs are available to mitigate the events." [RG_1.233 §C.1 p.11]
- "A deterministic DBA is associated with each DBE that includes the required safety function challenges, but the DBA analysis is performed with the assumption that the required safety functions are performed by SR SSCs." [RG_1.233 §C.1 p.12]

| 항목 | 값 | 출처 |
|---|---|---|
| Task 1 | Identify SSC Functions in the Prevention and Mitigation of LBEs | [NEI_18-04 §4.1 p.42] |
| Task 2 | Identify and Evaluate SSC Capabilities and Programs to Support Defense-in-Depth | [NEI_18-04 §4.1 p.42] |
| Task 3 | Determine the Required and Safety-Significant Functions | [NEI_18-04 §4.1 p.42] |
| Tasks 4 and 5 | Evaluate and Classify SSC Functions | [NEI_18-04 §4.1 p.44] |
| Task 6 | SSC Reliability and Capability Targets | [NEI_18-04 §4.1 p.45] |
| Task 7 | Determine SSC Specific Design Criteria and Special Treatment Requirements | [NEI_18-04 §4.1 p.46] |

- "Figure 4-1. SSC Function Safety Classification Process" [NEI_18-04 Figure 4-1 p.40]

![[NEI_18-04_Fig_4-1.png]]

## 해설
원문은 SSC%%t:SSC%%를 세 범주로 나눈다. SR%%t:SR%%은 두 경우로, Design Basis Event%%t:DBE%%의 결말을 Frequency-Consequence Target%%t:FC_TARGET%% 안으로 완화하고 Design Basis Accident%%t:DBA%%에서 10 CFR 50.34 선량 한도를 만족시키도록 설계자가 고른 SSC%%t:SSC%%와, 결말이 그 한도를 넘는 Beyond Design Basis Event%%t:BDBE%%의 빈도가 DBE%%t:DBE%% 영역으로 올라오지 않게 하는 데 의지하는 SSC%%t:SSC%%이다. NSRST%%t:NSRST%%는 risk-significant 기능이나 심층방어%%t:DID%% 적절성에 special treatment%%t:SPECIAL_TREATMENT%%가 필요한 기능을 수행하는 비안전 등급 SSC%%t:SSC%%이고, 나머지는 모두 NST%%t:NST%%이다. §6 용어집의 NST%%t:NST%% 정의는 같은 내용이고, NSRST%%t:NSRST%% 정의는 심층방어%%t:DID%% 적절성에 필요한 기능을 special treatment%%t:SPECIAL_TREATMENT%% 조건 없이 적는다.

원문은 이 과정을 SSC%%t:SSC%% 분류가 아니라 SSC%%t:SSC%% 기능 분류라고 부른다. LBE%%t:LBE%%에 나타나는 예방하거나 완화하는 기능만 관심 대상이기 때문이다. 따라서 SSC%%t:SSC%% 단위로 등급을 매기더라도 성능 요건과 special treatment%%t:SPECIAL_TREATMENT%% 요건은 LBE%%t:LBE%%에서 식별된 특정 기능에 적용된다. 분류에 필요한 정보는 LBE%%t:LBE%% 선정 절차의 Task 10이 끝나면 갖춰진다.

Task 1은 두 경우의 초점을 구분한다. Initiating Event%%t:IE%%의 결말을 성공적으로 완화하는 SSC%%t:SSC%%에서는 대응 능력과 safety margin%%t:SAFETY_MARGIN%%이 분류와 special treatment%%t:SPECIAL_TREATMENT%%의 초점이 된다. 반대로 사건 전개 중에 고장 나는 SSC%%t:SSC%%에서는 LBE%%t:LBE%% 빈도를 낮춰 예방에 기여하는 신뢰도가 초점이 되며, 이것이 reliability target으로 이어진다.

판정 순서는 세 단계이다. 먼저 DBE%%t:DBE%%와 결말이 큰 BDBE%%t:BDBE%%마다 Required Safety Function%%t:RSF%%을 수행할 수 있는 SSC%%t:SSC%%를 찾고, 설계자가 그중 한 조합을 골라 SR%%t:SR%%로 분류한다. 이 SSC%%t:SSC%%만 DBA%%t:DBA%% 해석에 포함된다. 다음으로 나머지 비안전 등급 SSC%%t:SSC%% 가운데 risk-significant인 것을 NSRST%%t:NSRST%%로 분류한다. 마지막으로 남은 SSC%%t:SSC%% 중 심층방어%%t:DID%% 기준을 위해 special treatment%%t:SPECIAL_TREATMENT%%가 필요한 것을 NSRST%%t:NSRST%%로, 나머지를 NST%%t:NST%%로 분류한다. 판정 기준은 [[Risk_Significant_SSC]]와 [[Safety_Significant_SSC]]에 있다.

모든 SR%%t:SR%% SSC%%t:SSC%%는 Design Basis External Hazard Level%%t:DBEHL%%의 영향으로부터 보호되어야 하므로, NST%%t:NST%%나 NSRST%%t:NSRST%% SSC%%t:SSC%%의 고장이 SR%%t:SR%% SSC%%t:SSC%%의 RSF%%t:RSF%% 수행을 방해하지 않도록 하는 설계 요건이 생길 수 있다. Task 6과 Task 7은 분류 결과에서 요건을 도출한다. SR%%t:SR%%과 NSRST%%t:NSRST%% SSC%%t:SSC%%에는 설계 요건과 special treatment%%t:SPECIAL_TREATMENT%% 요건이 붙고, NST%%t:NST%% SSC%%t:SSC%%의 reliability target과 capability target은 규제 요건이 아닌 소유자 설계 요건에 속한다.

**Natrium 심사 사례.** 원문은 Task 5A에서 SR%%t:SR%%로 분류한 SSC%%t:SSC%%만 DBA%%t:DBA%% 해석에 포함된다고 적는다. Natrium 건설허가 심사에서 사업자는 일부 피동 NSRST%%t:NSRST%% SSC%%t:SSC%%를 저하된 성능으로 DBA%%t:DBA%% 선원항(source term)%%t:SOURCE_TERM%% 해석에 포함했고, NRC staff는 이 접근을 합리적이라고 보되 수용성은 SSC%%t:SSC%% 설계와 credit한 저하 수준에 달려 있다고 판단했다. 이 credit은 Task 5A 문장과 문언상 다르지만, `SER`은 이를 원문 §5.3·§5.6.2의 두 문장, 곧 DBA%%t:DBA%%에서 SR%%t:SR%% SSC%%t:SSC%%만 RSF%%t:RSF%%를 수행한다고 가정한다는 문장과 피동 기능은 완전 고장 대신 성능 저하를 고려한다는 문장에 대한 사업자 해석으로 본다.

**규정 대비 메모(C67, 상위 dispute).** NEI 18-04 §5.3 Task 10은 DBA%%t:DBA%%를 구성할 때 SR%%t:SR%% SSC%%t:SSC%%만 연계된 RSF%%t:RSF%%를 수행한다고 가정한다고 적고, [[RG_1.233]] C.1도 DBA%%t:DBA%% 해석은 RSF%%t:RSF%%를 SR%%t:SR%% SSC%%t:SSC%%가 수행한다는 가정으로 한다고 적어, 비SR%%t:SR%% SSC%%t:SSC%%의 비RSF%%t:RSF%% 기능을 배제하지 않는 것으로 읽힐 여지가 있다. `SER`은 이 읽기와 §5.6.2의 피동 기능 저하 문장에 근거한 사업자 해석, 곧 피동 NSRST%%t:NSRST%% SSC%%t:SSC%%의 저하 성능 credit을 합리적이라고 보되 수용성은 SSC%%t:SSC%% 설계와 credit한 저하 수준에 달려 있다고 판단하고, 최종 판단을 operating license%%t:OL%% 단계로 미루었다. 그러나 NEI 18-04 §4.1과 표 3-1, 그리고 [[RG_1.233]] C.1의 DBA%%t:DBA%% 도출 문장은 DBA%%t:DBA%% 완화에 동원되는 SSC%%t:SSC%%를 SR%%t:SR%% SSC%%t:SSC%%로만 한정하며, `SER`은 이 문장들을 언급하지 않는다. 또 §5.6.2의 저하 문장은 Table 5-2 심층방어%%t:DID%% 지침의 맥락에 있고 DBA%%t:DBA%% 해석을 지칭하지 않으므로, 권위 문서 사이의 해석 차이가 남는다.

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
- [[Natrium_SER_SSC_Classification_Review]]
