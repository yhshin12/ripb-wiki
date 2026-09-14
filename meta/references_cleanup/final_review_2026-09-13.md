# FINAL review — references/ cleanup pipeline (whole change set, 2026-09-13)

Scope: the uncommitted working tree of `C:\Obsidian\ripb` — `scripts/refclean/` (core, 8 profiles, 5 patch files, 11 test files), `scripts/clean_references.py`, `scripts/convert_references.py`, the 9 cleaned files in `references/`, `references/figures/`, `references/raw/_verify/*.json`, `AGENTS.md` §3, and the ledger with its 8 per-document reports. Method: read-only; no subagents; five passes — (1) spec D1–D7 / plan / ledger, (2) every core module line by line, (3) all 8 profiles and all 11 test files, (4) output sampling against the PDFs (ch3 p113, ch6 p61, ch5 p13, ch7 p262, RG p64, NEI p52) plus scripted probes over the 9 outputs and the 9 raw JSON trees, (5) in-memory rebuilds of all 9 documents (no PNGs, nothing written) to read the QA fields that the build report does not print, and one run of the test suite (193 passed, 18 s). No vault file other than this one was modified.

## Strengths

- **The verified outputs are correct at every sampled point.** ch3 §3.9.4.3 (RRS-SPLX-CN) carries `8.13E-02 | 2.78E-01` directly under its "are listed below." sentence, as printed on p113; all 88 announcement sentences have their table (87 immediately, 1 after a two-sentence paragraph). ch6 Table 6.4-5 reproduces p61 cell for cell, including the previously lost `Ess` factors at C-10/C-17; the six load tables sum to 522 non-empty factors, and pdfplumber, opendataloader and PyMuPDF agree on all of them (`ch6_load_tables.odl_diff` empty). RG SFR-DC 4 matches p64 (title, status from Table 1, criterion text, rationale); Table 1 row 14 renders `Reactor coolant ~~pressure~~ boundary.` / `<ins>Primary</ins> coolant ~~pressure~~ boundary.` exactly as the spec example requires; the 178 records show 0 PDF-vs-JSON word differences. NEI Table 4-1 is the 6-column matrix of p52 with the RISC-2 check in the NSRST column; Table 5-9 is present although the main JSON nests it under a list item (see Important 1). ch5 DL3-RR2 lists the 51 LBEs of p13–14 with the correct type runs. ch4 Table 4.2-2 carries the 11 `Mean Dose Margin[d]` values of the spec (3.79 … 15.0).
- **Decisions D1–D7 are honoured.** `references/raw/` is git-ignored (`.gitignore:4`) and Obsidian-ignored (`app.json userIgnoreFilters`); exponents are `1E-07` form with mantissa kept (ch3 1674, NEI 50, ch7 `3.98E+15` only with superscript evidence; `x10-` residue 0 in all files); no TOC/LoT/LoF text survives (scripted check: 0 lines); figures are PNG embeds with the caption as alt text (43 + 11 + 6 + 4 + 1, every referenced PNG exists); withheld figures/sections are `> [!withheld] SRI — …` callouts (13 in ch1, 1 in ch11, sentence verbatim including the period where printed); record format is used exactly where D6 says (RG A–C, ch5 5.2-1…5.2-4) and nowhere else (ch7 DL tables are Markdown tables); emphasis is limited to the RG redline, the GDC-19 italics (3 ×) and the five ch1 bold status terms (`body.count("**") == 10` is asserted).
- **Verbatim discipline is enforced by tests**, not only claimed: every profile test file asserts a do-not-fix list (`HCI`, `sends a sends a`, `poistion`, `DL3- HR2`, `watercooled`, `fire- resistant`, `NRSRT`, `complimentary`, `5E-07/plant year`, …) and the repeated-sentence counts (ch3 `md.count(s) == txt.count(s)`).
- **Core architecture is sound and small** (1,470 lines for doc/pdfaux/normalize/structure/tables/figures/emit/verify). Profiles are pure `f(doc, aux)` steps with an explicit `STEPS` list; the PSAR base pipeline (`profiles/psar.py:121-148`) is 18 named steps, easy to reason about. Manual items go through JSON patches with `count` and `evidence` fields (all 18 patches carry `count: 1`), and an unmatched patch fails the run.
- **Multiple independent extractions are used where the converter is untrustworthy**: ch5 records from pdfplumber cross-checked against the ODL grid inside the step and against PyMuPDF `find_tables` in the tests; ch6 tables from pdfplumber cross-checked against ODL; ch7 DL tables from word positions with a two-way token-coverage check; RG cells from character-level spans cross-checked against the JSON cell text; NEI struct-tree cells checked for presence line by line (`test_smoke_struct_tree_cells_present`).
- **The ledger is honest and specific.** Every deviation from the literal spec is recorded as a ruling with its cost (type-run grouping in ch5, Table 11.5-1 spanning rows, supplied header rows in ch7 with an HTML comment, the two unprovable RG joins), and the core patch wave is traceable to the individual reports.

