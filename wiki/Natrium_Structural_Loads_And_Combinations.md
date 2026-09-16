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

# Natrium 구조 하중과 하중조합 (Natrium Structural Loads and Loading Combinations)

> [!abstract] 요약
> `PSAR` §6.4.2.2는 safety-significant 구조물의 설계 하중을 normal, severe environmental, extreme environmental, abnormal의 네 범주로 나누고 범주마다 기호와 값을 정의한다.
> Safety-Related%%t:SR%% 하부구조의 조합은 `ANSI/AISC N690-18`과 `ACI 349-13`에, Non-Safety-Related with Special Treatment%%t:NSRST%% 하부·상부구조의 조합은 `IBC-2021` §1605.1의 Load and Resistance Factor Design에 기초하며, extraordinary events 조합은 Table 6.4-7, 6.4-8, 6.4-11, 6.4-12가 담는다.
> 구조 안정성 안전율은 SR%%t:SR%% 하부구조에 Table 6.4-9, NSRST%%t:NSRST%% 하부구조에 전도 1.50, 활동 1.10, 부력 1.10을 둔다.

## 원문 사실
- "Safety-significant structures are designed and analyzed for appropriate combinations of design loads and loading combinations, including normal loads, severe environmental loads, extreme environmental loads, and abnormal loads." [PSAR_ch06 §6.4.2.2 p.24]
- "The applied design loads and associated symbols are described in the following sections." [PSAR_ch06 §6.4.2.2 p.24]
- "Dead loads include the self-weight of the safety-significant structure, such as the walls, roof, slab, steel beams, and columns, including permanent plant equipment, and mechanical and electrical distribution systems." [PSAR_ch06 §6.4.2.2.1 p.25]
- "Dead loads are determined in accordance with ASCE 7-16 (Reference 6.4-2)." [PSAR_ch06 §6.4.2.2.1 p.25]
- "The normal weight of reinforced concrete and steel is based on a design density of 150 pounds per cubic foot and 490 pounds per cubic foot, respectively." [PSAR_ch06 §6.4.2.2.1 p.25]
- "In addition, significant loads associated with support loads of distribution systems, such as piping, cable trays, and NI Heating, Ventilation, and Air Conditioning System components, are also included as dead loads." [PSAR_ch06 §6.4.2.2.1 p.25]
- "A uniform dead load of 20 pounds per square foot (psf) is applied to the concrete walls to represent penetration sleeves or wall-supported systems and components." [PSAR_ch06 §6.4.2.2.1 p.25]
- "Contained liquid (e.g., tanks, Spent Fuel Pool) is treated as a dead load, as well as the weight of NI Cranes and Hoists crane trolleys and bridges." [PSAR_ch06 §6.4.2.2.1 p.25]
- "Live loads are loads produced by the use and occupancy of the building that does not include construction loads or environmental loads, such as wind, snow, rain, earthquake, flood, or dead load." [PSAR_ch06 §6.4.2.2.1 p.25]
- "Live load refers to a normal load that may vary with intensity or point of application." [PSAR_ch06 §6.4.2.2.1 p.25]
- "Live loads include moveable equipment or equipment that is likely to be moved as a non-permanent weight." [PSAR_ch06 §6.4.2.2.1 p.25]
- "For floor beams, girders, and slabs at roof and elevated floor levels, a 4,000 pound-force concentrated load is used in locations that maximize moment and shear without carrying out to other members." [PSAR_ch06 §6.4.2.2.1 p.25]
- "For equipment supports, live loads also consider contributory loads due to associated equipment operation and movement." [PSAR_ch06 §6.4.2.2.1 p.25]
- "Live loads are applied, removed, or shifted in location as necessary to obtain the worst-case loading conditions." [PSAR_ch06 §6.4.2.2.1 p.25]
- "Floor area live loads are omitted from areas occupied by permanent plant equipment whose weights are specifically included in the design dead loads except where access is available." [PSAR_ch06 §6.4.2.2.1 p.25]
- "Live loads associated with elevators and machinery are increased from 20 percent to 100 percent in accordance with ASCE 7-16 to account for impact." [PSAR_ch06 §6.4.2.2.1 p.25]
- "Temporary equipment laydown loads are evaluated, and the maximum of the actual laydown load is utilized." [PSAR_ch06 §6.4.2.2.1 p.25]
- "Uniform live loads are the maximum loads expected by the intended use." [PSAR_ch06 §6.4.2.2.1 p.25]
- "A uniform load of 20 psf is used for the roof live load of the NSRST superstructures, with allowed reductions in accordance with ASCE 7-16." [PSAR_ch06 §6.4.2.2.1 p.25]
- "The NSRST superstructures are designed for a ground snow load of 35 psf." [PSAR_ch06 §6.4.2.2.1 p.26]
- "Roofs are evaluated to confirm they possess adequate stiffness to preclude progressive deflection as meltwater is created from the snow load or from rainfall on the surface." [PSAR_ch06 §6.4.2.2.1 p.26]
- "Ice Loads (I) Ice loading for NSRST superstructure are considered as 0.25-inch nominal ice thickness with 50 miles per hour concurrent wind speed in accordance with ASCE 7-16 with an ice density not less than 56 pounds per cubic foot for the NSRST superstructures." [PSAR_ch06 §6.4.2.2.1 p.26]
- "Soil lateral earth pressure loads resulting from soil bearing pressure and hydrostatic pressure are applied to exterior walls up to the specified finished grade elevation of safety-significant substructures." [PSAR_ch06 §6.4.2.2.1 p.26]
- "Lateral earth pressure is based upon the appropriate lateral earth pressure coefficient, soil density, and includes the effects of groundwater." [PSAR_ch06 §6.4.2.2.1 p.26]
- "Submerged soil pressures include the effect of the buoyant soil plus the hydrostatic loads due to normal ground water or flooding." [PSAR_ch06 §6.4.2.2.1 p.26]
- "Vertical pressure due to buoyancy effects from design groundwater level on the underside of the foundation are also considered." [PSAR_ch06 §6.4.2.2.1 p.26]
- "During construction, the effects by crane and vehicle surcharge loads are added to the lateral soil pressure." [PSAR_ch06 §6.4.2.2.1 p.26]
- "Dynamic seismic-induced soil pressures on embedded below-grade walls are calculated directly as part of the seismic analysis of the structures and included as a component of SSE loads for SR substructures." [PSAR_ch06 §6.4.2.2.1 p.26]
- "Snow loads for NSRST superstructures are considered to bound the rain loads for NSRST superstructures." [PSAR_ch06 §6.4.2.2.1 p.26]
- "NSRST superstructure roofs are evaluated to confirm they possess adequate stiffness to preclude progressive deflection as meltwater is created from the snow load or from rainfall on the surface." [PSAR_ch06 §6.4.2.2.1 p.26]
- "A groundwater level of 15 feet below the finished plant grade is used for structural stability checks." [PSAR_ch06 §6.4.2.2.1 p.26]
- "Soil friction resisting buoyancy is used for the evaluation of embedded structures." [PSAR_ch06 §6.4.2.2.1 p.26]
- "The normal force due to soil pressure is calculated using soil properties as described in Section 2.6.4." [PSAR_ch06 §6.4.2.2.1 p.26]
- "Soil friction is not used when waterproofing is provided on the exterior surface of the below grade substructures." [PSAR_ch06 §6.4.2.2.1 p.26]
- "Hydrostatic loads are the result of fluid pressures acting on the internal surface of compartments, such as the Spent Fuel Pool and liquid radioactive water processing tanks." [PSAR_ch06 §6.4.2.2.1 p.26]
- "The compartments may have constant or fluctuating liquid levels." [PSAR_ch06 §6.4.2.2.1 p.26]
- "Loads resulting from groundwater pressure based on the groundwater and external flooding are included as part of the soil pressure loads." [PSAR_ch06 §6.4.2.2.1 p.27]
- "The external flooding from the design basis flood does not impact the NI buildings as described in Section 2.5.1.1." [PSAR_ch06 §6.4.2.2.1 p.27]
- "Impulsive hydrodynamic loads resulting from the seismic excitation of fluids (e.g., Spent Fuel Pool) are included as a component of the SSE load." [PSAR_ch06 §6.4.2.2.1 p.27]
- "Thermal loads consist of thermally induced forces and moments resulting from normal plant operation, start-up, shutdown, or environmental conditions." [PSAR_ch06 §6.4.2.2.1 p.27]
- "Thermal loads due to axial restraints and thermal gradients as well as self-relieving nature of thermal loads are considered." [PSAR_ch06 §6.4.2.2.1 p.27]
- "Pipe reactions coming from piping system supports during normal operating, start-up, or shutdown conditions are based on the critical transient or steady-state condition, excluding dead load and earthquake reactions." [PSAR_ch06 §6.4.2.2.1 p.27]
- "Appropriate dynamic load factors are used when applying transient loads." [PSAR_ch06 §6.4.2.2.1 p.27]
- "The NI Cranes and Hoists crane self-weights are included as dead loads." [PSAR_ch06 §6.4.2.2.1 p.27]
- "The crane live loads are defined as the rated capacity of the crane and are used for the design of the runway’s beams, connections, and crane supports." [PSAR_ch06 §6.4.2.2.1 p.27]
- "The crane live loads consider the maximum wheel loads including vibration forces as well as vertical impact, lateral, and longitudinal forces induced by a moving crane." [PSAR_ch06 §6.4.2.2.1 p.27]
- "Further details of the NI Cranes and Hoists are provided in Section 1.1.4.3.13." [PSAR_ch06 §6.4.2.2.1 p.27]
- "The maximum crane wheel loads are increased by 25 percent to consider the effects of impact, vibration, and unexpected force." [PSAR_ch06 §6.4.2.2.1 p.27]
- "The longitudinal and lateral forces are calculated as 10 percent and 20 percent of the sum of the rated capacity and applied on the traction surface of the crane girder." [PSAR_ch06 §6.4.2.2.1 p.27]
- "The crane test load is considered in the crane’s support design." [PSAR_ch06 §6.4.2.2.1 p.27]
- "The OBE is defined as one-third of the safe shutdown earthquake." [PSAR_ch06 §6.4.2.2.2 p.27]
- "Earthquake loads from the operating basis earthquake are evaluated in accordance with Appendix S of 10 CFR Part 50." [PSAR_ch06 §6.4.2.2.2 p.27]
- "The basic wind speed is 110 miles per hour (180 kilometers per hour) for Risk Category III buildings (NCB) and is 115 miles per hour (190 kilometers per hour) for Risk Category IV (RAB, RXB, FHB) buildings in accordance with ASCE 7-16." [PSAR_ch06 §6.4.2.2.2 p.27]
- "Normal wind loading (not including tornado winds) is applied in accordance with ASCE 7-16 and wind load calculations follow procedures outlined in ASCE 7-16." [PSAR_ch06 §6.4.2.2.2 p.27]
- "Wind loads on components and cladding are also applied in accordance with ASCE 7-16." [PSAR_ch06 §6.4.2.2.2 p.27]
- "The SSE for the evaluation of safety-significant structures is described in Section 2.6.2." [PSAR_ch06 §6.4.2.2.3 p.28]
- "The NSRST superstructures are designed for the extreme winter precipitation load of 75 psf in accordance with Interim Staff Guidance DC/COL-ISG-007." [PSAR_ch06 §6.4.2.2.3 p.28]
- "The extreme winter precipitation load is considered as a ground snow load per ASCE 7-16." [PSAR_ch06 §6.4.2.2.3 p.28]
- "Abnormal loadings are considered as applicable for the following cases:" [PSAR_ch06 §6.4.2.2.4 p.28]
- "Internal Flooding Loads (Fa)" [PSAR_ch06 §6.4.2.2.4 p.28]
- "Accident Pressure Loads (Pa)" [PSAR_ch06 §6.4.2.2.4 p.28]
- "Accident Thermal Loads (Ta)" [PSAR_ch06 §6.4.2.2.4 p.28]
- "Accident Pipe Reaction Loads (Ra)" [PSAR_ch06 §6.4.2.2.4 p.29]
- "Pipe Break Loads, subcategorized as:" [PSAR_ch06 §6.4.2.2.4 p.29]
- "Pipe Break Reaction Loads (Yr)" [PSAR_ch06 §6.4.2.2.4 p.29]
- "Pipe Break Jet Impingement Loads (Yj)" [PSAR_ch06 §6.4.2.2.4 p.29]
- "Pipe Break Missile Impact Loads (Ym)" [PSAR_ch06 §6.4.2.2.4 p.29]
- "The loading combinations used for the design of concrete and structural steel of SR substructures, primarily based on ANSI/AISC N690-18 and ACI 349-13, are provided in Table 6.4-11 and Table 6.4-12." [PSAR_ch06 §6.4.2.2.5 p.29]
- "The loading combinations used for the design of the NSRST RAB substructure and the NSRST superstructures are in accordance with IBC-2021 load combinations for strength design or Load and Resistance Factor Design (Section 1605.1 of IBC-2021) as shown below:" [PSAR_ch06 §6.4.2.2.5 p.29]
- "D – Dead Load" [PSAR_ch06 §6.4.2.2.5 p.29]
- "E – determined from ASCE 7-16 or Ess – Combined effect of horizontal and vertical earthquake induced forces as defined in Section 2.3.6 of ASCE 7-16" [PSAR_ch06 §6.4.2.2.5 p.29]
- "Ess – Safe Shutdown Earthquake" [PSAR_ch06 §6.4.2.2.5 p.29]
- "F – Load due to fluids with well-defined pressures and maximum heights" [PSAR_ch06 §6.4.2.2.5 p.29]
- "H – Load due to lateral earth pressures, ground water pressure or pressure of bulk materials" [PSAR_ch06 §6.4.2.2.5 p.29]
- "L – Live Load" [PSAR_ch06 §6.4.2.2.5 p.29]
- "Lr – Roof Live Load" [PSAR_ch06 §6.4.2.2.5 p.30]
- "S – Snow Load" [PSAR_ch06 §6.4.2.2.5 p.30]
- "R – Rain Load" [PSAR_ch06 §6.4.2.2.5 p.30]
- "W – Wind Load" [PSAR_ch06 §6.4.2.2.5 p.30]
- "f1 = 1 (for places of public assembly live loads in excess of 100 psf, and parking garages and 0.5 for other live loads)" [PSAR_ch06 §6.4.2.2.5 p.30]
- "f2 = 0.7 (for roof configurations that do not shed snow off the structure and 0.2 for other roof configurations)" [PSAR_ch06 §6.4.2.2.5 p.30]
- "ACI 318-19 and AISC 360-16 load combinations are used if determined to be more stringent." [PSAR_ch06 §6.4.2.2.5 p.30]
- "NSRST structures are evaluated for extraordinary events such as extreme winter precipitation, tornado missiles, and accidents per building’s functional requirements using load combinations per Table 6.4-7, Table 6.4-8, Table 6.4-11 and Table 6.4-12." [PSAR_ch06 §6.4.2.2.5 p.30]

