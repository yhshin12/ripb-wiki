# PSAR_ch05 report — Kemmerer Unit 1 PSAR Chapter 5 (Task 9c)

Status: DONE_WITH_CONCERNS. Every dispatch item and every H item of `review_ch45` Part B is implemented and
verified against the PDF with two independent extractions. The concerns are core-side (§6) and two format
decisions that deviate from the literal dispatch wording (§2).

§1–§6 describe the state of 2026-09-11. **§7 (2026-09-13) supersedes them where the core patches changed the
picture**: two profile steps were removed, one new step was added for a regression the patches introduced, and
the verification numbers were re-derived.

Files created (ownership per brief): `scripts/refclean/profiles/psar_ch05.py` (8 steps, 596 lines),
`scripts/refclean/tests/test_psar_ch05.py` (10 unit tests on synthetic input + 14 checks on the real document).
No `scripts/refclean/patches/PSAR_ch05.json`: no class-C item remained (the note, the reference entry and the
two missing headings are all rule-based), so no patch file was created.
Regenerated: `references/TP_Natrium_PSAR2025_ch5_Safety Functions, Design Criteria, and SSC Safety
Classification.md` (1,844 lines, 126,143 bytes) and `references/raw/_verify/PSAR_ch05.json`. The final run was
made with figures; the chapter has no body figure (review §3: 0 in PDF and md; the three cover rasters go with
the cover page), so no `references/figures/PSAR_ch05/` directory is produced.

## 1. Steps in `psar_ch05.STEPS` (run order)

| Step | What it does | Evidence (PDF page) | Review item |
|---|---|---|---|
| `drop_lot_residue` | Drops the `LIST OF TABLES` title left on p3. The List of Tables has 4 dot-leader lines, below the core `drop_toc` threshold of 5, so the page is not classified as a TOC page and only its entries (which carry leaders) were removed. | p3 | B17 |
| `promote_missing_headings` | Promotes `5.3.3 Reactivity Control` and `5.3.3.1 PDC 20 - Protection System Functions` (p30), which the PyMuPDF whitelist misses because they share a text block with the preceding `Section 7.5.1, …` line. Each title is re-checked as a whole PDF line before promotion, and both refs are inserted into `aux.headings` so `--verify` compares 67 against 67. | p30 | B6 |
| `join_enumeration_breaks` | Joins a paragraph that ends without terminal punctuation to the following paragraph when the latter starts with `(n)` or a lowercase word (4 places: PDC 17 p28, PDC 31 p36, PDC 71 p44, PDC 77 p47). A paragraph ending in `:` is not joined, which keeps the real paragraph break of PDC 78 (`… conditions are met:` / `(1) postulated leakage …`, 25 pt line spacing in the PDF). List items are excluded, so the five printed bullets of PDC 73 are untouched. | p28, p36, p44, p47 | B19 |
| `split_merged_paragraphs` | Restores 13 paragraph boundaries opendataloader merged: a PDF body line preceded by a vertical gap > 6 pt (normal line gap 1.7 pt, paragraph gap 12.8 pt) whose previous line ends a sentence is a paragraph start; where the first 60 characters of such a line occur exactly once inside a paragraph element after a sentence end, the element is split there. Pages 22, 23, 28, 31, 32, 33 (×2), 37, 38, 43, 46, 48 (×2). | p22–p48 | B22 |
| `rpcs_lists` | Turns the content of each of the 53 `Relevant PSAR Chapters and Sections` subheadings into list items, one per reference (210 items). Wrapped lists are joined first (PDC 15 p27, PDC 61 p42, PDC 73 p46); every part must match `(Section\|Chapter) n(.n)*` or the list is left untouched and reported in QA. The §5.3 `References` heading and entry 5.3-1, glued to the PDC 82 list, are split off and the entry is joined with its second line. | p21–p50 | B7, B20 |
| `ordered_lists` | The 12 numbered items rendered as `- 1. …` (bullet plus printed number) become Markdown ordered-list paragraphs `1. …` (PDC 11 p25, PDC 26 criterion p33–34 and implementation p34–35). | p25, p33–35 | B21 |
| `table_notes` | Table 5.2-4: rejoins the note fragment `application.` left as a body paragraph on p20 and writes the note marker as `<sup>1</sup>`, after confirming on the PDF line that the `1` is a raised 7.68 pt span against the 10.98 pt body. Table 5.2-3: asserts Note 1 is complete (contains `RFH-FDIV-CN`, ends `… provided by DL3-RR10.`). | p16, p20 | B3, B19 |
| `psf_records` | Rebuilds Tables 5.2-1 … 5.2-4 from the PDF and replaces the rendering of the four merged table elements with PSF records (§2). | p6–p20 | B1, B2, B8–B14, B16 |

