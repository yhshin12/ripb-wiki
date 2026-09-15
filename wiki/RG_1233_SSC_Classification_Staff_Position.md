---
type: regulation
aliases: []
sources:
- RG_1.233
- NEI_18-04
status: checked
verified: 2026-09-16
term: null
tags:
- rg-1233
terms_pending: []
---

# SSC 안전 분류에 대한 NRC 직원 입장 (Staff Position C.2 on SSC Safety Classification)

> [!abstract] 요약
> 직원 입장 C.2는 NEI 18-04가 비경수형원전(non-light-water reactor)%%t:NON_LWR%%의 Structures, Systems, and Components%%t:SSC%%를 Safety-Related%%t:SR%%, Non-Safety-Related with Special Treatment%%t:NSRST%%, special treatment%%t:SPECIAL_TREATMENT%%가 없는 비안전 등급으로 분류하는 수용 가능한 방법이라고 본다. 명확화는 두 가지로, 분류는 NEI 18-04의 통합 방법론 안에서만 유효하고 PRA에 명시적으로 모델링되지 않은 필수 지원 SSC%%t:SSC%%와 인적 행위도 상위 기능에 맞춰 분류하기를 기대하며, NEI 18-04의 safety-related는 10 CFR 50.2의 정의와 같지 않다.

## 원문 사실
- "The second major component of the NEI 18-04 methodology involves assessing the risk significance of SSCs and determining if special treatments beyond normal industrial practices are needed to ensure SSC performance of safety functions in the prevention and mitigation of LBEs." [RG_1.233 §C.2 p.15]
- "A designer would classify a safety function as a “required safety function” if that function is needed to keep the frequency or consequence of a DBE below the F-C target using realistic assumptions, or the consequences of a DBA below the reference values included in NRC regulations using conservative assumptions." [RG_1.233 §C.2 p.16]
- "SSCs selected by the reactor designer from the SSCs that are available to perform the required safety functions to mitigate the consequences of DBEs to within the LBE F-C target and to mitigate DBAs that only rely on the SR SSCs to meet the 10 CFR 50.34 dose limits using conservative assumptions" [RG_1.233 §C.2 p.16]
- "SSCs selected by the reactor designer and relied on to perform required safety functions to prevent the frequency of BDBE with consequences greater than the 10 CFR 50.34 dose limits from increasing into the DBE region and beyond the F-C target" [RG_1.233 §C.2 p.16]
- "non-SR SSCs relied on to perform risk significant functions; risk-significant SSCs are those that perform functions that prevent or mitigate any LBE from exceeding the F-C target or that make significant contributions to the cumulative risk metrics selected for evaluating the total risk from all analyzed LBEs" [RG_1.233 §C.2 p.16]
- "non-SR SSCs relied on to perform functions requiring special treatment for DID adequacy" [RG_1.233 §C.2 p.16]
- "all other SSCs (with no special treatment required)" [RG_1.233 §C.2 p.16]
- "None of the non-SR with no special treatment SSCs are classified as safety significant, but they may have requirements to ensure that failures following a design-basis internal or external event do not adversely impact SR or NSRST SSCs in their performance of safety-significant functions." [RG_1.233 §C.2 p.16]
- "Additionally, “nonsafety-related” is used in NEI 18-04 but is not a defined term in NRC regulations and has different meanings depending on the context in which it has been used in guidance documents and specific applications." [RG_1.233 §C.2 fn5 p.16]
- "For SSCs classified as SR, required functional design criteria (RFDC) and lower-level design criteria are defined to capture design-specific criteria that may supplement or may not be captured by the principal design criteria for a reactor design developed using the guidance in RG 1.232." [RG_1.233 §C.2 p.17]
- "NEI 18-04 states that NSRST SSCs are not directly associated with RFDC but are subject to special treatment as a result of risk significance or assessments of DID." [RG_1.233 §C.2 p.17]
- "“Barrier functions” can also include indirect functions, in which an SSC serves to protect one or more other SSCs that may be classified as barriers." [RG_1.233 §C.2 p.17]
- "The Commission’s SRM dated December 4, 2018 (Ref. 37), approved the methodology described in SECY-18-0096 for establishing functional containment performance criteria for non-LWRs." [RG_1.233 §C.2 p.17]
- "The magnitudes of the safety margins in performance are set considering the uncertainties in performance, the nature of the associated LBEs, and criteria for adequate DID." [RG_1.233 §C.2 p.17]
- "C.2 Staff Position: NEI 18-04 provides an acceptable method for assessing and classifying non-LWR SSCs as SR, NSRST, or non-SR with no special treatment." [RG_1.233 §C.2 p.18]
- "The classifications and related outcomes may not apply for alternative approaches that do not follow the other parts of the NEI 18-04 methodology." [RG_1.233 §C.2.a p.18]
- "The staff expects that SSCs that provide essential support (including required human actions) for SR or NSRST SSCs will be classified in a manner consistent with the higher-level function, even if the supporting SSC is not explicitly modeled in the PRA." [RG_1.233 §C.2.a p.18]
- "Use of the term “safety-related” in NEI 18-04 for non-LWRs is not the same as the definition in 10 CFR 50.2, and the SSCs included in the “safety-related” classification for non-LWRs may not be the same as those considered safety-related for LWRs." [RG_1.233 §C.2.b p.18]
- "As used in this RG and NEI 18-04, the term “nonsafety-related” means SSCs or an SSC that is not safety-related." [RG_1.233 §C.2.b p.18]
- "A PRA Safety Function that is required to be fulfilled to maintain the consequence of one or more DBEs or the frequency of one or more high-consequence BDBEs inside the F-C Target" [NEI_18-04 §6 p.90]
- "This may lead to design requirements to prevent any adverse impacts from failure of an SSC classified as NST or NSRST that could otherwise prevent an SR SSC from performing its RSFs." [NEI_18-04 §4 p.38]
- "Safety-significant SSCs are within the scope of the PRA-modeled SSCs and include SSCs that perform a risk-significant function and those that are needed to meet DID criteria." [NEI_18-04 §4.1 Task 3 p.43]

