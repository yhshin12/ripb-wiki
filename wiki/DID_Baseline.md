---
type: concept
aliases: []
sources:
- NEI_18-04
status: checked
verified: 2026-09-15
term: null
tags: []
terms_pending: []
---

# 심층방어 baseline의 평가와 변경 관리 (Baseline Evaluation of Defense-in-Depth)

> [!abstract] 요약
> 심층방어(Defense-in-Depth)%%t:DID%% 적절성 평가는 설계가 성숙함에 따라 되풀이되며, 불확실도와 compensatory action%%t:COMPENSATORY_ACTION%%의 적절성을 함께 검토한다. 통합 설계 과정을 처음 완전히 거칠 때 baseline 평가를 수행해 관리 문서에 기록하고, 이후의 변경은 네 가지 질문으로 선별해 하나라도 해당하면 모든 attribute를 다시 평가한다.

## 원문 사실
- "Because the design, safety analyses, and PRA will be developed in phases and in an iterative fashion, the DID adequacy evaluation and baseline, including compensatory action selection and sufficiency, is updated as the design matures." [NEI_18-04 §5.5 p.68]
- "The evaluation of DID adequacy requires recurring examination of the design as it matures and thus recurring consideration of the three questions in the risk triplet: 1) What can go wrong? 2) How likely is it? and 3) What are the consequences?" [NEI_18-04 §5.9.4 p.85]
- "This should be done at the natural design phase review points as specific engineering information is “baselined” for the next design phase." [NEI_18-04 §5.9.4 p.85]
- "In the reviews, hazards analysis updates, PRA updates, DBA safety analysis, and plant-level risk profiles (e.g., LBEs identified, changes in margins or uncertainties, or layers of defense features, human performance assumptions, etc.) should be explicit components of the review and decision to continue to the next engineering phase." [NEI_18-04 §5.9.4 p.85]
- "The scope and level of detail of the PRA will evolve as the level of design and site information matures." [NEI_18-04 §5.9.4 p.85]
- "Relative risk and reliability analyses should be developed in advance of the full PRA, as they provide very valuable inputs to design functionality requirements as well as early means to resolve operational challenges." [NEI_18-04 §5.9.4 p.85]
- "It is during this period of the design development that basic decisions on layers of defense that comprise a portion of the DID strategy are best formulated, documented, and evaluated in appropriate design descriptions at plant and system levels." [NEI_18-04 §5.9.4 p.85]
- "The greatest number of uncertainties exist in the beginning of the design cycle and are resolved systematically through the iterative design process." [NEI_18-04 §5.9.4 p.85]
- "Those are state-of-knowledge uncertainties that are transient in nature; they are unverified assumptions that are worked out over the design process and sometimes beyond." [NEI_18-04 §5.9.4 p.85]
- "During design phase reviews, the DID evaluation should examine significant assumptions or features that could materially alter plant or individual LBE risk profiles, and it should determine whether there are single features that are risk-significant that would benefit from additional compensatory actions to improve performance capability or performance assurance." [NEI_18-04 §5.9.4 p.85]
- "Permanent uncertainties are typically broken down into two groups: those that are caused by variability or randomness, such as plant performance, and those that are results of gaps in knowledge." [NEI_18-04 §5.9.4 p.86]
- "DID adequacy evaluations should include both types of permanent uncertainties in reaching a final design adequacy conclusion." [NEI_18-04 §5.9.4 p.86]
- "Attention in the evaluation of DID adequacy is paid to hazards excluded from the PRA that could either pose on-site risks to personnel or plant performance and those that could pose risks to the public due to significant non-radiological consequences." [NEI_18-04 §5.9.4 p.86]
- "DID adequacy evaluations will examine the nominal performance of the plant against various risk objectives." [NEI_18-04 §5.9.4 p.86]
- "Evaluations will also include quantified uncertainties for PRA-derived LBEs in two ways—frequency uncertainty and consequence uncertainty." [NEI_18-04 §5.9.4 p.86]
- "DID adequacy evaluations should include the necessity, scope, and sufficiency of existing design and operational programs being applied to a design or portion of a design." [NEI_18-04 §5.9.4 p.86]
- "Specific consideration should be given to the RIPB capabilities of each program type to provide meaningful contributions to risk reduction or performance assurance based on the risk significance of SSCs associated with each LBE." [NEI_18-04 §5.9.4 p.86]
- "Particular attention should be paid to the number of layers of defense that are associated with IEs that can progressively cascade to the point of challenging public safety objectives." [NEI_18-04 §5.9.4 p.86]
- "Initiating events that cannot cascade to a point of threating public health should be found acceptable with fewer layers of defense than events that have the potential to release large amounts of radiation." [NEI_18-04 §5.9.4 p.86]
- "For risk-significant BDBEs, the evaluation should take into account both the magnitude of the consequences and the time frame for actions in determining the need for or choice of compensatory actions." [NEI_18-04 §5.9.4 p.86]
- "Where dose predictions fall below regulatory limits, the availability of programmatic actions to mitigate those events should be considered over more sweeping changes to plant design to eliminate the BDBE which could be impractical to implement or excessively burdensome." [NEI_18-04 §5.9.4 p.86]
- "Small changes to the design that improve the likelihood of successful actions should be considered in the light of the stage of design development attained." [NEI_18-04 §5.9.4 p.86]
- "For any BDBE that exceeds regulatory siting limits, if practical, design changes should be considered over reliance on emergency planning programmatic DID alone." [NEI_18-04 §5.9.4 p.86]
- "As illustrated in Figure 5-4, there will be a number of iterations through the integrated design process to reflect different design development phases and the feedback loops indicated in Figure 5-2 in which the DID evaluation leads to changes in the plant design to enhance the plant capability DID or changes to the protective measures reflected in the programmatic DID." [NEI_18-04 §5.9.5 p.86]
- "Like many other licensing basis topics, changes in physical, functional, operational, or programmatic features require consideration of the potential for reduction of DID before proceeding." [NEI_18-04 §5.9.5 p.86]
- "This requires that a current baseline for DID be available as a reference for change evaluation." [NEI_18-04 §5.9.5 p.86]
- "These changes in turn require revisions to the PRA and all the subsequent tasks in the integrated design process." [NEI_18-04 §5.9.5 p.86]
- "The first complete pass through the integrated design process will require a baseline DID evaluation which completes the actions during execution of the IDP." [NEI_18-04 §5.9.5 p.86]
- "The baseline DID evaluation will be documented in sufficient detail so it can be efficiently updated in future design development iterations." [NEI_18-04 §5.9.5 p.86]
- "The checklists in Table 5-9 and Table 5-10 will serve as a reminder as to the scope of the evaluation which will be recorded in a controlled document." [NEI_18-04 §5.9.5 p.86]
- "The documentation of the DID baseline should be derived from the design records, primarily those that verified that the attributes described previously were adequate." [NEI_18-04 §5.9.6 p.87]
- "The development of the baseline should support and complement existing change control requirements such as 10 CFR 50.59 where the impact on DID is considered." [NEI_18-04 §5.9.6 p.87]
- "The threshold for evaluating a change to the DID baseline should be informed by the risk significance of changes in LBE performance in the PRA." [NEI_18-04 §5.9.6 p.87]
- "Does the change introduce a new LBE for the plant?" [NEI_18-04 §5.9.6 p.87]
- "Does the change increase the risk of LBEs previously considered to be of no/low risk significance to the point that it will be considered risk-significant after the change is made?" [NEI_18-04 §5.9.6 p.87]
- "Does the change reduce the number of layers of defense for any impacted LBEs or materially alter the effectiveness of an existing layer of defense?" [NEI_18-04 §5.9.6 p.87]
- "Does the change significantly increase the dependency on a single feature relied on in risk-significant LBEs?" [NEI_18-04 §5.9.6 p.87]
- "If the answer to any of the above questions is yes, a complete evaluation of all of the DID attributes is performed." [NEI_18-04 §5.9.6 p.88]
- "As a result of the more comprehensive evaluation of DID changes, the IDP will reject the change or recommend additional compensatory actions to plant capability or programmatic capability, if practical, to return a baseline LBE performance to within the current DID baseline." [NEI_18-04 §5.9.6 p.88]
- "If the compensatory actions are not effective, the change may require NRC notification in accordance with current license and regulatory requirements." [NEI_18-04 §5.9.6 p.88]
- "The evaluation of DID adequacy should be documented in two parts, quantitative and qualitative, covering the DID attributes established above." [NEI_18-04 §5.9.6 p.88]
- "The purpose is to explain how margins are established between the frequencies and consequences of individual LBEs and the F-C Target used to evaluate the risk significance of LBEs." [NEI_18-04 §5.9.6 p.88]
- "Additionally, qualitative evaluation of DID adequacy is performed for each LBE." [NEI_18-04 §5.9.6 p.88]
- "Adequate qualitative DID is provided when a qualitative evaluation determines that observable attributes of the design demonstrate the conservative principles supporting DID and are, in combination, sufficient." [NEI_18-04 §5.9.6 p.88]
- "The conclusion is reached through an integrated decision-making process." [NEI_18-04 §5.9.6 p.88]
- "For each iteration of the design evaluation lifecycle in Figure 5-4, the DID evaluation from the baseline will be re-evaluated based on a review to determine which programmatic or plant capability attributes have been affected for each layer of defense." [NEI_18-04 §5.9.7 p.88]
- "Changes that impact the definition and evaluation of LBEs, safety classification of SSCs, or risk significance of LBEs or SSCs will need to have the DID adequacy re-evaluated and the baseline updated as appropriate." [NEI_18-04 §5.9.7 p.88]