## Issues

#### Critical (Must Fix)

None. No output error was found in the samples, and no core rule was found to alter or drop source text in the current corpus. The findings below are latent data-loss paths, unenforced QA, and documentation gaps.

#### Important (Should Fix)

1. **`doc._items` silently drops any non-list/non-paragraph child of a list item** — `scripts/refclean/doc.py:63-69` handles only `list`, `paragraph`, `heading` kids. In the NEI main JSON, Table 5-9 (page 87) is a `table` kid of the list item whose content is the caption; the core stream never contains that table. The output is correct only because `profiles/nei1804.py:502-509` transplants Table 5-9 from the struct-tree JSON and happens to find the caption as a list item. Any future document with a table, image or caption nested under a list item loses it without a warning. Fix: route nested kids through the same dispatcher as top-level nodes (emit `table`/`image`/`caption` elements with `meta={"in_item": True}`), or at minimum append a `doc.meta["doc_warnings"]` entry naming the dropped node type, id and page.
2. **`tables.from_odl` overwrites overlapping cell positions silently** — `tables.py:72-74` assigns `grid[i][j]` for every spanned position; a second cell claiming the same position replaces the first. The ch7 JSON has 2 such overlaps (table id 8849 p334: `MTS` replaced by `AC PANELBOARD`; table 3325 p131), both inside figure-debris tables that are later dropped, so nothing is lost today. Fix: when `grid[i][j]` is already a non-empty `Cell`, keep the first and record a warning (`doc.meta`/`t.meta`), so the loss is visible in the build report.
3. **QA that is computed is not enforced.** (a) RG: `rg_stats["warnings"]` (PDF-vs-JSON diffs for all 178 criteria, Table 1 and the acronyms) is written at `profiles/rg1232.py:1100` under a key the build report ignores (`clean_references.py:92-93` prints only `*_warnings`/`*_qa`), and `tests/test_rg1232.py` never asserts it is empty; the in-memory rebuild shows it is empty today, but a regression would be invisible. (b) ch7: the two-way token-coverage check of the DL tables (`profiles/psar_ch07.py:488-504`, `removed_not_in_table` / `table_not_in_removed`) lives in `doc.meta["dl_tables"]` and is asserted nowhere (currently 0/0 over 27 tables). (c) verify has no pass/fail: `verify.py:79-121` reports `missing_pct` but no threshold, and only ch5 pins its accepted residual (`test_psar_ch05.py:454-467`: exactly 172 tokens, all explained); ch1 (1.66 %), ch7, ch11, RG and NEI residuals are explained in prose reports only. Fix: rename to `rg_warnings` / `ch07_dl_qa` (or add them to the report explicitly), assert `== []` / `== 0` in the real-document tests, and pin each document's accepted `missing_tokens` (or a per-document ceiling) so that a future core change that drops text turns the suite red.
4. **Dead workaround code retained as "regression guards" after the core patch wave.** The in-memory rebuild shows they now do zero work: `profiles/psar_ch05.py:69-137` `restore_subheads` → `{converted: 0, split: 0, inserted: 0}`; `profiles/psar_ch07.py:31-100` `missing_headings` (+ `_View`), `:104-184` `missing_subheads` with `_marks`/`underlined_lines` (a near-verbatim copy of `pdfaux.py:192-233`), `:813-877` `misplaced_subheads` → all `[]`; `profiles/psar_ch06.py:80-105` `missing_headings` (re-runs `numbered_headings` with a hard-coded 72 pt margin and mutates `aux.headings`) → nothing added; `profiles/psar_ch03.py:74-87` `merge_captioned_sheets` and the "defensive" fill-downs at `:101-131` duplicate `attach_captions_and_merge`/`from_odl`. About 350 lines of repair logic whose only remaining purpose is to hide a future core regression instead of reporting it. Fix: replace each with an assertion step that records a QA entry when the core result deviates (the pattern `psar_ch01._merged` and `psar_ch11.check_expected_headings` already use), and delete the duplicated detection code. `retry_unmatched_subheads` (ch7, 2 real hits) and `standalone_subheads` (4) stay.
5. **Two real-document test files test the on-disk artefact, not the code.** `tests/test_psar_ch03.py:127-131` (`_md()` reads `references/…ch3….md`) and `tests/test_psar_ch07.py:75-79` (`built` reads `OUT`) skip or pass against whatever file is on disk, so a profile regression in ch3/ch7 stays green until someone rebuilds. The other six document tests build in memory (`test_psar_ch01.py:194-211` pattern). Fix: adopt the in-memory fixture in both files; keep the PDF-level DL-table tests as they are.
6. **PSAR ch4 has no output-level test.** It is the only document "complete via core" and the only one without a `test_psar_ch04.py`; the Task 7 acceptance items (headings `## 4.1 …`/`### 4.2.1 …`, Table 4.2-2 `[d]` = 3.79 … 15.0, `5E-07` present, no `SUBJECT TO DOE`) are verified only by this review's probe. Fix: add a small in-memory build test with those assertions and the notes-as-list check for Tables 4.2-3/4.2-4 (Task 9g).
7. **Figure text policy is applied per agent, not by rule, and departs from spec §3 for ch7.** Spec §3 (그림 row) keeps informative labels — legends and explanatory boxes — in a callout; D3 only mandates PNG + caption + debris deletion. NEI does this for 3 figures (`nei1804.py:203-241`), ch7 for the two SLDs via patches, ch1 for the site legend; ch7 Figure 7.6.2-1 (p262: block diagram with a `LEGEND` SR/NSRST/NST and the RMC/CTC/UMC/AMC/FHC controller boxes, 150 tokens) and 7.2.3-1/-2 (131 tokens) keep nothing but the PNG, and `figures.figures_step` (`figures.py:73-80`) drops every element whose centre lies in the box, tables included (`:79`), with no mechanism to keep a legend. Fix: either record a ruling in the ledger that PSAR block-diagram labels are debris (and say so in AGENTS.md), or add a generic step that emits `> [!figure] Labels in Figure N (transcribed …)` from the text-layer lines inside the box when they exceed a token threshold — the ch7 patch text shows the accepted format.
8. **AGENTS.md §3 is accurate but insufficient for the next session** (`AGENTS.md:36-58`). It does not say that `references/<stem>.md` and `references/figures/` are generated and must not be hand-edited (corrections go to `scripts/refclean/patches/<KEY>.json` with `count` and `evidence`), that the acceptance gate is `--verify` **plus** `python -m pytest scripts/refclean/tests -q` (the spec §8 spot checks live in the tests, not in `--verify`), what a profile is (`STEPS`/`steps()`/`metadata()` contract, the frozen-core rule of the agent brief), or the conventions that a reader of the cleaned files meets first: `<!-- page a-b | x..y -->` range anchors, `> [!withheld]`, record format (D6), `<sup>n</sup>` table notes vs `[^n]` footnotes, `> [!figure]` callouts, `<!-- source: … -->` and `<!-- header row supplied … -->` comments. `log.md` has the 2026-09-11 conversion entry but no entry for the cleanup pipeline (Task 13 asks for one). Fix: one short subsection "Cleanup pipeline" in §3 with those seven points, plus the log entry.
9. **`verify.py` blind spots should be stated next to the numbers they produce.** (a) `pdf_page_text` (`verify.py:52-61`) discards the header/footer band, which is exactly where the PSAR sheet captions and the 106 ch5 subheading labels are printed — their loss cannot be detected by the metric (only by the ch5 tests). (b) A table border in the top 14 % / bottom 14 % still acts as a rule (`pdfaux.py:125-138`), so first/last table rows on some pages are excluded from the PDF side (ch1 p17 acronym row, ledger "parked"). (c) `_sheet_credit` (`:64-76`) credits header/caption tokens globally, masking an equal-count loss elsewhere; the metric is a document-level bag of words and cannot see attribution or order. (d) Hyphen tokenisation (`risk-` + `significant` vs `risk-significant`) and `<sub>`/`<sup>` markup inflate `missing` by ≈ 100 tokens in RG/NEI, so "0.7–1.3 % explained by inspection" is the practical floor, not "0". (e) `pages_with_missing_gt3` is unreliable for profile-rendered `raw_md` tables (RG Table 1 → 52 pages, 116–278 tokens each) and RG's non-monotonic anchors (30 duplicate anchor lines). (f) `headings_whitelist`/`headings_emitted` are counts only and are 0/0 for RG and NEI. Fix: (i) treat a rule as a band boundary only when no text block lies between it and the page edge; (ii) tokenise the PDF side after joining line-end hyphens; (iii) print the blind-spot list in the report header or in AGENTS.md so the next reader does not take `missing_pct` as a completeness proof.

