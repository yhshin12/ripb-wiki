# PSAR_ch06 report — Kemmerer Unit 1 PSAR Chapter 6 (Task 9d)

Status: DONE_WITH_CONCERNS (every dispatch item and every H item of `review_ch6` is fixed and verified against the
PDF; the concerns are core-side and are listed in §6).

Files created (ownership per brief): `scripts/refclean/profiles/psar_ch06.py` (11 steps),
`scripts/refclean/patches/PSAR_ch06.json` (1 patch: the λ block, the only class C item of this chapter),
`scripts/refclean/tests/test_psar_ch06.py` (8 unit tests on synthetic input + 7 checks on the real document).
Regenerated: `references/TP_Natrium_PSAR2025_ch6_Safety-Significant SSC Criteria and Capabilities.md` (1,872 lines),
`references/raw/_verify/PSAR_ch06.json`. No figure PNGs: the chapter has no body figure (the three cover rasters are
decorative and are removed with the cover page), so the final run with figures produces no
`references/figures/PSAR_ch06/` directory.

## 1. Steps in `psar_ch06.STEPS` (in run order)

| Step | What it does | Evidence (PDF page) | Review item |
|---|---|---|---|
| `missing_headings` | Re-runs `pdfaux.numbered_headings` with the document body margin (72 pt) instead of the per-page modal x0 and promotes the headings the core whitelist missed: 6.1.1.4.2, 6.1.1.5 (p6), 6.4.1.3, 6.4.1.3.1 (p16), 6.4.2.2.5 (p29). Then retries the subheadings left unmatched because their heading was still glued to them — "SR Substructure Loading Combinations". Added refs go into `aux.headings`, so `--verify` compares 74 against 74. | p6, p16, p29 | #5, #6, #7 |
| `nested_dash_items` | Items whose text starts with a dash bullet (`- for systems with single supports, and`) lose the dash and nest one level under the preceding item (5 places: p17 ×2, p29 ×3; p48 ×2 keep their depth). | p17, p29, p48 (render) | #21 |
| `drop_sheet_labels` | Removes the stand-alone `(Sheet n of 2)` paragraphs left by the header band (p59, 60, 65, 66, 67, 68, 71, 72, 73, 74). | — | #14, #19 |
| `load_combination_tables` | Rebuilds Tables 6.4-5/-6/-7/-8/-11/-12 from pdfplumber: both sheets parsed, the 3-level header (group / load case / equation) flattened to one row, span cells filled right, the empty leading column of 6.4-12 dropped, the symbol column recombined (`W (2)`+`tw` → `Wtw (2)`, `L`+`r` → `Lr`, `Y (8)`+`j` → `Yj (8)`), sheet 2 appended without its repeated header, notes re-extracted from the PDF text lines of the last sheet page and attached to the table. Attribution is by PDF page only (61–62, 63–64, 65–66, 67–68, 71–72, 73–74); the bold caption line of both sheet pages must start with `Table <id> ` or the step raises. Every cell is compared with the opendataloader grid (`odl_diff`). | p61–68, p71–74 | #1, #2, #3, #14, #15 |
| `stability_table_notes` | Table 6.4-9: the five notes printed `(1)Refer …` are re-extracted from the PDF lines, normalised to `(1) Refer …` and attached to the table (they were separate paragraphs). | p69 | #3 |
| `merge_regulatory_guide_sheets` | Table 6.4-4: sheet 2 (no caption, identical header) is appended to sheet 1 once the sheet label is gone → 8 rows, one header. | p59–60 | #2, #14 |
| `seismic_classification_cells` | Table 6.4-1B: the sub-bullets nested inside the cell lists (dropped by the core cell reader) are restored from the opendataloader JSON — 13 lines, e.g. `Maximum Considered Earthquake Ground Motion1 ≥ SSE`, `Seismic Risk Category IV`, `Importance Factor, I = 1.5`. The footnote row `1 See Section 6.4.1.2.3` becomes the table note `<sup>1</sup> See Section 6.4.1.2.3`. | p55 (render) | #12, #16 |
| `glued_note_markers` | Table-note superscripts extracted glued to the word become `<sup>n</sup>`, but only for (word, digit) pairs attested as a superscript span on that table's page: `Motion1` ×3 (p55), `Wind3`, `Protection2` ×2, `Yes1` ×2, `FHB2` ×3, `RAB2` ×3 (p77, after fill-down) = 14 replacements. | p55, p77 (PyMuPDF spans) | #12 |
| `formula_blocks` | IBC-2021 combinations one per line (7 items, split before `1.4 (`/`1.2 (`/`0.9 (`/`0.9 D`); the symbol legend as a list (12 entries D, E, Ess, F, H, L, Lr, S, R, W, f1, f2 — the E entry keeps its embedded `or Ess – …` verbatim); the cracked-section properties as 4 lines and their 10 definitions as a list under `Where`. Each block is rewritten only when the split yields exactly the expected count (7 / 12 / 4 / 10), recorded in `doc.meta['ch6_formulas']`. | p29–30, p32–33 | #11 |
| `transient_titles` | The 30 design-transient titles (A.1–A.11, B.1–B.9, C.1–C.2, D.1–D.2, Test 1–6) become subheadings. Their parent, the underlined `Service Level X Conditions` / `Test Conditions`, is H6 (6.4.3.1.1 is H5), so the titles are deeper than H6 and are written as bold paragraphs, per the spec's heading rule. | p39–44 | #8 |
| `source_notes` | HTML comments `<!-- source: … -->` at the seven source defects (§4). No value is changed, moved or inserted. | p17, p29, p33–34, p64, p68, p69, p78 | #4 |