## 2. PSF records (spec D6)

Source of the records: `pdfplumber.find_tables()` on the 15 sheet pages (ruled cells; one text line per LBE, per
type and per SSC). The opendataloader grid is not usable as the source here: `tables._cell_text` reads only the
first level of a cell, so the text of nested list items is dropped — the `Associated LBE(s)` cell of DL3-RC1
(ODL ids 106–117, p6) loses 12 of its 31 LBE IDs (DHS-ISTL-1, DHS-ISTL-2, DHS-RNBK-1, DHS-RNBK-3, IPI-IHEL-BL,
DHP-L1PP-1, DHP-L1PP-4, DHP-LAPP-BL, DHP-LOOP-2, DHP-LOOP-4, DHS-ISTL-4, DHS-RNBK-2) — and the ODL grid also
cannot express the SSC line breaks or the DL3-RR2 row split.

Row logic: a row that carries a PSF ID starts a record; `DL3-RR2 (continued)` (p14) continues the previous one
(the label is dropped); a row whose SSC cell is vertically merged repeats that SSC; a row with an empty SSC cell
and text in the SRDC cell is a sentence fragment and is appended to the previous SRDC (DL3-RR2, p13);
LBE→type pairs are read by line position (`page.within_bbox(cell).extract_text_lines()`, |Δtop| ≤ 3 pt) and the
result must equal the order-based pairing of the two cell texts, otherwise the run reports a QA entry.

Record layout (`### Table 5.2-n …` caption heading, one `####` record per PSF ID, table notes after the last
record; page anchors are emitted before the first record of each sheet page):

```markdown
#### DL3-RR4 — EVST Barrier

- **PSF-ID:** DL3-RR4
- **SR Function Description:** EVST Barrier
- **Associated LBE / Type:**
  - BDBE: RFH-FDET-BL, RFH-FDET-1

| SR SSC(s) | SRDC |
|---|---|
| Ex-Vessel Fuel Handling System (FHE); Sodium Processing System (SPS) | During postulated accidents the EVST, … |
```

Field names are the column headers of the sheet, verbatim and per table: `PSF ID` in 5.2-1/5.2-2/5.2-4 but
`PSF-ID` in 5.2-3; `Associated LBE(s)` in 5.2-1 but `Associated LBE` in 5.2-2/5.2-3; `PSF Description`,
`NSRST SSC Safety Significance Criteria (Risk-Significant or DID)`, `Associated LBE ID` and `SSC(s)` in 5.2-4.
Table 5.2-4 has no SRDC column, so its records carry the criteria field and an `SSC(s)` list (one item per SSC
name) instead of the two-column table.

Two deviations from the literal dispatch wording, both deliberate:

1. **One field `Associated LBE(s) / Type` instead of two.** The two columns are a pair list (222 entries), and
   two flat fields would leave the pairing positional. The field carries one sub-item per consecutive type run,
   `  - DBE: LFF-SAO-BL, RFH-FDIV-1, RFH-FDIV-3`, which keeps the source order (every list in this chapter is
   contiguous by type, asserted in the tests), states each pairing unambiguously, and avoids repeating the type
   222 times. Records whose LBE cell is `None` keep both printed values: `- **Associated LBE / Type:** None / N/A`
   (30 records). Cost: the cleaned file contains 169 fewer `AOO`/`DBE`/`BDBE` tokens than the PDF (§4).
2. **One table row per SSC cell, not per SSC name.** Where the source prints several SSCs against one SRDC
   (e.g. `Nuclear Instrumentation System (XIS)` + `Reactor Instrumentation System (RIS)` for the single SRDC
   "XIS and RIS shall send monitored signals …"), the row keeps them together separated by `; ` rather than
   duplicating the SRDC text, so the row still reproduces one printed table row. Where the SSC cell spans several
   SRDC rows (DL3-RR3, DL3-RR4, DL3-RR5), the SSC is filled down and each SRDC gets its own row.

