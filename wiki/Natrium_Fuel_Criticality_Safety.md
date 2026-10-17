---
type: natrium
aliases: []
sources:
- PSAR_ch03
- PSAR_ch05
- PSAR_ch07
- SER_KU1_CP
status: checked
verified: 2026-10-17
term: null
tags:
- natrium
- psar-ch3
terms_pending: []
---

# Natrium 신연료·사용후핵연료 Criticality Safety 방법 (Natrium Fuel Criticality Safety)

> [!abstract] 요약
> `PSAR` Chapter 3 §3.14는 principal design criteria%%t:PDC%% 62와 `10 CFR 50.68`(`10 CFR 50.68(b)(7)` 농축도 한계 제외) 부합을 다루며, 핵연료는 Water Pool·Ex-Vessel·In-Vessel Fuel Handling System과 Reactor Enclosure System이 저장·취급한다. 미임계는 `k_eff`와 Monte Carlo 불확실도의 합이 Upper Subcritical Limit(`USL`) 아래임을 계산해 판정하고, 최종 방법론·해석·결과는 operating license%%t:OL%% 단계에서 제공될 예정이다.

## 원문 사실
- "This section demonstrates conformance with Principal Design Criterion 62, “Prevention of Criticality in Fuel Storage and Handling” (as described in Section 5.3) and 10 CFR 50.68, except for the U-235 enrichment limit defined in 10 CFR 50.68(b)(7)." [PSAR_ch03 §3.14 p.127]
- "Special nuclear material, other than fuel onsite, is less than the quantity necessary for a critical mass." [PSAR_ch03 §3.14 p.127]
- "Radiation monitoring in the Fuel Handling Building to detect excessive radiation levels is described in Section 7.6.6." [PSAR_ch03 §3.14 p.127]
- "A nuclear material control and accounting program will be provided at operating license stage." [PSAR_ch03 §3.14 p.127]
- "Fuel is stored and handled by the following Structures, Systems, and Components:" [PSAR_ch03 §3.14.1 p.127]
- "Each of the preliminary calculations showed the maximum calculated keff remained below the applicable USL." [SER_KU1_CP §3.13.1.3 p.319]
- "The staff determined that the preliminary FHE design is consistent with PDC 62 because it provides an acceptable means of criticality prevention based on the evaluation of the supporting criticality analyses for the EVST and NAPS, provided in SE section 3.13" [SER_KU1_CP §7.3.2.1.7 p.516]
- "Consistent with PDC 62, Prevention of criticality in fuel storage and handling, criticality in the fuel storage and handling system is prevented in accordance with 10 CFR 50.68(b) and the criticality analysis is described in Section 3.14." [PSAR_ch07 §7.3.1.2 p.167]
- "Therefore, the NRC hereby grants USO an exemption from the requirements of 10 CFR 50.68(b)(7) to allow the applicant to follow the requirements of 10 CFR 50.68(b) in lieu of" [SER_KU1_CP App. B.2.4 p.737]
- "Exemption to 10 CFR 50.68(b)(7) is addressed in NAT-9403, “Regulatory Exemptions” (ML24088A084), and evaluated in appendix B of this SE." [SER_KU1_CP §3.13 p.315]

| 번호 | 핵연료 저장·취급 SSC (원문 목록) | 출처 |
|---|---|---|
| 1 | Water Pool Fuel Handling System described in Section 7.3.1 | [PSAR_ch03 §3.14.1 p.127] |
| 2 | Ex-Vessel Fuel Handling System described in Section 7.3.2 | [PSAR_ch03 §3.14.1 p.127] |
| 3 | In-Vessel Fuel Handling System described in Section 7.3.3 | [PSAR_ch03 §3.14.1 p.127] |
| 4 | Reactor Enclosure System described in Section 7.1.2 | [PSAR_ch03 §3.14.1 p.127] |

