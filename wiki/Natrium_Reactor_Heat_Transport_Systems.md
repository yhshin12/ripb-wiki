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

# Natrium 원자로와 heat transport 계통 (Natrium Reactor and Heat Transport Systems)

> [!abstract] 요약
> `PSAR` 1장의 계통 개요는 Natrium의 Reactor Core System, `RES`, Reactor Air Cooling System, Primary Heat Transport System, Intermediate Heat Transport System, Intermediate Air Cooling System, 소듐 커버가스(cover gas)%%t:COVER_GAS%% 계통, Sodium Processing System, Control Rod Drive System을 요약한다. 이 요약은 원자로 용기와 guard vessel 구조, primary·중간 루프의 자연 순환 열제거, 중력 구동 scram을 포함한다.

## 원문 사실
- "The Reactor Core System (RCC) comprises various removable core assemblies (e.g., fuel, control, reflector, shield)." [PSAR_ch01 §1.1.4.1.1 p.21]
- "The RCC is designed to sustain a nuclear chain reaction for fission heat generation within the thermal-mechanical constraints of the components (e.g., fuel, cladding, structures)." [PSAR_ch01 §1.1.4.1.1 p.21]
- "Thermal power and reactivity are controlled by a combination of fuel management operations on a cycle-by-cycle basis and the insertion and withdrawal of control rods throughout a cycle." [PSAR_ch01 §1.1.4.1.1 p.21]
- "The Primary Sodium Pumps (PSPs) of the PHT supply sodium coolant flow to the core inlet plenum located at the bottom of the reactor core." [PSAR_ch01 §1.1.4.1.1 p.21]
- "Fuel assemblies are placed in the In-Vessel Storage (IVS) for decay before removing from the reactor vessel for longer-term storage." [PSAR_ch01 §1.1.4.1.1 p.21]
- "The RES provides all structural, functional, and interface support for the PHT, RCC, and Control Rod Drive System (CRD)." [PSAR_ch01 §1.1.4.1.2 p.21]
- "The RES provides one of the functional containment boundaries for the primary sodium coolant and sodium cover gas as described in Section 1.3.2.1." [PSAR_ch01 §1.1.4.1.2 p.21]
- "The RES has been designed with the following fundamental features: an integral reactor, reactor seismic isolation, top supported vessels, a passively cooled reactor head, single rotatable plug, in-vessel core assembly storage, and passive safety cooling via the Reactor Air Cooling System (RAC)." [PSAR_ch01 §1.1.4.1.2 p.21]
- "Additional features, such as no penetrations through the Reactor Vessel (RV), minimize the potential for primary system leakage or rupture." [PSAR_ch01 §1.1.4.1.2 p.21]
- "while the inert gas-filled annulus between the RV and Guard Vessel (GV) protects the system from sodium-air reactions in the highly unlikely event of a RV leak" [PSAR_ch01 §1.1.4.1.2 p.21]
- "The RAC primary objective is to provide passive decay heat removal to the environment through natural convection of air." [PSAR_ch01 §1.1.4.1.3 p.22]
- "The RAC is inherently reliable since it is not subject to the types of failure modes normally associated with active cooling systems (such as via pumped flow through heat exchangers)." [PSAR_ch01 §1.1.4.1.3 p.22]
- "It is continually in service with no operator actions nor SSC state change to initiate cooling operation." [PSAR_ch01 §1.1.4.1.3 p.22]
- "RAC heat removal performance is monitored during system operation including post-accident conditions." [PSAR_ch01 §1.1.4.1.3 p.22]
- "The RV is designed to thermally radiate heat across the argon gas space to the GV." [PSAR_ch01 §1.1.4.1.3 p.22]
- "This increases the capacity of RAC heat removal without increasing the surface area of the GV." [PSAR_ch01 §1.1.4.1.3 p.22]
- "The PHT, which is contained within the RES, consists of the hot pool, cold pool, warm pool, two IHXs, and two PSPs." [PSAR_ch01 §1.1.4.1.4 p.22]
- "The PHT safety function is to maintain primary sodium temperatures within design limits that preclude damage to the RV, the fuel, or reactor internal components." [PSAR_ch01 §1.1.4.1.4 p.22]
- "During a design basis event, the PHT safety function is to facilitate natural circulation of the primary sodium to transfer heat from the reactor core to the reactor vessel walls, where the heat is exchanged to the guard vessel and to the RAC." [PSAR_ch01 §1.1.4.1.4 p.22]
- "In addition, the void area between the sodium hot pool and the reactor head is inerted using argon gas provided by the Sodium Cover Gas (SCG)." [PSAR_ch01 §1.1.4.1.4 p.22]
- "The IHT working fluid is liquid sodium." [PSAR_ch01 §1.1.4.1.5 p.22]
- "during normal operations and is driven by natural circulation when power is not available." [PSAR_ch01 §1.1.4.1.5 p.23]
- "The boundary between the IHT and PHT occurs at the IHX nozzle to IHT pipe welds." [PSAR_ch01 §1.1.4.1.5 p.23]
- "The IHT transfers heat to the IAC through the Sodium-Air Heat Exchanger (AHX) for decay heat removal and for reactor startup and shutdown operations." [PSAR_ch01 §1.1.4.1.5 p.23]
- "In this role, the IHT provides part of the normal, preferred pathway for rejection of decay heat." [PSAR_ch01 §1.1.4.1.5 p.23]
- "The IAC is the preferred heat removal system for the reactor during upset events." [PSAR_ch01 §1.1.4.1.6 p.23]
- "The IAC consists of two AHXs, each contained in a chimney structure." [PSAR_ch01 §1.1.4.1.6 p.23]
- "The IAC transfers heat to the atmosphere in three system modes of operation." [PSAR_ch01 §1.1.4.1.6 p.23]
- "In active mode, there is forced circulation of the sodium in the intermediate loop provided by the ISP and forced air flow across the AHX provided by the IAC air blower." [PSAR_ch01 §1.1.4.1.6 p.23]
- "In blower mode, there is natural circulation of the sodium in the intermediate loop and forced air flow across the AHX provided by the IAC air blower." [PSAR_ch01 §1.1.4.1.6 p.23]
- "In passive mode, there is natural circulation of the sodium in the intermediate loop and natural convection flow of the air across the AHX." [PSAR_ch01 §1.1.4.1.6 p.23]
- "The SCG comprises the primary sodium cover gas supporting the PHT and the intermediate sodium cover gas supporting the IHT." [PSAR_ch01 §1.1.4.1.7 p.23]
- "The Sodium Processing System (SPS) monitors and removes contaminants including cesium and compounds including oxygen and hydrogen from the liquid sodium inventory." [PSAR_ch01 §1.1.4.1.8 p.24]
- "The purification equipment consists of cold traps, which remove oxides and hydrogen impurities, and a cesium trap, which removes cesium released to the coolant from fuel pin failures." [PSAR_ch01 §1.1.4.1.8 p.24]
- "The SPS-I contains the same equipment and function as the SPS-P with the exception that the SPS-I does not contain a cesium trap or associated radiological monitoring." [PSAR_ch01 §1.1.4.1.8 p.24]
- "The SPS-E contains the same equipment and function as the SPS-I." [PSAR_ch01 §1.1.4.1.8 p.24]
- "The purpose of the CRD is to provide core reactivity control for the purpose of core power control, power shaping, and reactor shutdown." [PSAR_ch01 §1.1.4.1.9 p.24]
- "The CRD consists of thirteen CRDMs that control the position of nine primary CRAs and four secondary CRAs that are used to ensure reactor shutdown when required in response to an off-normal condition." [PSAR_ch01 §1.1.4.1.9 p.24]
- "The CRD scram function is gravity-driven and is fail safe on a loss of electrical power." [PSAR_ch01 §1.1.4.1.9 p.24]
- "The scram function is controlled by the RPS." [PSAR_ch01 §1.1.4.1.9 p.24]
- "The CRDM motor controllers are supplied power from the NI Uninterruptible AC Power Supply System (NUP) which includes battery backup." [PSAR_ch01 §1.1.4.1.9 p.24]
- "The GV transfers a portion of the heat through convection directly into the RAC air flow path." [PSAR_ch01 §1.1.4.1.3 p.22]
- "To enhance total heat transferred, heat is thermally radiated to the collector cylinder which through convection transfers heat to the RAC air flow path." [PSAR_ch01 §1.1.4.1.3 p.22]
- "Hot sodium is driven through the intermediate loops by the Intermediate Sodium Pumps (ISPs) ... during normal operations and is driven by natural circulation when power is not available." [PSAR_ch01 §1.1.4.1.5 p.22-23]
- "The Primary Sodium Processing System (SPS-P) draws primary sodium from the RV using a submersible electromagnetic pump and delivers it to the sodium monitoring and purification equipment located below grade in the RAB." [PSAR_ch01 §1.1.4.1.8 p.24]