Result: 62 records (25 SR + 37 NSRST), 56 SRDC rows, 222 LBE entries in 52 type runs, 30 records with
`None / N/A`, 4 caption headings, 0 `(Sheet n of m)`, 0 `(continued)`, 0 `<br>`, no flat grid table left.

## 3. Dispatch items — result

| # | Item | Result |
|---|---|---|
| 1 | D6 record format for 5.2-1/-2/-3 (SR) and 5.2-4 (NSRST); caption kept as heading; fields = column headers verbatim; two-column `SR SSC(s)`/`SRDC` table; notes under the last record; replace via `meta['rendered']` | Done (§2), with the two documented deviations. The four table elements keep their `table` kind (so the frontmatter `tables:` list stays populated) and only their rendering is replaced. |
| 2 | 62 PSF IDs present exactly once; SRDC/SSC text matches the PDF; DL3-RR2 merged; 5.2-3 Note 1 has RFH-FDIV-CN; 5.2-4 SSC names include AMC | Done. The 62 IDs appear in review §2a order, once each; per-PSF LBE counts equal the review §2a list (total 222). DL3-RR2: one record, 51 LBEs (33 from p13 + 18 from p14), the split sentence reads `… shall retain radionuclide fission products to establish …`. Note 1 contains `RFH-FDIV-CN` and ends `… including mitigation provided by DL3-RR10.` `Auxiliary Monitoring and Control System (AMC)` appears in DL4-RR3a, DL4-RR3b and DL4-RR4a; the phantom `Auxiliary NI Fire Protection System` is gone; `Gaseous Radwaste Processing System (RWG)` and `Water Pool Fuel Handling System (FHP)` are complete. |
| 3 | PDC headings `#### 5.3.1.1 PDC 1 - …`; RPCS lists as list items; no false list markers; page-split paragraphs joined (B19 rules and exceptions) | Done. 53 PDC headings in the order 1–5, 10–26, 28–37, 44–46, 60–64, 70–82, matching the PDF whitelist; 53 `##### Implementation Summary` and 53 `##### Relevant PSAR Chapters and Sections`; every RPCS list consists of `- Section x.y` / `- Chapter n` items only (210 items). No `- 1.` double markers and no heading rendered as a list item. Every page-crossing paragraph was checked against the PDF (§4); PDC 78 stays split and the PDC 73 bullets stay bullets. |
| 4 | Keep the source inconsistencies of review §5 | Done: `Water Fuel Pool Handling System (FHP)` ×3 (DL3-HR10, DL3-HR13, DL5-PAM1) beside `Water Pool Fuel Handling System (FHP)`, `sends a sends a signal`, `from effecting all rods`, `radionuclide release limits design`, `one rod bundle form the reactor core`, `… their safety functions is described in Section 8.1`, `design limits is not exceeded`. All asserted in the tests. |

## 4. Verification

`python scripts/clean_references.py --only PSAR_ch05 --verify` (final run, with figures):

| Metric | Core only (before this module) | After |
|---|---|---|
| missing tokens / PDF tokens | 9 / 15,607 (0.06 %) | 177 / 15,607 (1.13 %), all explained below |
| of which LBE IDs silently lost | 5 (`DHS-RNBK-1`, `DHP-L1PP-4`, `DHP-LAPP-BL`, `DHP-LOOP-2`, `DHS-ISTL-4`; 7 further losses were masked because the same IDs occur elsewhere in the document) | 0 |
| residue (dot leader, entity, `[[`, running header, DOE footer, sheet heading, `x10-`, `<br>`) | 0 | 0 |
| headings emitted / whitelist | 65 / 65 | 67 / 67 |
| unmatched headings / subheads / orphan captions / failed patches | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| pages_with_missing_gt3 | 9 | 8 |
| table rows repeating a PSF LBE list | 156 | 0 (62 records) |

The 177 missing tokens are all intended representation changes:

