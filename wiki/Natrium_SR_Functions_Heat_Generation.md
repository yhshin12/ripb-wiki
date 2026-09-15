---
type: natrium
aliases: []
sources: [PSAR_ch05]
status: checked
verified: 2026-09-16
term:
tags: [natrium]
terms_pending: []
---
# Natrium controlling heat generation SR 기능 (SR Functions Supporting Control of Heat Generation)

> [!abstract] 요약
> controlling heat generation을 뒷받침하는 Safety-Related%%t:SR%% 기능은 DL3-RC1과 DL3-RC2 두 개이다. DL3-RC1은 latch 해제로 흡수체를 중력 삽입하는 scram으로 Anticipated Operational Occurrence%%t:AOO%%, Design Basis Event%%t:DBE%%, Beyond Design Basis Event%%t:BDBE%%에 걸쳐 credit되고, DL3-RC2는 전력 상실 시 원자로 scram으로 연관 Licensing Basis Event%%t:LBE%%가 없다.

## 원문 사실
| 표 | 제목 | 출처 |
|---|---|---|
| Table 5.2-1 | SR Functions Supporting Control of Heat Generation | [PSAR_ch05 Table 5.2-1 p.6] |

| PSF ID | SR Function Description | 출처 |
|---|---|---|
| DL3-RC1 | Scram - Gravity Driven Absorber Insertion by Latch Release | [PSAR_ch05 Table 5.2-1 p.6] |
| DL3-RC2 | Reactor Scram on Loss of Power | [PSAR_ch05 Table 5.2-1 p.7] |

| PSF ID | Associated LBE / Type | 출처 |
|---|---|---|
| DL3-RC1 | AOO: DHP-L1PP-BL, DHP-LOOP-BL, DHS-ISTL-BL, OTH-LMAC-BL, RPD-CW1ACS-BL, RPD-SS-BL | [PSAR_ch05 Table 5.2-1 p.6] |
| DL3-RC1 | DBE: DHP-L1PP-2, DHP-LOOP-1, DHS-ISTL-1, DHS-ISTL-2, DHS-RNBK-1, DHS-RNBK-3, IPI-IHEL-BL | [PSAR_ch05 Table 5.2-1 p.6] |
| DL3-RC1 | BDBE: DHP-L1PP-1, DHP-L1PP-4, DHP-LAPP-BL, DHP-LOOP-2, DHP-LOOP-4, DHS-ISTL-4, DHS-RNBK-2, IPI-IHEL-1, IPI-IHEL-2, OTH-LMAC-1, OTH-LMAC-2, OTH-LMAC-4, RPD-CW1ACS-1, RPD-CW1ACS-2, RPD-CW1ACS-4, RPD-SS-1, RPD-SS-2, RPD-SS-4 | [PSAR_ch05 Table 5.2-1 p.6] |
| DL3-RC2 | None / N/A | [PSAR_ch05 Table 5.2-1 p.7] |

