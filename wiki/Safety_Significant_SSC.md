---
type: concept
aliases: []
sources: [NEI_18-04]
status: checked
verified: 2026-09-15
term: SS_SSC
tags: []
terms_pending: []
---
# Safety-Significant SSC의 범위 (Safety-Significant SSCs)

> [!abstract] 요약
> Safety-Significant SSC%%t:SS_SSC%%는 Safety-Related%%t:SR%%와 Non-Safety-Related with Special Treatment%%t:NSRST%%로 분류된 Structures, Systems, and Components%%t:SSC%% 전체이다. Risk-Significant SSC%%t:RS_SSC%%는 모두 여기에 들고, SR%%t:SR%% SSC%%t:SSC%%는 risk significance 기준을 넘지 않아도 들며, 그 밖의 SSC%%t:SSC%%는 integrated decision-making process%%t:IDP%%가 심층방어(Defense-in-Depth)%%t:DID%%에 special treatment%%t:SPECIAL_TREATMENT%%가 필요하다고 판단할 때만 든다.

## 원문 사실
- "The meaning of safety-significant SSC in this process is the same as that used in NRC regulations." [NEI_18-04 §4.2.1 p.46]
- "When used to qualify an object, such as a system, structure, component, or accident sequence, this term identifies that object as having an impact on safety, whether determined through risk analysis or other means, that exceeds a predetermined significance criterion." [NEI_18-04 §4.2.1 p.47]
- "An SSC that performs a function whose performance is necessary to achieve adequate defense-in-depth or is classified as Risk-Significant (see Risk-Significant SSC)." [NEI_18-04 §6 p.90]
- "Safety-significant SSCs include all those SSCs classified as SR or NSRST. None of the NST SSCs are classified as safety-significant." [NEI_18-04 §4 p.38]
- "This guidance document makes use of the concept of SSC safety significance that is associated with 10 CFR 50.69 and also addresses the possibility that an SSC that is not SR nor risk-significant may be classified as safety-significant based on DID considerations." [NEI_18-04 §4.1 p.45]
- "The PRA model does not include all the SSCs in the plant but does include any SSC that performs a prevention or mitigation function for the sources of radioactive material in the scope of the PRA." [NEI_18-04 §4.1 Task 3 p.43]
- "Safety-significant SSCs are within the scope of the PRA-modeled SSCs and include SSCs that perform a risk-significant function and those that are needed to meet DID criteria." [NEI_18-04 §4.1 Task 3 p.43]
- "Safety-Related SSCs may or may not be risk-significant depending on whether they meet the SSC risk significance criteria." [NEI_18-04 §4.1 Task 3 p.43]
- "While SR SSCs perform RSFs that are needed to keep one or more DBEs or high-consequence BDBEs within the F-C Target, if there is sufficient redundancy or diversity provided by other SSCs that perform these RSFs, a given SR SSC is not necessarily risk-significant." [NEI_18-04 §4.1 Task 3 p.43]
- "However, all SR SSCs contribute to the layers of defense in meeting the DID adequacy criteria and are the primary means of fulfilling the RSFs, and hence all SR SSCs are classified as safety-significant whether or not they meet the risk significance criteria." [NEI_18-04 §4.1 Task 3 p.43]
- "Any SSCs that do not meet the risk-significance criteria should be classified as safety-significant only if the integrated decision-making process determines that some form of special treatment is necessary to establish the adequacy of DID." [NEI_18-04 §4.3 p.48]
- "This makes sense because the DID evaluation, which incorporates traditional engineering judgments made via an integrated decision-making process (IDP), will consider additional sources of uncertainty that are not fully resolved in the PRA." [NEI_18-04 §4.3 p.48]
- "If a non-risk-significant SSC is classified as safety-significant, it means that some type of special treatment should be applied to support the adequacy of DID." [NEI_18-04 §4.3 p.48]
- "All safety-significant SSCs are classified as SR or NSRST. All NST SSCs are not safety-significant." [NEI_18-04 §4.3 p.48]

- "Figure 4-2. Definition of Risk-Significant and Safety-Significant SSCs" [NEI_18-04 Figure 4-2 p.43]

![[NEI_18-04_Fig_4-2.png]]

- "Figure 4-3. LMP SSC Safety Categories and Safety Significant SSCs" [NEI_18-04 Figure 4-3 p.45]

![[NEI_18-04_Fig_4-3.png]]

## 해설
원문은 safety-significant의 뜻을 NRC 규제에서 쓰는 뜻과 같다고 밝히고, 위험 분석이든 다른 수단이든 미리 정한 기준을 넘는 안전 영향을 가진 대상을 가리키는 NRC 용어집 정의를 인용한다. 이 개념은 10 CFR 50.69의 SSC%%t:SSC%% safety significance 개념을 따르되, SR%%t:SR%%도 아니고 risk-significant도 아닌 SSC%%t:SSC%%가 심층방어%%t:DID%% 고려로 safety-significant가 될 가능성까지 다룬다. 이 절차에서 Safety-Significant SSC%%t:SS_SSC%%는 SR%%t:SR%%이나 NSRST%%t:NSRST%%로 분류된 SSC%%t:SSC%% 전체와 같고, Non-Safety-Related with No Special Treatment%%t:NST%% SSC%%t:SSC%%는 하나도 여기에 들지 않는다.

범위는 PRA 모델 SSC%%t:SSC%%의 부분집합이다. PRA 모델은 발전소의 모든 SSC%%t:SSC%%를 포함하지 않지만 PRA 범위 안의 방사성 물질 원천에 대한 예방하거나 완화하는 기능을 하는 SSC%%t:SSC%%는 모두 포함한다. Safety-Significant SSC%%t:SS_SSC%%는 그 안에서 risk-significant 기능을 수행하는 것과 심층방어%%t:DID%% 기준에 필요한 것으로 이루어진다.

SR%%t:SR%% SSC%%t:SSC%%는 risk significance 기준을 만족할 수도 있고 아닐 수도 있다. 같은 Required Safety Function%%t:RSF%%을 수행하는 다른 설비가 충분히 중복되거나 다양하면 개별 SR%%t:SR%% SSC%%t:SSC%%는 risk-significant가 아닐 수 있다. 그래도 모든 SR%%t:SR%% SSC%%t:SSC%%는 Layers of Defense%%t:LAYERS_OF_DEFENSE%%에 기여하고 RSF%%t:RSF%%를 수행하는 주된 수단이므로, 기준 충족 여부와 무관하게 safety-significant로 분류된다.

SR%%t:SR%% SSC%%t:SSC%%를 제외하면, risk significance 기준을 넘지 않는 SSC%%t:SSC%%는 IDP%%t:IDP%%가 심층방어%%t:DID%% 적절성을 위해 어떤 형태의 special treatment%%t:SPECIAL_TREATMENT%%가 필요하다고 판단할 때에만 safety-significant로 분류된다. 원문은 그 이유를, 공학적 판단을 담은 심층방어%%t:DID%% 평가가 PRA에서 다 풀리지 않은 불확실도까지 고려하기 때문이라고 설명한다. 이렇게 분류된 SSC%%t:SSC%%에는 special treatment%%t:SPECIAL_TREATMENT%%를 적용해야 한다.

## 관련 문서
- [[SSC_Safety_Classification]]
- [[Risk_Significant_SSC]]
- [[Special_Treatment]]
- [[SSC_Reliability_And_Capability]]
- [[Integrated_Decision_Making_Process]]
- [[Plant_Capability_DID]]
- [[NEI_18-04]]