| LBE IE Series Name | Functional: Margin Adequacy | Functional: Multiple Protective Measures | Functional: Prevention and Mitigation Balance | Physical: Functional Reliability | Physical: No Single Feature Relied Upon | 출처 |
|---|---|---|---|---|---|---|
| Normal Operation | √ | √ |  | √ |  | [NEI_18-04 Table 5-9 p.87] |
| AOOs | √ | √ |  | √ |  | [NEI_18-04 Table 5-9 p.87] |
| DBEs | √ | √ | √ | √ | √ | [NEI_18-04 Table 5-9 p.87] |
| BDBEs | √ | √ | √ | √ | √ | [NEI_18-04 Table 5-9 p.87] |
| DBAs | √ | √ | √ | √ | √ | [NEI_18-04 Table 5-9 p.87] |

| LBE IE Series Name | Quality/Reliability: Design, Manufacturing, Construction, O&M | Compensation for Uncertainties: Human Errors | Compensation for Uncertainties: Mechanical Failures | Compensation for Uncertainties: Unknowns | Emergency Response Capability | 출처 |
|---|---|---|---|---|---|---|
| Normal Operation | √ | √ | √ | √ |  | [NEI_18-04 Table 5-10 p.87] |
| AOOs | √ | √ | √ | √ |  | [NEI_18-04 Table 5-10 p.87] |
| DBEs | √ | √ | √ | √ | √ | [NEI_18-04 Table 5-10 p.87] |
| BDBEs | √ | √ | √ | √ | √ | [NEI_18-04 Table 5-10 p.87] |
| DBAs | √ | √ | √ | √ | √ | [NEI_18-04 Table 5-10 p.87] |

