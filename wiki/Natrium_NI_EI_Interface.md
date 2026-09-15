---
type: natrium
aliases: []
sources: [PSAR_ch01]
status: checked
verified: 2026-09-16
term:
tags: [natrium]
terms_pending: []
---
# Nuclear Island와 Energy Island의 interface (Nuclear Island and Energy Island Interface)

> [!abstract] 요약
> Kemmerer Unit 1의 Nuclear Island와 Energy Island는 가능한 한 서로 독립적으로 기능하도록 설계되고, 두 island는 열을 옮기고 저장하는 Nuclear Island Salt System으로 물리적으로 연결된다. Energy Island의 Structures, Systems, and Components%%t:SSC%%는 모두 Non-Safety-Related with No Special Treatment%%t:NST%%로 분류되며, Nuclear Island 경계 조건은 이 interface가 안전해석에 영향을 주지 않도록 설계되었다고 적는다.

## 원문 사실
- "The IHT transports reactor heat from the intermediate heat exchangers to the Nuclear Island (NI) Salt System (NSS) via sodium-salt heat exchangers, which transport heat to the Energy Island (EI) hot salt storage tank for thermal energy storage." [PSAR_ch01 §1.1.3 p.19]
- "The NI, which contains the reactor and its supporting systems, is designed to function as independently as possible from the EI, which contains the thermal energy storage tanks, steam generator, feedwater system, condenser, turbine, and supporting EI systems." [PSAR_ch01 §1.1.3 p.20]
- "The EI is physically connected to the NI by the NSS that transports heat between the islands and stores excess thermal energy, providing a buffer that allows steam generation and thermal energy storage operations (e.g., ramp rates) to be independent from reactor power operations as described in “Regulatory Management of Natrium Nuclear Island and Energy Island Design Interfaces,” (Reference 1.1-1)." [PSAR_ch01 §1.1.3 p.20]
- "The EI structures, systems, and components (SSCs) are classified as non-safety-related with no special treatment (NST)." [PSAR_ch01 §1.1.3 p.20]
- "As described in Reference 1.1-1, the NI boundary conditions have been intentionally designed so the interface with the EI does not impact the Kemmerer Unit 1 safety analysis." [PSAR_ch01 §1.1.4.2 p.28]
- "All EI systems and functions described in the following sections are classified as NST." [PSAR_ch01 §1.1.4.2 p.28]
- "Cold salt from the TSS cold salt storage flows through the ESS to NSS cold salt piping via the ESS cold salt transfer pumps, across the EI and NI boundary, to the IHT SHXs." [PSAR_ch01 §1.1.4.2.1 p.28]
- "The NSS isolation valves outside of the RAB form the boundary between the NSS and ESS systems." [PSAR_ch01 §1.1.4.2.1 p.29]
- "The NSS to ESS to TSS to SGS systems form the salt loop that transfers heat from the NI to the EI." [PSAR_ch01 §1.1.4.2.1 p.29]
- "The EI facilities support thermal energy storage and steam generation plant operations that are independent from reactor power operations due to the TSS as described in NATD-LIC-RPRT-0001." [PSAR_ch01 §1.1.4.4.9 p.39]
- "The independence of plant operations between the EI SSCs and the NI SSCs is a key aspect of the plant design philosophy." [PSAR_ch01 §1.1.4.4.9 p.39]
- "The NI boundary conditions have been intentionally designed so the interrelationship with the EI does not impact the NI safety analysis." [PSAR_ch01 §1.1.4.4.9 p.39]
- "Thus, the EI facilities provide appropriate housing for EI systems and components used to supply energy to the grid while maintaining isolation from any events impacting NI safety functions associated with reactivity control, core cooling, or containing the release of radioactivity." [PSAR_ch01 §1.1.4.4.9 p.39]
- "TerraPower, LLC, “Regulatory Management of Natrium Nuclear Island and Energy Island Design Interfaces,” NATD-LIC-RPRT-0001-A, Revision 0, Accession No. ML24011A321." [PSAR_ch01 §1.1 References p.40]

## 해설
Nuclear Island는 원자로와 그 지원 계통을 담고, Energy Island는 열에너지 저장 탱크, 증기 발생기, 급수 계통, 복수기, 터빈과 지원 계통을 담으며, Nuclear Island는 Energy Island와 가능한 한 독립적으로 기능하도록 설계된다. 두 island의 물리적 연결은 island 사이에 열을 옮기고 남는 열에너지를 저장하는 Nuclear Island Salt System이다. 이 계통은 Intermediate Heat Transport System에서 sodium-salt heat exchanger를 거쳐 열을 받아 Energy Island의 고온 염 저장 탱크로 보내며, 완충을 제공해 증기 생산과 열에너지 저장 운전(예: ramp rate)이 원자로 출력 운전과 독립적일 수 있게 한다. 이 설계 interface의 규제 관리는 TerraPower의 `NATD-LIC-RPRT-0001-A` 보고서에 기술된다.

Energy Island의 SSC%%t:SSC%%는 NST%%t:NST%%로 분류되고, `Secondary Systems and Components` 절(`§1.1.4.2`)도 이어지는 절에 기술된 모든 Energy Island 계통과 기능을 NST%%t:NST%%로 분류한다. 경계 조건에 관한 문장은 두 곳에 있다. 한 곳은 Energy Island와의 interface가 Kemmerer Unit 1 안전해석에 영향을 주지 않도록 Nuclear Island 경계 조건을 의도적으로 설계했다고 적고, 다른 곳은 Energy Island와의 상호관계가 Nuclear Island 안전해석에 영향을 주지 않도록 설계했다고 적는다.

염 루프는 `NSS`, `ESS`, `TSS`, `SGS` 순으로 이어져 Nuclear Island에서 Energy Island로 열을 옮긴다. 저온 염은 `TSS` 저온 저장에서 `ESS` 저온 염 이송 펌프로 `NSS` 저온 염 배관을 지나 island 경계를 넘어 Intermediate Heat Transport System의 sodium-salt heat exchanger로 가고, `RAB` 밖의 `NSS` 격리 밸브가 `NSS`와 `ESS`의 경계를 이룬다. Energy Island 시설은 `TSS` 덕분에 원자로 출력 운전과 독립적인 열에너지 저장과 증기 생산 운전을 지원하며, 두 island SSC%%t:SSC%% 사이 운전의 독립성은 발전소 설계 철학의 핵심 측면의 하나이다. Energy Island 시설은 전력망 공급에 쓰는 계통과 기기를 수용하면서, 반응도 제어, 노심 냉각, 방사능 방출 격납과 관련된 Nuclear Island 안전 기능에 영향을 주는 사건과의 격리를 유지한다.

Energy Island 시설 절은 보고서를 `NATD-LIC-RPRT-0001`로, 참고문헌 목록은 `NATD-LIC-RPRT-0001-A`, `Revision 0`로 적는다.

## 관련 문서
- [[Natrium_Plant_Overview]]
- [[Natrium_SSC_Safety_Classification]]
- [[SSC_Safety_Classification]]
- [[PSAR_ch01]]