- **169** `AOO`/`DBE`/`BDBE` tokens (14 + 48 + 107): the LBE field states each type once per run (52 runs) instead
  of once per printed line (221 type tokens reach the verifier; the 222nd, one `DBE` in the DL2-RR2 row of p18, is
  cut off by the verifier's own header/footer band, see §6.3). No LBE ID is lost: the per-record LBE counts equal
  the review §2a list and the pairing is checked against two other extractions.
- **2** `continued`: the `(continued)` sheet label of DL3-RR2 (p14), removed when the record was merged.
- **6** tokens of the deleted List of Tables page (decision D4): `LIST OF TABLES` and the printed page numbers
  `5.2-2`, `5.2-4`, `5.2-8`, `5.2-13`.

`pages_with_missing_gt3` = {3: 29 (the deleted List of Tables page), 13: 26, 6: 25, 8: 18, 9: 17, 14: 16, 17: 9,
19: 4}; the seven table pages carry the per-page share of the 169 type labels.

Independent checks:

1. **opendataloader cross-check, inside the run** (`crosscheck_odl`, reported through `doc.meta['psar_ch05_qa']`):
   every record is compared with a second grid built from the ODL JSON with a recursive cell reader (description,
   LBE list, type list, criteria, SSC text, and each SSC/SRDC row). 0 differences for all 62 records.
2. **PyMuPDF `find_tables`, in the tests**: a third extraction of all 15 sheet pages; per PSF the LBE list, the
   type list, the SRDC texts in order and the SSC lines must match the records. 0 differences.
3. **LBE→type pairing** is derived from line positions inside the two cells and must equal the order-based
   pairing (`_pair_by_y`); any disagreement is a QA entry, and none occurred.
4. **Paragraph structure**: every page break of §5.1–§5.5 was compared with the PDF (last body line of page n
   against the first body line of page n+1); all 6 full-width page-end lines are joined and all short ones stay
   separate. Every PDF body paragraph start (338 checked) begins a paragraph, a list item or a heading.
5. `python -m pytest scripts/refclean/tests -q` → 113 passed, 24 of them this chapter's.

## 5. Review ch45 Part B items

| Item | Sev | Status |
|---|---|---|
| B1 SRDC truncated in 55 of 57 cells | H | Fixed. The re-converted input (`--content-safety-off off-page`) carries the full cells; all 56 SRDC cells verified word for word against PyMuPDF and the ODL grid. |
| B2 Table 5.2-4 SSC cells truncated (AMC lost) | H | Fixed and verified (3 × AMC, RWG, FHP). |
| B3 Table 5.2-3 Note 1 truncated (`RFH-FDIV-CN` lost) | H | Fixed; completeness asserted in the step and in the tests. |
| B4 11 underlined subheadings lost | H | Fixed by the re-conversion (`--include-header-footer`): 53 Implementation Summary + 53 Relevant PSAR Chapters and Sections. |
| B5 subheading labels glued to text | M | Fixed by the core `insert_subheads`; all 106 labels are `#####` headings. |
| B6 67 headings as list items / glued / buried | M | Fixed: 67 numbered headings, 2 of them promoted by this module. |
| B7 §5.3 References buried, entry 5.3-1 split | M | Fixed: `### References (5.3)` + one entry. |
| B8 93 rows with an empty PSF ID | H | Obsolete in the record format: each record states its PSF ID once and carries all of its rows. |
| B9 DL3-RR2 split into 32 rows, SRDC cut | H | Fixed: one record, 51 LBEs, one SRDC sentence. |
| B10 15 sheets not merged, 11 repeated header rows | M | Fixed: 4 tables, one caption heading each. |
| B11 unlabeled 5th column of Table 5.2-4 | M/C | Resolved by the record format: the LBE/type pairs sit under the `Associated LBE ID` field, so no unnamed column remains. |
| B12 LBE/type pairing only positional | M | Fixed: pairs read by line position, rendered grouped per type run. |
| B13 123 `<br>` | L | 0 in the output. |
| B14 SSC lists without separators | M | Fixed from the PDF line structure: `; ` inside a table cell, one list item per SSC in Table 5.2-4. |
| B15 running-header residue | M | 0 (core). |
| B16 caption rendering split three ways | M | 4 caption headings at the level of §5.2 + 1, no sheet labels. |
| B17 TOC and List of Tables | M | Dropped (the LoT title by this module). |
| B18 cover page | M | Dropped by the core; frontmatter carries title, issuer, revision and source. |
| B19 16 paragraph/list splits | M | Fixed: 4 enumeration joins here, the rest by the core `join_breaks`; both documented exceptions respected. |
| B20 reference lists rendered as list items | L | Kept as list items on the dispatch instruction (the review proposed removing the markers); each item is now a single reference. |
| B21 `- 1.` double markers | L | 12 ordered-list paragraphs. |
| B22 PDF paragraphs merged | M | 13 boundaries restored (§1). |
| B23 25 change bars | M | Not restored (decision D7). |
| B24 frontmatter and page anchors | M | Frontmatter + 49 page anchors, including one per sheet page inside the record blocks. |
| B25 exponents, formulas, glyphs, reading order | — | None in this chapter; `x10-` residue 0. |

## 6. Concerns and core patch requests

Core modules were not modified. The following are for the controller.

1. **`tables._cell_text` loses nested cell content** (`scripts/refclean/tables.py`, lines 40–54). It reads the
   cell's direct `kids` and, for a `list` kid, only its `list items`; text inside `kids` of a list item (nested
   lists, paragraphs) is dropped. Evidence: the DL3-RC1 `Associated LBE(s)` cell of ch5 p6 loses 12 of 31 IDs
   (ODL ids 109–117). Patch: make the reader recursive, collecting `content` in pre-order over `kids` and
   `list items` (see `psar_ch05._node_text`), keeping the current bold rule for the first level. Any document
   with nested lists inside table cells is affected.