| 원문 조합식 (IBC-2021 §1605.1) | 출처 |
|---|---|
| 1.4 (D + F) | [PSAR_ch06 §6.4.2.2.5 p.29] |
| 1.2 (D + F) + 1.6 (L + H) + 0.5 (Lr or S or R) | [PSAR_ch06 §6.4.2.2.5 p.29] |
| 1.2 (D + F) + 1.6 (Lr or S or R) + 1.6 H + (f1 L or 0.5 W) | [PSAR_ch06 §6.4.2.2.5 p.29] |
| 1.2 (D + F) + 1.0 W + f1 L + 1.6 H + 0.5 (Lr or S or R) | [PSAR_ch06 §6.4.2.2.5 p.29] |
| 1.2 (D + F) + 1.0E + f1 L + 1.6 H + f2 S | [PSAR_ch06 §6.4.2.2.5 p.29] |
| 0.9 D + 1.0 W + 1.6 H | [PSAR_ch06 §6.4.2.2.5 p.29] |
| 0.9 (D + F) + 1.0 E + 1.6 H | [PSAR_ch06 §6.4.2.2.5 p.29] |

- "The required factors of safety and load combinations for structural stability, such as overturning moments, sliding, and floatation of SR substructure foundations are addressed in Table 6.4-9." [PSAR_ch06 §6.4.2.2.6 p.30]
- "The following minimum factors of safety for structural stability of NSRST substructure are:" [PSAR_ch06 §6.4.2.2.6 p.30]

