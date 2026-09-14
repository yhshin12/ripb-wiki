# PSAR_ch03 — refclean chapter hook report (2026-09-11)

**Status: DONE_WITH_CONCERNS** (all brief items fixed and PDF-checked; concerns are minor and listed in §5).

Document: Kemmerer Unit 1 PSAR Chapter 3, Licensing Basis Events (132 pp.).
Output: `references/TP_Natrium_PSAR2025_ch3_Licensing Basis Events.md` (built with figures; `Fig_3.5-1.png`, 659,835 B).

## 1. Files touched

| File | Change |
|---|---|
| `scripts/refclean/profiles/psar_ch03.py` | new; `STEPS` = 15 element-level steps (below) |
| `scripts/refclean/tests/test_psar_ch03.py` | new; 17 tests (6 synthetic unit tests, 11 smoke tests on the built output and the PDF) |
| `scripts/refclean/patches/PSAR_ch03.json` | not created: every class-C item is implemented as an element-level step with an explicit anchor check, so no text patch is required |

No core module was edited.

## 2. Implemented steps (order of `STEPS`) and PDF evidence

| # | Step | What it does | Evidence |
|---|---|---|---|
| 1 | `drop_invisible_periods` | deletes the 6 lone `.` paragraphs | 2.0-pt Arial `.` at x = 18 pt, p97, p100, p103 (2 each) |
| 2 | `merge_captioned_sheets` | drops `(Sheet n of m)` body lines; merges the caption-less next sheet into Table 3.1-1 (13 rows) and Table 3.5-4 (28 rows) | p15-16, p60-61 |
| 3 | `fix_hazard_tables` | Table 3.1-2 label `Individual Hazards - Qualitatively Screened Out` (the ` -` is a separate PDF word dropped by the converter), `(continued)` removed; defensive fill-down of 3.1-2 col 1 and 3.1-3 `Analysis` | p17-22 (rendered) |
| 4 | `fix_dba_summary` | Table 3.5-4: checks the 5th header `DBA 30-day Low Population Zone Boundary TEDE (rem)`; defensive fill-down of DBA ID/title/doses; `Secondary-to-Primary` (line-end hyphen) | p60-61 (rendered) |
| 5 | `fix_bdbe_note` | Table 3.5-3 note `\*Denotes high-consequence BDBE` (literal asterisk escaped) | p59 |
| 6 | `source_term_tables` | Tables 3.2-1…3.2-18: one header row `Isotope | 2hr | …`; subtitle line `Cumulative Activity Release to Environment (Ci)` under the caption; Tables 3.2-4/-5/-6 get a leading `Release` column (`Plenum Release` / `Non-Plenum Release`, verbatim labels); sheet 2 of Table 3.2-4 merged (40 rows) | p25-43; p28-29 rendered |
| 7 | `move_initial_conditions_table` | Low/Full Power table moved directly after "…used in the LBE analyses:" (3.3.4.2) | p50 |
| 8 | `reorder_lbe_subsections` | 3.8.1.11 (OTH-LMAC-4) and 3.8.2.6 (IPI-IHEL-2): x.1 LBE Description + its paragraph, then x.2 Radiological Consequences + its paragraph | p87, p89 (rendered) |
| 9 | `relocate_lbe_tables` | within 3.6–3.9, the i-th "… are listed below." sentence of kind k (frequency / 30-day EAB TEDE / enveloping DBA dose; kind judged on the whole sentence) receives the i-th mini-table of kind k, placed directly after the paragraph that holds the sentence; multi-row mini-tables are first split into one-row tables; the step refuses (warning, order unchanged) if counts differ | PDF: every table follows its paragraph on the same page (p77 rendered: the DL3-RR10 sentences stay in the paragraph before the table) |
| 10 | `promote_missed_headings` | 3.12.3, 3.14.2.2, 3.14.2.3 promoted (rule: whole item/para = `N title`, parent emitted, identical PDF line at the page margin) | p124, p130 |
| 11 | `split_glued_references` | `… stage. References` (3.11) and `… TP-LIC-RPT-0011. References` (3.13) split; entries become list items → `References (3.11)`, `References (3.13)` | p120, p126 |
| 12 | `criticality_block` | 3.14.2 block rebuilt from the review §5-4 answer block (re-checked on rendered p127-129): two intro paragraphs, `k<sub>eff</sub> + 2σ < USL (Equation 3.14-1)`, `USL = 1 + bias – σ<sub>bias</sub> – Δ<sub>SM</sub> – Δ<sub>AOA</sub> (Equation 3.14-2)`, 4 "Where," bullets; symbols restored in 3 later sentences; 5 orphan symbol lines deleted | p127-129 |
| 13 | `join_split_paragraphs` | page-break halves (`… assumed to occur` + `2.5 days after …` p65-66; `… out of the` + `HAA is assumed …` p105-106) and `(Reference 3.11-1)`, `(Reference 3.14-3/-5/-6)` continuations joined | p65-66, p105-106, p120, p128 |
| 14 | `symbol_subscripts` | `keff` → `k<sub>eff</sub>` (9×), `F<sub>ΔH</sub>`, `F<sub>Z</sub>`, `F<sub>XY</sub>` | 7.7-pt subscript spans p122, p127-131 |
| 15 | `fix_list_markers` | `● Heat removal exceeds …` → list item; nested `- Peak Power`, `- Minimum Power` lose the duplicated dash | p50, p9 |

## 3. Brief items — result