#### Minor (Nice to Have)

1. `structure.drop_toc` (`structure.py:32`) drops any body paragraph containing `(?:\.\s?){4,}` anywhere — a quoted ellipsis of four dots would delete the whole paragraph. No hit in this corpus (probe over all 9 JSON trees). Restrict to elements on TOC pages or to leader-at-line-end.
2. `structure.attach_captions_and_merge` (`structure.py:353-360`) overwrites `pending` silently when two captions precede one table; only the final pending caption is reported (`:387-388`). LoT-vs-`tables` comparison shows no loss today (5/5, 25/25, 5/5, 4/4, 19/20, 33/38, 4/4). Record every overwritten caption in `orphan_captions`.
3. `tables.append_rows` (`tables.py:144-149`) does not check `n_cols`; a caption-equal sheet with a different column count would produce a ragged Markdown table. None exists now (scripted check: 0 ragged tables in 9 files). Add a guard that refuses the merge and reports it.
4. `promote_headings` wrapped-title continuation (`structure.py:107-114`, `:136-139`) checks only `rest_needed[:25]` but removes `len(rest_needed)` characters from the next element; combined with `pdfaux.numbered_headings:176-181` (appends following block lines to the title), a body line could be swallowed into a heading. Probe: no heading ends with `.` and exceeds 12 words, so no current case. Compare the full `rest_needed`.
5. `hdr_to_captions` (`structure.py:337-341`) never resets `last`, so a genuinely repeated caption number far apart would be dropped as a sheet repeat. Reset `last` when a non-hdr, non-caption element intervenes.
6. `figures_step` runs before `promote_headings` in `psar.steps` (`psar.py:129-131`), so the `numbered` guard at `figures.py:70` is dead for PSAR; a numbered heading printed inside a figure box would be deleted as debris. Currently 100 % of headings match. Either move the guard to a text test or run `promote_headings` first.
7. `normalize._MANT_NEG` (`normalize.py:6`) converts `2 x 10-1/2` style dimensions; add `(?![/\d])` after the exponent. `obsidian_escape` (`:66-68`) handles only `$`; the plan's line-leading `*` rule is implemented separately in four profiles (`nei1804.py:1096-1097`, ch1/ch3 notes, ch7 `<sup>*</sup>`). Centralise.
8. `join_breaks` (`structure.py:209-217`) treats any lowercase-starting body element as a continuation, so an unterminated item followed by `a) …` would be merged; no `a) … b) … c)` joins found. Exclude `LIST_LABEL` starts.
9. Ordered-list rendering is inconsistent across chapters: ch3 (4 lines, PDC 26) and ch6 (27 lines) still emit `- 1. …` double markers, while ch5/ch7/ch11/NEI convert them. Move the "item text starts with `N.`" rule into the core (`normalise_item_levels` or emit).
10. Frontmatter: PSAR `figures:` entries lack the `Figure` prefix (`figures.py:85` → `"1.1-1 Heat Transport …"`) while `withheld:`/`tables:` and NEI's list carry it; `revision`/`date` are hard-coded in `psar.metadata` (`psar.py:164-165`); `cleaned:` records `refclean 0.1.0` (`refclean/__init__.py:3`, never bumped through the patch wave) plus today's date, so every rebuild changes 9 files even when content is identical. Bump VERSION on core changes and consider dropping the date.
11. `clean_references.apply_patches` (`clean_references.py:52-57`) replaces all occurrences when `count` is absent; make `count` mandatory. The `ModuleNotFoundError` skip in `main` (`:115-120`) is dead now that all profiles exist.
12. ch1 emits `## LIST OF ACRONYMS AND ABBREVIATIONS` (line 66) before `# Chapter 1 …` (line 562): an H2 without an H1 parent for heading-path chunkers. Acceptable as front matter, but worth an ordering rule (chapter title first) or a note.
13. `references/figures/` is 26 MB (ch7 alone 18 MB, 200 dpi full-page renders) and currently untracked; the commit will add it. Decide on Git LFS or on a lower dpi for full-page SLDs before the first commit.
14. `scripts/patch_underlines.py` is untracked in the same tree; spec §2.3 rejects it. Exclude it from the commit or mark it superseded.
15. Test brittleness by design: the real-document tests pin exact counts (`len(rows) == 487`, `missing == 172`, `E-notation == 50`, `body.count("**") == 10`). They are golden locks on a fixed corpus and served their purpose during the patch wave (7 red tests flagged 3 real regressions), but they should be marked (`@pytest.mark.golden`) so a deliberate core change can be told apart from a regression; `test_structure.py` (7 tests) does not cover `attach_captions_and_merge`, `hdr_to_captions`, `drop_toc`, `fix_false_items` or `verify` with synthetic input.
16. RG page anchors are non-monotonic and 30 anchor lines are exact duplicates (criterion text pages, then rationale from the first page again); ledger ruling accepted, but the spec's "anchor before the first element of each page" is not literally met. Note it in AGENTS.md next to the range-anchor extension.