| PSF ID | SR SSC(s) | SRDC | 출처 |
|---|---|---|---|
| DL3-RC1 | Control Rod Drive System (CRD) | Upon receipt of a scram signal from RPS, the Control Rod Drive System shall release the control rod assemblies in time to establish reasonable assurance radionuclide release results in calculated radiological dose under the 10 CFR 50.34 dose criteria at a safe shutdown condition. | [PSAR_ch05 Table 5.2-1 p.6] |
| DL3-RC1 | Reactor Core System (RCC) | Upon CRD rod release, control rod assemblies shall insert into the core to a depth and within a time limit to establish reasonable assurance radionuclide release results in calculated radiological dose under the 10 CFR 50.34 dose criteria at a safe shutdown condition. | [PSAR_ch05 Table 5.2-1 p.6] |
| DL3-RC1 | Reactor Enclosure System (RES) | Upon CRD rod release, RES shall provide structural support and position control preventing binding of CRDL and ensure control rod release is uninhibited to establish reasonable assurance radionuclide release results in calculated radiological dose under the 10 CFR 50.34 dose criteria at a safe shutdown condition. | [PSAR_ch05 Table 5.2-1 p.6] |
| DL3-RC1 | Reactor Protection System (RPS) | The RPS shall receive monitored signals and generate a scram signal upon exceeding a scram setpoint in time to establish reasonable assurance radionuclide release results in calculated radiological dose under the 10 CFR 50.34 dose criteria at a safe shutdown condition. | [PSAR_ch05 Table 5.2-1 p.6] |
| DL3-RC1 | Nuclear Instrumentation System (XIS) | XIS shall send monitored signals to the RPS in time to establish reasonable assurance radionuclide release results in calculated radiological dose under the 10 CFR 50.34 dose criteria at a safe shutdown condition. | [PSAR_ch05 Table 5.2-1 p.6] |
| DL3-RC1 | Reactor Instrumentation System (RIS) | RIS shall send monitored signals to the RPS in time to establish reasonable assurance radionuclide release results in calculated radiological dose under the 10 CFR 50.34 dose criteria at a safe shutdown condition. | [PSAR_ch05 Table 5.2-1 p.6] |
| DL3-RC2 | Control Rod Drive System (CRD) | Upon receipt of a scram signal from RPS, the Control Rod Drive System shall release the control rod assemblies in time to establish reasonable assurance radionuclide release results in calculated radiological dose under the 10 CFR 50.34 dose criteria at a safe shutdown condition. | [PSAR_ch05 Table 5.2-1 p.7] |
| DL3-RC2 | Reactor Protection System (RPS) | Upon power loss, the RPS shall fail safe by generating a scram signal in time to establish reasonable assurance radionuclide release results in calculated radiological dose under the 10 CFR 50.34 dose criteria at a safe shutdown condition. | [PSAR_ch05 Table 5.2-1 p.7] |

## 해설
두 PRA Safety Function%%t:PSF%%의 Safety-Related Design Criteria%%t:SRDC%%는 모두 해당 기능이 제때 수행되어, 방사성 핵종 방출에 따른 계산 선량이 안전 정지 조건에서 10 CFR 50.34 선량 기준 아래에 있다는 합리적 보증을 확립해야 한다는 문구로 끝난다.

DL3-RC1에 credit된 SR%%t:SR%% Structures, Systems, and Components%%t:SSC%%는 여섯 계통이다. Control Rod Drive System은 Reactor Protection System의 scram 신호를 받으면 제어봉 집합체를 풀어야 하고, Reactor Core System에서는 풀린 제어봉 집합체가 정해진 깊이와 시간 한계 안에 노심으로 들어가야 한다. Reactor Enclosure System은 구조 지지와 위치 제어를 제공해 `CRDL`의 binding을 막고 제어봉 해제가 방해받지 않게 해야 한다. Reactor Protection System은 감시 신호를 받아 scram setpoint를 넘으면 scram 신호를 만들어야 하며, Nuclear Instrumentation System과 Reactor Instrumentation System은 감시 신호를 제때 Reactor Protection System에 보내야 한다. DL3-RC1이 credit되는 사건은 AOO%%t:AOO%%, DBE%%t:DBE%%, BDBE%%t:BDBE%% 칸에 사건 식별자로 나열된다.

DL3-RC2의 SR%%t:SR%% SSC%%t:SSC%%는 Control Rod Drive System과 Reactor Protection System이다. Control Rod Drive System의 기준은 DL3-RC1과 같고, Reactor Protection System은 전력을 잃으면 scram 신호를 만들어 fail safe해야 한다. DL3-RC2의 `Associated LBE` 칸은 None / N/A이다.

## 관련 문서
- [[Natrium_SSC_Safety_Classification]]
- [[Natrium_Control_Heat_Generation]]
- [[Natrium_SR_Functions_Heat_Removal]]
- [[Natrium_NSRST_Functions]]
- [[Required_Safety_Function]]
- [[Required_Functional_Design_Criteria]]
- [[PSAR_ch05]]
