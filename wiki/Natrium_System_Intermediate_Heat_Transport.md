---
type: natrium
aliases: []
sources:
- PSAR_ch07
status: checked
verified: 2026-09-16
term: null
tags:
- natrium
- psar-ch7
terms_pending: []
---

# Natrium Intermediate Heat Transport System (IHT)

> [!abstract] 요약
> Intermediate Heat Transport System(`IHT`)은 정상 출력 운전에서 primary coolant의 열을 `NSS`로, 기동·정지 중에는 `IAC`로 보내며, 펌프 유량을 잃으면 `IAC` `AHX`로 자연 순환한다. 대부분의 구성품은 Non-Safety-Related with Special Treatment%%t:NSRST%%·`SCN1`이고 `ISP` trip circuit breaker와 trip actuator만 Safety-Related%%t:SR%%·`SCS1`이며, SR%%t:SR%% 기능은 `DL3-HR3`와 `DL3-HR12`이다.

## 원문 사실
- "The Intermediate Heat Transport System (IHT) transports heat from the primary coolant to the Nuclear Island Salt System (NSS) for electrical power generation and energy storage during normal reactor power operation, and to the Intermediate Air Cooling System (IAC) for rejection to the atmosphere during reactor start-up and shutdown operation as the normal and preferred means of providing reactor cooling." [PSAR_ch07 §7.1.4.1 p.82]
- "In the event of a loss of pumped flow, the IHT is designed to provide natural circulation of intermediate coolant for reactor decay heat removal through the IAC Sodium-Air Heat Exchangers (AHXs)." [PSAR_ch07 §7.1.4.1 p.82]
- "Intermediate sodium is maintained at a higher pressure than primary sodium coolant, such that sodium flows into the PHT in the unlikely event of IHX tube leakage." [PSAR_ch07 §7.1.4.1 p.82]
- "The intermediate sodium is chemically compatible with the primary sodium coolant." [PSAR_ch07 §7.1.4.1 p.82]
- "The IHT piping includes features to detect and contain potential sodium leakage to limit sodium interactions with the surroundings." [PSAR_ch07 §7.1.4.1 p.82]
- "Leakage is directed away from safety-related (SR) structures, systems, and components in the Head Access Area and into catch pans by the leakage containment equipment." [PSAR_ch07 §7.1.4.1 p.82]
- "The IHT piping includes features to limit heat loss to the surroundings and protect against hazards associated with high surface temperatures." [PSAR_ch07 §7.1.4.1 p.82]
- "The compliance with regulatory criteria, identification of design criteria, and codes and standards that define the IHT design basis are described below." [PSAR_ch07 §7.1.4.2 p.83]
- "Principal Design Criteria (PDC) are identified in Section 5.3." [PSAR_ch07 §7.1.4.2 p.83]
- "Compliance with PDC that are applicable to the IHT is described below." [PSAR_ch07 §7.1.4.2 p.83]
- "Consistent with PDC 2, Design bases for protection against natural phenomena, safety-significant IHT components are designed to withstand the effects of natural phenomena without loss of capability to perform safety-significant functions." [PSAR_ch07 §7.1.4.2 p.83]
- "The methods applied for the evaluation of natural phenomena and the determination of associated design basis hazard levels are described in Section 6.1.1." [PSAR_ch07 §7.1.4.2 p.83]
- "Safety-significant IHT components are designed, based on the appropriate combination of the effects of normal and accident conditions with the effects of natural phenomena, to maintain capability to perform safety-significant functions." [PSAR_ch07 §7.1.4.2 p.83]
- "The SR IHT components required to support emergency shutdown of the ISPs are located below-grade within, and protected by, the reinforced concrete Nuclear Island Control Building substructure (described in Section 7.8.4)." [PSAR_ch07 §7.1.4.2 p.83]
- "The Nuclear Island Control Building provides protection from applicable natural phenomena including tornadoes and associated missiles, external flooding, and extreme climate conditions." [PSAR_ch07 §7.1.4.2 p.83]
- "Safety-significant IHT components are designed to withstand the effects of earthquakes in accordance with the methods described in Section 6.4.1." [PSAR_ch07 §7.1.4.2 p.83]
- "Consistent with PDC 3, Fire protection, the design of IHT piping includes containment features for potential sodium leakage, which allows timely detection of leakage in order to minimize possibility of fire due to sodium interactions with the surroundings." [PSAR_ch07 §7.1.4.2 p.83]
- "Design of the IHT provides for the selection of non-combustible and non-fire sustaining materials to the extent practical." [PSAR_ch07 §7.1.4.2 p.83]
- "Fire detection and firefighting features are described in Section 7.5.2." [PSAR_ch07 §7.1.4.2 p.83]
- "Consistent with PDC 4, Environmental and dynamic effects design bases, the IHT is designed to accommodate the effects of, and to be compatible with, the environmental conditions associated with normal operation, maintenance, testing, anticipated operational occurrences (AOOs), and postulated accidents." [PSAR_ch07 §7.1.4.2 p.83]
- "Selection of IHT materials of construction considers material compatibility with liquid sodium and its aerosols, vapors, and oxidation products." [PSAR_ch07 §7.1.4.2 p.83]
- "Material selection for IHT components in contact with salt from the NSS considers material compatibility with the molten salt environment." [PSAR_ch07 §7.1.4.2 p.83]
- "The IHT component design and material selection is made with consideration of service temperatures, service degradation of material properties, and applicable degradation mechanisms." [PSAR_ch07 §7.1.4.2 p.83]
- "Equipment qualification for environmental service conditions is provided by the IHT component quality, design, and qualification requirements in accordance with the Equipment Qualification Program (described in Chapter 8)." [PSAR_ch07 §7.1.4.2 p.83]
- "SR IHT components required to support emergency shutdown of the ISPs are located below-grade within the reinforced concrete Nuclear Island Control Building substructure for protection from the effects from missiles and discharging fluids." [PSAR_ch07 §7.1.4.2 p.83]
- "The IHT piping located within the Reactor Building substructure is protected from external hazards by the structure." [PSAR_ch07 §7.1.4.2 p.83]
- "Consistent with PDC 10, Reactor design, the design of the IHT supports the reactor core heat removal function that maintains sufficient margin to Specified Acceptable System Radionuclide Release Design Limits during normal operation and shutdown conditions." [PSAR_ch07 §7.1.4.2 p.84]
- "Safety-significant features support ISP trip to limit heat input to the primary coolant during AOOs." [PSAR_ch07 §7.1.4.2 p.84]
- "Consistent with PDC 34, Residual heat removal, the IHT design provides residual heat removal during normal operations and AOOs." [PSAR_ch07 §7.1.4.2 p.84]
- "Reactor core decay heat and other residual heat is transferred to the intermediate sodium through the IHX and to the atmosphere through the IAC AHX, as described in Section 7.2.2, at a sufficient rate that Specified Acceptable System Radionuclide Release Design Limits and the primary coolant boundary design conditions are not exceeded." [PSAR_ch07 §7.1.4.2 p.84]
- "Two intermediate loops are provided such that a single failure in one loop does not prevent the residual heat removal function." [PSAR_ch07 §7.1.4.2 p.84]
- "Consistent with PDC 35, Emergency core cooling, the IHT supports emergency core cooling by providing ISP emergency shutdown to limit heat input to the primary coolant system such that the Reactor Air Cooling System (RAC) heat removal capacity is not exceeded for postulated accidents." [PSAR_ch07 §7.1.4.2 p.84]
- "The ISP emergency shutdown design includes two series trip circuit breakers for protection against single failure of a breaker to trip." [PSAR_ch07 §7.1.4.2 p.84]
- "The design includes redundant shutdown signals from the protection system." [PSAR_ch07 §7.1.4.2 p.84]
- "Consistent with PDC 70, Intermediate coolant system, the design of the IHT provides sufficient margin such that the design conditions of the intermediate coolant boundary are not exceeded during conditions of normal operation, including AOOs." [PSAR_ch07 §7.1.4.2 p.84]
- "The intermediate coolant boundary operates at low pressure and is designed and constructed to satisfy applicable stress limits under anticipated operating conditions with sufficient margin to design conditions." [PSAR_ch07 §7.1.4.2 p.84]
- "Over-pressure protection of the intermediate coolant boundary is provided by the Sodium Cover Gas System, as described in Section 7.2.3, such that the integrity of the primary coolant boundary at the PHT IHX is maintained." [PSAR_ch07 §7.1.4.2 p.84]
- "Consistent with PDC 72, Sodium heating systems, the IHT maintains primary sodium above the freezing temperature of liquid sodium with adequate margin." [PSAR_ch07 §7.1.4.2 p.84]
- "When decay heat is unavailable or insufficient to maintain adequate sodium temperatures, the IHT SSCs can add heat to the primary sodium via kinetic energy of the ISPs." [PSAR_ch07 §7.1.4.2 p.84]
- "Consistent with PDC 73, Sodium leakage detection and reaction prevention and mitigation, the design of the IHT provides means to detect and identify sodium leakage, to limit and control the extent of sodium-air and sodium-concrete reactions, and to mitigate the effects of fires resulting from sodium-air reactions." [PSAR_ch07 §7.1.4.2 p.84]
- "Leakage containment and detection features are provided to contain and identify potential sodium leakage from IHT piping." [PSAR_ch07 §7.1.4.2 p.84]
- "Consistent with PDC 74, Sodium/water reaction prevention/mitigation, the IHT is designed and located to avoid contact between sodium and water." [PSAR_ch07 §7.1.4.2 p.84]
- "Water-containing systems are not located in areas of the Reactor Building and Reactor Auxiliary Building where potential sodium leakage from IHT components could result in sodium-water reactions." [PSAR_ch07 §7.1.4.2 p.84]
- "The IHT piping located in the yard area is protected to prevent potential sodium leakage exposure to water from atmospheric conditions including precipitation." [PSAR_ch07 §7.1.4.2 p.84]
- "Consistent with PDC 75, Quality of the intermediate coolant boundary, the intermediate coolant boundary is designed, fabricated, erected, and tested to quality standards commensurate with its safety-significant function in accordance with the applicable design and construction code requirements." [PSAR_ch07 §7.1.4.2 p.85]
- "Consistent with PDC 76, Fracture prevention of the intermediate coolant boundary, the intermediate coolant boundary is designed with sufficient margin to provide assurance that, when stressed under operating, maintenance, testing, and postulated accident conditions, the boundary behaves in a non-brittle manner and the probability of rapidly propagating fracture is minimized." [PSAR_ch07 §7.1.4.2 p.85]
- "Material selection, design, and fabrication of intermediate coolant boundary components considers the effects of elevated operating temperatures, fatigue, loss of ductility, and chemical compatibility to provide assurance that the material behaves in a non-brittle manner and provides resistance to rapidly propagating fracture." [PSAR_ch07 §7.1.4.2 p.85]
- "The intermediate coolant boundary operates at low pressure and is designed and constructed to satisfy applicable stress limits under anticipated operating conditions with sufficient margin to design conditions." [PSAR_ch07 §7.1.4.2 p.85]
- "Over-pressure protection of the intermediate coolant boundary is provided by the Sodium Cover Gas System as described in Section 7.2.3." [PSAR_ch07 §7.1.4.2 p.85]
- "Consistent with PDC 77, Inspection of the intermediate coolant boundary, the intermediate coolant boundary is designed to permit periodic inspection and functional testing of important areas and features to assess structural and leaktight integrity." [PSAR_ch07 §7.1.4.2 p.85]
- "The intermediate coolant boundary is within the scope of pre-service and in-service monitoring and non-destructive examination performed under the Reliability and Integrity Management Program described in Chapter 8." [PSAR_ch07 §7.1.4.2 p.85]
- "Consistent with PDC 78, Primary Coolant System Interfaces, the intermediate sodium is chemically compatible with the primary coolant." [PSAR_ch07 §7.1.4.2 p.85]
- "The intermediate loop interface with the primary coolant system consists of a single passive barrier within the IHX." [PSAR_ch07 §7.1.4.2 p.85]
- "The intermediate loop is maintained at a higher pressure than the primary coolant during normal operation, AOOs, shutdown, and accident conditions such that postulated leakage flows into the primary system to prevent loss of core cooling capability." [PSAR_ch07 §7.1.4.2 p.85]
- "The Reactor Vessel cover gas space accommodates increased primary coolant inventory due to IHX leakage and the Reactor Protection System initiates reactor scram and ISP trip on a high primary coolant level condition such that primary coolant system safety-significant functions are maintained and Specified Acceptable System Radionuclide Release Design Limits are not exceeded." [PSAR_ch07 §7.1.4.2 p.85]
- "PRA safety functions (PSFs) are determined through the plant-specific PRA described in Section 3.1." [PSAR_ch07 §7.1.4.2 p.85]
- "The safety-significant PSFs are identified as SR functions or non-safety-related with special treatment (NSRST) functions as defined in Section 5.2." [PSAR_ch07 §7.1.4.2 p.85]
- "The IHT supports the following safety-significant functions, which are designated as SR or NSRST to indicate the safety classification of IHT components relied upon to perform the function:" [PSAR_ch07 §7.1.4.2 p.85]
- "Safety classifications for IHT components are listed in Table 7.1.4-1." [PSAR_ch07 §7.1.4.2 p.86]
- "The Safety-Related Design Criteria corresponding to the SR functions applicable to the IHT are derived as described in Section 6.1.2 and identified in Section 5.2." [PSAR_ch07 §7.1.4.2 p.86]
- "The Safety-Related Design Criteria are incorporated into the design of the IHT as described in Section 7.1.4.3." [PSAR_ch07 §7.1.4.2 p.86]
- "NRC regulatory guidance documents are listed in Section 1.4.1." [PSAR_ch07 §7.1.4.2 p.86]
- "Guidance applicable to the IHT, along with a description of the use and conformance to the guidance, includes:" [PSAR_ch07 §7.1.4.2 p.86]
- "RG 1.22, Revision 0, Periodic Testing of Protection System Actuation Functions (Safety Guide 22)" [PSAR_ch07 §7.1.4.2 p.86]
- "Full Conformance. The IHT ISP circuit breakers conform to references of “actuated device” and “actuated equipment.”" [PSAR_ch07 §7.1.4.2 p.86]
- "RG 1.36, Revision 1, Nonmetallic Thermal Insulation for Austenitic Stainless Steel Full Conformance." [PSAR_ch07 §7.1.4.2 p.86]
- "Methods and procedures are used for selection of non-metallic insulation to prevent stress-corrosion cracking of stainless steel by minimizing leachable chlorides and fluorides to the lowest practicable levels." [PSAR_ch07 §7.1.4.2 p.86]
- "Seismic classifications for IHT components are determined in accordance with the methods described in Section 6.4.1." [PSAR_ch07 §7.1.4.2 p.87]
- "Seismic special treatment is applied based on the seismic classification." [PSAR_ch07 §7.1.4.2 p.87]
- "The seismic classification of IHT components is listed in Table 7.1.4-1." [PSAR_ch07 §7.1.4.2 p.87]
- "Seismic design, analysis, and qualification is performed as described in Section 6.4." [PSAR_ch07 §7.1.4.2 p.87]
- "The IHT components are qualified to withstand seismic loads associated with the safe shutdown earthquake (described in Section 2.6.2) without loss of the capability to perform safety-significant functions." [PSAR_ch07 §7.1.4.2 p.87]
- "Codes and standards are applied for the design, fabrication, testing, inspection, and maintenance of IHT components as special treatments, as described in Section 6.3." [PSAR_ch07 §7.1.4.2 p.87]
- "The safety-significant IHT piping and components are designed in conformance with the industry consensus codes and standards indicated in Table 7.1.4-2." [PSAR_ch07 §7.1.4.2 p.87]