## Recommendations

1. Before committing: apply Important 3 (assert `rg_stats.warnings == []`, ch7 coverage `== 0`, pin per-document residuals), Important 5 (in-memory fixtures for ch3/ch7 tests), Important 6 (ch4 test), and Important 8 (AGENTS.md §3 subsection + log.md entry). These are small, protect the verified state, and make the acceptance criteria executable rather than narrative.
2. In the same or the next change set: Important 1 and 2 (core guards for nested kids and overlapping cells — both are a few lines plus a warning), Important 4 (convert dead repair steps to QA assertions), Important 7 (figure-label ruling or generic callout step).
3. Triage of the ledger's parked/deferred items: **keep parked** — verify band blind spot on table borders (Important 9a/b, verify-side only), ch1 figure-internal text, ch7 colour-coded SR/NSRST classification (class C, not derivable from text), ch11 org-chart transcription (class C), NEI raster-figure transcription (class C), RG two ambiguous joins and `Background` depth (rulings recorded), italics and change bars (D7), ch6 ≈ 40 merged paragraphs and ch3/ch6 `- 1.` markers (Minor 9), duplicate anchor pairs when a multi-page table starts on a heading page (cosmetic). **Fix before commit** — none of the parked items; the pre-commit set is the enforcement work above.
4. Adopt one QA reporting contract for profiles: every profile writes to `doc.meta["<key>_qa"]` and `doc.meta["<key>_warnings"]`, the build report prints them, and the real-document test asserts both empty. Half the profiles already do this; ch6 raises `ValueError` instead (acceptable, fail-fast), ch7 and RG use unprinted keys.
5. Document in `verify.py`'s module docstring (or the report header) what the metric can and cannot see (Important 9), and add a `--strict` flag that fails when `missing_tokens` exceeds the per-document pin.