## 해설
Reactor Core System은 핵연료, 제어, 반사체, 차폐 같은 교체 가능한 노심 집합체로 이루어지고, 핵연료, 피복, 구조물 같은 구성품의 열·기계 제약 안에서 핵분열 열 생산을 위한 연쇄 반응을 유지하도록 설계된다. 열출력과 반응도는 주기별 핵연료 관리와 주기 중 제어봉 삽입·인출의 조합으로 제어된다. Primary Heat Transport System의 Primary Sodium Pump가 노심 하부의 입구 plenum으로 냉각재를 공급하며, 핵연료 집합체는 원자로 용기 밖 장기 저장으로 옮기기 전에 붕괴를 위해 In-Vessel Storage에 둔다.

`RES`는 Primary Heat Transport System, Reactor Core System, Control Rod Drive System의 구조·기능·interface 지지를 모두 제공하고, primary 소듐 냉각재와 커버가스%%t:COVER_GAS%%에 대한 functional containment 경계의 하나를 이룬다. 기본 특징으로는 integral reactor, reactor seismic isolation, top supported vessel, passively cooled reactor head, single rotatable plug, in-vessel core assembly storage, Reactor Air Cooling System에 의한 passive safety cooling이 열거된다. Reactor Vessel에 관통부가 없어 primary 계통 누설이나 파단 가능성이 줄고, Reactor Vessel과 Guard Vessel 사이의 불활성 기체 annulus가 가능성이 매우 낮은 Reactor Vessel 누설 시 소듐-공기 반응으로부터 계통을 보호한다.

