---
type: natrium
aliases: []
sources: [PSAR_ch03, RG_1.253]
status: checked
verified: 2026-09-16
term:
tags: [natrium, lbe]
terms_pending: []
---
# Natrium 재해 선별 (Natrium Hazard Screening)

> [!abstract] 요약
> Kemmerer Unit 1의 재해 선별은 `RG 1.247`의 재해 목록을 포함한 적용 재해 전체를 대상으로 `ASME/ANS RA-S-1.4-2021`의 일반 선별 기준을 쓰고 공존 재해와 cliff edge effects%%t:CLIFF_EDGE_EFFECT%%를 검토한다. 남은 재해 가운데 지진과 강풍은 design basis hazard level을 construction permit%%t:CP%% 신청에 credit하되 operating license%%t:OL%% 단계의 PRA로 확인하며, 내부 화재와 내부 침수 PRA는 OL%%t:OL%% 단계에 제공된다.

## 원문 사실
- "A hazard screening analysis has been performed for all applicable hazards, which includes all hazards identified in Tables B-1 and B-2 of RG 1.247." [PSAR_ch03 §3.1.1.5 p.9]
- "The hazard screening for at-power operation and low-power shutdown uses the generic screening criteria specified in ASME/ANS RA-S-1.4-2021 and examines coexistent hazards and cliff-edge effects." [PSAR_ch03 §3.1.1.5 p.9]
- "Table 3.1-2 summarizes the hazards that screened out of the at-power operation PRA and low-power shutdown PRA." [PSAR_ch03 §3.1.1.5 p.9]
- "Table 3.1-3 summarizes the hazards that are addressed by detailed PRA or design basis hazard levels (DBHLs)." [PSAR_ch03 §3.1.1.5 p.9]
- "No adjustments are made to the PRA and uncertainty assessments to address the bounding site characterizations and structure, system, or component (SSC) fragilities based on the DBHLs described in Section 6.1.1" [PSAR_ch03 §3.1.1.15 p.13]
- "Determination of whether an IE can be caused by chemical hazards is considered in the internal and external hazards screening discussed in Section 3.1.1.5." [PSAR_ch03 §3.1.1.7 p.11]
- "NEI 21‑07, Revision 1, Section 6.1.1 clarified NEI 18‑04 by defining and using the term DBHL rather than DBEHL." [RG_1.253 §A.3.7 p.34]
- "Specifically, DBHLs address both traditional external hazards (e.g., seismic events, external floods, high winds) and internal hazards (e.g., internal fires, internal floods, turbine missiles, and high energy line breaks)." [RG_1.253 §A.3.7 p.34]

