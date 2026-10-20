---
type: source
key: RG_1.232
title: Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors
file: references/RG_1.232_Guidance for Developing Principal Design Criteria for Non-Light-Water
  Reactors.md
pdf: references/raw/RG_1.232_Guidance for Developing Principal Design Criteria for
  Non-Light-Water Reactors.pdf
sha256_pdf: 8eaa6f99f55366d362a8503b20e2190140677fecd8258a4faf9da8adaf04b985
sha256_md: 20bdb90917a36e2c25c2dd91b808c4a565e5c3a36c088dbd6b58bf747051bfe6
pdf_pages: 133
build:
  converter: opendataloader-pdf 2.5.7 (markdown_page_separator=<!-- page %page-number%
    -->, image_output=external, image_format=png, content_safety_off=off-page, detect_strikethrough=True)
  cleaned: scripts/clean_references.py (refclean 0.1.0) 2026-10-20
  missing_pct: 0.74
ingest: complete
units:
- unit: §A-C, Table 1, Appendix B (SFR-DC)
  status: complete
- unit: Appendix C (MHTGR-DC, Criteria 1-72); Appendix A not ingested by user decision
  status: complete
---

# Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors (RG_1.232)

> [!abstract] 요약
> `RG 1.232`는 non-light-water reactor의 principal design criteria%%t:PDC%% 개발 지침이다. `10 CFR Part 50` Appendix A의 general design criteria%%t:GDC%%를 신형로에 맞추어 적응한 advanced reactor design criteria를 본문과 부록 A에, sodium-cooled fast reactor%%t:SFR%% 기준을 부록 B에, modular high-temperature gas-cooled reactor 기준을 부록 C에 담고, Table 1이 세 기준 집합의 대조표를 준다.

## 서지
- 키: `RG_1.232`
- 원문: `references/raw/RG_1.232_Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors.pdf`

## 구조
<!-- sync:begin -->
- PDF 쪽 수: 133
- 인쇄 쪽: p1-28 = 1..27; p29-61 = A-1..A-33; p62-103 = B-1..B-42; p104-133 = C-1..C-30
- 표 (5):
  - Table 1: Non-Light-Water-Reactor Crosswalk
  - Acronyms/Abbreviations
  - Appendix A table: ARDC (criterion records)
  - Appendix B table: SFR-DC (criterion records)
  - Appendix C table: MHTGR-DC (criterion records)
- 그림 (0):
- 비공개 (0):
<!-- sync:end -->

## 알려진 모순
- SFR-DC 35: 표 1은 상태를 `Same as ARDC`로 적지만, 부록 B 조문에는 같은 번호의 ARDC 조문에 없는 단일 고장 가정 문단이 있다. [[SFR_DC_Residual_Heat_Removal_And_ECC]]
- SFR-DC 56: 근거는 reactor라는 말을 지웠다고 적지만, 조문에는 reactor containment structure가 남아 있다. [[SFR_DC_Reactor_Containment]]

## 관련 문서
- [[Principal_Design_Criteria_Non_LWR]]
- [[Non_LWR_Design_Criteria_Crosswalk]]
- [[SFR_DC_Overall_Requirements]]
- [[SFR_DC_Reactor_Design_And_Coolant_Boundary]]
- [[SFR_DC_Electric_Power_And_Control_Room]]
- [[SFR_DC_Protection_Systems]]
- [[SFR_DC_Reactivity_Control]]
- [[SFR_DC_Primary_Coolant_Boundary]]
- [[SFR_DC_Residual_Heat_Removal_And_ECC]]
- [[SFR_DC_Containment_Heat_Removal_And_Cleanup]]
- [[SFR_DC_Structural_And_Equipment_Cooling]]
- [[SFR_DC_Reactor_Containment]]
- [[SFR_DC_Fuel_And_Reactivity_Control]]
- [[SFR_DC_Intermediate_Coolant_System]]
- [[SFR_DC_Sodium_Specific_Criteria]]
- [[SFR_DC_Primary_Coolant_And_Cover_Gas]]
- [[MHTGR_DC_Overall_Requirements]]
- [[MHTGR_DC_Reactor_Design_And_Functional_Containment]]
- [[MHTGR_DC_Electric_Power_And_Control_Room]]
- [[MHTGR_DC_Reactivity_Control]]
- [[MHTGR_DC_Heat_Transport_Systems]]
- [[MHTGR_DC_Reactor_Containment_Not_Applicable]]
- [[MHTGR_DC_Fuel_And_Radioactivity_Control]]
- [[MHTGR_DC_Reactor_Building_Criteria]]