- "The criticality analysis of the Spent Fuel Pool (SFP) conforms to Regulatory Guide (RG) 1.240, “Fresh and Spent Fuel Pool Criticality Analysis,” Revision 0, that endorses Nuclear Energy Institute (NEI) 12-16, “Guidance for Performing Criticality Analyses of Fuel Storage at Light-Water Reactor Power Plants,” Revision 4 (Reference 3.14-1) to provide guidelines for criticality analysis of fuel storage areas." [PSAR_ch03 §3.14.1 p.127]
- "RG 1.240 is used as guidance to establish the methodology for criticality analysis in New Assembly Preconditioning Station (NAPS), Ex-Vessel Storage Tank (EVST), and In-Vessel Storage (IVS)." [PSAR_ch03 §3.14.1 p.127]
- "Structures, Systems, and Components that form the fuel storage locations and the handling equipment associated with the transfer of core assemblies are designed in accordance with Principal Design Criterion 62." [PSAR_ch03 §3.14.1 p.127]
- "The design prevents inadvertent criticality by using geometrically safe configurations and utilizing fixed borated neutron absorbers." [PSAR_ch03 §3.14.1 p.127]
- "Subcriticality is determined by the calculation of k<sub>eff</sub> and assuring it is below the Upper Subcritical Limit (USL), while considering additional margin for uncertainty." [PSAR_ch03 §3.14.2 p.127]
- "The USLs are developed based on applicable benchmarks neutronically similar to the fuel storage systems." [PSAR_ch03 §3.14.2 p.127]
- "The USL varies based on system conditions." [PSAR_ch03 §3.14.2 p.127]
- "For example, the USL for the IVS and EVST is different than the USL for the SFP because fuel in the IVS and EVST is moderated by sodium and fuel in the SFP is moderated by water." [PSAR_ch03 §3.14.2 p.127]
- "The computed k<sub>eff</sub> for the system plus twice the Monte Carlo uncertainty (σ) must be less than the USL:" [PSAR_ch03 §3.14.2 p.128]
- "k<sub>eff</sub> + 2σ < USL (Equation 3.14-1)" [PSAR_ch03 §3.14.2 p.128]
- "This ensures that the USL is met at a 95 percent probability and 95 percent confidence level." [PSAR_ch03 §3.14.2 p.128]
- "USL = 1 + bias – σ<sub>bias</sub> – Δ<sub>SM</sub> – Δ<sub>AOA</sub> (Equation 3.14-2)" [PSAR_ch03 §3.14.2 p.128]

| 기호 | 원문 정의 | 출처 |
|---|---|---|
| Bias | Bias is calculated as the difference between the calculated k<sub>eff</sub> and the critical experiment model. | [PSAR_ch03 §3.14.2 p.128] |
| Bias | Because a positive bias can be non-conservative, the bias is set to zero when the calculated average k<sub>eff</sub> is greater than 1.0. | [PSAR_ch03 §3.14.2 p.128] |
| σ<sub>bias</sub> | σ<sub>bias</sub> is the uncertainty in the bias. | [PSAR_ch03 §3.14.2 p.128] |
| Δ<sub>SM</sub> | Δ<sub>SM</sub> is an administrative margin, typically 0.05. | [PSAR_ch03 §3.14.2 p.128] |
| Δ<sub>AOA</sub> | Δ<sub>AOA</sub> is an additional subcritical margin to account for extensions in the area of applicability if the available benchmarks are not sufficiently similar to the fuel storage systems. | [PSAR_ch03 §3.14.2 p.128] |