| Hazard | Analysis | 출처 |
|---|---|---|
| Dropped/Collapsing/Falling Loads | Dropped/Collapsing/Falling Loads are selected for inclusion in the Internal Events PRA | [PSAR_ch03 Table 3.1-3 p.21-22] |
| High Air Temperature | High Air Temperature requires additional analysis and will be included in the PRA, as necessary | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Volcanic Phenomena – Supervolcano Eruption | Volcanic hazards are assessed in Section 4-9 of NAT-3226-A, Revision 0A (Reference 3.1-7), which are incorporated by reference into Section 2.7. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Volcanic Phenomena and Extreme Snow (including snowstorm) | Volcanic hazards are assessed in Section 4-9 of NAT-3226-A, Revision 0A (Reference 3.1-7), which are incorporated by reference into Section 2.7. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Volcanic Phenomena and Earthquake | Volcanic hazards are assessed in Section 4-9 of NAT-3226-A, Revision 0A (Reference 3.1-7), which are incorporated by reference into Section 2.7. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Earthquakes, Seismic Events/Hazards | The seismic DBHL is credited for the CPA, but seismic hazards are selected for seismic PRA development. Efficacy of the DBHL will be confirmed with the seismic PRA at the OL stage | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Explosion after Pipeline Accident Within the Site | The seismic DBHL is credited for the CPA, but seismic hazards are selected for seismic PRA development. Efficacy of the DBHL will be confirmed with the seismic PRA at the OL stage | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Explosion Within Plant | The seismic DBHL is credited for the CPA, but seismic hazards are selected for seismic PRA development. Efficacy of the DBHL will be confirmed with the seismic PRA at the OL stage | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Explosion Within the Site | The seismic DBHL is credited for the CPA, but seismic hazards are selected for seismic PRA development. Efficacy of the DBHL will be confirmed with the seismic PRA at the OL stage | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Soil Liquefaction | The seismic DBHL is credited for the CPA, but seismic hazards are selected for seismic PRA development. Efficacy of the DBHL will be confirmed with the seismic PRA at the OL stage | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Internal Fire | The internal fire hazards are selected for fire PRA development. The fire PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Explosion after Pipeline Accident Within the Site | The internal fire hazards are selected for fire PRA development. The fire PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Explosion Within Plant | The internal fire hazards are selected for fire PRA development. The fire PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Explosion Within the Site | The internal fire hazards are selected for fire PRA development. The fire PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Explosive Electrical Faults | The internal fire hazards are selected for fire PRA development. The fire PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Fire from Cask Transporter, on-site materials | The internal fire hazards are selected for fire PRA development. The fire PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Non-Safety Building Fire | The internal fire hazards are selected for fire PRA development. The fire PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Sodium Fire | The internal fire hazards are selected for fire PRA development. The fire PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Standby Diesel Generator on-site | The internal fire hazards are selected for fire PRA development. The fire PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Extreme Winds | The high winds DBHL is credited for the CPA, but high winds hazards are selected for high winds PRA development. Efficacy of the DBHL will be confirmed with the high winds PRA at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Strong Wind | The high winds DBHL is credited for the CPA, but high winds hazards are selected for high winds PRA development. Efficacy of the DBHL will be confirmed with the high winds PRA at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Cyclones (hurricanes, tornadoes, and tropical typhoons) | The high winds DBHL is credited for the CPA, but high winds hazards are selected for high winds PRA development. Efficacy of the DBHL will be confirmed with the high winds PRA at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Extreme Air Pressure (High/Low Gradient) | The high winds DBHL is credited for the CPA, but high winds hazards are selected for high winds PRA development. Efficacy of the DBHL will be confirmed with the high winds PRA at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Strong Winds and Extreme air pressure | The high winds DBHL is credited for the CPA, but high winds hazards are selected for high winds PRA development. Efficacy of the DBHL will be confirmed with the high winds PRA at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Strong Winds and Ice barriers | The high winds DBHL is credited for the CPA, but high winds hazards are selected for high winds PRA development. Efficacy of the DBHL will be confirmed with the high winds PRA at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Strong Winds and Extreme rain | The high winds DBHL is credited for the CPA, but high winds hazards are selected for high winds PRA development. Efficacy of the DBHL will be confirmed with the high winds PRA at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Strong Winds and Snow Drift | The high winds DBHL is credited for the CPA, but high winds hazards are selected for high winds PRA development. Efficacy of the DBHL will be confirmed with the high winds PRA at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Tornadoes and Extreme hail | The high winds DBHL is credited for the CPA, but high winds hazards are selected for high winds PRA development. Efficacy of the DBHL will be confirmed with the high winds PRA at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Internal Flood | The internal flooding hazards are selected for internal flooding PRA development. The internal flooding PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Pipe Failure Effects | The internal flooding hazards are selected for internal flooding PRA development. The internal flooding PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Pipe Whip | The internal flooding hazards are selected for internal flooding PRA development. The internal flooding PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Steam Release | The internal flooding hazards are selected for internal flooding PRA development. The internal flooding PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Spray | The internal flooding hazards are selected for internal flooding PRA development. The internal flooding PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |
| Jet Effects | The internal flooding hazards are selected for internal flooding PRA development. The internal flooding PRA will be available at the OL stage. | [PSAR_ch03 Table 3.1-3 p.21-22] |