Reactor Air Cooling System의 주목적은 공기 자연 대류로 환경에 피동 붕괴열 제거를 제공하는 것이다. 이 계통은 펌프 유동 열교환기 같은 능동 냉각 계통의 일반적 고장 모드를 겪지 않아 본질적으로 신뢰성이 높고, 냉각을 시작하는 데 운전원 조치나 Structures, Systems, and Components%%t:SSC%% 상태 변화가 필요 없이 계속 운전되며, 사고 후를 포함한 운전 중 열제거 성능이 감시된다. Reactor Vessel은 argon 기체 공간을 가로질러 Guard Vessel로 열을 복사하도록 설계되고, Guard Vessel은 열의 일부를 대류로 공기 유로에 직접 전달한다. 총 열전달을 늘리기 위해 열을 collector cylinder로도 복사하며 collector cylinder는 대류로 공기 유로에 열을 전달하는데, 이것이 Guard Vessel 표면적을 늘리지 않고 Reactor Air Cooling System 열제거 용량을 키운다.

Primary Heat Transport System은 `RES` 안에 있고 hot pool, cold pool, warm pool, `IHX` 두 기, Primary Sodium Pump 두 기로 이루어진다. 안전 기능은 Reactor Vessel, 핵연료, 원자로 내부 구성품의 손상을 막는 설계 한계 안에 primary 소듐 온도를 유지하는 것이고, Design Basis Event%%t:DBE%% 중에는 primary 소듐의 자연 순환으로 노심의 열을 Reactor Vessel 벽으로 옮겨 Guard Vessel과 Reactor Air Cooling System으로 전달하게 한다. hot pool과 원자로 헤드 사이 공간은 Sodium Cover Gas 계통이 공급하는 argon으로 불활성화된다.