| Function ID | Function Description | IHT Functional Support | 출처 |
|---|---|---|---|
| DL2-HR2 | ISP Trip on Low IHT level (NSRST) | The ISP is automatically tripped to limit loss of intermediate sodium due to leakage. | [PSAR_ch07 §7.1.4.2 p.86] |
| DL4-HR7 | Manual ISP Trip (NSRST) | Operator manual trip of ISP as backup to SR automatic trip to limit heat addition to primary coolant. | [PSAR_ch07 §7.1.4.2 p.86] |
| DL3-HR3 | ISP Trip on High High Primary Sodium Temperature (SR) | The ISP is automatically tripped to limit heat addition to the primary coolant. | [PSAR_ch07 §7.1.4.2 p.86] |
| DL3-HR12 | ISP Trip on High High Primary Sodium Level (SR) | The ISP is automatically tripped to limit intermediate sodium flow to the primary system through IHX tube leakage. | [PSAR_ch07 §7.1.4.2 p.86] |
| DL4-HR1 | IAC Passive Mode Operation (NSRST) | The IHT provides natural circulation of intermediate sodium coolant to transport heat from the PHT IHX to the IAC AHX for licensing basis events when the ISP and RAC are unavailable. | [PSAR_ch07 §7.1.4.2 p.86] |
| DL4-HR3 | ISP Trip Automatic Backup (NSRST) | The trip of the ISP as backup to the SR automatic trip to limit heat addition to primary coolant. | [PSAR_ch07 §7.1.4.2 p.86] |
| DL4-DID1 | Intermediate Leak Guard Piping (NSRST) | The IHT provides sodium leakage detection and containment for IHT piping located within the Reactor Building. | [PSAR_ch07 §7.1.4.2 p.86] |

