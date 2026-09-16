---
type: natrium
aliases: []
sources:
- PSAR_ch06
status: checked
verified: 2026-09-16
term: null
tags:
- natrium
terms_pending: []
---

# Natrium ASME 기기 하중과 응력 한계 (Natrium ASME Component Loads and Stress Limits)

> [!abstract] 요약
> `PSAR` §6.4.3은 `ASME` Code `Section III`, Division 5 기기·지지물·노심지지구조물의 구조 건전성을 정해진 하중과 하중조합에 대한 service stress limit 만족으로 보증한다고 적는다.
> Table 6.4-17은 적용 하중 14종을, Table 6.4-18은 Design부터 Test까지 아홉 조건의 하중조합과 service stress limit을 담는다.
> Operating Basis Earthquake%%t:OBE%%는 Safe Shutdown Earthquake%%t:SSE%%의 3분의 1로 설정되어 `10 CFR 50` Appendix S에 따른 명시적 응답·설계 해석이 필요 없고 피로해석에만 반영되며, 해석에 쓰는 프로그램에는 `ANSYS`, `TP RELAP5-3D`, `STAR-CCM+`가 있다.

## 원문 사실
- "This section addresses the design and analysis of ASME Code Section III, Division 5 mechanical components, supports, and core support structures." [PSAR_ch06 §6.4.3 p.37]
- "The plant transient events used in fatigue analyses are described in Section 6.4.3.1.1." [PSAR_ch06 §6.4.3 p.37]
- "Seismic analysis of mechanical systems and components is described in Section 6.4.3.2." [PSAR_ch06 §6.4.3 p.37]
- "The structural integrity of components, component supports, and core support structures is ensured by satisfying the ASME Section III, Division 5 service stress limits for specified loads and load combinations." [PSAR_ch06 §6.4.3 p.37]
- "Stress levels for load combinations, in the mechanical components and supports, are calculated using the methods and equations in the ASME Code, Section III." [PSAR_ch06 §6.4.3 p.37]
- "Load combinations and service stress limits are given in Section 6.4.3.3 for mechanical components and associated supports." [PSAR_ch06 §6.4.3 p.37]
- "This section addresses methods of analysis for components, supports, and core supports designated as ASME Code, Section III Class A and B." [PSAR_ch06 §6.4.3.1 p.38]
- "The computer programs used in the static and dynamic analysis of mechanical equipment include:" [PSAR_ch06 §6.4.3.1.2 p.44]
- "ANSYS: general purpose finite element analysis program used for static and dynamic analysis of mechanical components." [PSAR_ch06 §6.4.3.1.2 p.44]
- "TP RELAP5-3D: system thermal-hydraulic analysis code used to develop the thermal-hydraulic conditions for the ASME design transients." [PSAR_ch06 §6.4.3.1.2 p.44]
- "STAR-CCM+: general purpose computational fluid dynamics software used for detailed thermal hydraulic analyses." [PSAR_ch06 §6.4.3.1.2 p.44]
- "This section discusses the structural integrity of the components, component supports, and core support structures designed and constructed according to the rules of the ASME Code Section III." [PSAR_ch06 §6.4.3.3 p.45]
- "The loads considered for the design of Code Class A and B components, component supports, and core support structures are summarized in Table 6.4-17." [PSAR_ch06 §6.4.3.3.1 p.45]
- "Pressure loading is identified as either the design pressure, an operating pressure associated with a Service Level A, B, C, or D event, or a hydrostatic or pneumatic test pressure." [PSAR_ch06 §6.4.3.3.1 p.45]
- "Pressure may be internal or external to the component." [PSAR_ch06 §6.4.3.3.1 p.45]
- "For core support structures, design pressure differences and operating pressure differences associated with a Service Level A, B, C, or D event are considered." [PSAR_ch06 §6.4.3.3.1 p.45]
- "The plant transient events are defined in Section 6.4.3.1.1." [PSAR_ch06 §6.4.3.3.1 p.45]
- "The variations in pressure, temperature, and flow rate during the transients are developed and used as inputs to the applicable component’s stress analysis." [PSAR_ch06 §6.4.3.3.1 p.45]
- "The thermal transient loadings for the RV and other SSCs at the sodium-gas interface are evaluated for the specified thermal hydraulic conditions for each design transient." [PSAR_ch06 §6.4.3.3.1 p.46]
- "The thermal stresses resulting from thermal gradients are evaluated against the appropriate ASME Code criteria." [PSAR_ch06 §6.4.3.3.1 p.46]
- "Buoyancy loads are applicable to the components submerged in fluid." [PSAR_ch06 §6.4.3.3.1 p.46]
- "Buoyancy forces are calculated based on the weight of the fluid displaced." [PSAR_ch06 §6.4.3.3.1 p.46]
- "Seismic loadings are due to the vibratory ground motion associated with the SSE." [PSAR_ch06 §6.4.3.3.1 p.46]
- "The OBE is set at 1/3 of the SSE which eliminates the need for explicit response or design analysis per 10 CFR 50 Appendix S; however, the cyclic effects of OBE are included in the fatigue analysis as described in Section 6.4.3.2." [PSAR_ch06 §6.4.3.3.1 p.46]
- "Seismic loads can consist of both inertial loads and anchor motions, as applicable, where a component is supported at multiple locations." [PSAR_ch06 §6.4.3.3.1 p.46]
- "Code Class A or B components designed in accordance with HBB or HCB are subjected to static pressure testing loads in accordance with HBB-6000 or HCB-6000 as applicable." [PSAR_ch06 §6.4.3.3.1 p.46]
- "Component supports consider the weight of the pressure test medium where applicable." [PSAR_ch06 §6.4.3.3.1 p.46]
- "The Code Class A and B design and service load combinations and the applicable service stress limits are provided in Table 6.4-18." [PSAR_ch06 §6.4.3.3.1 p.46]
- "Static pressure tests are evaluated against the Test limits." [PSAR_ch06 §6.4.3.3.1 p.46]
- "The other test events described in Section 6.4.3.1.1 are evaluated against Level B Service Limits per HBB-3113.7 (Reference 6.4-23)." [PSAR_ch06 §6.4.3.3.1 p.46]
- "Where functionality of components and component supports cannot be ensured by satisfaction of the service stress limits alone, functional limits are established to support the required safety functions of components and component supports." [PSAR_ch06 §6.4.3.3.1 p.46]
- "The reactions loading due to discharge of a relief device is analyzed using the guidance of ASME Code Section III, Appendix O (Reference 6.4-22)." [PSAR_ch06 §6.4.3.3.2 p.46]
- "Reaction forces and moments are based on a static analysis with a dynamic load factor of 2.0 unless justification for a lower dynamic load factor is provided or dynamic analysis is performed." [PSAR_ch06 §6.4.3.3.2 p.46]
- "The reaction loads are included in the applicable load combination shown in Table 6.4-18." [PSAR_ch06 §6.4.3.3.2 p.46]
- "Applicable Loads for ASME Code Class A and B Components" [PSAR_ch06 Table 6.4-17 p.79]