| 항목 | 출처 |
|---|---|
| Overturning 1.50 | [PSAR_ch06 §6.4.2.2.6 p.30] |
| Sliding 1.10 | [PSAR_ch06 §6.4.2.2.6 p.30] |
| Buoyancy 1.10 | [PSAR_ch06 §6.4.2.2.6 p.30] |

- "Load Combinations and Load Factors for Concrete SR Substructures" [PSAR_ch06 Table 6.4-5 p.61-62]
- "Design Load Cases(1)(5): Load Combination Equation No. in ACI349-13" [PSAR_ch06 Table 6.4-5 p.61-62]
- "Normal and Severe" [PSAR_ch06 Table 6.4-5 p.61-62]
- "Extreme and Abnormal" [PSAR_ch06 Table 6.4-5 p.61-62]
- "Refer to Section 6.4.2.2 for descriptions of individual Design Loads." [PSAR_ch06 Table 6.4-5 Note 1 p.61-62]
- "Refer to Section 6.4.2.2.3 for guidance on consideration of directional effects due to wind pressure and missiles." [PSAR_ch06 Table 6.4-5 Note 2 p.61-62]
- "Load combinations presented above are evaluated with a 0.9 factor on the dead load component to assess the adverse effects of the reduced dead load. For any other load (e.g., Live) if the load reduces the effects of other loads, the corresponding factor for that load is 0.9 of the assigned factors, if it can be demonstrated that the load is always present or occurs simultaneously with the other loads. Otherwise, the factor for that load is zero." [PSAR_ch06 Table 6.4-5 Note 3 p.61-62]
- "The load factor is taken as 1.4 (in lieu of 1.2 in ACI 349-13) in accordance with Regulatory Position 5 in RG 1.142, and 1.2 in RG 1.199." [PSAR_ch06 Table 6.4-5 Note 4 p.61-62]
- "The load combinations presented in this table are more severe than or in direct agreement with ACI 349-13." [PSAR_ch06 Table 6.4-5 Note 5 p.61-62]
- "This load combination and its associated load factors are derived from ACI 349-13, with amendments in accordance with Interim Staff Guidance DC/COL-ISG-007." [PSAR_ch06 Table 6.4-5 Note 6 p.61-62]
- "In accordance with Regulatory Position 5 in RG 1.142, factored and combined as per Yj." [PSAR_ch06 Table 6.4-5 Note 8 p.61-62]
- "The load factor is taken as 1.0 (in lieu of 1.4 in ACI 349-13) in accordance with Regulatory Position 5 in RG 1.142." [PSAR_ch06 Table 6.4-5 Note 9 p.61-62]
- "The load factor is taken as 1.6 (in lieu of 1.2 in ACI 349-13) in accordance with Regulatory Position 5 in RG 1.142." [PSAR_ch06 Table 6.4-5 Note 10 p.61-62]
- "The load factor of 1.6 To is added in accordance with Regulatory Position 5 in RG 1.142." [PSAR_ch06 Table 6.4-5 Note 11 p.61-62]
- "The load factor is taken as 0.8 (in lieu of 1.2 in ACI 349-13) in accordance with Regulatory Position 5 in RG 1.142." [PSAR_ch06 Table 6.4-5 Note 12 p.61-62]
- "The load factor of 0.8 To is added in accordance with Regulatory Position 5 in RG 1.142." [PSAR_ch06 Table 6.4-5 Note 13 p.61-62]
- "The load factor is taken as 1.6 (in lieu of 1.2 in ACI 349-13) in accordance with Regulatory Position 5 in RG 1.142." [PSAR_ch06 Table 6.4-5 Note 14 p.61-62]
- "The load factor of 1.4 Ccr To is added in accordance with Regulatory Position 5 in RG 1.142." [PSAR_ch06 Table 6.4-5 Note 15 p.61-62]
- "The load factor is taken as 1.0 (in lieu of 0.8 in ACI 349-13) in accordance with Regulatory Position 5 in RG 1.142." [PSAR_ch06 Table 6.4-5 Note 16 p.61-62]
- "In ASCE/SEI 7-16, wind loads are consistent with strength-level design; a wind load factor of 1.0 is appropriate (in lieu of 1.6 in ACI 349-13). The basic wind speed for Risk Category III and IV structures in ASCE 7-16 is based on a 1700-year return period and, therefore, does not require the load factor of 1.6" [PSAR_ch06 Table 6.4-5 Note 17 p.61-62]

