# PSAR_ch01 report — Kemmerer Unit 1 PSAR Chapter 1 (Task 9a)

Status: DONE_WITH_CONCERNS (all dispatch items and all review H items fixed and verified against the PDF; the
concerns are core-side and listed in §5).

Files created (ownership per brief): `scripts/refclean/profiles/psar_ch01.py`, `scripts/refclean/patches/PSAR_ch01.json`
(empty list: every fix is a rule or a PDF-verified fixed list inside the module, none is a manual class C item),
`scripts/refclean/tests/test_psar_ch01.py` (10 unit tests on synthetic elements + 9 checks on the real document).
Regenerated: `references/TP_Natrium_PSAR2025_ch1_General Plant and Site Description.md` (1,799 lines),
`references/figures/PSAR_ch01/*.png` (6 PNGs, unchanged regions), `references/raw/_verify/PSAR_ch01.json`.

## 1. Steps in `psar_ch01.STEPS` (in run order)

> Updated 2026-09-13: the `drop_residue` step, the two sheet merges and four of the cell fixes moved into the
> core; see §6 for the current step list and what each step still does.

| Step | What it does | Evidence (PDF page) | Review item |
|---|---|---|---|
| `drop_residue` | Drops footer lines that opendataloader typed as body text (`- 1.2-1 Revision 1` inside References (1.2), `1.2-2 Revision 1` after Figure 1.2-1) and records them as page labels (p58 = 1.2-1, p59 = 1.2-2; the anchors and the frontmatter `page_labels` now carry them). Drops the 26 `(Sheet n of 26)` paragraphs. | p58, p59, p69–94 | #12, #6 |
| `split_paragraphs` | §1.1: splits the merged paragraph after `…Utilization Facilities.”` (the PDF prints two paragraphs). | p19 (render) | #1 |
| `join_page_breaks` | Joins a paragraph cut by a page break when it ends on a function word and the continuation starts with a capital: `…manipulation of the` ‖ `CRD. During shutdown…`, `…instead of the` ‖ `IAC blower. …`. Exactly 2 joins (asserted); a scan of all unterminated para→para pairs found no other page-crossing split. | p26→27, p63→64 | #16 |
| `nest_dash_items` | §1.4.1: the two `-` sub-bullets become depth-1 items under the third bullet (were `- - …`). | p66 (render) | #17 |
| `bold_status_terms` | D7: `**Full Conformance**`, `**Partial Conformance**`, `**Full Compliance**`, `**Partial Compliance**`, `**Not Applicable**` at the start of the five definition paragraphs. Bold is applied only where a PDF line on the same page starts with the term in `Arial,Bold`; Table 1.4-1/1.4-4 status cells are regular weight in the PDF and stay plain. The output contains no other `**`. | p66–67 (PyMuPDF spans) | #21 |
| `acronym_list` | 14 page fragments → `## LIST OF ACRONYMS AND ABBREVIATIONS` + one `Term \| Description` table, 487 rows (review count 487). `VS` / `VS30` → `V<sub>S</sub>` / `V<sub>S30</sub>` from a subscript detector (7.7 pt span with its baseline 2.1 pt below the 11 pt `V`; the only subscripts in the PDF). | p5–18; p17 spans | #5, #6, #20 |
| `table_141` | Table 1.4-1: 26 sheets → one table, 183 rows. New column `Comments`: the 26 rows whose status cell held label + comment are split into `Conformance Status` = `Full Conformance` (2) / `Partial Conformance` (24) and `Comments` = the rest, verbatim. Status distribution 96 Full / 24 Partial / 63 OL-stage sentences (kept whole in `Conformance Status`), identical to the review. | p69–94 (render p69: label and comment are separate paragraphs of one cell) | #6, #7 |
| `table_cell_fixes` | Fixed list, each must hit exactly one cell: `WaterCooled` → `Water-Cooled` (RG 1.68), `NATD-LIC-RPRT0002-A` → `NATD-LIC-RPRT-0002-A`, `Information Containment` → `Information - Containment` ((3)(v)); wrapped lines that `cell_md` joined with `; `: `3.12,; 3.13` → `3.12, 3.13`, `Limit; - All Parts` → `Limit - All Parts` (IEC 61000-3), `Nuclear facilities; - Equipment…` → `Nuclear facilities - Equipment…` (IEEE 344). | p73, p95, p105, p96, p111, p112 (PyMuPDF lines) | #4, #8 |
| `text_fixes` | `NUREG/ CR-7046` → `NUREG/CR-7046` (Ref 1.4-2; line ends `NUREG/`). | p67 | #19 |
| `site_layout_legend` | Figure 1.2-1: the facility legend is parsed from the PDF text layer (column under `FACILITY NUMBER/DESCRIPTION:`, 4.4 pt; a line without a facility number continues the previous entry) and inserted right after the figure image as `Facility number \| Facility`, 31 rows, `11 REACTOR BUILDING` … `85 AUXILIARY BOILER`, verbatim upper case; entry 84 = `STEAM GENERATOR BUILDING/TURBINE FACILITY BUILDING (STEAM) RACK` (two printed lines). The number sequence is checked against the expected list of 31. | p59 | #2 |
| `figure_notes` | Figure 1.3-1: the printed note `\*Sub-compartments within building provides additional confinement, depending on event.` (inside the figure box, therefore removed by the core) is kept as a paragraph after the image, leading `*` escaped; source wording (`provides`) unchanged. | p65 | #10, #23 |
| `check_withheld` | Figures 1.1-5 … 1.1-17: asserts heading + exactly one `> [!withheld] SRI — …` callout (extra callouts would be dropped); asserts no `[[` / `]]` anywhere (text and table cells). The current core output already satisfied this; the step is a guard. | p45–57 | #11 |