## Assessment

**Ready to commit? With fixes.** The nine cleaned files are correct at every sampled location, every D1–D7 decision is honoured, and the profile agents verified their tables with two or three independent extractions; there is no output defect that blocks the commit. What is missing is enforcement: two latent silent-loss paths in the core (nested list kids, overlapping cells) carry no warning, the RG and ch7 cross-checks and the per-document residuals are not asserted, two document tests read the artefact instead of building it, ch4 has no test, and AGENTS.md does not yet tell the next session that the outputs are generated and how corrections are made — a small, well-bounded set of fixes that should land with, or immediately after, this change set.

## Fix wave (2026-09-13)

Scope: Important 1–6, 8, 9 of this review. Important 7 (figure-label policy) was parked by the controller and is
untouched. Method: every change was followed by a rebuild of the affected documents and a byte comparison against
the pre-fix outputs; **all 9 cleaned files are byte-identical to the reviewed state**, so the fix wave adds
enforcement and removes dead code without altering a single output character. Test suite 193 → 211 (one synthetic
test of removed code deleted, 19 added). No commit was made.

### Important 1 — nested list-item kids no longer dropped

- `scripts/refclean/doc.py:58-104` — `_items` now routes every kid through the new `_item_kid` dispatcher
  (`doc.py:67-104`): `list` recurses one level deeper, `paragraph`/`heading` stay `para`, and `table` (via
  `tables.from_odl`), `image` and `caption` are emitted as their own elements in document order, all with
  `meta={"in_item": True}`. A kid of any other type with no text is reported instead of vanishing.
