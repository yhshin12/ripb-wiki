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
# 비경수로 PRA의 범위와 적정성 (Non-LWR PRA Scope and Adequacy)

> [!abstract] 요약
> 비경수로의 PRA는 고유·피동 특성에 더 의존하는 설계를 반영해 내부 사건과 외부 재해의 전 범위를 다뤄야 하지만, 상세 수준은 설계의 크기·복잡도·잠재 위험에 맞출 수 있다. 빈도와 결말은 평균 점추정값과 불확실도 분포로 정량화하며, 원문은 ASME/ANS RA-S-1.4를 범위와 기술적 적정성을 정하는 수용 가능한 수단으로 든다.

## 원문 사실
- "Since the non-LWRs are expected to make greater use of inherent and passive capabilities to achieve safety, the PRA model used for applications described in this document should address the full spectrum of internal events and external hazards that pose challenges to the capabilities of the plant." [NEI_18-04 §3.3.2 p.31]
- "The size, complexity, and potential risk of a given design should influence the level of detail necessary to support this process." [NEI_18-04 §3.3.2 p.31]
- "Reactor designs with small radionuclide inventories, few SSCs, and inherently safe responses to upsets may employ simple, yet fit-for-purpose PRAs." [NEI_18-04 §3.3.2 p.31]
- "This quantification includes mean point estimates and an appropriate quantification of uncertainty in the form of uncertainty probability distributions." [NEI_18-04 §3.3.2 p.31]
- "These distributions should account for quantifiable sources of parameter and model uncertainty in the event frequencies, mechanistic source terms, and offsite radiological consequences." [NEI_18-04 §3.3.2 p.31]
- "The analysis performed in support of the RIPB applications covered in this guideline should include an appropriate set of sensitivity analyses to provide adequate assurance that major contributors to risk and performance uncertainties are identified and addressed." [NEI_18-04 §3.3.2 p.31]
- "Plants comprised of multiple reactor modules require consideration of event sequences that impact reactor modules independently as well as those that impact two or more reactor modules concurrently." [NEI_18-04 §3.3.2 p.31]
- "If applicable, the PRA should include event sequences involving two or more reactor modules as well as two or more sources of radioactive material." [NEI_18-04 §3.3 p.29]
- "For non-LWRs, the guidance in the ASME/ANS RA-S-1.4 provides an acceptable means to establish the scope and technical adequacy of the PRA." [NEI_18-04 §3.3.3 p.31]
- "As the design matures and more design information becomes available for different types of risk evaluations, the scope of the PRA can be broadened to address other plant conditions and progressively confirm the plant capability to meet safety objectives." [NEI_18-04 §3.3.3 p.31]
- "the PRA complexity necessary to support decision-making and an application should be much less complex than for operating LWR plants." [NEI_18-04 §3.3.3 p.31]
- "Designers should note that 10 CFR 50.47 and 10 CFR 52.79 require 10 CFR 52 applications to address frequency and consequences of events, from AOOs to postulated event sequences, (regardless of reactor size or design) for which some aspects of PRA may be needed." [NEI_18-04 §3.3.3 p.31]
- "Designers may propose to address all or parts of the process by assessing fission product barriers and showing that radioactive materials are retained within the facility with a high degree of confidence." [NEI_18-04 §3.3 p.29]
- "Such an approach would still benefit from some of the information provided by a PRA, including the identification of challenges to the barriers and identification and evaluation of dependencies among the barriers and layers of defense." [NEI_18-04 §3.3 p.29]

## 해설
원문은 비경수로가 안전을 달성하는 데 고유·피동 특성을 더 많이 쓸 것으로 보고, PRA가 내부 사건과 외부 재해의 전 범위를 다뤄야 한다고 적는다. 동시에 상세 수준은 설계의 크기, 복잡도, 잠재 위험에 따라 달라지며, 방사성 물질 재고가 작고 Structures, Systems, and Components%%t:SSC%% 수가 적으며 교란에 본질적으로 안전하게 반응하는 설계는 단순하지만 목적에 맞는 PRA를 써도 된다. 원문은 많은 비경수로에 필요한 PRA가 운전 중인 경수로보다 훨씬 덜 복잡할 것이라고 본다.

다만 원자로 크기와 무관하게 일부 PRA 요소가 필요할 수 있다. 원문은 10 CFR 50.47과 10 CFR 52.79가 Anticipated Operational Occurrence%%t:AOO%%부터 가정한 Event Sequence%%t:ES%%까지 빈도와 결말을 다루도록 요구한다고 지적한다.

정량화는 평균 점추정값과 불확실도 확률 분포의 형태로 이루어진다. 분포에는 사건 빈도, Mechanistic Source Term%%t:MST%%, 부지 밖 방사선학적 결말의 모수·모델 불확실도를 반영하고, 위험과 성능 불확실도의 주요 기여 요인을 찾도록 민감도 분석을 함께 수행한다.

다중 모듈 발전소는 모듈에 따로 영향을 주는 ES%%t:ES%%와 둘 이상의 모듈에 동시에 영향을 주는 ES%%t:ES%%를 모두 고려해야 하며, 둘 이상의 방사성 물질 원천이 관련된 ES%%t:ES%%도 포함한다. 적정성의 기준으로 원문은 ASME/ANS RA-S-1.4를 들고, 설계가 성숙함에 따라 PRA 범위를 넓혀 간다고 적는다. 설계자가 핵분열생성물 방벽 평가로 절차의 일부나 전부를 대신하려 해도, 방벽에 대한 부담과 방벽 사이 의존성을 찾는 데는 PRA 정보가 여전히 쓸모 있다고 원문은 본다.

## 관련 문서
- [[PRA_Role_In_LBE_Selection]]
- [[Event_Sequence_Family]]
- [[NEI_18-04]]
