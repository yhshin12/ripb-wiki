---
type: natrium
aliases: []
sources:
- PSAR_ch01
status: checked
verified: 2026-09-16
term: null
tags:
- natrium
terms_pending: []
---

# Natrium의 controlling heat generation (Natrium Controlling Heat Generation)

> [!abstract] 요약
> Fundamental Safety Function%%t:FSF%%인 controlling heat generation은 노심에 제어봉을 넣어 수행하며, Defense Line%%t:DL%%에 걸쳐 능동, 피동, 고유 수단을 갖는다. 능동 수단인 power runback, 제어봉을 중력으로 넣는 피동 수단인 scram, scram을 뒷받침하는 driveline scram follow, 그리고 노심의 고유 반응도 되먹임이 이 기능을 수행한다.

## 원문 사실
- "The FSF of controlling heat generation is performed by inserting control rods into the reactor core and has active, passive, and inherent means of being achieved across the DLs." [PSAR_ch01 §1.3.2.2 p.63]
- "Control rods are positioned in the reactor core by the Control Rod Drive Mechanism System (CRD), which uses two diverse means of inserting two control rod banks of diverse geometrical design." [PSAR_ch01 §1.3.2.2 p.63]
- "Control rods are positioned in the core for reactivity control during power operation, are inserted into the core as required in response to abnormal events, and maintain the reactor shutdown." [PSAR_ch01 §1.3.2.2 p.63]
- "The power runback feature is an active means of achieving the FSF of controlling heat generation and prevents a scram for a variety of upset conditions during power operation." [PSAR_ch01 §1.3.2.2 p.63]
- "The power runback is performed by the CRD and Nuclear Island Rod Monitoring and Control System, which use control rod drive motors to insert control rods upon detection of abnormal conditions." [PSAR_ch01 §1.3.2.2 p.63]
- "The scram function results in passive gravity insertion of control rods into the reactor core to achieve the FSF of controlling heat generation." [PSAR_ch01 §1.3.2.2 p.63]
- "The scram is performed by the CRD and Reactor Protection System." [PSAR_ch01 §1.3.2.2 p.63]
- "The CRD driveline scram follow feature provides DID to the scram function." [PSAR_ch01 §1.3.2.2 p.63]
- "The CRD driveline scram follow is initiated by the Reactor Protection System coincident with a scram signal and drives the control rods into the core using the control rod drive motors." [PSAR_ch01 §1.3.2.2 p.63]
- "Inherent reactivity feedback of the reactor core also controls heat generation." [PSAR_ch01 §1.3.2.2 p.63]
- "As temperatures rise, the net negative feedback of the core reduces power." [PSAR_ch01 §1.3.2.2 p.63]
- "The natural feedbacks are self-regulating, inherent in the fuel design, and result in a safe and stable power level at which heat production and heat removal are in balance." [PSAR_ch01 §1.3.2.2 p.63]
- "The reactor core design features are described in Section 7.1.1, and the supporting analysis is provided in Chapter 3." [PSAR_ch01 §1.3.2.2 p.63]
- "The purpose of the CRD is to provide core reactivity control for the purpose of core power control, power shaping, and reactor shutdown." [PSAR_ch01 §1.1.4.1.9 p.24]
- "The CRD consists of thirteen CRDMs that control the position of nine primary CRAs and four secondary CRAs that are used to ensure reactor shutdown when required in response to an off-normal condition." [PSAR_ch01 §1.1.4.1.9 p.24]
- "The CRD scram function is gravity-driven and is fail safe on a loss of electrical power." [PSAR_ch01 §1.1.4.1.9 p.24]
- "The scram function is controlled by the RPS." [PSAR_ch01 §1.1.4.1.9 p.24]
- "The CRD gravity scram is backed up by CRDM motor drive-in of the CRAs for defense-in-depth." [PSAR_ch01 §1.1.4.1.9 p.24]

## 해설
Control Rod Drive Mechanism System은 기하학적 설계가 다른 두 제어봉 뱅크를 서로 다른 두 수단으로 삽입한다. 제어봉은 출력 운전 중 반응도 제어를 위해 노심 안에 위치하고, 비정상 사건에 대응해 필요할 때 노심에 삽입되며, 원자로 정지 상태를 유지한다. 계통 설명 절에 따르면 이 계통의 목적은 노심 출력 제어, 출력 분포 형성, 원자로 정지를 위한 반응도 제어이며, 열세 개의 구동 기구가 아홉 개의 primary 제어봉 집합체와 네 개의 secondary 제어봉 집합체의 위치를 조절하고, 이 집합체들이 off-normal 조건에서 필요할 때 원자로 정지를 보장한다.

power runback은 controlling heat generation을 달성하는 능동 수단으로, 출력 운전 중 여러 upset 조건에서 scram을 막는다. Control Rod Drive Mechanism System과 Nuclear Island Rod Monitoring and Control System이 이상 조건을 탐지하면 제어봉 구동 모터로 제어봉을 삽입해 수행한다. scram은 제어봉을 중력으로 노심에 피동 삽입하며, Control Rod Drive Mechanism System과 Reactor Protection System이 수행한다. 계통 설명 절은 scram 기능이 중력 구동이고 전력 상실 시 fail safe이며 Reactor Protection System이 제어한다고 적는다.

driveline scram follow 기능은 scram 기능에 대한 심층방어(Defense-in-Depth)%%t:DID%%를 제공한다. Reactor Protection System이 scram 신호와 동시에 이 기능을 시작하며, 제어봉 구동 모터가 제어봉을 노심으로 밀어 넣는다. 계통 설명 절도 중력 scram이 심층방어%%t:DID%%를 위해 구동 기구 모터에 의한 제어봉 집합체 삽입으로 뒷받침된다고 적는다.

노심의 고유 반응도 되먹임도 열생성을 제어한다. 온도가 오르면 노심의 순 음의 되먹임이 출력을 줄인다. 이 자연 되먹임은 자기 조절적이고 핵연료 설계에 내재하며, 열생산과 열제거가 균형을 이루는 안전하고 안정된 출력 준위에 이르게 한다. 노심 설계 특성과 뒷받침 해석은 다른 장에서 다룬다.

## 관련 문서
- [[Natrium_Fundamental_Safety_Functions]]
- [[Natrium_Control_Heat_Removal]]
- [[Natrium_DID_Approach]]
- [[SFR_DC_Reactivity_Control]]
- [[PSAR_ch01]]