- "The IHT supports electrical power generation and energy storage by transporting heat from the PHT IHXs to the NSS via the SHXs under normal operating conditions." [PSAR_ch07 §7.1.4.3 p.87]
- "The IHT provides low power and shutdown reactor core heat removal by circulating intermediate sodium coolant through the IAC AHXs, where heat is rejected to the atmosphere." [PSAR_ch07 §7.1.4.3 p.87]
- "The IHT provides for emergency shutdown of the ISPs to limit heat input to the PHT during limiting LBEs requiring the RAC operation, described in Section 7.2.1, and to limit intermediate sodium flow into the PHT in the unlikely event of IHX tube leakage." [PSAR_ch07 §7.1.4.3 p.87]
- "The IHT supports heat rejection via the IAC by circulating intermediate sodium through the inline AHX for reactor heat removal in low power operating modes and reactor shutdown conditions." [PSAR_ch07 §7.1.4.3 p.87]
- "In IAC Active Mode (described in Section 7.2.2), intermediate sodium is circulated by the ISPs." [PSAR_ch07 §7.1.4.3 p.87]
- "When the ISPs are not available to provide forced circulation, the IHT is designed to support IAC heat rejection in Blower Mode and Passive Mode through natural circulation of intermediate sodium." [PSAR_ch07 §7.1.4.3 p.87]
- "The elevation difference between the installation location of the IHX, where sodium is heated reducing its density, and the elevated AHX, where sodium is cooled increasing its density, provides the potential energy to drive natural circulation flow." [PSAR_ch07 §7.1.4.3 p.87]
- "The elevation difference between the IHX and the AHX is designed to provide the necessary natural circulation flow rate to meet specified heat removal requirements based on the limiting case without reliance on RAC heat rejection with flow in two intermediate loops." [PSAR_ch07 §7.1.4.3 p.87]
- "No manual operator actions or automatic actuations are required for the IHT to perform its passive heat removal safety-significant function." [PSAR_ch07 §7.1.4.3 p.87]
- "The IHT is configured to maintain intermediate sodium at a higher pressure than primary sodium whenever the intermediate loop contains liquid sodium." [PSAR_ch07 §7.1.4.3 p.87]
- "This design feature, combined with limitations on the primary and intermediate cover gas pressures, provides assurance that sodium flows into the primary system in the event of IHX tube leakage and prevents loss of primary coolant level within the Reactor Vessel that could affect core cooling or result in the release of primary coolant radionuclides to the IHT." [PSAR_ch07 §7.1.4.3 p.87]
- "For this condition, upon reaching the low level setpoint in the expansion tank or the high level setpoint in the reactor vessel, the associated ISP is automatically stopped to limit intermediate sodium flow into the reactor vessel." [PSAR_ch07 §7.1.4.3 p.87]
- "Introduction of cover gas at the IHT piping high points in the intermediate loop flow path prevents a siphon from forming and further limits the volume of intermediate sodium that could drain to the primary system." [PSAR_ch07 §7.1.4.3 p.87]
- "The intermediate loop siphon-break feature is designed to limit the volume of intermediate sodium introduced into the primary system during postulated IHX leak events to prevent reactor vessel overfill." [PSAR_ch07 §7.1.4.3 p.87]
- "During normal operation, IHT pressure is maintained at a lower pressure than NSS so that, in the event of an SHX leak, NSS coolant flows from the NSS to the intermediate loop." [PSAR_ch07 §7.1.4.3 p.88]
- "The effects of the sodium-salt reaction due to a postulated leak in the SHX is the subject of research and development as described in Section 13.2.3." [PSAR_ch07 §7.1.4.3 p.88]
- "The expansion tank interfaces with the Sodium Cover Gas System to provide an inert cover gas within the void space, as described in Section 7.2.3, to prevent sodium-air interaction and to provide IHT over-pressure protection." [PSAR_ch07 §7.1.4.3 p.88]
- "The expansion tank interfaces with the Sodium Processing System, described in Section 7.2.4, which provides intermediate sodium processing to limit contaminants and maintain sodium chemistry within limits." [PSAR_ch07 §7.1.4.3 p.88]
- "The IHT maintains a continuous flow of intermediate sodium through the expansion tank to circulate processed sodium through each intermediate loop and limit thermal stratification within the tank." [PSAR_ch07 §7.1.4.3 p.88]
- "Emergency shutdown features are provided for the ISPs." [PSAR_ch07 §7.1.4.3 p.88]
- "Two trip circuit breakers are installed in series, along with associated trip mechanisms, in the power supply circuit to each ISP motor." [PSAR_ch07 §7.1.4.3 p.88]
- "The trip circuit equipment is classified SR and is installed in the SR Nuclear Island Control Building substructure." [PSAR_ch07 §7.1.4.3 p.88]
- "Emergency shutdown of the ISPs is initiated in response to the following abnormal conditions sensed within the IHT or PHT:" [PSAR_ch07 §7.1.4.3 p.88]
- "Low level in an IHT expansion tank (trips associated ISP)" [PSAR_ch07 §7.1.4.3 p.88]
- "High-High primary sodium level (trips both ISPs)" [PSAR_ch07 §7.1.4.3 p.88]
- "High-High primary sodium temperature (trips both ISPs)" [PSAR_ch07 §7.1.4.3 p.88]
- "An automatic emergency shutdown signal actuates the SR trip mechanism and opens the trip circuit breakers." [PSAR_ch07 §7.1.4.3 p.88]
- "Backup to the emergency shutdown signal is provided by local manual breaker trip and by reducing pump speed to the minimum flow setpoint." [PSAR_ch07 §7.1.4.3 p.88]
- "The ISP trip initiated by abnormal level conditions in the IHT expansion tank or in the PHT sodium pool provides protection against Reactor Vessel overfill in the unlikely event of leakage within the IHX." [PSAR_ch07 §7.1.4.3 p.88]
- "The ISP trip initiated by abnormal temperature condition in the PHT cold pool reduces the heat load to the PHT caused by ISP operation in order to maintain heat removal requirements for the RAC within limits." [PSAR_ch07 §7.1.4.3 p.88]
- "IHT components are exposed to an internal environment of high temperature and liquid sodium." [PSAR_ch07 §7.1.4.3 p.88]
- "Externally, IHT components are exposed to the Reactor Auxiliary Building and Reactor Building internal environment, except for the portion of piping routed to the IAC outside of the Reactor Auxiliary Building." [PSAR_ch07 §7.1.4.3 p.88]
- "Material selections for IHT components are based on compatibility with the applicable design internal and external environments, as well as design loadings associated with plant operational events in accordance with applicable design code requirements." [PSAR_ch07 §7.1.4.3 p.88]
- "The IHT piping is designed to meet ASME B31.1 (Reference 7.1.4-1) requirements." [PSAR_ch07 §7.1.4.3 p.89]
- "IHT expansion tanks, drain tanks, SHXs, and ISP pump tanks are designed, fabricated, and tested in accordance with ASME BPVC Section VIII (Reference 7.1.4-2)." [PSAR_ch07 §7.1.4.3 p.89]
- "IHT piping is welded to interfacing components, including the IHXs, SHXs, AHXs, and drain valves to minimize the potential for sodium leakage at equipment connections." [PSAR_ch07 §7.1.4.3 p.89]
- "The IHT piping within the Reactor Building HAA includes a continuous leak guard enclosing the pipe as a secondary barrier for leak protection." [PSAR_ch07 §7.1.4.3 p.89]
- "The leak guard contains and redirects sodium leaks toward dedicated drains and containment features to prevent interaction with SR equipment in the HAA." [PSAR_ch07 §7.1.4.3 p.89]
- "Special treatments are initially selected as described in Section 6.3." [PSAR_ch07 §7.1.4.4 p.89]
- "Preliminary selection of design and construction codes and standards applicable to the IHT is described in Section 7.1.4.2." [PSAR_ch07 §7.1.4.4 p.89]
- "The following programmatic special treatments are preliminarily identified as applicable to the IHT to meet quality, design, reliability, and performance requirements, and the associated summary program descriptions are provided in Chapter 8." [PSAR_ch07 §7.1.4.4 p.89]
- "Quality Assurance Program Description" [PSAR_ch07 §7.1.4.4 p.89]
- "Design Reliability Assurance Program" [PSAR_ch07 §7.1.4.4 p.89]
- "Reliability and Integrity Management Program" [PSAR_ch07 §7.1.4.4 p.89]
- "Equipment Qualification Program" [PSAR_ch07 §7.1.4.4 p.89]
- "Post-Construction Inspection, Testing, and Analysis Program (described in Chapter 12)" [PSAR_ch07 §7.1.4.4 p.89]
- "The IHT provides instrumentation required for expansion tank level signals and ISP trip circuit breaker status." [PSAR_ch07 §7.1.4.5 p.89]

