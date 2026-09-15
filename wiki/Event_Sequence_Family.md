---
type: concept
aliases: []
sources:
- NEI_18-04
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
- "A representation of a scenario in terms of an Initiating Event defined for a set of initial plant conditions (characterized by a specified POS) followed by a sequence of system, safety function, and operator failures or successes, with sequence termination with a specified end state" [NEI_18-04 §6 p.90]
- "An event sequence may contain many unique variations of events (minimal cut sets) that are similar in terms of how they impact the performance of safety functions along the event sequence." [NEI_18-04 §6 p.90]
- "The set of conditions at the end of an Event Sequence that characterizes the impact of the sequence on the plant or the environment." [NEI_18-04 §6 p.90]
- "In most PRAs, end states typically include success states (i.e., those states with negligible impact) and Release Categories." [NEI_18-04 §6 p.90]
- "A standard arrangement of the plant during which the plant conditions are relatively constant, are modeled as constant, and are distinct from other configurations in ways that impact risk." [NEI_18-04 §6 p.90]
- "The term “event sequence” is used in lieu of the term “accident sequence” used in LWR PRA standards because the scope of the LBEs includes Anticipated Operational Occurrences and Initiating Events with no adverse impacts on public safety." [NEI_18-04 §1.3 p.10]
- "The collection of site, buildings, radionuclide sources, and SSCs seeking a single design certification or one or more operating licenses under the LMP framework." [NEI_18-04 §6 p.90]
- "The plant may include a single reactor unit or multiple reactor modules as well as non-reactor radionuclide sources." [NEI_18-04 §6 p.90]
- "A plant comprising multiple reactor modules that are designed and constructed using a modular design approach." [NEI_18-04 §6 p.90]
- "Modular design means a nuclear power plant that consists of two or more essentially identical nuclear reactors (modules)" [NEI_18-04 §6 p.90]
- "Multi-module plant adapted from ASME/ANS-Ra-S-1.4-2013, modular design from 10CFR52.1" [NEI_18-04 §6 p.90]
- "each reactor module is a separate nuclear reactor capable of being operated independent of the state of completion or operating condition of any other reactor module co-located on the same site, even though the nuclear power plant may have some shared or common systems." [NEI_18-04 §6 p.90]

## 해설
LBE%%t:LBE%%는 개별 ES%%t:ES%% 하나가 아니라, 발전소의 safety function에 비슷한 부담을 주는 ES%%t:ES%%를 묶은 Event Sequence Family%%t:EVENT_SEQ_FAMILY%%로 정의된다. 한 군에는 ES%%t:ES%%가 하나일 수도 여럿일 수도 있다. 원문은 이렇게 묶는 목적을 수많은 개별 사건을 다룰 수 있는 수로 줄여 LBE%%t:LBE%% 선정을 쉽게 하는 데 둔다.

원문이 드는 묶음 기준은 Initiating Event 시점의 POS%%t:POS%%, IE%%t:IE%%에 대한 발전소 응답과 그 과정에서 barrier%%t:BARRIER%%와 PRA Safety Function%%t:PSF%%을 지원하는 설비가 받는 부담, End State%%t:END_STATE%%, 영향받는 모듈과 방사성 물질 원천의 조합, 방출이 있을 때의 MST%%t:MST%%이다. 용어집 정의는 기준 항목이 일부 다르다. 용어집에는 hazard group, safety function별 발전소 응답, radionuclide transport barrier%%t:BARRIER%%별 응답이 더 있고, 모듈·원천 조합과 MST%%t:MST%%는 없다. 용어집은 방출이 있는 군이 release category 하나에만 대응한다고 명시한다.

방출이 있는 경우 같은 군 안의 ES%%t:ES%%는 MST%%t:MST%%와 부지 밖 결말이 같거나 비슷하다. 원문은 많은 LBE%%t:LBE%%가 방출을 수반하지 않으며, 방출을 막는 발전소 능력을 이해하는 것이 설계에 되돌려 줄 매우 중요한 통찰이라고 강조한다.

용어집은 ES%%t:ES%%를 특정 POS%%t:POS%%로 규정된 초기 발전소 조건에서 정의한 IE%%t:IE%% 뒤에 계통·safety function·운전원의 실패나 성공이 이어지고 지정된 End State%%t:END_STATE%%로 끝나는 시나리오의 표현으로 정의한다. 한 ES%%t:ES%%는 safety function 수행에 미치는 영향이 비슷한 여러 사건 변형, 즉 minimal cut set을 포함할 수 있다. End State%%t:END_STATE%%는 ES%%t:ES%% 끝에서 발전소나 환경에 대한 영향을 나타내는 조건의 집합이며, 대부분의 PRA에서 영향이 무시할 만한 성공 상태와 release category를 통상 포함한다. POS%%t:POS%%는 발전소 조건이 비교적 일정하고 일정하다고 모델링되며 위험에 영향을 주는 방식으로 다른 구성과 구별되는 발전소의 표준 배치이다. 원문 각주는 Anticipated Operational Occurrence%%t:AOO%%와 공중 안전에 악영향이 없는 IE%%t:IE%%까지 LBE%%t:LBE%% 범위에 들기 때문에 경수로 PRA 표준의 accident sequence 대신 event sequence라는 말을 쓴다고 밝힌다.

빈도는 plant-year당 사건 수로 표현하며, 이때 plant는 둘 이상의 원자로 모듈과 방사성 물질 원천을 포함할 수 있다. 즉 다중 모듈 발전소에서는 모듈 하나가 아니라 발전소 전체가 빈도의 기준이다. 용어집은 Plant%%t:PLANT%%를 Licensing Modernization Project%%t:LMP%% 체계에서 하나의 설계 인증이나 하나 이상의 운영허가를 받으려는 부지, 건물, 방사성 핵종 원천, Structures, Systems, and Components%%t:SSC%%의 집합으로 정의하며, 원자로 하나나 여러 원자로 모듈과 원자로가 아닌 방사성 핵종 원천을 포함할 수 있다고 적는다. Multi-Reactor Module Plant%%t:MULTI_MODULE_PLANT%%는 모듈식 설계로 설계·건설된 여러 원자로 모듈로 이루어진 발전소이다. 같은 항목의 모듈식 설계 정의는 본질적으로 동일한 원자로(모듈) 둘 이상으로 이루어진 원자력 발전소를 가리키며, 각 모듈은 일부 공용 계통이 있을 수 있더라도 같은 부지의 다른 모듈의 건설 완료나 운전 상태와 무관하게 운전할 수 있는 별개의 원자로이다. 출처 칸에 따르면 이 모듈식 설계 정의는 규정에서 가져왔다.

## 관련 문서
- [[Licensing_Basis_Event]]
- [[PRA_Role_In_LBE_Selection]]
- [[Non_LWR_PRA_Scope]]
- [[PRA_Safety_Function]]
- [[NEI_18-04]]
