---
type: natrium
aliases: []
sources:
- PSAR_ch01
- NEI_18-04
- SER_KU1_CP
status: checked
verified: 2026-09-16
term: null
tags:
- natrium
terms_pending: []
---

# Natrium의 심층방어 적용 (Natrium Defense-in-Depth Approach)

> [!abstract] 요약
> 이 보고서는 심층방어(Defense-in-Depth)%%t:DID%%를 인허가 기준과 적절한 보호의 합리적 보증 입증의 핵심 요소로 두고, plant capability, programmatic capability, 통합 적절성 평가의 세 요소가 baseline을 확립한다고 적는다. Plant capability 쪽 적절성은 Licensing Basis Event%%t:LBE%%마다 NEI 18-04 지침을 만족했다고 적지만, programmatic 쪽 적절성과 통합 평가는 operating license%%t:OL%% 단계에서 제공한다.

## 원문 사실
- "DID is a key element of the licensing basis and the demonstration of reasonable assurance of adequate protection of the health and safety of the public." [PSAR_ch01 §1.3.3 p.64]
- "The three DID elements, plant capability, programmatic capability, and integrated DID adequacy evaluation, establish the baseline DID." [PSAR_ch01 §1.3.3 p.64]
- "The guidelines for plant capability DID adequacy outlined in NEI 18-04, Section 5.6, including the plant capability attributes provided in NEI 18-04, Table 5-2, are satisfied for each LBE as described in Sections 4.2.1.1 to 4.2.1.4." [PSAR_ch01 §1.3.3 p.64]
- "The programmatic DID adequacy, including any additional special treatments identified, and the integrated DID adequacy evaluations will be provided at the operating license stage to establish the baseline DID." [PSAR_ch01 §1.3.3 p.64]
- "and determination of defense-in-depth (DID) adequacy were done via an integrated decision-making process" [PSAR_ch01 §1.3.1 p.60]
- "The CRD gravity scram is backed up by CRDM motor drive-in of the CRAs for defense-in-depth." [PSAR_ch01 §1.1.4.1.9 p.24]
- "The CRD driveline scram follow feature provides DID to the scram function." [PSAR_ch01 §1.3.2.2 p.63]
- "The systems implement the fundamental I&C system design principles of qualification, reliability, robustness, security, and defense-in-depth." [PSAR_ch01 §1.1.4.1.10 p.25]
- "Five DLs provide protection against unacceptable releases of radiation." [PSAR_ch01 §1.3.2 p.60]
- "This element provides a systematic and comprehensive process for examining the DID adequacy achieved by the combination of plant capability and programmatic elements." [NEI_18-04 §5.2 p.59]
- "This evaluation is performed by a risk-informed (RI) integrated decision-making process (IDP) to assess sufficiency of DID and to enable consideration of different alternatives for achieving commensurate safety levels at reduced burdens." [NEI_18-04 §5.2 p.59]
- "The outcome of the RI process also establishes a DID baseline for managing risk throughout the plant lifecycle." [NEI_18-04 §5.2 p.59]
- "The first complete pass through the integrated design process will require a baseline DID evaluation which completes the actions during execution of the IDP." [NEI_18-04 §5.9.5 p.86]
- "The baseline DID evaluation will be documented in sufficient detail so it can be efficiently updated in future design development iterations." [NEI_18-04 §5.9.5 p.86]
- "RG 1.253 section C.5 states that the NRC anticipates that the DID discussion at the CP stage may be limited to plant capabilities because programmatic capabilities may not have been established yet." [SER_KU1_CP §4.2.1.2 p.331]
- "As such, the staff determined that the limited detail provided in the PSAR on programmatic DID is reasonable." [SER_KU1_CP §4.2.1.2 p.331]
- "The staff will perform a more detailed evaluation of DID adequacy, including programmatic measures, at the OL" [SER_KU1_CP §4.2.2 p.331]
- "Prior to submittal of the operating licensing application, USO shall notify the NRC within 30 days after an integrated decision-making process panel is convened for internal approval of the safety analysis, risk assessment, or defense-in-depth adequacy of the design." [SER_KU1_CP §4.3.4 p.333]
- "The staff recommends that the CP include the following permit conditions:" [SER_KU1_CP §4.3.4 p.333]