- "The USLs are computed using either methodologies outlined in NUREG/CR-6698, “Guide for Validation of Nuclear Criticality Safety Calculational Methodology,” July 2001 (Reference 3.14-2) or Whisper-1.1 program described in LA-UR-14-26558, “Whisper: Sensitivity/Uncertainty-Based Computational Methods and Software for Determining Baseline Upper Subcritical Limits,” (Reference 3.14-3)." [PSAR_ch03 §3.14.2 p.128]
- "The methodology outlined in NUREG/CR-6698 selects applicable benchmark experiments similar to the plant system." [PSAR_ch03 §3.14.2 p.128]
- "Key parameters used to determine applicability include system geometry, U-235 enrichment, fissile material composition, neutron energy spectrum, coolant type, reflector material, fuel density, and temperature." [PSAR_ch03 §3.14.2 p.128]
- "Trends in the k<sub>eff</sub> results are examined as a function of the system parameters selected." [PSAR_ch03 §3.14.2 p.128]
- "Experiments are selected from the NEA/NSC/DOC(95)03, “International Handbook of Evaluated Criticality Safety Benchmark Experiments” (Reference 3.14-4)." [PSAR_ch03 §3.14.2 p.128]
- "These experiments can also be supplemented with key liquid metal fast reactor experiments from the NEA/NSC/DOC(2006)01, “International Handbook of Evaluated Reactor Physics Benchmark Experiments” (Reference 3.14-5)." [PSAR_ch03 §3.14.2 p.128]
- "After developing a list of applicable benchmarks, an MCNP 6.2 benchmark is developed for each experiment using LA-UR-17-29981, “MCNP User's Manual, Code Version 6.2,” 2017 (Reference 3.14-6)." [PSAR_ch03 §3.14.2 p.128]
- "Bias, σ<sub>bias</sub>, and Δ<sub>AOA</sub> are computed using the guidance provided in NUREG/CR-6698." [PSAR_ch03 §3.14.2 p.128]
- "An alternate method of USL computation utilizes more advanced sensitivity and uncertainty methods and the Whisper-1.1 program (Reference 3.14-3)." [PSAR_ch03 §3.14.2 p.129]
- "Whisper is developed by Los Alamos National Laboratory for criticality safety applications and is distributed with MCNP 6.2." [PSAR_ch03 §3.14.2 p.129]
- "Whisper includes approximately 1,100 MCNP benchmarks from the International Handbook of Evaluated Criticality Safety Benchmark Experiments that cover a wide range of criticality safety problems." [PSAR_ch03 §3.14.2 p.129]
- "Whisper uses sensitivity profile data, as computed by MCNP, along with nuclear data covariance files to calculate the bias, σ<sub>bias</sub>, and Δ<sub>AOA</sub> for an input application." [PSAR_ch03 §3.14.2 p.129]
- "Approximately 100 Whisper benchmarks will be selected." [PSAR_ch03 §3.14.2 p.129]
- "Whisper also provides parameters to account for MCNP software errors and uncertainties in cross-section data." [PSAR_ch03 §3.14.2 p.129]
- "However, these computed parameters are generally much less than the standard Δ<sub>SM</sub> value of 0.05 applied as a general administrative margin." [PSAR_ch03 §3.14.2 p.129]
- "Therefore, these parameters as provided by Whisper are not directly incorporated into the USL." [PSAR_ch03 §3.14.2 p.129]
- "The following sections describe the methodology utilized to perform the criticality analysis for each spent fuel storage location." [PSAR_ch03 §3.14.2 p.129]
- "The final methodology, analyses, and results will be provided at the operating license stage." [PSAR_ch03 §3.14.2 p.129]
- "The use of either method for USL development is at the discretion of the organization performing the criticality analysis." [PSAR_ch03 §3.14.2 p.129]
- "The procedures prohibiting the handling and storage at any one time of more fuel assemblies than have been determined to be safely subcritical under adverse moderation conditions by unborated water will be provided at the operating license stage." [PSAR_ch03 §3.14.2 p.129]
- "The SFP design, codes considered in the design of the SFP, controls for operation of the fuel handling equipment and fuel storage, layout, and associated subsystems and equipment are described in Section 7.3.1." [PSAR_ch03 §3.14.2.1 p.129]
- "The SFP is used for storage of spent fuel assemblies; fresh fuel assemblies are not stored in the SFP." [PSAR_ch03 §3.14.2.1 p.129]
- "The spent fuel is stored in two types of racks as described in Section 7.3.1." [PSAR_ch03 §3.14.2.1 p.129]
- "Failed fuel is canned in a Failed Fuel Canister and inerted." [PSAR_ch03 §3.14.2.1 p.129]
- "Because each Failed Fuel Canister is certified as leak-tight, the criticality analysis of the SFP will credit moderator exclusion within each Failed Fuel Canister." [PSAR_ch03 §3.14.2.1 p.129]
- "Borated stainless steel is used as a neutron absorber material in the racks; 90 percent of the boron is credited in the borated stainless steel neutron absorber plates." [PSAR_ch03 §3.14.2.1 p.129]
- "The SFP analysis follows the guidelines of RG 1.240 and NEI 12-16.The SFP does not contain soluble boron." [PSAR_ch03 §3.14.2.1 p.129]
- "The racks for intact and failed fuel are modeled in sufficient detail to capture the physics of the system and contain conservative reactivity assumptions." [PSAR_ch03 §3.14.2.1 p.129]
- "Conservative fuel assembly model – the following fuel assembly parameters are varied to determine the most reactive condition: enrichment, duct thickness, pellet density, pellet diameter, cladding thickness, and pin pitch." [PSAR_ch03 §3.14.2.1 p.130]
- "Simplifications to the model are justified by the analysis. The fuel is modeled as fresh fuel with no burnup." [PSAR_ch03 §3.14.2.1 p.130]
- "Conservative rack model – evaluates the most reactive placement of fuel within the SFP (e.g., lateral shifting within compartments), water density, and rack dimensions." [PSAR_ch03 §3.14.2.1 p.130]
- "Cases that bound credible abnormal events – evaluates temperatures beyond normal operating range, dropped and mispositioned assemblies, design basis seismic events, and low water density." [PSAR_ch03 §3.14.2.1 p.130]
- "The EVST design, codes considered in the design of the EVST, operation of the fuel handling equipment and fuel storage, layout, and associated subsystems are described in Section 7.3.2." [PSAR_ch03 §3.14.2.2 p.130]
- "The EVST is used as a staging area for both fresh and spent fuel assemblies." [PSAR_ch03 §3.14.2.2 p.130]
- "Conservative fuel assembly model – the following fuel assembly parameters are modeled to determine the most reactive condition: enrichment, duct thickness, pellet density, pellet diameter, cladding thickness, and pin pitch." [PSAR_ch03 §3.14.2.2 p.130]
- "Items may be conservatively replaced with sodium, such as the inlet nozzle, wire wrap, and handling socket." [PSAR_ch03 §3.14.2.2 p.130]
- "Simplifications to the model will be justified by the analysis. The fuel is modeled as fresh fuel with no credit for burnup." [PSAR_ch03 §3.14.2.2 p.130]
- "Conservative EVST model – Evaluates the most reactive placement of fuel within the EVST (i.e., lateral shifting within compartments), sodium density, and EVST dimensions." [PSAR_ch03 §3.14.2.2 p.130]
- "Cases that bound credible abnormal events – Evaluates temperatures beyond normal operating range, dropped and mispositioned assemblies, design basis seismic events, fuel pins flooded with sodium from assumed breach, sodium at solid density, and moderator treated as a void." [PSAR_ch03 §3.14.2.2 p.130]
- "The IVS design, layout, and codes considered in the design are described in Section 7.1.2 The operation of the fuel handling equipment and associated subsystems are described in Section 7.3.3." [PSAR_ch03 §3.14.2.3 p.130]
- "The IVS is used to store spent fuel assemblies." [PSAR_ch03 §3.14.2.3 p.130]
- "The IVS is located outside the core between the inner and outer core barrels." [PSAR_ch03 §3.14.2.3 p.130]
- "The model does not assume fuel assembly burnup for conservatism. Fuel is modeled as fresh at the maximum enrichment." [PSAR_ch03 §3.14.2.3 p.130]
- "A combined reactor core and IVS criticality model reports the k<sub>eff</sub> of the reactor core." [PSAR_ch03 §3.14.2.3 p.131]
- "The combined model of the reactor core and IVS reports k<sub>eff</sub> approximately equal to one and does not provide any information about the IVS." [PSAR_ch03 §3.14.2.3 p.131]
- "The exchange of neutrons between the reactor core and IVS is largely eliminated due to the distance between the core and IVS and the reflector and boron carbide shield assemblies along the perimeter of the reactor core." [PSAR_ch03 §3.14.2.3 p.131]
- "In the IVS models, the core is removed and a white or reflective boundary is placed on the inner surface of the IVS." [PSAR_ch03 §3.14.2.3 p.131]
- "This boundary condition allows k<sub>eff</sub> for the IVS to be computed separate from the reactor core." [PSAR_ch03 §3.14.2.3 p.131]
- "Modeling the inner surface as white or reflective is more reactive than other modeling options, such as modeling the core as sodium." [PSAR_ch03 §3.14.2.3 p.131]
- "Conservative fuel assembly model – the following fuel assembly parameters are varied to determine the most reactive condition: enrichment, duct thickness, pellet density, active fuel height, pellet diameter, cladding thickness, and pin pitch." [PSAR_ch03 §3.14.2.3 p.131]
- "Conservative IVS model – Evaluates the most reactive placement of fuel within the IVS (i.e., lateral shifting within compartments), sodium density, IVS dimensions, and core barrel dimensions." [PSAR_ch03 §3.14.2.3 p.131]
- "Cases that bound credible abnormal events – Evaluates temperatures beyond normal operating range, dropped and mispositioned assemblies, design basis seismic events, fuel pins flooded with sodium from assumed breach, sodium at solid density, and moderator treated as a void." [PSAR_ch03 §3.14.2.3 p.131]
- "The NAPS is a preconditioning station that stores fresh fuel assemblies in a gas." [PSAR_ch03 §3.14.2.4 p.131]
- "The gas heats the fuel prior to insertion into the EVST." [PSAR_ch03 §3.14.2.4 p.131]
- "Conservative fuel assembly model - the following fuel assembly parameters will be modeled at the most reactive condition: enrichment, duct thickness, pellet density, pellet diameter, cladding thickness, and pin pitch." [PSAR_ch03 §3.14.2.4 p.131]
- "Simplifications will be justified by the analysis. The fuel will be modeled as fresh fuel." [PSAR_ch03 §3.14.2.4 p.131]
- "Conservative NAPS model - Evaluates the most reactive placement of fuel within the NAPS (i.e., lateral shifting within compartments) and NAPS dimensions." [PSAR_ch03 §3.14.2.4 p.131]
- "Cases that bound credible abnormal events - Evaluates temperatures beyond normal operating range, dropped and misplaced assemblies, and design basis seismic events." [PSAR_ch03 §3.14.2.4 p.131]
- "This section addresses the analysis of criticality safety for new unirradiated fuel prior to placement in the NAPS." [PSAR_ch03 §3.14.2.5 p.132]
- "New fuel for Kemmerer Unit 1 is delivered to the site in a shipping container and brought into the designated FHB storage location." [PSAR_ch03 §3.14.2.5 p.132]
- "The shipping container is designed to maintain a subcritical configuration." [PSAR_ch03 §3.14.2.5 p.132]
- "The core assemblies will be removed from the shipping container and placed in the assembly receipt inspection stand (ARIS)." [PSAR_ch03 §3.14.2.5 p.132]
- "After receipt inspection is complete, each core assembly is removed and placed into the NAPS." [PSAR_ch03 §3.14.2.5 p.132]
- "The criticality analysis for the shipping container, storage location of the shipping containers within the FHB prior to the transfer to the ARIS, and ARIS will be available in support of the Operating License." [PSAR_ch03 §3.14.2.5 p.132]