## 해설
설계, 안전해석, PRA는 단계적·반복적으로 개발되므로, compensatory action%%t:COMPENSATORY_ACTION%%의 선정과 충분성을 포함한 심층방어%%t:DID%% 적절성 평가와 baseline은 설계가 성숙함에 따라 갱신된다. 적절성 평가는 설계를 되풀이해 검토하므로 risk triplet의 세 질문, 즉 무엇이 잘못될 수 있는지, 그 가능성이 얼마인지, 결말이 무엇인지를 되풀이해 고려한다. 원문은 이를 특정 공학 정보가 다음 설계 단계를 위해 baseline으로 확정되는 자연스러운 설계 단계 검토 시점에 수행하고, 재해 분석 갱신, PRA 갱신, Design Basis Accident%%t:DBA%% 안전해석, 발전소 수준 위험 프로파일을 검토와 다음 공학 단계 진행 결정의 명시적 구성 요소로 삼아야 한다고 적는다. 지식 상태 측면에서 PRA의 범위와 상세 수준은 설계·부지 정보와 함께 발전하며, 상대적 위험·신뢰도 분석은 설계 기능 요건과 운전상 문제의 조기 해결에 매우 유용한 입력이므로 완전한 PRA보다 먼저 개발해야 한다. 심층방어%%t:DID%% 전략의 일부인 Layers of Defense%%t:LAYERS_OF_DEFENSE%%에 관한 기본 결정은 이 초기 설계 시기에 발전소·계통 수준 설계 기술서에서 정식화·문서화·평가하는 것이 가장 좋다.