| Component | Safety Classification | Seismic Classification | 출처 |
|---|---|---|---|
| Piping, Boundary Valves, Expansion Tanks | NSRST | SCN1 | [PSAR_ch07 Table 7.1.4-1 p.90] |
| ISP Tank | NSRST | SCN1 | [PSAR_ch07 Table 7.1.4-1 p.90] |
| SHX | NSRST | SCN1 | [PSAR_ch07 Table 7.1.4-1 p.90] |
| Piping (HAA), Leakage Enclosure | NSRST | SCN1 | [PSAR_ch07 Table 7.1.4-1 p.90] |
| ISP Trip Circuit Breaker, Trip Actuator | SR | SCS1 | [PSAR_ch07 Table 7.1.4-1 p.90] |

| Standard | Edition | Title | 출처 |
|---|---|---|---|
| ASME Boiler and Pressure Vessel Code, Section VIII | 2021 | Rules for Construction of Pressure Vessels | [PSAR_ch07 Table 7.1.4-2 p.91] |
| ASME B31.1 | 2022 | Power Piping | [PSAR_ch07 Table 7.1.4-2 p.91] |
| ASME B36.19M (Reference 7.1.4-3) | 2004 | Stainless Steel Pipe | [PSAR_ch07 Table 7.1.4-2 p.91] |
| IEEE 308 (Reference 7.1.4-4) | 2001 | IEEE Standard Criteria for Class 1E Power Systems for Nuclear Power Generating Stations | [PSAR_ch07 Table 7.1.4-2 p.91] |
| IEEE 323 (Reference 7.1.4-5) | 2016 | IEEE Standard for Qualifying Class 1E Equipment for Nuclear Power Generating Stations | [PSAR_ch07 Table 7.1.4-2 p.91] |
| IEEE 603 (Reference 7.1.4-6) | 1991 | IEEE Standard Criteria for Safety Systems for Nuclear Power Generating Stations | [PSAR_ch07 Table 7.1.4-2 p.91] |