2. **`pdfaux.numbered_headings` misses headings that are not the first line of their PyMuPDF block**
   (ch5 `5.3.3` and `5.3.3.1` on p30 follow a reference line inside one block). Same root cause as reported for
   ch03 and ch06. Patch candidate: test every line of a block, not only `bl[0]`, when the line matches
   `NUM_HEAD`, sits at the body margin and is not a reference entry.
3. **`pdfaux.header_footer_band` is unreliable on `/Rotate 90` pages**, which weakens `verify` there. On ch5 p18
   the band is 131.2 … 622.8 pt, so the table header row (y = 106.5) and the whole last table row (y = 630.5:
   `DL2-RR2 … RFH-ESWR-1 DBE Water Pool Fuel Handling System (FHP)`) are excluded from the PDF side of the
   comparison. Content lost inside such rows would not be reported as missing. Patch candidate: on rotated pages
   derive the band from the footer text line (`x.y-n Revision 1`) and the running-header line instead of from
   page-wide rules, or ignore rules that coincide with a detected table box.
4. **`structure.drop_toc` threshold**: a List of Tables with fewer than 5 dot-leader lines is not recognised as a
   TOC page, so its title survives (ch5 p3). Patch candidate: also treat a page whose only content is a
   `LIST OF (TABLES|FIGURES)` heading plus leader lines as a TOC page.
5. **Page anchors inside merged multi-page tables** (already raised by ch01/ch03): the merged table element
   carries only its first page, so pages 7, 9–11, 13–16 and 18–20 would have no anchor. This module emits the
   anchors itself inside the rendered record block, which is why `--verify` reports per-page numbers for those
   pages at all. A core option (anchors between row groups from `Table.pages`) would remove the workaround.
6. **Format decisions** (§2): the grouped `Associated LBE(s) / Type` field and the one-row-per-SSC-cell rule are
   my reading of "keep the LBE→type pairing unambiguous" and "one row per SSC". Either is one small change in
   `psar_ch05.render_record` / `_lbe_field` if the controller prefers the literal two-field or one-row-per-name
   variant; the grouped field is also the only reason `--verify` reports 1.13 % missing instead of ≈ 0.05 %.

## 7. Core patch follow-up (2026-09-13)

The core patches requested in §6 are applied. This section records what was removed from the profile, what the
new core changed in the output, and one regression the patches introduced for this chapter.

### 7.1 Workarounds removed (each checked against the output)

| Removed | Now covered by | Check |
|---|---|---|
| `drop_lot_residue` | `pdfaux.is_toc_page` flags a titled List of Tables page with ≥ 2 leader lines, so `structure.drop_toc` deletes p3 | `aux.toc_pages == {2, 3}`; `LIST OF TABLES` occurs 0 times; the 6 page-3 tokens are no longer counted as missing (verify skips TOC pages) |
| `promote_missing_headings` (5.3.3, 5.3.3.1) | `pdfaux.numbered_headings` accepts any line of a block and the document margin | Core-only run: `len(aux.headings) == 67`, both numbers present, `unmatched_headings == []` |

Kept, with the reason re-checked under the new core:

- **pdfplumber as the record source.** `tables._cell_text` is recursive now, so the ODL cell text is complete
  (the DL3-RC1 case is fixed), but the ODL grid still has no line structure: the LBE→type pairing by line
  position, the one-SSC-per-line split and the DL3-RR2 row/sentence split need the PDF. The ODL cross-check
  inside the step now compares against complete cell text and still reports 0 differences for all 62 records.