| 주석 번호 | 짧은 주석 | 출처 |
|---|---|---|
| (7) | Not Used | [PSAR_ch06 Table 6.4-5 Note 7 p.61-62] |

- "Load Combinations and Load Factors for Structural Steel of SR Substructures" [PSAR_ch06 Table 6.4-6 p.63-64]
- "Design Load Cases(1): Load Combination Equation in AISC N690-18" [PSAR_ch06 Table 6.4-6 p.63-64]
- "Normal and Severe" [PSAR_ch06 Table 6.4-6 p.63-64]
- "Extreme and Abnormal" [PSAR_ch06 Table 6.4-6 p.63-64]
- "Refer to Section 6.4.2.2 for descriptions of individual Design Loads." [PSAR_ch06 Table 6.4-6 Note 1 p.63-64]
- "Refer to Seismic Design Criteria for guidance on consideration of seismic orthogonal effects and inclusion of portions of live and snow load in seismic mass." [PSAR_ch06 Table 6.4-6 Note 2 p.63-64]
- "Refer to Section 6.4.2.2.3 for guidance on consideration of directional effects due to wind pressure and missiles." [PSAR_ch06 Table 6.4-6 Note 3 p.63-64]
- "If the Dead Load acts to stabilize the structure against the destabilizing effects of lateral force or uplift, the load factor on Dead Load shall be 0.90 of the assigned factors and that on other gravity loads (e.g., L, Lr, S, Ccr) shall be zero." [PSAR_ch06 Table 6.4-6 Note 4 p.63-64]
- "The load combinations presented in this table are more severe than or in direct agreement with AISC N690-18." [PSAR_ch06 Table 6.4-6 Note 5 p.63-64]
- "This load combination and its associated load factors are derived from AISC N690-18, with amendments per ASCE 7, Section 2.3.3." [PSAR_ch06 Table 6.4-6 Note 6 p.63-64]
- "This load combination and its associated load factors are derived from AISC N690-18, with amendments in accordance with Interim Staff Guidance DC/COL-ISG-007." [PSAR_ch06 Table 6.4-6 Note 7 p.63-64]
- "In accordance with Regulatory Position 5 in RG 1.142, other (non-seismic) hydrodynamic loads are taken as per Yj." [PSAR_ch06 Table 6.4-6 Note 8 p.63-64]
- "This load combination is per AISC N690-18, NB2.5d.(6)." [PSAR_ch06 Table 6.4-6 Note 10 p.63-64]
- "The load factor is taken as 1.6 (in lieu of 0.8 in ANSI/AISC N690-18) in accordance with RG 1.243." [PSAR_ch06 Table 6.4-6 Note 11 p.63-64]
- "The load factor is taken as 1.4 (in lieu of 1.2 in ANSI/AISC N690-18) in accordance with RG 1.243." [PSAR_ch06 Table 6.4-6 Note 12 p.63-64]