## 해설
이 절은 NEI 18-04 방법론의 둘째 요소가 SSC%%t:SSC%%의 risk significance를 평가하고 Licensing Basis Event%%t:LBE%%의 방지·완화에서 안전 기능 수행을 보장하는 데 일반 산업 관행을 넘는 special treatment%%t:SPECIAL_TREATMENT%%가 필요한지 결정하는 것이라고 요약한다. 이 지침은 required safety function을 realistic 가정으로 Design Basis Event%%t:DBE%%의 빈도나 결말을 Frequency-Consequence Target%%t:FC_TARGET%% 아래로 유지하거나, conservative 가정으로 Design Basis Accident%%t:DBA%% 결말을 규정의 기준값 아래로 유지하는 데 필요한 기능이라고 풀어 쓴다. NEI 18-04 용어집의 Required Safety Function%%t:RSF%% 정의는 DBE%%t:DBE%% 결말이나 high-consequence Beyond Design Basis Event%%t:BDBE%% 빈도를 F-C Target%%t:FC_TARGET%% 안에 유지하는 기능이라고 적어, 이 지침의 풀이 문장에는 BDBE%%t:BDBE%% 빈도가 빠지고 DBA%%t:DBA%% 결말이 들어가 있다. 다만 이 지침의 SR%%t:SR%% 범주 둘째 항목은 결말이 10 CFR 50.34 선량 한도를 넘는 BDBE%%t:BDBE%%의 빈도가 DBE%%t:DBE%% 영역과 F-C Target%%t:FC_TARGET%% 밖으로 늘어나지 않게 하는 기능을 포함한다.

