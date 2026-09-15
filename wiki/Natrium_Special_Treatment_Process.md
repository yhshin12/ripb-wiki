---
type: natrium
aliases: []
sources: [PSAR_ch06, PSAR_ch01, NEI_18-04]
status: checked
verified: 2026-09-16
term:
tags: [natrium]
terms_pending: []
---
# Natrium의 special treatment 요건 개발 (Natrium Special Treatment Requirements for Safety-Significant SSCs)

> [!abstract] 요약
> `PSAR` Chapter 6은 special treatment%%t:SPECIAL_TREATMENT%%를 safety-significant Structures, Systems, and Components%%t:SSC%%가 `design basis functions`를 수행한다는 보증을 일반 산업 관행 이상으로 높이는 요건으로 정의한다. Chapter 7에 식별된 special treatment%%t:SPECIAL_TREATMENT%%는 예비적이며 reliability와 capability target이 확정된 뒤 확정되고, 그 뒤 관련 발전소 프로그램에 변경이 필요한지 평가하고 갱신된 프로그램은 operating license 단계에서 제공된다.

## 원문 사실
- "Special treatments are those requirements that provide increased assurance beyond normal industrial practices that safety-significant structures, systems, or components (SSCs) perform their design basis functions." [PSAR_ch06 §6.3 p.13]
- "Special treatments are developed to provide reasonable confidence that safety-significant SSCs meet the reliability and capability targets." [PSAR_ch06 §6.3 p.13]
- "The method for confirming specific reliability and capability targets for SSCs at the operating license (OL) stage is described in Section 6.2." [PSAR_ch06 §6.3 p.13]
- "Special treatments applied to safety-significant SSCs are identified in Chapter 7." [PSAR_ch06 §6.3 p.13]
- "The special treatments identified in Chapter 7 are preliminary and are selected using a systematic process considering the PRA safety functions performed by the SSC and the safety-significance, risk significance, and equipment type of the SSC." [PSAR_ch06 §6.3 p.13]
- "After the reliability and capability targets are confirmed, special treatments are finalized and applied to safety-significant SSCs to provide reasonable confidence that the levels of reliability, availability, and capabilities of functions of the SSCs assessed in the probabilistic risk assessment, or determined to be necessary for defense-in-depth, are met." [PSAR_ch06 §6.3 p.13]
- "The probabilistic risk assessment is described in Section 3.1." [PSAR_ch06 §6.3 p.13]
- "Some of the special treatments applied to safety-significant SSCs are related to seismic classification and plant programs." [PSAR_ch06 §6.3 p.13]
- "Seismic classifications and seismic special treatments are defined in Section 6.4.1." [PSAR_ch06 §6.3 p.13]
- "Plant programs that are identified as special treatments are summarized in Section 8.0." [PSAR_ch06 §6.3 p.13]
- "Once special treatments are finalized, plant programs identified in Section 8.0 will be assessed to see if any changes are warranted." [PSAR_ch06 §6.3 p.13]
- "Updated programs will be provided at the OL stage." [PSAR_ch06 §6.3 p.13]
- "special treatment refers to those requirements that provide increased assurance beyond normal industrial practices that structures, systems, and components (SSCs) perform their design-basis functions." [NEI_18-04 §4.4.5 p.50]
- "The programmatic DID adequacy, including any additional special treatments identified, and the integrated DID adequacy evaluations will be provided at the operating license stage to establish the baseline DID." [PSAR_ch01 §1.3.3 p.64]
- "In Regulatory Guide 1.201, the following definition of special treatment is provided:" [NEI_18-04 §4.4.5 p.46]

## 해설
`PSAR` Chapter 6의 정의는 NEI 18-04가 인용하는 `Regulatory Guide 1.201`의 special treatment%%t:SPECIAL_TREATMENT%% 정의와 문장 구조가 같지만, 대상을 safety-significant SSC%%t:SSC%%로 한정하고 `structures, systems, and components`를 `structures, systems, or components`로 적는다. special treatment%%t:SPECIAL_TREATMENT%%는 safety-significant SSC%%t:SSC%%가 reliability와 capability target을 만족한다는 `reasonable confidence`를 주도록 개발되며, operating license%%t:OL%% 단계에서 target을 확인하는 방법은 `Section 6.2`에 있다([[Natrium_Reliability_Capability_Targets]]).

safety-significant SSC%%t:SSC%%에 적용되는 special treatment%%t:SPECIAL_TREATMENT%%는 `Chapter 7`에 식별된다. 이것은 예비적이며, SSC%%t:SSC%%가 수행하는 PRA Safety Function%%t:PSF%%과 SSC%%t:SSC%%의 safety significance, risk significance, 기기 유형을 고려하는 체계적 과정으로 선정된다. reliability와 capability target이 확정되면 special treatment%%t:SPECIAL_TREATMENT%%가 확정·적용되어, PRA에서 평가했거나 심층방어(Defense-in-Depth)%%t:DID%%에 필요하다고 판단된 SSC%%t:SSC%% 기능의 reliability, availability, capability 수준이 만족된다는 `reasonable confidence`를 준다. 이 문장은 `Section 6.2`의 보증 문장과 달리 availability를 포함한다.

일부 special treatment%%t:SPECIAL_TREATMENT%%는 seismic classification이나 발전소 프로그램과 관련된다. seismic classification과 지진 special treatment%%t:SPECIAL_TREATMENT%%는 `Section 6.4.1`에서 정의되고([[Natrium_Seismic_Classification]]), special treatment%%t:SPECIAL_TREATMENT%%로 식별된 발전소 프로그램은 `Section 8.0`에 요약된다. special treatment%%t:SPECIAL_TREATMENT%%가 확정되면 그 프로그램에 변경이 필요한지 평가하고, 갱신된 프로그램은 OL%%t:OL%% 단계에서 제공된다. `PSAR` Chapter 1은 추가 special treatment%%t:SPECIAL_TREATMENT%%를 포함한 Programmatic Defense-in-Depth%%t:PROGRAMMATIC_DID%% 적절성 평가와 통합 심층방어%%t:DID%% 적절성 평가를 OL%%t:OL%% 단계에서 제공한다고 적는다. Chapter 6은 special treatment%%t:SPECIAL_TREATMENT%% 확정을 target 확정 뒤로 두며, 그 확정을 OL%%t:OL%% 단계와 직접 연결하지는 않는다.

## 관련 문서
- [[Special_Treatment]]
- [[Natrium_Reliability_Capability_Targets]]
- [[Natrium_Seismic_Classification]]
- [[Natrium_DID_Approach]]
- [[Natrium_Programmatic_And_Integrated_DID]]
- [[PSAR_ch06]]