- "Figure 7.1.4-1 Intermediate Loop Simplified Diagram" [PSAR_ch07 Figure 7.1.4-1 p.92]

![[PSAR_ch07_Fig_7.1.4-1.png]]

## 해설
Intermediate Heat Transport System(`IHT`)은 정상 출력 운전 중 primary coolant의 열을 발전과 에너지 저장을 위해 Nuclear Island Salt System(`NSS`)으로 보내고, 기동·정지 운전 중에는 정상·선호 원자로 냉각 수단으로서 Intermediate Air Cooling System(`IAC`)으로 보내 대기로 방출한다. 펌프 유량을 잃으면 `IAC` Sodium-Air Heat Exchanger(`AHX`)를 거치는 intermediate coolant 자연 순환으로 붕괴열을 제거하도록 설계된다. intermediate sodium은 primary sodium보다 높은 압력으로 유지되어 `IHX` tube 누설 시 `PHT` 쪽으로 흐르며, 두 소듐은 화학적으로 양립한다. `IHT` 배관에는 누설 탐지·격납 특성이 있어 Head Access Area의 SR%%t:SR%% Structures, Systems, and Components%%t:SSC%%에서 떨어진 catch pan으로 누설을 보낸다.

principal design criteria%%t:PDC%% 2와 4에 대해 `ISP` 비상 정지에 필요한 SR%%t:SR%% `IHT` 구성품은 지하 철근콘크리트 Nuclear Island Control Building 하부구조 안에서 보호되고, Reactor Building 하부구조 안의 `IHT` 배관도 구조물이 외부 재해로부터 보호한다. `NSS` 염과 접하는 구성품은 용융염 환경과의 양립성을 고려해 재료를 고른다. PDC%%t:PDC%% 10에 따라 safety-significant 특성이 Anticipated Operational Occurrence%%t:AOO%% 동안 primary coolant 열 입력을 제한하는 `ISP` trip을 지원한다. PDC%%t:PDC%% 34에 따라 두 intermediate loop가 있어 한 loop의 단일 고장이 잔열 제거를 막지 않는다. PDC%%t:PDC%% 35에 따라 `ISP` 비상 정지는 가상 사고에서 `RAC` 열제거 용량을 넘지 않도록 열 입력을 제한하며, 차단기 하나의 trip 실패에 대비한 직렬 trip circuit breaker 두 개와 보호 계통의 중복 정지 신호를 갖는다. PDC%%t:PDC%% 70과 75–77에 따라 intermediate coolant boundary는 저압으로 운전되고 과압 보호는 `SCG`가 제공하며 사용 전·가동 중 monitoring and non-destructive examination이 Reliability and Integrity Management Program 아래 수행된다. PDC%%t:PDC%% 72에 따라 `ISP` 운동 에너지로 primary sodium에 열을 더할 수 있고, PDC%%t:PDC%% 73과 74에 따라 누설 격납·탐지 특성이 있으며 `IHT` 누설이 소듐-물 반응을 일으킬 수 있는 Reactor Building과 Reactor Auxiliary Building 구역에는 물을 담은 계통이 없다. PDC%%t:PDC%% 78에 따라 primary coolant system과의 인터페이스는 `IHX` 안의 단일 피동 barrier%%t:BARRIER%%이고, 고수위에서 `RPS`가 scram과 `ISP` trip을 개시한다.