## 해설
이 보고서는 심층방어%%t:DID%%가 인허가 기준과, 공중의 건강과 안전에 대한 적절한 보호의 합리적 보증을 입증하는 핵심 요소라고 적는다. 심층방어%%t:DID%%의 세 요소인 plant capability, programmatic capability, 통합 적절성 평가가 baseline을 확립한다. Plant Capability Defense-in-Depth%%t:PLANT_CAPABILITY_DID%% 적절성에 대해서는 NEI 18-04의 해당 절 지침과 표의 plant capability 속성을 LBE%%t:LBE%%마다 만족했다고 적는다. 반면 추가로 식별된 special treatment%%t:SPECIAL_TREATMENT%%를 포함한 Programmatic Defense-in-Depth%%t:PROGRAMMATIC_DID%% 적절성과 통합 적절성 평가는 OL%%t:OL%% 단계에서 제공해 baseline을 확립하겠다고 적는다. 인허가 기준 방법론 절은 심층방어%%t:DID%% 적절성 결정이 integrated decision-making process%%t:IDP%%로 수행되었다고 적는다.

NEI 18-04는 셋째 요소를 plant capability와 programmatic 요소의 결합이 이룬 심층방어%%t:DID%% 적절성을 체계적이고 포괄적으로 검토하는 과정으로 두며, 이 평가를 risk-informed IDP%%t:IDP%%로 수행하고 그 결과가 발전소 수명 동안 위험 관리를 위한 baseline을 확립한다고 적는다. NEI 18-04는 또 통합 설계 과정의 첫 완전한 반복에서 baseline 평가가 필요하고, 이후 설계 반복에서 효율적으로 갱신할 수 있을 만큼 상세히 문서화한다고 적는다. 이 보고서는 세 요소가 baseline을 확립한다고 적으면서 그 가운데 두 요소를 OL%%t:OL%% 단계로 넘긴다. `PSAR` Chapter 4는 통합 심층방어%%t:DID%% 평가 결과와 baseline 확립도 OL%%t:OL%% 단계에서 제공한다고 적는다([[Natrium_Programmatic_And_Integrated_DID]]).

설계 수준의 서술로는 중력 scram을 구동 기구 모터에 의한 제어봉 집합체 삽입이 뒷받침하고, driveline scram follow가 scram 기능에 심층방어%%t:DID%%를 제공하며, instrumentation and control 계통이 `qualification, reliability, robustness, security, and defense-in-depth`를 기본 설계 원칙으로 구현한다는 문장이 있다. 다섯 Defense Line%%t:DL%%이 용납할 수 없는 방사선 방출을 막는다는 문장도 있으나, DL%%t:DL%%과 NEI 18-04 Layers of Defense%%t:LAYERS_OF_DEFENSE%%의 대응은 [[Natrium_Defense_Lines]]에 있다.

**NRC staff 평가.** `RG 1.253`은 construction permit%%t:CP%% 단계의 심층방어%%t:DID%% 논의가 plant capability에 한정될 수 있다고 예상하며, NRC staff는 이에 근거해 `PSAR`의 programmatic 심층방어%%t:DID%% 서술이 제한적인 것을 합리적이라고 보았다. programmatic 조치를 포함한 상세 평가는 OL%%t:OL%% 단계에서 한다. 또 staff는 OL%%t:OL%% 신청 전에 IDP%%t:IDP%% panel이 설계의 안전해석, 위험평가, 심층방어%%t:DID%% 적절성의 내부 승인을 위해 소집되면 30일 안에 NRC에 통지하도록 하는 허가 조건을 권고한다.

## 관련 문서
- [[DID_Adequacy_Framework]]
- [[Plant_Capability_DID]]
- [[Programmatic_DID]]
- [[DID_Baseline]]
- [[Natrium_Licensing_Basis_Methodology]]
- [[Natrium_Fundamental_Safety_Functions]]
- [[Natrium_Control_Heat_Generation]]
- [[PSAR_ch01]]
- [[Natrium_SER_Integrated_Evaluation_Review]]
- [[Natrium_SER_RD_And_Permit_Conditions]]