QA anomalies (fixed-list misses, count mismatches) are collected in `doc.meta['psar_ch01_qa']`; the real-document
test requires the list to be empty, so a core change that alters one of these inputs fails the test instead of
silently dropping a fix.

## 2. Dispatch items — result

| # | Item | Result |
|---|---|---|
| 1 | Figure 1.2-1 legend table | Done: 31 rows after the image (test `test_real_site_layout_legend`). |
| 2 | Table 1.4-1 one table; glued status/comment rows split; Tables 1.4-4/1.4-5 captions + merge | Done: 183 rows × 5 columns, 26 comments; 1.4-4 = 47 rows, 1.4-5 = 167 rows, each with its LoT caption as `###` heading and one header row (were already merged by the core). |
| 3 | Acronym list: one heading + one table | Done: H2 + 487-row table. |
| 4 | D7 bold status terms | Done: 5 terms, bold only where the PDF prints bold. |
| 5 | 7 hyphen losses; V<sub>S</sub> | 4 of 7 were already restored by the core hyphen map (`Tamper-Indicating`, `long-term`, `non-essential`, `in-plant`); the remaining 3 are fixed by the module. `V<sub>S</sub>`, `V<sub>S30</sub>` done. |
| 6 | Withheld figures 1.1-5 … 1.1-17 | Verified: 13 headings, 13 callouts, one each; no `[[`/`]]`. |
| 7 | Source typos (review §5.2) | Kept and asserted: `HCI` (hydrochloric acid), `Manufactures`, `and, provides`, `conditions.Each`, `an station blackout`, `areas.The`, `power- operated`, `800F`, `Division I`, `Low-, Medium- and High-Expansion`, `noncondensible`; duplicate `SSC` definitions kept. `TO ENVIROMENT` exists only inside a raster image. |

Review H items: #1 headings 74/74 (core) + §1.1 paragraph split (module); #2 legend; #3 `methodologies` already
present (core re-conversion); #4 hyphens; #5 captions — all fixed.

## 3. Verification

`python scripts/clean_references.py --only PSAR_ch01 --verify` (final run with figures):

| Metric | Before module | After module |
|---|---|---|
| missing tokens / PDF tokens | 441 / 24,067 (1.83 %) | 341 / 24,067 (1.42 %) |
| residue (dot leader, entity, `[[`, running header, DOE footer, sheet heading, `x10-`, `<br>`) | 0 | 0 |
| headings emitted / whitelist | 74 / 74 | 74 / 74 |
| failed patches, unmatched headings, orphan captions | 0, 0, 0 | 0, 0, 0 |
| pages_with_missing_gt3 | 17 | 52 (artefact, see below) |