| Screening Category | Hazard | 출처 |
|---|---|---|
| Individual Hazards - Qualitatively Screened Out | Abrasive Dust and Sandstorms | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Air Pollution | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Animals | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Argon Gas Leak | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Avalanche | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Biological Agents | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Biological Events, Biological phenomena in water (plants, marine growth), including biological contamination, Organic Material in Water | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Biological phenomena in air (insects, leaves), including biological contamination | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Blast (pressure wave, not a chemical explosion) inside building | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Chemical Release after Pipeline Accident | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Chemical Release after Pipeline Accident Within the Site | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Chemical Release after Transportation Accident | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Chemical Release Outside Site | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Chemical Release to Water | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Chemical Release Within the Site, Release of Chemicals from On-Site Storage | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Collision of ships and floating debris with water intakes | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Corrosion (e.g., from salt water) | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Direct Impact from Ship Collision | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Drought | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Eddy currents into ground | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Electromagnetic interference from off-site and on-site / Electromagnetic disturbance / Magnetic Disturbance | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Excavation Work – External to the Site Boundary | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Explosion After Pipeline Accident | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Explosion Outside Plant | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | External Fire | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Extreme Hail | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Extreme Rain / Intense Precipitation | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Extreme Snow (including snowstorm) | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Extreme snowpack | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Failure of a Dam Upstream of the Plant | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Fire generated from off-site sources | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Fog | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Forest Fire | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Frazil Ice | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Grass Fire (Off-Site) | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Grass Fire (On-Site) | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Ground Contamination | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Ground Washout | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Groundwater related effects | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | High Sea/River Water Level (e.g. high tide) | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | High Sea/River Water Temperature | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | High Tide | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Ice Barriers | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Ice Storm / sub-cooled rain | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Industrial or Military Facility Accident | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Internal Fire Spreading from Other Units on the Site | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Internal Flood and Harsh Environment Spreading from Other Units on the Site | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Internal missiles (from explosions, ruptures, collapses, dropping, high energy rotating machinery) | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Land Rise | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Landslide (above water) | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Lightning | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Low Air Temperature | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Low Sea/River/Lake Water Level | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Low Sea/River/Lake Water Temperature | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Marine Accidents, Ship Impact | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Missiles from Military Activity | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Missiles from other installations; Externally generated missiles | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Missiles from Other Units on the Site | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Mist | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Multi-Unit Issues | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Radioactive releases | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Railroad Accident | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Release of Corrosive Gases or Liquids from Off-Site Storage | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Release of Hazardous Gas (Asphyxiant, Toxic) from Off-Site Storage | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Release of Hazardous Gas (Asphyxiant, Toxic) from On-Site Storage, Toxic Gas | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Release of Hazardous/Corrosive Gases or Liquids from On-Site Storage | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Release of toxic gas inside plant | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | River Diversion | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | River transported material | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Salt Storm | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Seiche | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Shockwave from Transformer Explosion | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Sinkholes, Karsts | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Snow (drift) | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Soil Erosion, Coastal Erosion | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Soil Frost | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Soil shrink-swell consolidation | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Solid or Fluid (non-gaseous) Impurities from Ship Release | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Storm Surge | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Strong Water Current (underwater erosion) | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Structural Collapse | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Surface Ice, Ice Cover | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Truck Accident (Off-Site), Vehicle Impact (Off-Site) | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Tsunami | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Turbine-Generated Missiles | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Underwater Landslide | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Vibrations, Ground vibration (e.g., due to nearby explosions) | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Water currents during a Flood | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | Waves, Other Extraordinary Waves | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Qualitatively Screened Out | White Frost | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Coexistent Hazards - Qualitatively Screened Out | Chemical release and Contamination from chemicals | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Coexistent Hazards - Qualitatively Screened Out | Drought and External fire | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Coexistent Hazards - Qualitatively Screened Out | Drought and Low water level | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Coexistent Hazards - Qualitatively Screened Out | Explosion after pipeline accident and Chemical release after pipeline accident | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Coexistent Hazards - Qualitatively Screened Out | Explosion after transportation accident and Chemical release after transportation accident | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Coexistent Hazards - Qualitatively Screened Out | Explosion outside plant and Chemical release outside or inside site | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Coexistent Hazards - Qualitatively Screened Out | Extreme rain and Lightning | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Coexistent Hazards - Qualitatively Screened Out | Extreme snow (including snowstorm) and Earthquake | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Coexistent Hazards - Qualitatively Screened Out | High air temperature and High water temperature | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Coexistent Hazards - Qualitatively Screened Out | Low air temperature and Low water temperature | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Quantitatively Screened Out | Aircraft Crash, Aircraft Impact, Aviation Accident, Jet Impact | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Quantitatively Screened Out | Direct Impact of Heavy Transportation Within the Site | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Quantitatively Screened Out | Excavation Work Within the Site Area | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Quantitatively Screened Out | External Flooding | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Quantitatively Screened Out | Meteorite | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Quantitatively Screened Out | Orbital Debris | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Quantitatively Screened Out | Explosion after Transportation Accident, Vehicle/Ship Explosion (Off-Site) | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Quantitatively Screened Out | Vehicle Impact (On-Site), Truck Accident (On-Site) | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Quantitatively Screened Out | Vehicle/Ship Explosion (On-Site) | [PSAR_ch03 Table 3.1-2 p.17-20] |
| Individual Hazards - Quantitatively Screened Out | Volcanic Phenomena - Small Volcano Eruption | [PSAR_ch03 Table 3.1-2 p.17-20] |