The patch file holds the λ block only: the text layer of p33 scatters the equation (`λ V f = ---`, `Where λ V f`,
`= The wavelength`, …); the rendered page prints λ = V over f followed by three definitions, transcribed as
`λ = V / f` + `Where` + three list items (wording verbatim, the fraction written `V / f`).

## 2. Dispatch items — result

| # | Item | Result |
|---|---|---|
| 1 | Load-combination tables: every cell compared with pdfplumber; 3-level header flattened; `C-9` vs `C-9(6)`; page attribution; notes complete and attached | Done. 522 non-empty load factors, per table 125 / 193 / 52 / 48 / 52 / 52 (review targets met exactly). Header example: `Normal and Severe: C-9: 9-5 \| Extreme and Abnormal: C-9(6): 9-6` — the two C-9 columns stay distinct; group ranges as printed (in 6.4-6 "Extreme and Abnormal" starts at S-18). Notes: 17 / 12 / 10 / 9 / 9 / 9, numbered 1..n without gaps, each under its own table, with the printed header (`Notes` for 6.4-5, `Notes:` for the others). Captions checked on both sheet pages of every table. |
| 2 | Unmatched subheading p29; IBC combinations one per line; 12-symbol legend; λ block | Done: `##### 6.4.2.2.5 Loading Combinations` + `###### SR Substructure Loading Combinations`; `unmatched_subheads` is now empty; 7 combination lines; 12 legend items; λ block from the rendered page via the patch. |
| 3 | Glued note superscripts; design-transient titles as subheadings | Done: 14 `<sup>n</sup>` conversions, no `FHB2`/`RAB2`/`Yes1`/`Motion1`/`Wind3`/`Protection2` left; 30 bold-paragraph transient titles. |
| 4 | Source defects stay; HTML comment at most | Done, 7 comments (§4); all defect strings verified present and unchanged. |

## 3. Verification

`python scripts/clean_references.py --only PSAR_ch06 --verify` (final run, with figures):

| Metric | Before module | After module |
|---|---|---|
| missing tokens / PDF tokens | 33 / 21,427 (0.15 %) | 12 / 21,427 (0.06 %) |
| residue (dot leader, entity, `[[`, running header, DOE footer, sheet heading, `x10-`, `<br>`) | 0 | 0 |
| headings emitted / whitelist | 69 / 69 (5 of the 74 numbered headings were list items) | 74 / 74 |
| unmatched headings / subheads / orphan captions / failed patches | 0 / 1 / 0 / 0 | 0 / 0 / 0 / 0 |
| pages_with_missing_gt3 | 1 (p55, 32 tokens) | 1 (p77, 4 tokens) |

The 12 remaining missing tokens are all intended representation changes: `motion1` ×3, `yes1` ×2, `fhb2`, `rab2`
(7 tokens now written `Motion<sup>1</sup>` … per the table-note convention) and `significant`, `light-water`,
`cooled`, `columbium`, `vanadium` (5 tokens of the three line-end hyphen joins `safety-significant`,
`Light-Water-Cooled`, `Columbium-Vanadium` that the core hyphen map restores as single tokens).

Independent table check (`scratchpad/indep_check.py`, third extractor): case-ID column x-centres and factor words
taken from PyMuPDF word boxes, each factor assigned to the row line that contains it and to the nearest case column,
then compared with the cells of the emitted Markdown: **522 factors, 522 matched, 0 differences** over the six
tables, markers included (`1.4 (4)`, `1.0(16)`, `1.6(10)`, …). Together with `odl_diff == []` (pdfplumber vs
opendataloader, checked inside the step) three independent extractions agree on every (row, load case) → value.
The SSE row, empty in all six tables before the re-conversion, now carries its 11 factors (6.4-5: C-10, C-17;
6.4-6: S-18, S-24 0.7, S-25 0.7; 6.4-7: C-17; 6.4-8: S-24 0.7, S-25 0.7; 6.4-11: C-17; 6.4-12: S-24 0.7, S-25 0.7).

Tests: `python -m pytest scripts/refclean/tests/test_psar_ch06.py -q` → 15 passed. Whole directory at the time of
writing: 112 passed, 1 failed — `test_psar_ch05.py::test_real_lbe_counts_and_type_pairing` (53 vs 52 type runs),
which belongs to the ch5 agent and is outside this module's ownership.