| Load | Description | 출처 |
|---|---|---|
| Tdesign | Design Temperature | [PSAR_ch06 Table 6.4-17 p.79] |
| Pdesign | Design Pressure or Design Pressure Difference | [PSAR_ch06 Table 6.4-17 p.79] |
| Plant Transients | Transient temperatures, pressures, and flow rate as applicable | [PSAR_ch06 Table 6.4-17 p.79] |
| Safe Shutdown Earthquake | Seismic loads due to safe shutdown earthquake | [PSAR_ch06 Table 6.4-17 p.79] |
| Operating Basis Earthquake | Defined as 1/3 SSE. Considered for fatigue evaluation only | [PSAR_ch06 Table 6.4-17 p.79] |
| Dead Weight | Self-weight of component | [PSAR_ch06 Table 6.4-17 p.79] |
| Weight of Contents | Weight of sodium coolant or other process fluid | [PSAR_ch06 Table 6.4-17 p.79] |
| Buoyancy | Buoyancy forces | [PSAR_ch06 Table 6.4-17 p.79] |
| Preload | Loads due to bolt preload | [PSAR_ch06 Table 6.4-17 p.79] |
| Connected Piping | Mechanical and thermal loads due to attached piping | [PSAR_ch06 Table 6.4-17 p.79] |
| Mechanical | Mechanical reaction loads (including deadweight) induced by components or equipment other than piping. | [PSAR_ch06 Table 6.4-17 p.79] |
| Vibration | Vibratory loadings resulting from flow induced vibration or radiated vibration from equipment such as pumps. | [PSAR_ch06 Table 6.4-17 p.79] |
| Static Pressure Test | Hydrostatic or pneumatic test pressure in accordance with the requirements of HBB-6000 or HCB-6000 as applicable, and the weight of the test medium. | [PSAR_ch06 Table 6.4-17 p.79] |
| Support Motions | Loading applied to components supported at multiple locations resulting from differential thermal movement of their supports (thermal anchor motions). | [PSAR_ch06 Table 6.4-17 p.79] |

- "Load Combinations and Service Stress Limits for ASME Code Class A and B Components" [PSAR_ch06 Table 6.4-18 p.80]

