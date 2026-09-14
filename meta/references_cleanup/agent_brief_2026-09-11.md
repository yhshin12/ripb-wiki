# Brief for document-profile agents (refclean)

You extend the cleanup pipeline for ONE source document. Read this brief, then the plan
`docs/superpowers/plans/2026-09-11-references-cleanup.md` (Global Constraints + data model), the spec block at the top of
`meta/references_cleanup/cleanup_review_2026-09-11.md` (final decisions D1–D7), and your document's review
`meta/references_cleanup/file_reviews/review_<id>.md` (§1 findings, §5 ordered rules / do-not-fix list). Line numbers in the
review refer to an older md; locate things by text and PDF page.

## Environment
- Python: `C:\Code\Python\pykaeri\.venv12\Scripts\python.exe` only. PyMuPDF (`fitz`), pdfplumber, pypdf, pytest available.
- Vault: `C:\Obsidian\ripb`. Avoid `cd` in Bash; use absolute paths (or `PYTHONPATH=C:/Obsidian/ripb/scripts`).
- Build your document: `python C:\Obsidian\ripb\scripts\clean_references.py --only <KEY> --verify` (add `--no-figures` while iterating;
  do the final run WITH figures). Output: `references/<stem>.md`, `references/figures/<KEY>/`, report
  `references/raw/_verify/<KEY>.json` (summary, top_missing, top_extra, pages_missing).
- Tests: `python -m pytest C:\Obsidian\ripb\scripts\refclean\tests -q`.
- PDF checking: render pages with the Read tool (`pages: "12-13"`), or `fitz`/`pdfplumber` (words, tables, fonts).

## Ownership (hard rule)
You may create/edit ONLY:
- PSAR chapters: `scripts/refclean/profiles/psar_chNN.py` (module-level `STEPS = [f1, f2, ...]`, each `f(doc, aux) -> None`),
  `scripts/refclean/patches/PSAR_chNN.json`, `scripts/refclean/tests/test_psar_chNN.py`.
- RG 1.232: `scripts/refclean/profiles/rg1232.py`, `scripts/refclean/patches/RG_1.232.json`, `scripts/refclean/tests/test_rg1232.py`.
- NEI 18-04: `scripts/refclean/profiles/nei1804.py`, `scripts/refclean/patches/NEI_18-04.json`, `scripts/refclean/tests/test_nei1804.py`.
Other agents work on the other documents in parallel and share the core modules. Do NOT edit `doc.py`, `pdfaux.py`,
`structure.py`, `tables.py`, `figures.py`, `emit.py`, `verify.py`, `profiles/psar.py`, `profiles/__init__.py`,
`scripts/clean_references.py`, `scripts/convert_references.py`, or anything under `references/raw/` (read-only input).
If the core needs a change, write a local helper in your own module; if that is impossible, describe the exact core patch
(file, function, diff) in your final report.

## Core API you can use (see the plan for dataclasses)
- `doc.els`: list of `El(kind, text, page, bbox, font, size, level, list_style, table, id, meta)`. kinds: heading, para, item,
  table, image, caption, hdr, raw_md. `bbox` is opendataloader's box in the displayed page, origin bottom-left;
  `refclean.figures.odl_to_visible(bbox, fitz_page)` gives a PyMuPDF (y-down) rect.
- Headings: `meta['numbered']` + `meta['num']` (section number), `meta['sub']` (unnumbered subheading), `meta['figure']`.
  Final Markdown levels are assigned after your steps (`psar.assign_levels`); in your own profile (RG/NEI) you assign them.
- Tables: `e.table` = `Table(grid[[Cell(text,row,col,rowspan,colspan,bold,filled)]], header_rows, caption, notes, pages)`;
  `refclean.tables.render_md(t)`; to emit custom Markdown for a table element set `e.meta['rendered'] = "<markdown>"`
  (caption/notes still emitted by the emitter), or replace the element with `El('raw_md', markdown, page)`.
- Text is already normalised when PSAR hooks run: entities decoded, exponents in `1E-07` form, bullets stripped from items.
- `aux`: `headings`, `subheads`, `sups` ({page: [SupRef(base, sup, before)]}), `hyphen_map`, `figures`, `toc_pages`,
  `body_x0`, `meta['lines_by_page']` ({page: [Line(text,x0,y0,x1,y1,size,fonts,block,spans)]}, visible coords).
- `refclean.structure`: `promote_headings(doc, aux, refs=[HeadingRef...])`, `insert_subheads(doc, aux, subs=[SubRef...])`,
  `join_breaks`, `fix_false_items`, `attach_captions_and_merge`, `attach_table_notes`, `normalise_text`, `references_as_items`,
  `normalise_item_levels`, `withheld_callouts`, `drop_toc`, `hdr_to_captions`.
- Patches (`patches/<KEY>.json`): list of `{"find": exact text in final output, "replace": ..., "page": N, "evidence": "..."}`,
  applied to the rendered Markdown; a patch whose `find` is absent fails the run (reported as failed_patches). Use patches
  only for manual (class C) items that a rule cannot express.

## Process rules
- Do not dispatch subagents (no helpers, no reviewers). Do not run git commit/push (the user approves commits).
- Write your full report to the report file named in your dispatch; return only a short status in chat.
- Old review scratch scripts (prototypes such as `ch7c_dltab.py`, `ch3_simfix.py`, `rg_crit.py`) are in
  `C:\Users\User\AppData\Local\Temp\claude\C--Obsidian-ripb\db35be0e-3624-48f5-a63d-95732c7feeca\scratchpad\` — read-only
  references; copy logic into your own module if useful.

## Non-chapter profiles (RG 1.232, NEI 18-04)
`scripts/clean_references.py` calls `prof.steps()` (no argument) and `prof.metadata(doc, aux)` when the registry chapter is
None; `build_aux(chapter=None)` leaves `aux.headings` empty (you build your own heading refs), but `aux.figures`, `aux.sups`,
`aux.hyphen_map`, `aux.subheads` (underline-based, may be irrelevant for you) and `aux.meta['lines_by_page']` are filled.
You assign every heading's `level` yourself (the PSAR `assign_levels` does not run for you). Cover/front matter goes to the
frontmatter dict returned by `metadata()`; keys as in `profiles/psar.py::metadata` (doc_id, title, doc_type, issuer,
revision, date, source_pdf, raw_json, pdf_pages, tables, figures, tags, aliases + any document-specific keys).

## Output conventions (from the spec; binding)
- Table-note markers: `<sup>n</sup>` (notes listed under the table); page footnotes in running text: `[^n]` with the
  definitions at the end of the enclosing section. Symbol subscripts: `k<sub>eff</sub>`, `V<sub>S30</sub>`.
Verbatim source wording; exponents `1E-07`; no TOC; figures are PNG embeds (already produced by the core); withheld figures
use `> [!withheld] SRI — This information is withheld in accordance with 10 CFR 2.390`; tables: one logical table per
Markdown table with merged cells filled; record format only where the spec says (RG appendices A–C, PSAR ch5 Tables
5.2-1–5.2-4); keep source typos (review §5 do-not-fix list); emphasis only per D7.

## Definition of done
1. Every H-severity item in your review §1 is either fixed (and verified against the PDF) or listed as not fixed with the reason.
2. `--verify` run: no residue; `missing_pct` explained (intended deletions such as figure debris are fine); no failed patches.
3. Your tests pass and `python -m pytest ...\refclean\tests -q` is green.
4. Final reply (≤ 400 words): what you implemented, verification numbers, remaining issues, any core patch requests.