| 주석 번호 | 짧은 주석 | 출처 |
|---|---|---|
| (9) | Not Used | [PSAR_ch06 Table 6.4-6 Note 9 p.63-64] |

- "Load Combinations for Extraordinary Events on NSRST Substructure Analysis of Concrete Structures" [PSAR_ch06 Table 6.4-7 p.65-66]
- "Design Load Cases (1)(5): Load Combination Equation No. in ACI 349-13" [PSAR_ch06 Table 6.4-7 p.65-66]
- "Refer to Section 6.4.2.2 for description of individual design loads." [PSAR_ch06 Table 6.4-7 Note 1 p.65-66]
- "Refer to Section 6.4.2.2.3 for discussion of directional effects due to wind pressure and missiles." [PSAR_ch06 Table 6.4-7 Note 2 p.65-66]
- "Load combinations presented above are evaluated with a 0.9 factor on the dead load component to assess the adverse effects of the reduced dead load. For any other load (e.g., live) if the load reduces the effects of other loads, the corresponding factor for that load is 0.9 of the assigned factors, if it can be demonstrated that the load is always present or occurs simultaneously with the other loads. Otherwise, the factor for that load is zero." [PSAR_ch06 Table 6.4-7 Note 3 p.65-66]
- "The load factor is taken as 1.4 (in lieu of 1.2 in ACI 349-13) in accordance with Regulatory Position 5 in RG 1.142, and Section 1.2 in RG 1.199." [PSAR_ch06 Table 6.4-7 Note 4 p.65-66]
- "Load combinations presented in this table are more severe than or in direct agreement with ACI 349-13." [PSAR_ch06 Table 6.4-7 Note 5 p.65-66]
- "This load combination and its associated load factors are derived from ACI 349-13, with amendments per Interim Staff Guidance DC/COL-ISG-007." [PSAR_ch06 Table 6.4-7 Note 6 p.65-66]
- "In accordance with Regulatory Position 5 Table in RG 1.142, factored and combined as per Yj." [PSAR_ch06 Table 6.4-7 Note 9 p.65-66]
- "The load factor is taken as 1.0 (in lieu of 0.8 in ACI 349-13) in accordance with Regulatory Position 5 in RG 1.142." [PSAR_ch06 Table 6.4-7 Note 10 p.65-66]