| 번호 | 참고문헌 (원문) | 출처 |
|---|---|---|
| 3.14-1 | NEI, NEI 12-16, “Guidance for Performing Criticality Analyses of Fuel Storage at Light-Water Reactor Power Plants,” Revision 4. | [PSAR_ch03 §References (3.14) p.132] |
| 3.14-2 | NRC, NUREG/CR-6698, “Guide for Validation of Nuclear Criticality Safety Calculational Methodology,” January 2001. | [PSAR_ch03 §References (3.14) p.132] |
| 3.14-3 | B. Kiedrowski, LA-UR-14-26558, “Whisper: Sensitivity/Uncertainty-Based Computational Methods and Software for Determining Baseline Upper Subcritical Limits,” Los Alamos National Laboratory. | [PSAR_ch03 §References (3.14) p.132] |
| 3.14-4 | OECD, NEA/NSC/DOC(95)03, “International Handbook of Evaluated Criticality Safety Benchmark Experiments”. | [PSAR_ch03 §References (3.14) p.132] |
| 3.14-5 | OECD, NEA/NSC/DOC(2006)01, “International Handbook of Evaluated Reactor Physics Benchmark Experiments,” 2019. | [PSAR_ch03 §References (3.14) p.132] |
| 3.14-6 | Los Alamos National Laboratory, LA-UR-17-29981, “MCNP User's Manual, Code Version 6.2,” 2017. | [PSAR_ch03 §References (3.14) p.132] |