Intermediate Heat Transport System의 작동 유체는 액체 소듐이며, 고온 소듐은 정상 운전 중 `ISP`로 중간 루프를 흐르고 전력이 없으면 자연 순환으로 흐른다. Primary Heat Transport System과의 경계는 `IHX` 노즐과 Intermediate Heat Transport System 배관의 용접부이다. 이 계통은 Sodium-Air Heat Exchanger를 거쳐 Intermediate Air Cooling System으로 열을 옮겨 붕괴열 제거와 원자로 기동·정지 운전에 쓰이며, 이 역할에서 붕괴열 방출의 정상적이고 선호되는 경로의 일부가 된다. Intermediate Air Cooling System은 upset event 동안 원자로의 선호 열제거 계통이고, 각각 chimney 구조물 안에 든 Sodium-Air Heat Exchanger 두 기로 이루어지며, active, blower, passive 세 운전 모드로 대기에 열을 전달한다. active mode에서는 `ISP`가 중간 루프 소듐을, blower가 공기를 강제로 흘리고, blower mode에서는 소듐이 자연 순환하고 공기는 blower로 흐르며, passive mode에서는 소듐이 자연 순환하고 공기는 자연 대류로 흐른다. 두 계통의 열제거 역할은 [[Natrium_Control_Heat_Removal]]에서 안전 개요 절과 함께 다룬다.

Sodium Cover Gas 계통은 Primary Heat Transport System을 지원하는 primary 소듐 커버가스%%t:COVER_GAS%%와 Intermediate Heat Transport System을 지원하는 중간 소듐 커버가스%%t:COVER_GAS%%로 이루어진다. Sodium Processing System은 액체 소듐에서 cesium과 산소·수소 화합물 같은 오염물을 감시·제거하며, `SPS-P`는 Reactor Vessel에서 primary 소듐을 끌어와 감시·정화 설비로 보내며, 그 정화 설비는 산화물과 수소 불순물을 제거하는 cold trap과 핵연료봉 파손으로 냉각재에 방출된 cesium을 제거하는 cesium trap이다. `SPS-I`는 `SPS-P`와 설비·기능이 같되 cesium trap과 그에 딸린 방사선 감시가 없고, `SPS-E`는 `SPS-I`와 같다.

Control Rod Drive System의 목적은 노심 출력 제어, 출력 분포 조정, 원자로 정지를 위한 노심 반응도 제어이다. `thirteen` 구동 기구가 off-normal 조건에서 필요할 때 원자로 정지를 보장하는 데 쓰이는 primary 제어봉 집합체 `nine`개와 secondary 집합체 `four`개의 위치를 제어한다. scram 기능은 중력 구동이고 전력 상실 시 fail safe이며 `RPS`가 제어한다. 구동 모터 제어기는 축전지 백업을 포함하는 `NI Uninterruptible AC Power Supply System`에서 전력을 받는다. NRC 직원의 구동 계통 검토는 [[Natrium_NRC_Review_Reactivity_Control]]에 있다.

## 관련 문서
- [[Natrium_Plant_Overview]]
- [[Natrium_Control_Heat_Removal]]
- [[Natrium_Control_Heat_Generation]]
- [[Natrium_Functional_Containment]]
- [[Natrium_NRC_Review_Reactivity_Control]]
- [[Natrium_IC_Systems]]
- [[PSAR_ch01]]