불확실도는 설계 주기 초기에 가장 많고 반복 설계를 거치며 체계적으로 해소된다. 이는 일시적인 state-of-knowledge 불확실도로, 설계 과정에서, 때로는 그 이후에 해결되는 검증되지 않은 가정이다. 설계 단계 검토에서 평가는 발전소나 개별 Licensing Basis Event%%t:LBE%% 위험 프로파일을 크게 바꿀 수 있는 가정이나 특성을 검토하고, 추가 compensatory action%%t:COMPENSATORY_ACTION%%으로 성능 능력이나 성능 보증을 높일 수 있는 risk-significant 단일 특성이 있는지 판단해야 한다. 영구 불확실도는 발전소 성능 같은 변동성·무작위성에서 오는 것과 지식 격차에서 오는 것 두 부류로 나뉘며, 최종 설계 적절성 결론에는 두 부류를 모두 포함해야 한다. PRA에서 제외된 재해 가운데 작업자나 발전소 성능에 부지 내 위험을 줄 수 있는 것과, 비방사선학적 결말이 커서 공중에 위험을 줄 수 있는 것에도 주의를 기울인다. 적절성 평가는 발전소의 공칭 성능을 여러 위험 목표와 비교하고, PRA에서 도출한 LBE%%t:LBE%%의 정량화된 불확실도를 빈도 불확실도와 결말 불확실도라는 두 방식으로 포함한다.

compensatory action%%t:COMPENSATORY_ACTION%%의 적절성에 관해, 적절성 평가는 설계나 그 일부에 적용되는 기존 설계·운전 프로그램의 필요성, 범위, 충분성을 포함해야 하며, 각 LBE%%t:LBE%%와 관련된 Structures, Systems, and Components%%t:SSC%%의 risk significance에 따라 프로그램 유형마다 위험 저감이나 성능 보증에 의미 있게 기여할 risk-informed and performance-based%%t:RIPB%% 능력을 구체적으로 고려해야 한다. 공공 안전 목표를 위협할 만큼 연쇄 진행할 수 있는 Initiating Event%%t:IE%%에 몇 개의 층이 연관되는지에 특히 주의하며, 공중 보건을 위협할 만큼 연쇄 진행할 수 없는 IE%%t:IE%%는 대량의 방사선을 방출할 수 있는 사건보다 적은 층으로도 수용될 수 있다. risk-significant Beyond Design Basis Event%%t:BDBE%%에서는 결말의 크기와 조치에 쓸 수 있는 시간을 함께 고려해 compensatory action%%t:COMPENSATORY_ACTION%%의 필요와 선택을 정한다. 선량 예측이 규제 한계 아래이면 실행이 비현실적이거나 부담이 과도할 수 있는 광범위한 설계 변경보다 그 사건을 완화하는 프로그램 조치를 우선 고려하고, 조치 성공 가능성을 높이는 작은 설계 변경은 도달한 설계 진척 단계에 비추어 고려한다. 규제 부지 한계를 넘는 BDBE%%t:BDBE%%에는 실행 가능하면 비상계획 차원의 Programmatic Defense-in-Depth%%t:PROGRAMMATIC_DID%%에만 의존하기보다 설계 변경을 고려해야 한다.