- "The design prevents inadvertent criticality by using geometrically safe configurations and utilizing fixed borated neutron absorbers." [PSAR_ch03 §3.14.1 p.127]
- "The design of the RES In-Vessel Storage, FHI, FHE, and FHP fuel storage and handling systems prevents inadvertent criticality by using design attributes such as geometrically safe configurations and fixed neutron absorbers." [PSAR_ch05 §5.3.5.3 p.42]
- "Criticality in the SFP fuel storage area is prevented by fixed borated stainless steel neutron absorber plates in the fuel region of the storage racks and by having a subcritical geometry configuration" [PSAR_ch07 §7.3.1.2 p.167]
- "The computed k<sub>eff</sub> for the system plus twice the Monte Carlo uncertainty (σ) must be less than the USL:" [PSAR_ch03 §3.14.2 p.128]
- "Δ<sub>SM</sub> is an administrative margin, typically 0.05." [PSAR_ch03 §3.14.2 p.128]
- "via a geometrically sub-critical configuration which limits k<sub>eff</sub> ≤ 0.95 based on the most reactive fuel configuration." [PSAR_ch07 §7.3.2.2 p.187]
- "This section demonstrates conformance with Principal Design Criterion 62, “Prevention of Criticality in Fuel Storage and Handling” (as described in Section 5.3) and 10 CFR 50.68, except for the U-235 enrichment limit defined in 10 CFR 50.68(b)(7)." [PSAR_ch03 §3.14 p.127]
- "criticality in the fuel storage and handling system is prevented in accordance with 10 CFR 50.68(b) and the criticality analysis is described in Section 3.14." [PSAR_ch07 §7.3.1.2 p.167]
- "The SFP analysis follows the guidelines of RG 1.240 and NEI 12-16.The SFP does not contain soluble boron." [PSAR_ch03 §3.14.2.1 p.129]
- "Since the SFP does not employ soluble boron, the storage racks maintain stored spent fuel subcritical by controlling the relative spacing within the racks (geometry control) and the installation of fixed borated neutron absorbers within the assembly storage cells." [PSAR_ch07 §7.3.1.1 p.164]