범주 정의에서 SR%%t:SR%%은 DBE%%t:DBE%% 결말을 F-C Target%%t:FC_TARGET%% 안으로 완화하고 SR%%t:SR%% SSC%%t:SSC%%만으로 DBA%%t:DBA%%를 10 CFR 50.34 선량 한도 안으로 완화하는 SSC%%t:SSC%%, 그리고 위의 BDBE%%t:BDBE%% 빈도 방지 기능을 수행하는 SSC%%t:SSC%%이다. NSRST%%t:NSRST%%는 risk-significant 기능이나 심층방어(Defense-in-Depth)%%t:DID%% 적절성에 special treatment%%t:SPECIAL_TREATMENT%%가 필요한 기능을 수행하는 비안전 SSC%%t:SSC%%이며, 나머지는 special treatment%%t:SPECIAL_TREATMENT%%가 필요 없는 SSC%%t:SSC%%이다. 마지막 범주의 SSC%%t:SSC%%는 safety significant가 아니지만, 설계기준 내부·외부 사건 뒤의 고장이 SR%%t:SR%%이나 NSRST%%t:NSRST%% SSC%%t:SSC%%의 safety-significant 기능 수행에 악영향을 주지 않게 하는 요건을 가질 수 있다. NEI 18-04는 같은 요건의 보호 대상을 SR%%t:SR%% SSC%%t:SSC%%의 RSF%%t:RSF%% 수행으로 적는다.

SR%%t:SR%% SSC%%t:SSC%%에는 Required Functional Design Criteria%%t:RFDC%%와 하위 설계 기준을 정해 `RG 1.232`로 만든 principal design criteria%%t:PDC%%가 담지 못하거나 보완할 설계 고유 기준을 담고, NSRST%%t:NSRST%% SSC%%t:SSC%%는 RFDC%%t:RFDC%%와 직접 연결되지 않지만 risk significance나 심층방어%%t:DID%% 평가 결과로 special treatment%%t:SPECIAL_TREATMENT%%를 받는다. barrier function에는 다른 barrier%%t:BARRIER%% SSC%%t:SSC%%를 보호하는 간접 기능도 포함되며, Commission은 비경수형원전%%t:NON_LWR%%의 functional containment 성능 기준을 정하는 방법론을 승인했다. 성능의 safety margin%%t:SAFETY_MARGIN%% 크기는 성능 불확실도, 관련 LBE%%t:LBE%%의 성격, 심층방어%%t:DID%% 적절성 기준을 고려해 정한다.

직원 입장 C.2의 명확화 a는 분류와 그 결과가 NEI 18-04의 다른 부분을 따르지 않는 대안 접근에는 적용되지 않을 수 있다고 적고, SR%%t:SR%%이나 NSRST%%t:NSRST%% SSC%%t:SSC%%에 필수 지원을 제공하는 SSC%%t:SSC%%와 필요한 인적 행위를 PRA에 명시적으로 모델링되지 않았더라도 상위 기능과 일관되게 분류하기를 기대한다. NEI 18-04는 safety-significant SSC%%t:SSC%%가 PRA에 모델링된 SSC%%t:SSC%% 범위 안에 있다고 적으므로, 이 기대는 NEI 18-04 문장의 범위를 넘는다. 명확화 b는 NEI 18-04의 safety-related가 10 CFR 50.2 정의와 같지 않고 그 범주의 SSC%%t:SSC%%가 LWR의 safety-related SSC%%t:SSC%%와 다를 수 있으며, nonsafety-related는 NRC 규정에 정의되지 않은 말로 이 지침과 NEI 18-04에서는 safety-related가 아닌 SSC%%t:SSC%%를 뜻한다고 적는다.

## 관련 문서
- [[NRC_Endorsement_Of_NEI_18-04]]
- [[SSC_Safety_Classification]]
- [[Safety_Significant_SSC]]
- [[Risk_Significant_SSC]]
- [[Required_Safety_Function]]
- [[Required_Functional_Design_Criteria]]
- [[Special_Treatment]]
- [[Natrium_SSC_Safety_Classification]]
- [[Mechanistic_Source_Term_Conditions]]
- [[RG_1.233]]