기능 표에서 SR%%t:SR%% 기능은 primary coolant 열 추가를 제한하는 `DL3-HR3`(`ISP Trip on High High Primary Sodium Temperature`)와 `IHX` tube 누설을 통한 primary system 유입을 제한하는 `DL3-HR12`(`ISP Trip on High High Primary Sodium Level`)이다. NSRST%%t:NSRST%% 기능은 누설에 의한 intermediate sodium 손실을 제한하는 `DL2-HR2`(`ISP Trip on Low IHT level`), 수동 trip `DL4-HR7`, `ISP`와 `RAC`를 쓸 수 없는 Licensing Basis Event%%t:LBE%%에서 `IHX`에서 `AHX`로 자연 순환하는 `DL4-HR1`, 자동 backup trip `DL4-HR3`, Reactor Building 안 `IHT` 배관의 소듐 누설 탐지·격납인 `DL4-DID1`(`Intermediate Leak Guard Piping`)이다. regulatory guide%%t:RG%% 부합은 `RG 1.22`(`ISP` circuit breaker가 “actuated device”와 “actuated equipment”에 부합)와 `RG 1.36` 완전 부합이며, 구성품은 Safe Shutdown Earthquake%%t:SSE%% 하중에서 safety-significant 기능을 잃지 않도록 검증된다.