| Item | Result |
|---|---|
| 1 (H) LBE mini-tables | Confirmed still wrong before the hook (29 displaced + 2 pairs merged into one table by the core sheet merger: RRS-CGR-CN+RRS-ISPL-CN p112, RRS-SPLX-CN+RRS-SPLA-CN p113). After the hook: sentences/tables freq 45/45, dose 34/34, DBA 9/9; the (kind, values, innermost section) sequence of all 88 tables equals the PDF sequence extracted from p63-118 (test `test_lbe_tables_follow_pdf`; the same test on a build without the step gives 31 mismatches). All 106 LBE sections carry exactly one table per announced kind. RRS-SPLX-CN (3.9.4.3) shows 8.13E-02 / 2.78E-01 rem; DHS-ISTL-2 frequency 1.05E-03/3.02E-03/7.45E-03 sits in 3.7.2.2. |
| 2 (H) Table 3.5-4, 3.1-2, 3.1-3 | LPZ header present (re-conversion); 28 rows, 21 DBA IDs, no empty cell; the 7 row-spanned DBE rows filled (DHS-ISTL-2, DHS-RNBK-3, RFH-ESWR-1, RFH-FDIV-1, RFH-FDIV-3, RRS-CGR-1, RRS-RWG-2). Table 3.1-2: 110 rows, labels 90/10/10 as in the PDF; Table 3.1-3: 34 rows, `Analysis` filled (e.g. Sodium Fire → internal-fire text). |
| 3 Source-term tables | 18 tables, single header row, subtitle line; Tables 3.2-4/-5/-6 with `Release` column (3.2-4: 16 Plenum + 24 Non-Plenum rows; 3.2-5 I-131 2hr = 1.22E+00 Plenum vs 4.71E+00 Non-Plenum). All values unchanged. |
| 4 §3.14 block | Replaced; answer block matches the rendered PDF (p128 shows "(σ)" in the sentence, both equation numbers right-aligned on the equation lines, 4 bullets). |
| 5 Order/noise | Initial-conditions table under 3.3.4.2; 3.8.1.11 / 3.8.2.6 order fixed; 6 stray periods removed; LBE titles: all 106 LBE headings end with their `(ID)` (already complete in the core output; guarded by a test). |
| 6 Keep repeats | PDF = output counts: "The fuel performance acceptance criteria are satisfied." 51, "are listed below." 88, "This is the most limiting DBE that mapped to the" 20, DL3-RR10 sentence 9; identical-value tables kept (2.27E-03/5.75E-03/9.37E-03 ×2, 1.00E+01/1.40E+01/2.10E+01 ×3). Source typos kept (`RFH-FDSP-CN DBA The 5th`, `NEI 12-16.The`, `IAC, (IPI-IHEL-1)`, `K-effective 1.0`). |

Review §1 H items F1-F9: F1-F6 and F8 fixed here; F7 (exponents: `1E-03`, `1E-02 per plant-year`, `5E-07 … 1E-04`, `1E-02/plant-year`) and F9 (3.8.3.8 RPD-SS-4 heading) were already correct in the core output (verified in the build).

## 4. Verification

- Build: `python scripts/clean_references.py --only PSAR_ch03 --verify` (with figures): no failed patches, no unmatched headings/subheads, no orphan captions, residue `{}`.
- Headings: whitelist 455, emitted 458 (= 455 + the 3 promoted in step 10; review outline count 458); 7 `References (3.x)` headings.
- Bag of words: PDF 32,754 tokens, missing 18 (0.05 %), all explained: `keff` 9, `fz` 1, `fxy` 1 (subscript markup splits the token), `continued` 2 (sheet-repeat suffix removed from Table 3.1-2 labels), `list` + `3.5-10` (List of Figures, D4), `content` + `of-application` + `secondary-to` (PDF line-end hyphen tokenisation; the output holds the complete words `Content-of-Application`, `Secondary-to-Primary`).
- `pages_with_missing_gt3` = 5 (p19, p20, p59, p6, p128): window artefacts only — merged multi-sheet tables sit under the first sheet's page anchor (p19/p20/p59), LoF p6, and the `k<sub>eff</sub>` tokens on p128.
- Page anchors: 116, strictly increasing; pages without an own anchor are continuation sheets of merged tables (p16, 18-20, 22, 29, 56, 58-59, 61).
- Tests: `python -m pytest scripts/refclean/tests -q` → 58 passed (17 in `test_psar_ch03.py`).

## 5. Concerns / remaining issues

1. Step warnings are stored in `doc.meta['ch03_warnings']`, which `clean_references.py` does not print; the tests assert the outcomes instead. Optional core patch: in `scripts/clean_references.py::build`, add `"warnings": [w for k, v in doc.meta.items() if k.endswith("_warnings") for w in v]` to `report`.
2. Core behaviours worked around locally (optional core patches, not required for ch3):
   - `structure.attach_captions_and_merge` merges any two adjacent caption-less tables with identical headers, including two different tables on the same page (the ch3 DBA mini-tables). Guard proposal: merge only if `t.pages[0] > prev_tab.table.pages[-1]`.
   - `pdfaux.numbered_headings` inspects only the first line of each PyMuPDF block, so headings that share a block with preceding list items are missed (ch3: 3.12.3, 3.14.2.2, 3.14.2.3). Proposal: test every block line that sits at the body margin.
3. Not done (review L/optional): `LBE: <ID>` label per mini-table (F30; LBE identity comes from the heading path), Figure 3.5-1 alt text with axis names (F23, class C), Rev. 1 change bars (D7: not restored), the 4 numbered PDC-26 items render as `- 1. …` bullets.
4. The p112→p113 page break inside 3.9.4.3.2 leaves two paragraphs ("… pipe segment." / "The mechanistic source term evaluates …"); the text is verbatim and the first part ends a sentence, so it was not joined.