그림 5-4처럼 통합 설계 과정은 설계 개발 단계와 그림 5-2의 되먹임 고리를 반영해 여러 번 반복되며, 그 과정에서 심층방어%%t:DID%% 평가는 Plant Capability Defense-in-Depth%%t:PLANT_CAPABILITY_DID%%를 높이는 설계 변경이나 Programmatic Defense-in-Depth%%t:PROGRAMMATIC_DID%%에 반영된 protective measure%%t:PROTECTIVE_MEASURE%%의 변경으로 이어진다. 다른 인허가 기준 주제처럼, 물리적·기능적·운전·프로그램 특성의 변경은 진행 전에 심층방어%%t:DID%% 저하 가능성을 검토해야 한다. 이를 위해 변경 평가의 기준이 되는 현행 baseline이 있어야 하며, 이런 변경은 PRA와 통합 설계 과정의 후속 과업 전부의 개정을 요구한다. 통합 설계 과정을 처음 완전히 거칠 때 integrated decision-making process%%t:IDP%% 수행 중의 조치를 완료하는 baseline 평가가 필요하고, 이 평가는 이후 설계 반복에서 효율적으로 갱신할 수 있을 만큼 상세하게 문서화한다. 표 5-9와 표 5-10의 점검표는 관리 문서에 기록할 평가 범위를 상기시키는 역할을 한다. 표 5-9는 정상 운전, Anticipated Operational Occurrence%%t:AOO%%, Design Basis Event%%t:DBE%%, BDBE%%t:BDBE%%, DBA%%t:DBA%%별로 여유 적절성, 다중 protective measure%%t:PROTECTIVE_MEASURE%%, 예방·완화 균형, 기능 신뢰도, 단일 특성 비의존의 적용을 표시하며, 정상 운전과 AOO%%t:AOO%%에는 예방·완화 균형과 단일 특성 비의존 표시가 없다. 표 5-10은 품질·신뢰도, 인적 오류·기계적 고장·미지 요소에 대한 불확실도 보상, 비상 대응 능력을 같은 구분별로 표시하며, 정상 운전과 AOO%%t:AOO%%에는 비상 대응 능력 표시가 없다.

baseline 문서는 설계 기록, 주로 앞서 설명한 attribute가 적절함을 검증한 기록에서 도출하며, 심층방어%%t:DID%% 영향을 고려하는 10 CFR 50.59 같은 기존 변경 관리 요건을 뒷받침하고 보완해야 한다. baseline 변경을 평가할 문턱은 PRA에서 LBE%%t:LBE%% 성능 변화의 risk significance를 근거로 정해야 한다. 원문은 변경이 발전소에 새 LBE%%t:LBE%%를 도입하는지, 위험이 없거나 낮던 LBE%%t:LBE%%를 risk-significant로 만드는지, 영향받는 LBE%%t:LBE%%의 층 수를 줄이거나 기존 층의 효과를 크게 바꾸는지, Risk-Significant LBE%%t:RS_LBE%%에서 단일 특성 의존을 크게 늘리는지를 묻고, 하나라도 해당하면 모든 attribute를 완전히 평가한다. 그 결과 IDP%%t:IDP%%는 변경을 거부하거나, 실행 가능하면 LBE%%t:LBE%% 성능을 현행 baseline 안으로 되돌리는 추가 compensatory action%%t:COMPENSATORY_ACTION%%을 권고한다. 조치가 효과적이지 않으면 변경은 현행 인허가·규제 요건에 따라 NRC 통보가 필요할 수 있다.

적절성 평가는 정량과 정성 두 부분으로 문서화한다. 정량 부분은 개별 LBE%%t:LBE%%의 빈도·결말과 Frequency-Consequence Target%%t:FC_TARGET%% 사이의 여유를 정하는 방법을 설명하고, 정성 평가는 LBE%%t:LBE%%마다 수행한다. 설계의 관찰 가능한 attribute가 심층방어%%t:DID%%를 뒷받침하는 보수적 원칙을 보여 주고 결합해 충분하다고 정성 평가가 판단하면 정성적 심층방어%%t:DID%%가 적절하며, 이 결론은 IDP%%t:IDP%%로 내린다. 그림 5-4의 설계 평가 수명 주기를 반복할 때마다 층별로 어떤 프로그램·발전소 능력 attribute가 영향을 받았는지 검토해 baseline의 평가를 재평가하며, LBE%%t:LBE%% 정의·평가, SSC%%t:SSC%% 안전 분류, LBE%%t:LBE%%나 SSC%%t:SSC%%의 risk significance에 영향을 주는 변경은 적절성을 재평가하고 필요하면 baseline을 갱신해야 한다.

## 관련 문서
- [[DID_Adequacy_Framework]]
- [[Integrated_Decision_Making_Process]]
- [[DID_Integrated_Process]]
- [[DID_Risk_Margins]]
- [[Programmatic_DID]]
- [[NEI_18-04]]