## 해설
`PSAR` Chapter 3 §3.14는 PDC%%t:PDC%% 62(`Prevention of Criticality in Fuel Storage and Handling`)와 `10 CFR 50.68` 부합을 보이되 `10 CFR 50.68(b)(7)`의 U-235 농축도 한계는 예외로 한다고 적는다. 부지의 핵연료 외 특수핵물질은 임계 질량에 필요한 양보다 적고, Fuel Handling Building의 과도한 방사선 준위 탐지는 Section 7.6.6에 있으며, nuclear material control and accounting program은 OL%%t:OL%% 단계에서 제공될 예정이다(`will`). 핵연료를 저장·취급하는 Structures, Systems, and Components%%t:SSC%%는 Water Pool Fuel Handling System(Section 7.3.1), Ex-Vessel Fuel Handling System(Section 7.3.2), In-Vessel Fuel Handling System(Section 7.3.3), Reactor Enclosure System(Section 7.1.2)이다. Spent Fuel Pool(`SFP`) 임계 해석은 `NEI 12-16`을 승인한 `RG 1.240`을 따르고, 같은 지침이 New Assembly Preconditioning Station(`NAPS`), Ex-Vessel Storage Tank(`EVST`), In-Vessel Storage(`IVS`) 임계 해석 방법론 수립에도 쓰인다. 설계는 기하학적으로 안전한 배치와 고정 borated 중성자 흡수체로 비의도적 임계를 막는다.