| 주석 번호 | 짧은 주석 | 출처 |
|---|---|---|
| (7) | Not Used | [PSAR_ch06 Table 6.4-7 Note 7 p.65-66] |
| (8) | Not Used | [PSAR_ch06 Table 6.4-7 Note 8 p.65-66] |

- "Load Combinations for Extraordinary Events on NSRST Substructure Analysis of Steel Structures" [PSAR_ch06 Table 6.4-8 p.67-68]
- "Design Load Cases (1): Load Combination Equation in AISC N690-18" [PSAR_ch06 Table 6.4-8 p.67-68]
- "Refer to Section 6.4.2.2 for descriptions of individual Design Loads." [PSAR_ch06 Table 6.4-8 Note 1 p.67-68]
- "Refer to Section 6.4.2.2.3 for discussion of directional effects due to wind pressure and missiles." [PSAR_ch06 Table 6.4-8 Note 2 p.67-68]
- "If the dead load acts to stabilize the structure against the destabilizing effects of lateral force or uplift, the load factor on dead load is 0.90 of the assigned factors and for other gravity loads (e.g., L, Lr, S, Ccr) is zero." [PSAR_ch06 Table 6.4-8 Note 3 p.67-68]
- "Load combinations presented in this table are more severe than or in direct agreement with AISC N690-18." [PSAR_ch06 Table 6.4-8 Note 4 p.67-68]
- "This load combination and its associated load factors are derived from AISC N690-18, with amendments in accordance with Interim Staff Guidance DC/COL-ISG-007." [PSAR_ch06 Table 6.4-8 Note 5 p.67-68]
- "In accordance with Regulatory Position 5 in RG 1.142, other (non-seismic) hydrodynamic loads are taken as Yj." [PSAR_ch06 Table 6.4-8 Note 6 p.67-68]
- "Load combination is in accordance with AISC N690-18, NB2.5d.(6)." [PSAR_ch06 Table 6.4-8 Note 8 p.67-68]
- "The load factor is taken as 1.4 (in lieu of 1.2 in AISC N690-18) in accordance with RG 1.243." [PSAR_ch06 Table 6.4-8 Note 9 p.67-68]

| 주석 번호 | 짧은 주석 | 출처 |
|---|---|---|
| (7) | Not Used | [PSAR_ch06 Table 6.4-8 Note 7 p.67-68] |

- "Load Factors and Factors of Safety for SR Structural Stability" [PSAR_ch06 Table 6.4-9 p.69]

| Design Load Cases (1) | Design Load Cases (1) | St-1 | St-2 | St-3 | St-4 | St-7 | 출처 |
|---|---|---|---|---|---|---|---|
| Dead | D | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | [PSAR_ch06 Table 6.4-9 p.69] |
| Soil | H | 1.0 | 1.0 | 1.0 | 1.0 |  | [PSAR_ch06 Table 6.4-9 p.69] |
| Wind | W(2) |  | 1.0 |  |  |  | [PSAR_ch06 Table 6.4-9 p.69] |
| Safe Shutdown Earthquake | Ess | 1.0 |  |  |  | 1.0(5) | [PSAR_ch06 Table 6.4-9 p.69] |
| Tornado Wind Pressure | Wtw(2) |  |  | 1.0 | 1.0 |  | [PSAR_ch06 Table 6.4-9 p.69] |
| Tornado - Generated Differential Pressure | Wtp |  |  | 0.5 |  |  | [PSAR_ch06 Table 6.4-9 p.69] |
| Tornado - Generated Missiles | Wtm(2) |  |  | 1.0 |  |  | [PSAR_ch06 Table 6.4-9 p.69] |
| Buoyancy | F’ |  |  |  |  | 1.0 | [PSAR_ch06 Table 6.4-9 p.69] |
| Minimum Factors of Safety | Minimum Factors of Safety | St-1(4) | St-2 | St-3 | St-4 | St-7 | [PSAR_ch06 Table 6.4-9 p.69] |
| Overturning Factor of Safety | 1.1 | 1.5 | 1.1 | 1.1 | -- |  | [PSAR_ch06 Table 6.4-9 p.69] |
| Sliding Factor of Safety | 1.1 | 1.5 | 1.1 | 1.1 | -- |  | [PSAR_ch06 Table 6.4-9 p.69] |
| Floatation Factor of Safety | -- | -- | -- | -- | 1.1 |  | [PSAR_ch06 Table 6.4-9 p.69] |

- "Refer to Section 6.4.2.2 for descriptions of individual design loads." [PSAR_ch06 Table 6.4-9 Note 1 p.69]
- "Refer to Section 6.4.2.2.3 for discussion of directional effects due to wind pressure and missiles." [PSAR_ch06 Table 6.4-9 Note 2 p.69]
- "The overturning factor of safety, sliding factor of safety and Floatation Factor of Safety is 1.5 when OBE is used and 1.1 when SSE is used." [PSAR_ch06 Table 6.4-9 Note 4 p.69]
- "Vertical earthquake uplift is added to buoyancy using SSE." [PSAR_ch06 Table 6.4-9 Note 5 p.69]

| 주석 번호 | 짧은 주석 | 출처 |
|---|---|---|
| (3) | Not Used | [PSAR_ch06 Table 6.4-9 Note 3 p.69] |