`IAC` Active Mode에서는 `ISP`가 intermediate sodium을 순환시키고, `ISP`를 쓸 수 없으면 Blower Mode와 Passive Mode에서 자연 순환으로 `IAC` 열방출을 지원한다. `IHX`와 높은 곳의 `AHX` 사이 고도차가 자연 순환의 구동력을 주며, 고도차는 `RAC` 열방출에 기대지 않고 두 intermediate loop에 유동이 있는 제한 사례의 열제거 요건을 만족하도록 설계된다. `IHT`가 피동 열제거 safety-significant 기능을 수행하는 데 수동 운전원 조치나 자동 작동은 필요 없다. `IHX` 누설 시 expansion tank 저수위나 원자로 용기 고수위 setpoint에서 해당 `ISP`가 자동 정지되고, 배관 최고점의 커버가스(cover gas)%%t:COVER_GAS%% 도입이 siphon 형성을 막는 siphon-break 특성으로 원자로 용기 과충수를 막는다. 정상 운전 중 `IHT` 압력은 `NSS`보다 낮게 유지되어 `SHX` 누설 시 `NSS` 냉각재가 intermediate loop로 흐르며, 가상 `SHX` 누설에 의한 sodium-salt 반응 영향은 연구개발 대상이다(Section 13.2.3). 각 `ISP` motor 전원 회로에는 SR%%t:SR%% trip circuit breaker 두 개가 직렬로 있고, 비상 정지는 expansion tank 저수위(해당 `ISP`), primary sodium High-High 수위(두 `ISP`), primary sodium High-High 온도(두 `ISP`)에서 개시되며, 국부 수동 차단기 trip과 최소 유량 setpoint로의 속도 감소가 backup이다. `IHT` 배관은 `ASME B31.1`, expansion tank·drain tank·`SHX`·`ISP` pump tank는 `ASME BPVC Section VIII`로 설계되고, `HAA` 안의 `IHT` 배관은 연속 leak guard로 둘러싸인다.