- `scripts/refclean/doc.py:108,148-157` — `elements_from_json(tree, warn=None)` collects those reports;
  `load_doc` stores them in `doc.meta["doc_warnings"]`, which the build report already prints under `warnings`.
- Corpus effect (probe over all 9 JSON trees): exactly one such kid exists — NEI table id 2133 on p87
  (Table 5-9). It now reaches the stream and is consumed by `nei1804.tables`, whose page filter already drops the
  main-JSON tables of p87; output unchanged. No document produces a `doc_warnings` entry.
- Test: `scripts/refclean/tests/test_doc.py:52-76` (synthetic item with caption/table/image/nested-list/empty-kid).

### Important 2 — overlapping ODL cells keep the first cell and are reported

- `scripts/refclean/tables.py:65-91` — `from_odl` skips a position already holding a non-empty `Cell`, and records
  `{row, col, kept, dropped}` in `Table.meta["overlaps"]` when the two texts differ (an identical-text or
  empty-vs-empty overwrite is not a loss and is not reported).
- `scripts/refclean/tables.py:96-108` — new `overlap_warnings(doc)` turns the surviving tables' overlaps into
  `doc.meta["table_warnings"]` entries; `scripts/clean_references.py:30,76` calls it after the profile steps, so
  only losses that reached the output are reported.
- Corpus effect: ch7 table 8849 p334 (`MTS` vs `AC PANELBOARD`) is the single real overlap; table 3325 p131 is
  empty-vs-empty. Both tables are dropped as figure debris, so the build report stays empty.
- Tests: `tests/test_doc.py:78-99` (first cell kept, `meta['overlaps']`, absent key when nothing overlaps, warning
  text).

### Important 3 — computed QA is now asserted, and the build has a coverage gate

- RG: `profiles/rg1232.py:1103-1113` — the PDF-vs-JSON diff list is published as `doc.meta["rg_warnings"]` (printed
  under `warnings`) together with a compact `doc.meta["rg_qa"]` (criteria 178 = 55/65/58, Table 1 65 rows,
  29 redline cells, 42 acronyms, 39 references, `pdf_vs_json_diffs` 0, `hyphen_joins_unlisted` 0). `rg_stats` keeps
  the bulky detail for `metadata()`. Asserted in `tests/test_rg1232.py:267-277`.