- "Load Combinations for Extraordinary Events on NSRST Superstructure Analysis of Concrete Structures" [PSAR_ch06 Table 6.4-11 p.71-72]
- "Design Load Cases (1)(5): Load Combination Equation No. in ACI 349-13" [PSAR_ch06 Table 6.4-11 p.71-72]
- "Refer to Section 6.4.2.2 for descriptions of individual design loads." [PSAR_ch06 Table 6.4-11 Note 1 p.71-72]
- "Refer to Section 6.4.2.2.3 for guidance on consideration of directional effects due to wind pressure and missiles." [PSAR_ch06 Table 6.4-11 Note 2 p.71-72]
- "Load combinations presented are evaluated with a 0.9 factor on the dead load component to assess the adverse effects of the reduced dead load. For any other load (e.g., live) if the load reduces the effects of other loads, the corresponding factor for that load is 0.9 of the assigned factors, if it can be demonstrated that the load is always present or occurs simultaneously with the other loads. Otherwise, the factor for that load is zero." [PSAR_ch06 Table 6.4-11 Note 3 p.71-72]
- "Load factor is 1.4 (in lieu of 1.2 in ACI 349-13) are in accordance with Regulatory Position 5 in RG 1.142, and Section 1.2 in RG 1.199." [PSAR_ch06 Table 6.4-11 Note 4 p.71-72]
- "Load combinations presented in this table are more severe than or in direct agreement with ACI 349-13." [PSAR_ch06 Table 6.4-11 Note 5 p.71-72]
- "This load combination and associated load factors are derived from ACI 349-13, with amendments per Interim Staff Guidance DC/COL-ISG-007." [PSAR_ch06 Table 6.4-11 Note 6 p.71-72]
- "Per Regulatory Position 5 Table in RG 1.142, factored and combined as per Yj." [PSAR_ch06 Table 6.4-11 Note 8 p.71-72]
- "Load factor is 1.0 (in lieu of 0.8 in ACI 349-13) are in accordance with Regulatory Position 5 in RG 1.142." [PSAR_ch06 Table 6.4-11 Note 9 p.71-72]

| 주석 번호 | 짧은 주석 | 출처 |
|---|---|---|
| (7) | Not Used | [PSAR_ch06 Table 6.4-11 Note 7 p.71-72] |

- "Load Combinations for Extraordinary Events on NSRST Superstructure Analysis of Steel Structures" [PSAR_ch06 Table 6.4-12 p.73-74]
- "Design Load Cases (1): Load Combination Equation in AISC N690-18" [PSAR_ch06 Table 6.4-12 p.73-74]
- "Descriptions of individual design loads are provided in Section 6.4.2.2." [PSAR_ch06 Table 6.4-12 Note 1 p.73-74]
- "Refer to Section 6.4.2.2.3 for guidance on consideration of directional effects due to wind pressure and missiles." [PSAR_ch06 Table 6.4-12 Note 2 p.73-74]
- "If the dead load acts to stabilize the structure against the destabilizing effects of lateral force or uplift, the load factor on dead load is 0.90 of the assigned factors and that on other gravity loads (e.g., L, Lr, S, Ccr) are zero." [PSAR_ch06 Table 6.4-12 Note 3 p.73-74]
- "Load combinations presented in this table are more severe than or in accordance with AISC N690-18." [PSAR_ch06 Table 6.4-12 Note 4 p.73-74]
- "Load combination and associated load factors are derived from AISC N690-18, with amendments in accordance with Interim Staff Guidance DC/COL ISG-007." [PSAR_ch06 Table 6.4-12 Note 5 p.73-74]
- "In accordance with Regulatory Position 5 in RG 1.142, other (non-seismic) hydrodynamic loads are Yj." [PSAR_ch06 Table 6.4-12 Note 6 p.73-74]
- "This load combination is per AISC N690-18, NB2.5d.(6)." [PSAR_ch06 Table 6.4-12 Note 8 p.73-74]
- "Load factor is 1.4 (in lieu of 1.2 in AISC N690-18) are in accordance with RG 1.243." [PSAR_ch06 Table 6.4-12 Note 9 p.73-74]

| 주석 번호 | 짧은 주석 | 출처 |
|---|---|---|
| (7) | Not Used | [PSAR_ch06 Table 6.4-12 Note 7 p.73-74] |

| 하중 (원문 행 이름) | 출처 |
|---|---|
| Dead | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Live | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Roof Live | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Snow | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Rain | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Hydrostatic | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Soil | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Pipe Reactions | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Thermal | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Crane | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Wind | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Extreme Winter Precipitation Event | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Operating Earthquake | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Safe Shutdown Earthquake | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Tornado Wind Pressure | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Tornado - Generated Differential Pressure | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Tornado - Generated Missiles | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Accident Internal Flooding | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Accident Pressure | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Accident Thermal | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Accident Pipe Reactions | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Accident Pipe Break Reactions | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Accident Pipe Break Jet Impingement | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Accident Pipe Break Missile Impact | [PSAR_ch06 Table 6.4-5 p.61-62] |
| Atmospheric Ice, Self-weight | [PSAR_ch06 Table 6.4-6 p.63-64] |
| Atmospheric Ice, Concurrent Wind Loading | [PSAR_ch06 Table 6.4-6 p.63-64] |
| Soil (not applicable for steel structures) | [PSAR_ch06 Table 6.4-6 p.63-64] |