- **Page anchors inside the record block.** `emit.render` now gives a merged table one range anchor
  (`<!-- page 6-7 | 5.2-2..5.2-3 -->` … `<!-- page 17-20 | 5.2-13..5.2-16 -->`) and `verify.md_pages` credits
  every page of the range. The profile still announces each further sheet page before the first record printed on
  it, which keeps each record citable by page; the range start is never repeated, so nothing is announced twice
  (asserted in `test_real_page_anchors`: ranges `[(6,7), (8,11), (12,16), (17,20)]`, single anchors
  `[7, 9, 10, 11, 13, 14, 15, 16, 18, 19, 20]` inside the table range).
- `join_enumeration_breaks` (4 joins), `split_merged_paragraphs` (13 splits), `rpcs_lists` (53 lists, 210 items),
  `ordered_lists` (12), `table_notes` (Table 5.2-4 marker and the `application.` fragment) are unaffected by the
  core patches and unchanged.

### 7.2 New step: `restore_subheads` (regression introduced by the patches)

`structure.hdr_to_captions` now drops an `hdr` element whose text repeats the previous `hdr` (a running table
title repeated on every sheet page). In this chapter the two PDC subheadings are printed in the page header band
on 11 pages, so every repeat of `Implementation Summary` / `Relevant PSAR Chapters and Sections` is removed: 8
labels disappear, and the cursor of `structure.insert_subheads` then consumes a later label for each missing one,
leaving 19 labels unmatched (44 of 53 `Implementation Summary` and 43 of 53 `Relevant PSAR Chapters and Sections`
survived, so 9 PDC implementation summaries ran into the criterion text and 10 reference lists lost their label).

`restore_subheads` (first step of the profile) repairs them from the PDF underline list: a label left as a plain
element becomes a heading (2), a label glued to the text it introduces is split off (9), and a label dropped with
the header band is re-inserted before the element carrying its following PDF line (8). The step verifies the
per-page label sequence against `aux.subheads`, emits QA on any mismatch, and clears the entries it repaired from
`doc.meta['unmatched_subheads']` while recording one line in `doc.meta['psar_ch05_warnings']`, which the build
report now prints. Result: 53 + 53 labels, `unmatched_subheads == []`, QA empty.

**Core patch request (new):** restrict the running-title dedupe in `hdr_to_captions` to header texts that belong
to the same table (caption or repeated column title) — for example only drop an `hdr` repeat while the previous
element is a table of the same caption, or skip any `hdr` whose text is in `aux.subheads`. Any PSAR chapter whose
underlined subheadings fall into the header band is affected in the same way.

### 7.3 Verification after the patches

`python scripts/clean_references.py --only PSAR_ch05 --verify` (final run, with figures):

| Metric | Before the patches | After |
|---|---|---|
| PDF tokens compared | 15,607 | 16,078 (the header/footer band no longer cuts the rotated table pages) |
| missing tokens | 177 (1.13 %) | 172 (1.07 %) |
| missing breakdown | 169 type-run labels + 2 `continued` + 6 List-of-Tables tokens | 170 type-run labels (222 − 52, the p18 `DBE` is now compared too) + 2 `continued` |
| pages_with_missing_gt3 | 8 | 7 (only table pages, all from the type-run compaction) |
| residue / unmatched / orphan captions / failed patches | 0 | 0 |
| headings emitted / whitelist | 67 / 67 | 67 / 67 |
| `Implementation Summary` / `Relevant PSAR Chapters and Sections` | 53 / 53 | 53 / 53 (19 repaired by `restore_subheads`) |

Output structure unchanged: 1,844 lines, 62 PSF records, 56 SRDC rows, 222 LBE entries in 52 type runs, 210
reference items, 12 ordered-list items, 0 `(Sheet`, 0 `(continued)`, 0 `<br>`, 0 running-header residue.
`python -m pytest scripts/refclean/tests/test_psar_ch05.py -q` → 24 passed (unit test for `restore_subheads`
added; the anchor test now covers range anchors; the residual test is re-derived from the new numbers:
`missing[aoo] + missing[dbe] + missing[bdbe] == 222 - 52` and the rest is exactly `{"continued": 2}`).
The full suite reports 2 failures outside this chapter (`test_psar_ch01.py::test_real_value_fixes_and_kept_typos`,
`test_psar_ch07.py::test_built_headings_and_lists`); all 24 checks of this chapter pass.