Composition of the 341 missing tokens (complete list, not only the top 40):
- 326 (95.6 %) Figure 1.2-1 drawing text on p59, rendered in the PNG: 276 `X` fence glyphs; drawing labels
  `HWY 189` ×3, `RETENTION POND` ×3, `TRUE NORTH AND PLANT NORTH 0°` ×2, `CL REACTOR` ×2, `LEGEND:`/`FENCE`;
  30 hexagon facility numbers (their second occurrence; the legend keeps each number once).
- 4 Figure 1.3-1 box labels (`Environment` ×3, `Matrix`), rendered in the PNG.
- 11 tokenisation artefacts, no text loss: `1.Although`/`2.References`/`3.References` (opendataloader dropped the
  space after the enumerator in RG 1.13; the tokens become `1.although`), and the PDF-side halves of the restored
  hyphenations (`Water-`/`Cooled` counts as `water` + `cooled` in the PDF, `water-cooled` in the output).

`pages_with_missing_gt3` rises from 17 to 52 because the merged multi-page tables (acronyms p5–18, Table 1.4-1
p69–94, 1.4-4 p97–105, 1.4-5 p106–115) are emitted under the anchor of their first page, while the verifier compares
each PDF page with the output of pages p−1…p+1 only. A diagnostic re-run that adds each multi-page table's tokens to
every page in `Table.pages` leaves 2 pages above the threshold: p59 (331, Figure 1.2-1 drawing text) and p65 (16,
Figure 1.3-1 labels). Core change proposed in §5 (item 6).