## 해설
Normal load는 고정하중, 활하중, 지붕 활하중, 적설, 착빙, 토압, 강우, 부력, 정수압, 열하중, 배관반력, 크레인하중으로 이루어진다. 콘크리트와 강재의 설계 밀도는 각각 150 pounds per cubic foot과 490 pounds per cubic foot이고, 관통 슬리브나 벽 지지 계통을 대표하는 균일 고정하중 20 pounds per square foot을 콘크리트 벽에 적용한다. 활하중에는 지붕과 상부 바닥 층의 보·거더·슬래브에 대해 최대 모멘트·전단을 주는 위치에 4,000 pound-force 집중하중을 쓰고, 승강기와 기계류의 활하중은 충격을 고려해 20 percent에서 100 percent까지 증가시킨다. NSRST%%t:NSRST%% 상부구조의 지붕 활하중은 20 psf, 지상 적설하중은 35 psf, 착빙하중은 공칭 두께 0.25-inch에 동시 풍속 50 miles per hour, 착빙 밀도 56 pounds per cubic foot 이상이다. 구조 안정성 점검에 쓰는 지하수위는 완성 부지 표고 아래 15 feet이다. 크레인의 최대 바퀴하중은 25 percent 증가시키고, 종방향·횡방향 힘은 정격용량 합의 10 percent와 20 percent로 계산한다.

Severe environmental load는 Operating Basis Earthquake%%t:OBE%%와 풍하중이다. OBE%%t:OBE%%는 Safe Shutdown Earthquake%%t:SSE%%의 3분의 1로 정의하고 `10 CFR Part 50` Appendix S에 따라 평가한다. 기본 풍속은 `Risk Category III`인 `NI` Control Building에 110 miles per hour, `Risk Category IV`인 Reactor Auxiliary Building·Reactor Building·Fuel Handling Building에 115 miles per hour이다. Extreme environmental load에는 Safe Shutdown Earthquake%%t:SSE%%와 `DC/COL-ISG-007`에 따른 extreme winter precipitation load 75 psf가 들어가고, 같은 절의 토네이도 하중은 [[Natrium_Tornado_Winter_Precipitation_Design]]이 다룬다. Abnormal load는 내부 침수, 사고 압력, 사고 열하중, 사고 배관반력, 그리고 배관 파단에 따른 반력·제트 충돌·비산물 충격의 일곱 가지다.

SR%%t:SR%% 하부구조의 콘크리트·강재 조합은 Table 6.4-11과 Table 6.4-12에 있다고 본문이 적지만, 표 제목이 가리키는 내용과 견주면 이 교차참조는 원문의 결함이다. 두 표는 NSRST%%t:NSRST%% 상부구조의 extraordinary events 조합을 담는다. 원문 오기는 고치지 않았다. NSRST%%t:NSRST%% Reactor Auxiliary Building 하부구조와 상부구조는 `IBC-2021` §1605.1의 Load and Resistance Factor Design 조합 일곱 개를 쓰고, `ACI 318-19`·`AISC 360-16`의 조합이 더 엄격하면 그쪽을 쓴다. extraordinary events, 곧 extreme winter precipitation, 토네이도 비산물, 사고는 건물의 기능 요건에 따라 Table 6.4-7, Table 6.4-8, Table 6.4-11, Table 6.4-12의 조합으로 평가한다.

표의 주석은 조합 계수를 어떤 규정이 바꾸었는지 적는다. `ACI 349-13`의 계수를 `RG 1.142` Regulatory Position 5에 따라 1.2에서 1.4나 1.6으로, 0.8에서 1.0으로 바꾼 경우가 반복되고, 강재 표에서는 `RG 1.243`에 따라 `ANSI/AISC N690-18`의 계수를 바꾼다. 풍하중 계수는 `ASCE/SEI 7-16`의 풍속이 1700-year return period 기반이므로 1.6 대신 1.0을 쓴다. 고정하중이 안정화에 기여하면 그 계수를 0.90배로 낮추고 다른 중력하중의 계수는 `zero`가 된다. 구조 안정성의 최소 안전율은 NSRST%%t:NSRST%% 하부구조에서 전도 1.50, 활동 1.10, 부력 1.10이고, SR%%t:SR%% 하부구조에서는 OBE%%t:OBE%%를 쓰면 1.5, Safe Shutdown Earthquake%%t:SSE%%를 쓰면 1.1이다. Table 6.4-9는 최소 안전율 값이 St- 머리보다 한 열 왼쪽에 인쇄되어 있어 열 대응이 어긋나 있고, Table 6.4-8은 Accident Thermal 행에 기호와 계수가 없으며 Accident Pipe Break Missile Impact 행이 없다. 둘 다 원문 인쇄 상태이며 고치지 않았다. 조합별 계수 행렬은 원문 표에 있고 이 노트는 하중 행 이름과 기호만 옮긴다.

## 관련 문서
- [[Natrium_Safety_Significant_Structures]]
- [[Natrium_Tornado_Winter_Precipitation_Design]]
- [[Natrium_Design_Basis_Hazard_Levels]]
- [[Natrium_Seismic_Analysis_Methods]]
- [[PSAR_ch06]]