`Table 7.1.4-1`에서 배관·경계 밸브·expansion tank, `ISP` tank, `SHX`, `HAA` 배관과 leakage enclosure는 NSRST%%t:NSRST%%·`SCN1`이고, `ISP` trip circuit breaker와 trip actuator는 SR%%t:SR%%·`SCS1`이다. `Table 7.1.4-2`는 `ASME BPVC Section VIII`(2021), `ASME B31.1`(2022), `ASME B36.19M`(2004), `IEEE 308`(2001), `IEEE 323`(2016), `IEEE 603`(1991)을 적는다. programmatic special treatment는 Quality Assurance Program Description, Design Reliability Assurance Program, Reliability and Integrity Management Program, Equipment Qualification Program, Post-Construction Inspection, Testing, and Analysis Program으로 예비 식별되고, `IHT`는 expansion tank 수위 신호와 `ISP` trip circuit breaker 상태 계측을 제공한다.

## 관련 문서
- [[Natrium_System_Primary_Heat_Transport]]
- [[Natrium_System_Intermediate_Air_Cooling]]
- [[Natrium_System_Sodium_Cover_Gas]]
- [[Natrium_Building_Reactor_Auxiliary]]
- [[Natrium_SR_Functions_Heat_Removal]]
- [[Natrium_NSRST_Functions]]
- [[Natrium_Reactor_Heat_Transport_Systems]]
- [[PSAR_ch07]]