미임계는 `k_eff`를 계산해 Upper Subcritical Limit(`USL`) 아래임을 확인하고 불확실도에 대한 추가 여유를 고려해 판정한다. `USL`은 저장 계통과 중성자적으로 유사한 benchmark에 기반해 개발되며 계통 조건에 따라 달라지는데, 원문은 `IVS`·`EVST`의 연료가 소듐으로, `SFP`의 연료가 물로 감속되기 때문에 `USL`이 다르다고 적는다. 판정식은 계통 `k_eff`에 Monte Carlo 불확실도의 두 배를 더한 값이 `USL`보다 작아야 한다는 것이며(`Equation 3.14-1`), 이는 `95 percent` 확률·신뢰 수준에서 `USL`을 만족함을 보장한다. `USL`은 `1 + bias – σ_bias – Δ_SM – Δ_AOA`로 정의되고(`Equation 3.14-2`), bias는 계산 `k_eff`와 임계 실험 모형의 차이로 계산하되 평균 `k_eff`가 `1.0`보다 크면 0으로 둔다. `Δ_SM`은 행정 여유로 통상 `0.05`이고, `Δ_AOA`는 가용 benchmark가 저장 계통과 충분히 유사하지 않을 때 area of applicability 확장을 반영하는 추가 미임계 여유이다.

`USL`은 `NUREG/CR-6698` 방법론이나 `LA-UR-14-26558`에 기술된 `Whisper-1.1` 프로그램으로 계산한다. `NUREG/CR-6698` 방법은 계통과 유사한 benchmark 실험을 고르며, 적용성 판단의 주요 변수는 계통 형상, U-235 농축도, 핵분열 물질 조성, 중성자 에너지 스펙트럼, 냉각재 종류, 반사체 재료, 연료 밀도, 온도이다. 실험은 `NEA/NSC/DOC(95)03`에서 고르고 `NEA/NSC/DOC(2006)01`의 액체금속 고속로 실험으로 보완할 수 있으며, 실험마다 `MCNP 6.2` benchmark를 만들어 bias, `σ_bias`, `Δ_AOA`를 계산한다. 대안인 `Whisper-1.1`은 Los Alamos National Laboratory가 개발해 `MCNP 6.2`와 함께 배포되며 International Handbook of Evaluated Criticality Safety Benchmark Experiments의 약 `1,100`개 benchmark를 포함하고, 민감도 프로파일과 핵자료 공분산으로 bias와 불확실도를 계산한다. 약 `100`개 Whisper benchmark가 선정될 예정이며, Whisper가 주는 소프트웨어 오차·단면적 불확실도 변수는 일반 행정 여유 `0.05`보다 훨씬 작아 `USL`에 직접 반영하지 않는다. 두 방법 가운데 어느 것을 쓸지는 임계 해석 수행 조직의 재량이며, 최종 방법론·해석·결과와 한 번에 취급·저장할 수 있는 집합체 수를 제한하는 절차는 OL%%t:OL%% 단계에서 제공될 예정이다.

저장 위치별 모형은 네 곳 모두 conservative fuel assembly model, 위치별 conservative model, 신뢰할 만한 이상 사건을 포괄하는 사례로 이루어진다. `SFP`에는 사용후핵연료만 저장하고 신연료는 저장하지 않으며, 파손 연료는 Failed Fuel Canister에 담아 불활성화하고 canister가 leak-tight로 인증되므로 해석은 canister 안의 moderator exclusion을 credit한다. rack의 중성자 흡수재는 borated stainless steel이고 흡수판 붕소의 `90 percent`를 credit하며, `SFP`에는 soluble boron이 없다. 연료 집합체 모형은 농축도, duct 두께, pellet 밀도·직경, 피복 두께, pin pitch를 변화시켜 가장 반응도가 큰 조건을 찾고 연소도 없이 신연료로 모형화한다. `EVST`는 신연료와 사용후핵연료의 staging 구역이고, `IVS`는 사용후핵연료를 저장하며 inner·outer core barrel 사이 노심 바깥에 있다. 노심과 `IVS`를 합친 모형은 노심의 `k_eff`만 보고하고 `IVS` 정보를 주지 않으므로, `IVS` 모형에서는 노심을 제거하고 `IVS` 내면에 white 또는 reflective 경계를 두어 `IVS`의 `k_eff`를 따로 계산하며, 이 경계 조건이 노심을 소듐으로 모형화하는 것보다 반응도가 크다. `NAPS`는 신연료 집합체를 기체 속에 저장해 `EVST` 삽입 전에 가열하는 설비이다. 신연료는 shipping container로 부지에 반입되어 `FHB` 지정 저장 위치로 옮겨지고, 집합체는 container에서 꺼내 assembly receipt inspection stand(`ARIS`)에 놓였다가 인수 검사 뒤 `NAPS`로 들어가며, shipping container·보관 위치·`ARIS`의 임계 해석은 Operating License를 뒷받침하도록 제공될 예정이다.

