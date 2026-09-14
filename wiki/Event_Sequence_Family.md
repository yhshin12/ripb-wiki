---
type: concept
aliases: []
sources: [NEI_18-04]
status: checked
verified: 2026-09-15
term: EVENT_SEQ_FAMILY
tags: []
terms_pending: []
---
# LBE와 Event Sequence Family (LBEs as Event Sequence Families)

> [!abstract] 요약
> Licensing Basis Event%%t:LBE%%는 PRA에 모델링된 개별 Event Sequence%%t:ES%%를 비슷한 특성으로 묶은 Event Sequence Family%%t:EVENT_SEQ_FAMILY%%로 정의된다. 묶는 기준은 Plant Operating State%%t:POS%%, Initiating Event%%t:IE%%, 발전소 응답, end state, 영향받는 모듈과 원천, Mechanistic Source Term%%t:MST%%이며, 빈도는 다중 모듈 발전소 전체의 plant-year당 사건 수로 표현한다.

## 원문 사실
- "A grouping of event sequences with a common or similar POS, Initiating Event, hazard group, challenges to the plant safety functions, response of the plant in the performance of each safety function, response of each radionuclide transport barrier, and end state." [NEI_18-04 §6 p.90]
- "An event sequence family may involve a single event sequence or several event sequences grouped together." [NEI_18-04 §6 p.90]
- "Each event sequence family involving a release is associated with one and only one release category." [NEI_18-04 §6 p.90]
- "Each event sequence family reflected in the LBE definitions is defined as a collection of event sequences that similarly challenge plant safety functions." [NEI_18-04 §3.3 p.29]
- "If the event sequence involves a radiological release, each sequence in the family will have the same or similar mechanistic source term and offsite radiological consequences." [NEI_18-04 §3.3 p.29]
- "Many of the LBEs do not involve a release and understanding the plant capabilities to prevent release is an extremely important insight to feed back to the design." [NEI_18-04 §3.3 p.29]
- "Selection of LBEs is facilitated by grouping many individual events into a manageable event sequence family." [NEI_18-04 §3.3 p.29]
- "Each LBE in this evaluation is defined as a family of event sequences modeled in the PRA that groups the individual modeled PRA event sequences according to the similarity of the following elements of the event sequence:" [NEI_18-04 §3.3.5 p.34]
- "Plant operating state at the time of the Initiating Event" [NEI_18-04 §3.3.5 p.34]
- "Plant response to the IE and any independent or consequential failures represented in the event sequence, including the nature of the challenge to the barriers and SSCs supporting each PSF" [NEI_18-04 §3.3.5 p.34]
- "Event sequence end state" [NEI_18-04 §3.3.5 p.34]
- "Combination of reactor modules and radionuclide sources affected by the sequence" [NEI_18-04 §3.3.5 p.34]
- "Mechanistic source term (MST) for sequences involving a radiological release" [NEI_18-04 §3.3.5 p.34]
- "The frequency basis of the event sequence quantification is events per (multi-reactor module/multi-source) plant-year." [NEI_18-04 §3.3.5 p.33]
- "The event sequence frequencies are expressed in terms of events/plant-year where a plant may be comprised of two or more reactor modules and sources of radioactive material." [NEI_18-04 §3.3.5 p.35]

## 해설
LBE%%t:LBE%%는 개별 ES%%t:ES%% 하나가 아니라, 발전소의 safety function에 비슷한 부담을 주는 ES%%t:ES%%를 묶은 Event Sequence Family%%t:EVENT_SEQ_FAMILY%%로 정의된다. 한 군에는 ES%%t:ES%%가 하나일 수도 여럿일 수도 있다. 원문은 이렇게 묶는 목적을 수많은 개별 사건을 다룰 수 있는 수로 줄여 LBE%%t:LBE%% 선정을 쉽게 하는 데 둔다.

원문이 드는 묶음 기준은 Initiating Event 시점의 POS%%t:POS%%, IE%%t:IE%%에 대한 발전소 응답과 그 과정에서 방벽과 PRA Safety Function%%t:PSF%%을 지원하는 설비가 받는 부담, end state, 영향받는 모듈과 방사성 물질 원천의 조합, 방출이 있을 때의 MST%%t:MST%%이다. 용어집 정의는 hazard group과 방벽별 응답까지 들어 조금 더 넓게 적으며, 방출이 있는 군은 release category 하나에만 대응한다고 명시한다.

방출이 있는 경우 같은 군 안의 ES%%t:ES%%는 MST%%t:MST%%와 부지 밖 결말이 같거나 비슷하다. 원문은 많은 LBE%%t:LBE%%가 방출을 수반하지 않으며, 방출을 막는 발전소 능력을 이해하는 것이 설계에 되돌려 줄 매우 중요한 통찰이라고 강조한다.

빈도는 plant-year당 사건 수로 표현하며, 이때 plant는 둘 이상의 원자로 모듈과 방사성 물질 원천을 포함할 수 있다. 즉 다중 모듈 발전소에서는 모듈 하나가 아니라 발전소 전체가 빈도의 기준이다.

## 관련 문서
- [[Licensing_Basis_Event]]
- [[PRA_Role_In_LBE_Selection]]
- [[Non_LWR_PRA_Scope]]
- [[PRA_Safety_Function]]
- [[NEI_18-04]]