Tests: `python -m pytest scripts/refclean/tests -q` → 58 passed at the final run (19 in `test_psar_ch01.py`; the
suite includes other agents' tests), 6.2 s.

## 4. Remaining issues (not fixed, with reason)

- Table 1.4-4 Section cells `7.1.3 11.2` ((2)(xviii)) and `7.6.5 11.2` ((2)(xix)): the PDF prints two lines in one
  cell; opendataloader already joined them with a space. Left verbatim; normalising to `7.1.3, 11.2` would insert a
  comma absent from the source (review #8 marks this as a decision item).
- `1.Although`, `2.References`, `3.References` (RG 1.13 comments): the PDF prints the enumerator and the text
  separated by a tab stop; opendataloader delivers them without a space. Left as extracted (no generic re-spacing
  rule; the only effect is 3 verifier tokens).
- Figure-internal text exists only in the PNGs: raster Figures 1.1-1 … 1.1-4 labels and bullets, Figure 1.2-1 drawing
  labels (`HWY 189`, `RETENTION POND`, `CL REACTOR`, north arrow `TRUE NORTH AND PLANT NORTH 0°`, symbol legend
  `FENCE`/`FACILITY NUMBER`, graphic scale), Figure 1.3-1 barrier chain and the five green barrier labels (vector
  outlines, not in the text layer). Transcription would be class C; the north-arrow statement duplicates §1.2
  (“plant north” faces true north).
- The acronym heading is H2 and precedes the H1 chapter title (front matter before `Chapter 1`), as prescribed by
  review §4. A structure-aware chunker sees it without an H1 parent.
- Rev. 1 change bars are not marked (D7).
- The frontmatter additions suggested in review §5.1-12 (`withheld_figures`, `applicant`, `doe_agreement`) are
  produced by `profiles/psar.py::metadata` (core, not owned).

## 5. Core patch requests

1. **`structure.attach_captions_and_merge` — sheets not merged when `(Sheet n of m)` was demoted to para.**
   `demote_other_headings` turns ODL's `(Sheet 1 of 26)` headings into `para` before this step, whose sheet skip only
   covers caption/heading/hdr; the para then separates the sheets. ch1 works around it in `drop_residue` + `_merge_run`.
   ```diff
   -        if e.kind in ("caption", "heading", "hdr") and re.fullmatch(r"\(?Sheet \d+ of \d+\)?", txt):
   +        if e.kind in ("caption", "heading", "hdr", "para") and re.fullmatch(r"\(?Sheet \d+ of \d+\)?", txt):
                continue
   ```
2. **`structure.hdr_to_captions` — repeated non-caption header titles.** `LIST OF ACRONYMS AND ABBREVIATIONS` is kept
   on all 14 pages as `hdr` and blocks the same-header merge. Proposed: drop an `hdr` whose text equals the previous
   kept `hdr` (the caption branch already dedupes):
   ```diff
   +            if base == last_hdr:
   +                continue
   +            last_hdr = base
                out.append(e)
   ```
   (`last_hdr = None` initialised next to `last`.)
3. **`pdfaux.hyphen_map` — table-cell hyphens.** Lines are paired in reading order; in a table row the line after
   `Water-` (p73) or `NATD-LIC-RPRT-` (p95) is the next column of the same row, so the pair is never formed. Proposed:
   pair each hyphen-ending line with the nearest line below it on the same page whose x-range overlaps (same column),
   instead of `zip(all_lines, all_lines[1:])`. The spaced form `Information -` (p105) is not a line-end hyphen and
   needs a separate rule (keep ` - ` when the next cell line is joined).
4. **Footer lines typed as body text.** On p58/p59 opendataloader did not type `1.2-1 Revision 1` / `1.2-2 Revision 1`
   as footer. A core rule (in `doc.elements_from_json` or a structure step) could drop body elements matching
   `^\d+(?:\.\d+)*-\d+ Revision \d+$` and harvest the label; ch1 does this locally.
5. **`tables.cell_md` `ENUM` false positives.** `\(?\d{1,2}[.)]` matches the section number `3.13`, and `- ` matches a
   wrapped title line (`- All Parts`), producing `3.12,; 3.13` and `Limit; - All Parts`. Proposed:
   `\(?\d{1,2}[.)](?!\d)` (keeps `1.Although`, rejects `3.13`) and treat `- ` as an enumerator only when the previous
   line ends with `:` or also starts with `- `.
6. **`verify.verify` — multi-page tables.** Add each multi-page table's tokens to the window of every page in
   `table.pages`:
   ```diff
   +    span = collections.defaultdict(collections.Counter)
   +    for e in doc.els:
   +        if e.kind == "table" and len(e.table.pages) > 1:
   +            toks = collections.Counter(_tokens(e.meta.get("rendered") or T.render_md(e.table)))
   +            for p in e.table.pages:
   +                span[p].update(toks)
        ...
            for q in (pno - 1, pno, pno + 1):
                win.update(_tokens(out_pages.get(q, "")))
   +        win.update(span.get(pno, {}))
   ```
   (`from . import tables as T`.) For ch1 this reduces `pages_with_missing_gt3` from 52 to 2.
7. **`figures.figures_step` drops printed figure notes** (text inside the figure box such as Figure 1.3-1's `*` note).
   Optional core rule: keep lines inside the box that start with `*` or `Note` as a paragraph after the image.
8. Minor: `clean_references.build` does not surface profile QA lists; adding any `doc.meta` key ending in `_qa` to the
   report would make `psar_ch01_qa` visible without running the tests.

## 6. Core patch follow-up (2026-09-13)

The 2026-09-13 core patches took over five of the workarounds in `profiles/psar_ch01.py`. Each was verified against
the rebuilt output before removal; the cleaned Markdown is identical to the verified 2026-09-11 version except for
the frontmatter `withheld:` list and the range anchors of the four multi-page tables (core changes 5 and 6).

### 6.1 Removed from the chapter hook (now core)

| Removed | Core replacement | Evidence in the rebuild |
|---|---|---|
| `drop_residue` step (whole step) with the `FOOTER_LABEL` / `SHEET_ONLY` patterns | `psar.drop_stray_footers` (footer lines typed as body text, page-label harvest) and `structure.attach_captions_and_merge` (skips `(Sheet n of m)` paras/items) | before the hook runs: page labels p58 = 1.2-1 and p59 = 1.2-2 are set, no `x.y-n Revision 1` element and no `(Sheet …)` element remain |
| `_merge_run(doc, ACRONYM_HEADER)` and the deletion of the repeated running titles | `structure.hdr_to_captions` dedupes the running title; `attach_captions_and_merge` merges the 14 caption-less fragments | before the hook: one `hdr` on p5 and one 488-row table with `pages = [5…18]` |
| `_merge_run(doc, T141_HEADER)` | `attach_captions_and_merge` (caption + same header, next table on a later page) | before the hook: one 184-row table with `pages = [69…94]`, caption attached |
| `CELL_FIXES` entry `WaterCooled` → `Water-Cooled` | `pdfaux.hyphen_map` pairs a dash line with the nearest overlapping line below it | `WaterCooled` has 0 hits before the hook; RG 1.68 reads `Water-Cooled` |
| `CELL_FIXES` entries `3.12,\n3.13`, `Limit\n- All Parts`, `Nuclear facilities\n- Equipment` | `tables.cell_md` no longer treats `3.13` or a `- ` continuation line as an enumerator | the cells still hold the line breaks but now render as `3.12, 3.13`, `… Part 3: Limit - All Parts`, `… Nuclear facilities - Equipment important to safety - Seismic qualification`, identical to the removed fixes |

`_merge_run` was replaced by `_merged(doc, header, what)`, which only checks that the core produced one table per
logical table and records a QA entry otherwise. A merge regression now fails `test_real_no_qa_issues` instead of
being silently repaired inside the hook.

### 6.2 Kept (still not covered by the core)

- `CELL_FIXES`: `NATD-LIC-RPRT0002-A` (p95) and `Information Containment` (p105). The core hyphen map cannot see
  either case: on p95 the dash does not end the visual line (`NATD-LIC-RPRT- ML24283A066 Principal Design Criteria
  for the`, the row continuing in the next column), and on p105 the printed form is a spaced dash (`Preliminary
  Design Information -`), which is not a line-end hyphen. Both still match exactly one cell.
- `TEXT_FIXES`: `NUREG/ CR-7046` (p67) — a line wrap after `NUREG/` in running text, not a dash.
- `split_paragraphs`, `join_page_breaks` (2 joins), `nest_dash_items`, `bold_status_terms` (D7), `acronym_list`
  (H2 heading and `V<sub>S</sub>` / `V<sub>S30</sub>` from the subscript detector), `table_141` (status/comments
  split of the 26 glued rows), `site_layout_legend`, `figure_notes`, `check_withheld`.

### 6.3 Tests

- Removed `test_drop_residue_footer_labels_and_sheet_paras`; the real-document assertions (page-label anchors, no
  `(Sheet`, no `1.2-x Revision 1` line) keep covering the result, which is now produced by the core.
- `test_table_141_merge_and_status_split` → `test_table_141_status_split` (input is the pre-merged table the core
  now delivers) plus `test_table_141_unmerged_sheets_are_reported_not_half_split`, which asserts that a merge
  regression leaves the sheets untouched and yields a QA entry instead of a half-split table.
- `test_acronym_list_merge_and_subscripts` → `test_acronym_list_heading_and_subscripts` plus
  `test_acronym_list_reports_a_failed_core_merge`.
- `test_cell_fix_requires_exactly_one_hit` now uses a deliberately absent string instead of `WaterCooled`.
- No assertion was loosened. `test_psar_ch01.py`: 20 tests, all passing.

### 6.4 Verification after the rebuild

`python scripts/clean_references.py --only PSAR_ch01 --verify` (with figures):

| Metric | 2026-09-11 core | 2026-09-13 core |
|---|---|---|
| pdf_tokens | 24,067 | 26,258 |
| missing tokens | 341 (1.42 %) | 853 (3.25 %) |
| pages_with_missing_gt3 | 52 | 4 (p59 331, p65 16, p69 5, p92 5) |
| residue, failed patches, unmatched headings, orphan captions | 0 | 0 |
| headings emitted / whitelist | 74 / 74 | 74 / 74 |
| report `warnings` / `qa` | — | `[]` / `{}` |

The rise of `pdf_tokens` (+2,191) and of `missing_tokens` is an accounting effect of the new `header_footer_band`
thresholds (14 %/86 %): the per-sheet captions, the `(Sheet n of m)` markers and the repeated header rows now fall
inside the counted body band, while the cleaned file keeps one caption and one header row per logical table.
Classification of the 853 missing tokens (`classify_missing.py` in the scratchpad):

- 506 repeated captions, sheet markers and header rows of the four multi-page tables (intended de-duplication:
  Table 1.4-1 caption ×25, `(Sheet n of 26)` ×26, `Guide Number | Title | Revision | Conformance Status` ×25,
  `Term | Description` ×13, and the corresponding lines of Tables 1.4-4 and 1.4-5);
- 334 figure text on p59 (277 `X` fence glyphs plus the drawing labels) and p65 (Figure 1.3-1 box labels), both
  rendered into the PNGs;
- 13 tokenisation artefacts without text loss: `1.Although` / `2.References` / `3.References` (the converter dropped
  the space after the enumerator), the PDF-side halves of the restored hyphenations (`Water-`/`Cooled`,
  `Tamper-`/`Indicating`, `long-`/`term`, `non-`/`essential`, `NATD-LIC-RPRT-`/`0002-A`), one `Term` header laid out
  as two visual lines, and `VS` (the output writes `V<sub>S</sub>`).

`pages_with_missing_gt3` fell from 52 to 4 through the range anchors (core change 6). The four remaining pages are
p59 and p65 (figure text as above), p69 (`(Sheet 1 of 26)` plus the `1.Although` / `2.References` tokens) and p92
(`(Sheet 24 of 26)` plus the `Tamper-`/`Indicating` halves).

### 6.5 Observations on the new core (no action requested)

- The narrower body band (86 % of the page height) excludes the last table row of the acronym pages from the PDF
  side of the comparison (`VS30 Time-averaged …` sits at y = 693 pt on p17 of 792 pt). The row is present in the
  output; the effect is that the verifier no longer checks those rows.
- When a multi-page table starts on the page of the preceding element, two anchors appear in sequence
  (`<!-- page 5 | iv -->` from the acronym heading, then `<!-- page 5-18 | iv..xvii -->` from the table). Cosmetic.
- Items 1–6 of §5 are implemented; §5 item 7 (printed figure notes) and item 8 (QA keys in the report) are covered
  differently: the hook still adds the Figure 1.3-1 note itself, and the report now prints `warnings` / `qa`.

### 6.6 Second core round (withheld dedupe exception, ENUM for bare section numbers)

(a) `structure.hdr_to_captions` no longer dedupes header-band lines containing "withheld". Rebuilt output: the 13
withheld markers of Figures 1.1-5 … 1.1-17 are intact — 13 callouts, one directly under each figure heading, no
`[[` / `]]` anywhere. `check_withheld` reports no QA entry and needs no workaround; it stays as a guard.

(b) `tables.ENUM` now treats a whole line that is a bare dotted section number as an enumerator. Two consequences
for ch1, both checked against the PDF:

- Table 1.4-3, TP-LIC-RPT-0011 `Section(s)`: the cell is `3.12,` / `3.13` in the PDF (p96, x = 428, y = 124 / 138) —
  one wrapped list whose first line ends with a comma, not two items. The new rule rendered it `3.12,; 3.13`, so the
  cell fix `3.12,\n3.13` → `3.12, 3.13` was reinstated in `CELL_FIXES`.
- Table 1.4-4 `Section` cells of (2)(xviii) and (2)(xix): the PDF prints `7.1.3` (p102, y = 456) and `11.2`
  (y = 473) on two lines at x = 488 in the Section column, and likewise `7.6.5` / `11.2` (y = 514 / 531).
  opendataloader delivers each cell as a single paragraph (`7.1.3 11.2`), so the new ENUM rule never sees a second
  line and the space join survived. Two `CELL_FIXES` entries now restore the spec separator: `7.1.3; 11.2` and
  `7.6.5; 11.2`. `5.3.2.10, 7.6.7` ((2)(xxviii)) is a single printed line and stays as printed. This closes the
  open decision of review #8 in favour of the convention the core now applies to the same construct.

`test_real_value_fixes_and_kept_typos` asserts the three repaired cells and the unchanged comma form. Rebuild after
both changes: `missing_tokens` 853 (3.25 %), `pages_with_missing_gt3` 4, residue 0, failed patches 0, qa `{}`,
74/74 headings — identical to §6.4 (the separators do not change token counts). `test_psar_ch01.py`: 20 passed.