- ch7: `profiles/psar_ch07.py:358-372` — the two-way DL-table token coverage is summarised in
  `doc.meta["ch07_dl_qa"]` (27 tables, 167 rows, 309 removed elements, `removed_not_in_table` 0,
  `table_not_in_removed` 0) and any non-zero residual is appended to `ch07_warnings`. Asserted in
  `tests/test_psar_ch07.py:254-265`.
- Verify threshold: `scripts/clean_references.py:8-12,118-120,135-142` — `--max-missing-pct` (default 2.0) makes a
  `--verify` run exit 1 and print `FAIL (PDF coverage): …` when any document exceeds it (checked: `--only
  PSAR_ch01 --max-missing-pct 1.0` exits 1; the default run exits 0).
- Per-document residual pins (±10 tokens, each with a comment accounting for the residual, ch5's test as the
  model): `tests/test_psar_ch01.py:330-348`, `tests/test_psar_ch03.py:364-383`,
  `tests/test_psar_ch04.py:144-154`, `tests/test_psar_ch05.py:423-436` (pre-existing),
  `tests/test_psar_ch06.py:283-300`, `tests/test_psar_ch07.py:268-287`, `tests/test_psar_ch11.py:360-378`,
  `tests/test_rg1232.py:279-297`, `tests/test_nei1804.py:410-432`. Each also asserts `residue == {}`,
  `headings_whitelist == headings_emitted`, the per-document warning lists empty, and the set of pages above the
  3-token threshold.

### Important 4 — dead workaround code removed (output proven unchanged)

Each removal was verified by rebuilding the document and diffing against the pre-fix output (no difference), after
a probe had shown the step produced nothing (`{converted: 0, split: 0, inserted: 0}`, `[]`, no hit).

- `profiles/psar_ch05.py` — `restore_subheads` with `_follower`, `_sub_heading` and `SUBHEAD_LABELS` deleted
  (−69 lines, was `:69-137`), removed from `STEPS` (`psar_ch05.py:552`). The regression check it existed for now
  rests on the core: `tests/test_psar_ch05.py:370-374` (53 `##### Implementation Summary` + 53
  `##### Relevant PSAR Chapters and Sections`, with a comment saying why) and `:202-206`
  (`unmatched_subheads == []`). Its synthetic test was deleted with it (the only test removed in this wave).
- `profiles/psar_ch07.py` — `NUM_HEAD`, `find_missing_headings`, `_View`, `missing_headings`, `_marks`,
  `underlined_lines` and `missing_subheads` deleted (was `:27-185`), `misplaced_subheads` deleted (was
  `:813-877`); `_next_pdf_line` and `_match_end` stay (used by `retry_unmatched_subheads`). `STEPS` is now
  `psar_ch07.py:809-811`; the docstring step list was corrected (`:5-7`). −9,863 characters (≈ 213 lines).
  Regression checks already in the suite: `tests/test_psar_ch07.py:220` (289 numbered headings) and `:281`
  (`headings_whitelist == headings_emitted == 289`).
- `profiles/psar_ch06.py` — `missing_headings` deleted (was `:80-105`) and the now unused
  `from ..pdfaux import numbered_headings` import; `STEPS` is `psar_ch06.py:456`. The five headings it used to
  re-derive stay asserted in `tests/test_psar_ch06.py:177-185`.
- `profiles/psar_ch03.py` — `merge_captioned_sheets` and `SHEET_ONLY` deleted (was `:74-87`; probe: 0 sheet-label
  drops, 0 merges) and the defensive fill-downs inside `fix_hazard_tables` (`psar_ch03.py:92-106`, was
  `:110-131`); `_fill_down` stays for Table 3.5-4. The results remain asserted in
  `tests/test_psar_ch03.py:271-282` (90/10/10 group rows, 34 non-empty rows, 13 rows, no `(Sheet`).

### Important 5 — ch3/ch7 tests build in memory

- `tests/test_psar_ch03.py:1-2,125-149` — new module-scoped `built` fixture (load → `psar.steps(3)` → render →
  patches) plus an `md` fixture returning the full text; `_md()` and `MD_PATH` are gone and the ten output tests
  take the fixture.