## 해설
재해 선별은 `RG 1.247`의 두 재해 표에 있는 재해를 모두 포함하는 적용 재해 전체에 대해 수행되었고, 출력 운전과 저출력 정지에 대해 `ASME/ANS RA-S-1.4-2021`의 일반 선별 기준을 쓰며 공존 재해와 cliff edge effects%%t:CLIFF_EDGE_EFFECT%%를 검토한다. 화학 재해가 Initiating Event%%t:IE%%를 일으킬 수 있는지도 이 선별에서 다룬다.

선별 제외 표는 개별 재해의 정성 선별, 공존 재해의 정성 선별, 개별 재해의 정량 선별로 나뉜다. 정량 선별로 제외된 재해에는 항공기 충돌, 부지 내 중량물 운송 충돌, 부지 내 굴착, 외부 홍수, 운석, 궤도 잔해, 운송 사고 뒤 폭발, 부지 내 차량 충돌과 폭발, 소형 화산 분화가 있다. 정성 선별로 제외된 공존 재해에는 극한 강설과 지진, 고온 공기와 고온 수온 같은 조합이 있다.

분석으로 넘어가는 재해 표에서 낙하·붕괴 하중은 내부 사건 PRA에 포함되고, 고온 공기는 추가 분석을 거쳐 필요하면 PRA에 포함되며, 화산 현상은 참조 포함된 부지 보고서에서 평가된다. 지진, 부지 내와 발전소 내 폭발, 토양 액상화 행은 seismic design basis hazard level을 CP%%t:CP%% 신청에 credit하되 지진 PRA 개발 대상으로 선정해 OL%%t:OL%% 단계에서 그 효능을 확인한다고 적고, 극한 바람, 강풍, 사이클론, 극한 기압과 강풍 조합 행은 high winds design basis hazard level을 같은 방식으로 다룬다. 내부 화재, 소듐 화재, 폭발성 전기 결함, 부지 내 대기 디젤 발전기 같은 행은 화재 PRA 개발 대상이고, 내부 침수, 배관 파손 영향, pipe whip, 증기 방출, spray, jet effects 행은 내부 침수 PRA 개발 대상이며, 두 PRA는 OL%%t:OL%% 단계에 제공된다. 부지 내와 발전소 내 폭발 행은 지진 행과 화재 행에 모두 나온다.

이 보고서는 design basis hazard levels로 정한 부지 특성과 Structures, Systems, and Components%%t:SSC%% 취약도를 반영하려고 PRA와 불확실도 평가를 조정하지는 않는다고 적는다. 이 용어가 NEI 18-04의 Design Basis External Hazard Level%%t:DBEHL%%과 같은 개념인지는 이 노트가 인용한 원문에 없다. [[RG_1.253]]은 NEI 21-07 Revision 1의 Section 6.1.1이 DBEHL%%t:DBEHL%% 대신 design-basis hazard level%%t:DBHL%%이라는 용어를 정의해 써서 NEI 18-04를 명확히 했다고 적고, DBHL%%t:DBHL%%이 지진·외부 침수·강풍 같은 전통적 외부 hazard와 내부 화재·내부 침수 같은 내부 hazard를 모두 다룬다고 적는다. 이 보고서의 design basis hazard levels가 DBHL%%t:DBHL%%과 같은 것인지도 이 노트가 인용한 원문에는 없다.

## 관련 문서
- [[Natrium_PRA_Scope]]
- [[Non_LWR_PRA_Scope]]
- [[Required_Safety_Function]]
- [[PSAR_ch03]]
- [[RG_1247_Hazard_List]]
- [[RG_1253_CP_PRA_Acceptability]]
- [[Natrium_SER_DBHL_Review]]
- [[Natrium_SER_PRA_Review]]