| Condition | Load Combinations | Service Stress Limit | 출처 |
|---|---|---|---|
| Design | Pdesign + Tdesign(1) + DW + BOLT + WC + B + CP + MECH | Design | [PSAR_ch06 Table 6.4-18 p.80] |
| Service Level A Transients | PT + DW + BOLT + WC + B + CP + MECH + VIBR(2) + DISP | A | [PSAR_ch06 Table 6.4-18 p.80] |
| Service Level B Transients | PT + DW + BOLT + WC + B + CP + MECH + VIBR(2) + DISP | B | [PSAR_ch06 Table 6.4-18 p.80] |
| Service Level B OBE | PT(3) + DW + BOLT + WC + B + CP + MECH + VIBR(2) +/- OBE(4) + DISP | B | [PSAR_ch06 Table 6.4-18 p.80] |
| Service Level C Transients | PT + DW + BOLT + WC + B + CP + MECH + VIBR(2) + DISP | C | [PSAR_ch06 Table 6.4-18 p.80] |
| Service Level D Transients | PT + DW + BOLT + WC + B + CP + MECH | D | [PSAR_ch06 Table 6.4-18 p.80] |
| Service Level D SSE | PT(3) + DW + BOLT + WC + B + CP + MECH +/- SSE | D | [PSAR_ch06 Table 6.4-18 p.80] |
| Static Pressure Test | PTEST + DW + BOLT +CP + MECH | Test | [PSAR_ch06 Table 6.4-18 p.80] |
| Test (Other than static pressure tests) | PT + DW + BOLT + WC + B + CP + MECH | B | [PSAR_ch06 Table 6.4-18 p.80] |

- "Design Temperature is for determination of material properties only." [PSAR_ch06 Table 6.4-18 Note 1 p.80]
- "Vibration loads are only applicable for fatigue analysis." [PSAR_ch06 Table 6.4-18 Note 2 p.80]
- "The PT conditions for seismic events (SSE and OBE) are steady state 100% power." [PSAR_ch06 Table 6.4-18 Note 3 p.80]
- "OBE loads are only applicable for fatigue analysis when OBE is less than or equal to one-third of SSE." [PSAR_ch06 Table 6.4-18 Note 4 p.80]

## 해설
구조 건전성은 정해진 하중과 하중조합에 대해 `ASME` `Section III`, Division 5의 service stress limit을 만족하는 것으로 보증하고, 응력은 같은 코드의 방법과 식으로 계산한다. 적용 하중은 설계온도와 설계압력, 플랜트 과도의 온도·압력·유량, Safe Shutdown Earthquake%%t:SSE%%와 OBE%%t:OBE%%, 자중과 내용물 무게, 부력, 볼트 preload, 연결 배관, 배관 외 기기의 기계적 반력, 유동유발 진동과 펌프 같은 기기에서 전달되는 진동, 정압시험, 지지물의 열이동에 따른 support motion이다. 노심지지구조물에는 설계 압력차와 Service Level A–D의 운전 압력차를 고려한다.

OBE%%t:OBE%%는 Safe Shutdown Earthquake%%t:SSE%%의 3분의 1로 설정되므로 `10 CFR 50` Appendix S에 따른 명시적 응답·설계 해석이 필요 없고, 그 반복 효과만 피로해석에 넣는다. Table 6.4-18의 주석도 OBE%%t:OBE%% 하중이 Safe Shutdown Earthquake%%t:SSE%%의 3분의 1 이하일 때 피로해석에만 적용된다고 적고, 지진 사건의 과도 조건은 정상상태 100% power로 둔다고 적는다. 진동하중 역시 피로해석에만 적용하며, 설계온도는 재료 물성 결정에만 쓴다.

하중조합은 Design, Service Level A–D 과도, Service Level B OBE%%t:OBE%%, Service Level D Safe Shutdown Earthquake%%t:SSE%%, Static Pressure Test, 그 밖의 시험의 아홉 조건으로 나뉜다. service stress limit은 Design 조건이 Design, Service Level A 과도가 A, Service Level B 과도와 Service Level B OBE%%t:OBE%%가 B, Service Level C 과도가 C, Service Level D 과도와 Service Level D Safe Shutdown Earthquake%%t:SSE%%가 D, Static Pressure Test가 Test, 그 밖의 시험이 B이다. Table 6.4-18의 조합 기호와 Table 6.4-17의 하중 이름의 대응은 원문에 없다. 정압시험은 `HBB-6000` 또는 `HCB-6000`에 따르고 Test 한계로 평가하며, 그 밖의 시험 사건은 `HBB-3113.7`에 따라 Level B Service Limit으로 평가한다. Service stress limit만으로 기능을 보증할 수 없는 기기와 지지물에는 functional limit을 따로 설정한다.

압력 방출 장치의 방출 반력은 `ASME` Code `Section III` Appendix O의 지침으로 해석하고, 더 낮은 값의 정당화나 동적해석이 없으면 dynamic load factor 2.0의 정적해석으로 반력과 모멘트를 정한다. 정적·동적 해석에 쓰는 프로그램에는 유한요소 해석의 `ANSYS`, 설계 과도의 열수력 조건을 만드는 `TP RELAP5-3D`, 상세 열수력 해석의 `STAR-CCM+`가 있다.

## 관련 문서
- [[Natrium_ASME_Design_Transients]]
- [[Natrium_Piping_And_Industrial_Codes]]
- [[Natrium_Seismic_Analysis_Methods]]
- [[Natrium_PDC_Multiple_Barriers]]
- [[Natrium_PDC_Additional]]
- [[PSAR_ch06]]