- `tests/test_psar_ch07.py:76-98` — new `built_doc` fixture (the real build, 14 s) with `built` derived from it, so
  the eight existing `built` tests are unchanged and no longer read `references/…ch7….md`.

### Important 6 — PSAR ch4 output test added

- `tests/test_psar_ch04.py` (new, 154 lines, 6 tests): the 15 numbered headings with their levels and titles in
  printed order plus the single H1; Table 4.2-2 header with `Mean Dose Margin[d]` and its 11 values
  (3.79 … 15.0) with normalised exponents and the four `[a]`–`[d]` notes as a list; Tables 4.2-3/4.2-4 two-row
  headers flattened to `Parent: Child` with the row-spanned ID filled down (Task 9g); `5E-07`/`2E-06` present and
  no `x10-`/`×10-`, no TOC, no DOE footer, no dot leaders; page anchors p4–p16 with their printed labels (the p7
  anchor is indented inside the section 4.2 list); verify complete (0 missing tokens of 3,586).

### Important 8 — AGENTS.md §3

- `AGENTS.md:58-72` — new "Cleanup pipeline" subsection: `references/<stem>.md` and `references/figures/` are
  generated and must not be hand-edited; a five-row table gives the core / registry / profile / patches / QA
  contracts (`steps()`/`metadata()`, `psar_ch<NN>.py STEPS`, `patches/<KEY>.json` with `count` + `evidence`
  failing the run when absent, `*_warnings`/`*_qa`); the build and the `--max-missing-pct` gate; the acceptance
  gate `python -m pytest scripts/refclean/tests -q` with the residual pins; and the output conventions a reader
  meets (range anchors and the non-monotonic RG anchors, `> [!withheld]`, record format, `<sup>n</sup>` vs `[^n]`,
  `<!-- source: … -->`, the emphasis whitelist). `log.md:95-100` records the wave (rule 7).

### Important 9 — verify.py blind spots documented

- `scripts/refclean/verify.py:1-25` — the module docstring now states what the numbers mean and lists eight blind
  spots: header/footer band, table borders near a page edge, the global sheet credit, bag-of-words (no order or
  attribution), hyphen and `<sub>`/`<sup>` tokenisation, `pages_with_missing_gt3` for `raw_md` tables and
  non-monotonic anchors, heading counts vs sets, and the skipped pages. The per-document pins point at it.

### Minor findings touched

- Minor 16 (RG anchors non-monotonic) — noted in the AGENTS.md conventions bullet, as the review asked.
- One unused import removed as a consequence of Important 4 (`collections` in `profiles/psar_ch05.py`).
- No other Minor finding was changed.

### Final state

`python scripts/clean_references.py --verify` (with figures): 9/9 documents built, `failed_patches` 0,
`residue {}` and `warnings []` everywhere, exit 0. `python -m pytest scripts/refclean/tests -q`: 211 passed, 38 s.

| Document | pdf_tokens | missing_tokens | missing_pct | pages > 3 missing | residue | headings (whitelist/emitted) |
|---|---|---|---|---|---|---|
| PSAR_ch01 | 26,258 | 437 | 1.66 | 4 | {} | 74 / 74 |
| PSAR_ch03 | 35,315 | 51 | 0.14 | 3 | {} | 458 / 458 |
| PSAR_ch04 | 3,586 | 0 | 0.00 | 0 | {} | 15 / 15 |
| PSAR_ch05 | 16,078 | 172 | 1.07 | 7 | {} | 67 / 67 |
| PSAR_ch06 | 22,629 | 29 | 0.13 | 1 | {} | 74 / 74 |
| PSAR_ch07 | 118,355 | 507 | 0.43 | 9 | {} | 289 / 289 |
| PSAR_ch11 | 20,417 | 168 | 0.82 | 6 | {} | 127 / 127 |
| RG_1.232 | 45,533 | 337 | 0.74 | 52 | {} | 0 / 0 (own heading list) |
| NEI_18-04 | 34,001 | 385 | 1.13 | 22 | {} | 55 / 55 |

Every number is identical to the pre-fix build, which is the point: the wave changed enforcement, not output.