## 4. Source defects kept (review §5 "자동 수정 금지")

Each is reproduced exactly as printed and carries one HTML comment; no value was estimated, moved or inserted.

| Defect | Location in output | Comment key |
|---|---|---|
| α values of ASCE/SEI 4-16 §4.5.1 absent (confirmed absent from the text layer and the render of p17) | after the two nested items `for systems with single supports, and` / `… multiple supports …` | `alpha` |
| Cross-reference "Table 6.4-11 and Table 6.4-12" for the SR substructure combinations | §6.4.2.2.5 paragraph | `xref` |
| Mesh-size expressions printed without a left-hand side | after `For hard rock: = [(6,400 ft/sec) …` | `mesh` |
| Table 6.4-6 prints `Yi (7)` where the other tables use `Yj` | after Table 6.4-6 | `6.4-6` |
| Table 6.4-8 sheet 2: `Accident Thermal` row without symbol and without factors; no `Accident Pipe Break Missile Impact` row | after Table 6.4-8 | `6.4-8` |
| Table 6.4-9 "Minimum Factors of Safety" block printed one column left of the St- headers | after Table 6.4-9 | `6.4-9` |
| Table 6.4-16 event ID `A. 9`; B.3 named "…Sodium Loop" in the table and "…Sodium Pump" in §6.4.3.1.1 | after Table 6.4-16 | `6.4-16` |

Other source spellings verified unchanged: `DC/COL ISG-007` (6.4-12 note 5), `GT STRUDLVersion 40`,
`Tornado - Generated`, `ACI349-13`, `AISC348-14`, `10 CFR 50 Appendix S`, `1.4 (4)` spacing.

## 5. Deliberate representation decisions

- Parenthesised table-note markers stay literal (`C-9(6)`, `1.0(16)`, `Yj (8)`, `Design Load Cases(1)(5)`): they are
  unambiguous as printed, the dispatch requires `C-9(6)` to remain searchable, and converting them would add about
  200 `<sup>` spans to the load tables. Only markers glued into fake identifiers (`FHB2` → `FHB<sup>2</sup>`) are
  converted, as the brief requires.
- Load symbols stay plain (`Lr`, `Ess`, `Wtw`, `Ccr`, `Tdesign`): review #13 recommends plain spelling for search
  consistency with the body text, which prints them the same way. The spec's `<sub>` convention is therefore not
  applied in this chapter; one regex pass over the tables and the load-definition subheadings would change it.
- The label columns of a load table repeat the flattened span label
  (`Design Load Cases(1)(5): Load Combination Equation No. in ACI349-13` in both columns), which is the spec's
  fill-down rule for merged cells applied to the header row.
- Sheet-2 pages (57, 60, 62, 64, 66, 68, 72, 74) have no page anchor, because their rows are merged into the table
  anchored at the sheet-1 page. This matches the core behaviour for tables merged before this module (6.4-2).

## 6. Concerns / core patch requests (core modules were not edited)

1. `pdfaux.build_aux` sets `body_x0` to the per-page modal x0 of long lines. On pages dominated by 90 pt list
   indents (ch6 p6, p16, p29) this is 90, so `numbered_headings` rejects the headings printed at the 72 pt margin —
   5 of 74 in this chapter — and `fix_false_items` turns real list items on those pages into paragraphs. Suggested
   patch (`pdfaux.py::build_aux`): accumulate the x0 counter over all pages, take the document-wide modal x0 as the
   margin, and fall back to the per-page value only when the page has no line at that margin. This module works
   around it locally; other chapters are likely affected.
2. `tables._cell_text` iterates only the first list level of a cell: a list nested inside a list item is dropped.
   In ch6 Table 6.4-1B this lost 13 sub-bullets (MCE ground motion, seismic risk category, importance factor — 32 of
   the 33 missing tokens before this module). Suggested patch: recurse into each list item's `kids` (`walk(it)`
   after appending the item text), keeping the bold detection as it is.
3. `verify.pdf_page_text` clips to `header_footer_band`, which promotes any page-wide thin rectangle to a
   header/footer rule. Table borders qualify, so rows near the top of a table page are removed from the PDF side of
   the comparison (ch6 p61–74 and p69: 41 `1.0` and 23 `1.2` tokens appear as "extra" instead of matching, and a
   real loss in those rows would not be reported as missing). Suggested patch: accept a rule as a band boundary only
   when no text block lies between it and the page edge, or take the band from the opendataloader header/footer
   elements.
4. Not addressed here (outside the dispatch item list, class B/M in the review): review #10 — about 40 body
   paragraphs remain merged because opendataloader joined them; a PDF-block-boundary split step (as written for
   ch11) would fix them. Review #21 — numbered lists still render `- 1.` (core list handling). Review #22 — Rev. 1
   change bars are not restored (D7 leaves this optional).