`PSAR` Chapter 5는 같은 임계 방지 수단을 `RES` In-Vessel Storage, `FHI`, `FHE`, `FHP`의 저장·취급 계통에 대해 적고 흡수체를 `fixed neutron absorbers`로 표기하며, Chapter 7 §7.3.1.2는 `SFP`에 대해 borated stainless steel 흡수판과 subcritical geometry를 적는다. Chapter 7 §7.3.2.2는 가장 반응도가 큰 연료 배치 기준으로 `k_eff` `≤ 0.95`라는 고정값을 적는 반면, 이 절은 위치와 조건에 따라 달라지는 `USL`을 기준으로 삼는다. 두 기준의 관계를 설명하는 원문은 vault에 없다. 또 Chapter 7 §7.3.1.2는 `10 CFR 50.68(b)` 부합을 적되 (b)(7) 면제를 언급하지 않고, 이 절은 `10 CFR 50.68(b)(7)` 농축도 한계를 예외로 적는다.

**규정 대비 메모(C35, 규정 불일치).** `PSAR` Chapter 3 §3.14.2는 계산한 k_eff에 Monte Carlo 불확실도의 두 배를 더한 값이 `USL`보다 작아야 한다는 기준을 두고, Chapter 7 §7.3.2.2는 가장 반응성이 큰 연료 배치에 기반해 k_eff ≤ 0.95로 제한하는 기하학적 미임계 배치를 적는다. `SER`은 예비 계산마다 최대 k_eff가 해당 `USL` 아래였다고 기술하고, `EVST`와 `NAPS`의 임계 해석 평가를 근거로 `FHE` 예비 설계가 PDC%%t:PDC%% 62와 정합한다고 판단했다. 따라서 `SER`이 ex-vessel 설비에 쓴 판정 기준은 `USL` 방법이며, Chapter 7의 고정값 0.95는 `SER`이 쓴 기준이 아니다. `SER`에는 이 0.95 문장에 대한 판단이 없다(vault 기준).

**규정 대비 메모(C36, 규정 불일치).** `PSAR` Chapter 3 §3.14는 10 CFR 50.68 부합을 보이되 50.68(b)(7)의 U-235 농축도 한계는 예외로 한다고 적고, Chapter 7 §7.3.1.2는 핵연료 저장·취급 계통의 임계가 50.68(b)에 따라 방지된다고 적는다. NRC는 50.68(b)(7) 요건에 대한 면제를 부여했고, `SER`은 이 면제를 부록 B에서 평가한다고 적는다. Chapter 7 §7.3.1.2는 50.68(b) 부합만 적고 (b)(7) 면제를 언급하지 않으므로, `SER`이 부여한 면제가 Chapter 7 기술에는 드러나지 않는다.

## 관련 문서
- [[Natrium_System_Water_Pool_Fuel_Handling]]
- [[Natrium_System_Ex_Vessel_Fuel_Handling]]
- [[Natrium_System_In_Vessel_Fuel_Handling]]
- [[Natrium_System_Reactor_Enclosure]]
- [[Natrium_Building_Fuel_Handling]]
- [[Natrium_Nuclear_Design]]
- [[PSAR_ch03]]
- [[Natrium_SER_Core_Fuel_Design_Review]]
