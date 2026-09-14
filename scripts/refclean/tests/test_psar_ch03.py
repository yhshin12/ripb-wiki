"""PSAR ch3 hooks: synthetic unit tests + checks of one real build (in memory: no PNG rendering, nothing written
to references/, so the tests exercise the code and not a stale artefact)."""
import collections
import importlib
import os
import re
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from refclean.doc import Doc, El  # noqa: E402
from refclean.profiles import psar_ch03 as P  # noqa: E402
from refclean.tables import Cell, Table, render_md  # noqa: E402

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")
STEM = "TP_Natrium_PSAR2025_ch3_Licensing Basis Events"
PDF_PATH = os.path.join(RAW, STEM + ".pdf")

FREQ_H = ["5th Percentile Frequency", "Mean Frequency", "95th Percentile Frequency"]
DOSE_H = ["5th Percentile 30-day EAB TEDE [rem]", "Mean 30-day EAB TEDE [rem]", "95th Percentile 30-day EAB TEDE [rem]"]
DBA_H = ["Enveloping 2-Hour EAB TEDE [rem]", "Enveloping 30-day LPZ TEDE [rem]"]
VAL = re.compile(r"\d\.\d{2}E[+-]\d{2}")


# ------------------------------------------------------------ synthetic ----
def _tab(rows, page=1, caption=""):
    grid = [[Cell(t, r, c, bold=(r == 0)) for c, t in enumerate(row)] for r, row in enumerate(rows)]
    return El("table", "", page, table=Table(grid=grid, header_rows=1, page=page, pages=[page], caption=caption))


def _h(num, title="x"):
    return El("heading", f"{num} {title}", 1, meta={"num": num, "numbered": True})


def _doc(els):
    return Doc(key="t", stem="t", raw_dir="", out_dir="", n_pages=1, page_labels={}, els=els)


def test_announcement_kinds():
    a = P.announcements
    assert a("The enveloping 2-hour Exclusion Area Boundary (EAB) Total Effective Dose Equivalent (TEDE) and 30-day "
             "Low Population Zone (LPZ) TEDE for this LBE are listed below.")[0][1] == "dba"
    # source typo: no period after 'DBA' -> the sentence starts earlier but is still a frequency sentence
    assert [k for _, k in a("This is the most limiting DBE that mapped to the RFH-FDSP-CN DBA The 5th percentile, "
                            "95th percentile, and mean frequency for this DBE are listed below.")] == ["freq"]
    txt = ("The 5th percentile, 95th percentile, and mean 30-day TEDE at the EAB for this DBE are listed below. The dose "
           "consequences do not include radionuclide release from SCG pathways.")
    assert [k for _, k in a(txt)] == ["dose"]
    assert [k for _, k in a("The 5th percentile, 95th percentile, and mean dose for this BDBE are listed below.")] == ["dose"]
    assert a("The following items are listed below.") == []


def test_relocate_fifo_per_kind():
    els = [
        _h("3.6"), _h("3.6.1.1", "A (AAA-BBB-BL)"),
        El("para", "The 5th percentile, 95th percentile, and mean frequency for this AOO are listed below.", 1),
        _h("3.6.1.2", "B (AAA-BBB-1)"),
        _tab([FREQ_H, ["1.00E-01", "2.00E-01", "3.00E-01"]]),           # A's table, pushed behind B's heading
        El("para", "The 5th percentile, 95th percentile, and mean 30-day TEDE at the EAB for this AOO are listed below.", 1),
        El("caption", "The 5th percentile, 95th percentile, and mean frequency for this AOO are listed below.", 1),
        _h("3.6.1.3", "C (AAA-BBB-2)"),
        _tab([DOSE_H, ["4.00E-01", "5.00E-01", "6.00E-01"]]),
        _tab([FREQ_H, ["7.00E-01", "8.00E-01", "9.00E-01"]]),
        _h("3.10"),
    ]
    d = _doc(els)
    P.relocate_lbe_tables(d)
    seq = [(e.kind, e.table.grid[1][0].text if e.kind == "table" else e.text[:12]) for e in d.els]
    assert seq == [("heading", "3.6 x"), ("heading", "3.6.1.1 A (A"), ("para", "The 5th perc"), ("table", "1.00E-01"),
                   ("heading", "3.6.1.2 B (A"), ("para", "The 5th perc"), ("table", "4.00E-01"),
                   ("para", "The 5th perc"), ("table", "7.00E-01"), ("heading", "3.6.1.3 C (A"), ("heading", "3.10 x")]
    assert "ch03_warnings" not in d.meta


def test_relocate_splits_merged_rows_and_paragraphs():
    els = [
        _h("3.6"), _h("3.9.4.1", "X (RRS-CGR-CN)"),
        El("para", "The enveloping 2-hour EAB TEDE and 30-day LPZ TEDE for this LBE are listed below. "
                   "The enveloping 2-hour EAB TEDE and 30-day LPZ TEDE for this LBE are listed below.", 1),
        _h("3.9.4.3", "Y (RRS-SPLX-CN)"),
        _tab([DBA_H, ["7.75E+00", "7.77E+00"], ["1.34E-01", "5.30E-01"]]),   # two PDF tables merged into one
        _h("3.10"),
    ]
    d = _doc(els)
    P.relocate_lbe_tables(d)
    kinds = [e.kind for e in d.els]
    assert kinds == ["heading", "heading", "para", "table", "para", "table", "heading", "heading"]
    assert d.els[3].table.grid[1][0].text == "7.75E+00" and d.els[5].table.grid[1][0].text == "1.34E-01"
    assert d.els[2].text.endswith("are listed below.") and d.els[4].text.startswith("The enveloping")


def test_relocate_refuses_on_count_mismatch():
    els = [_h("3.6"), El("para", "The mean frequency for this AOO are listed below.", 1), _h("3.10"),
           ]
    d = _doc(els)
    P.relocate_lbe_tables(d)
    assert d.meta["ch03_warnings"] and [e.kind for e in d.els] == ["heading", "para", "heading"]


def test_source_term_release_column():
    rows = [["Plenum Release"] * 3, [P.ST_LABEL] * 3, ["Isotope", "2hr", "8hr"], ["I-131", "1.22E+00", "2.44E+00"],
            ["Non-Plenum Release"] * 3, ["", P.ST_LABEL, P.ST_LABEL], ["Isotope", "2hr", "8hr"],
            ["I-131", "4.71E+00", "6.85E+00"]]
    d = _doc([_tab(rows, caption="Table 3.2-5 In-vessel Fuel Drop DBA, 1 Assembly"),
              _tab([["Non-Plenum Release"] * 3, ["", P.ST_LABEL, P.ST_LABEL], ["Isotope", "2hr", "8hr"],
                    ["Ce-141", "6.73E-01", "9.81E-01"]], page=2)])
    P.source_term_tables(d)
    assert len(d.els) == 1
    md = d.els[0].meta["rendered"].splitlines()
    assert md[0] == P.ST_LABEL
    assert md[2] == "| Release | Isotope | 2hr | 8hr |"
    assert md[4:] == ["| Plenum Release | I-131 | 1.22E+00 | 2.44E+00 |", "| Non-Plenum Release | I-131 | 4.71E+00 | 6.85E+00 |",
                      "| Non-Plenum Release | Ce-141 | 6.73E-01 | 9.81E-01 |"]


def test_source_term_single_group():
    d = _doc([_tab([[P.ST_LABEL] * 3, ["Isotope", "2hr", "8hr"], ["Xe-133", "1.21E+02", "1.88E+03"]],
                   caption="Table 3.2-1 Protected Loss of Flow or Loss of Offsite Power")])
    P.source_term_tables(d)
    assert render_md(d.els[0].table).splitlines()[0] == "| Isotope | 2hr | 8hr |"


# ------------------------------------------------------------ real document ----
@pytest.fixture(scope="module")
def built():
    if not os.path.exists(os.path.join(RAW, STEM + ".json")):
        pytest.skip("raw PSAR ch3 conversion not available")
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    prof = importlib.import_module("refclean.profiles.psar")
    doc = load_doc("PSAR_ch03", STEM, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=3, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in prof.steps(3):
        step(doc, aux)
    text = render(doc, prof.metadata(doc, 3, aux))
    text, failed = CR.apply_patches("PSAR_ch03", text)
    body = text.split("\n---\n", 1)[1]
    return doc, aux, text, body, failed


@pytest.fixture(scope="module")
def md(built):
    """The full built document (frontmatter + body), as references/<stem>.md would hold it."""
    return built[2]


HEAD = re.compile(r"^(#{1,6}) (?:(\d+(?:\.\d+)+) )?(.*)$")


def _md_lbe_items(md):
    """[(kind, values, innermost section)] for every mini-table inside 3.6-3.9, in document order."""
    items, sec, inside = [], None, False
    lines = md.split("\n")
    for i, ln in enumerate(lines):
        m = HEAD.match(ln)
        if m and m.group(2):
            sec = m.group(2)
            inside = re.match(r"^3\.[6-9](\.|$)", sec) is not None
            continue
        if inside and ln.startswith("|") and not lines[i - 1].startswith("|"):
            kind = P._table_kind(Table(grid=[[Cell(t.strip(), 0, j) for j, t in enumerate(ln.strip("|").split("|"))]] * 2))
            if kind:
                items.append((kind, tuple(VAL.findall(lines[i + 2])), sec))
    return items


def _pdf_lbe_items():
    fitz = pytest.importorskip("fitz")
    from refclean.pdfaux import page_lines
    if not os.path.exists(PDF_PATH):
        pytest.skip("PDF missing")
    pdf = fitz.open(PDF_PATH)
    sec_re = re.compile(r"^(3\.[6-9](?:\.\d+)+)\s+\S")
    items, sec = [], None
    for pno in range(63, 119):
        lines = sorted(page_lines(pdf[pno - 1]), key=lambda ln: (ln.y0, ln.x0))
        i = 0
        while i < len(lines):
            ln = lines[i]
            m = sec_re.match(ln.text)
            if m and abs(ln.x0 - 72) < 3:
                sec = m.group(1)
            if re.match(r"^(5th Percentile|Enveloping 2-Hour)", ln.text):
                hdr, j = ln.text, i + 1
                while j < len(lines) and not VAL.search(lines[j].text):
                    hdr += " " + lines[j].text
                    j += 1
                kind = "dba" if "Enveloping" in hdr else ("freq" if "Frequency" in hdr else "dose")
                items.append((kind, tuple(VAL.findall(lines[j].text)), sec))
                i = j + 1
                continue
            i += 1
    pdf.close()
    return items


@pytest.mark.refs
def test_lbe_tables_follow_pdf(md):
    got, want = _md_lbe_items(md), _pdf_lbe_items()
    assert collections.Counter(k for k, *_ in want) == {"freq": 45, "dose": 34, "dba": 9}
    assert got == want


def _sections(md, depth=4, prefix=r"3\.[6-9]"):
    """{section number: text} for numbered headings of the given depth (text up to the next heading of <= depth)."""
    out, cur, buf = {}, None, []
    for ln in md.split("\n"):
        m = HEAD.match(ln)
        if m and m.group(2) and len(m.group(2).split(".")) <= depth:
            if cur:
                out[cur] = "\n".join(buf)
            cur = m.group(2) if (len(m.group(2).split(".")) == depth and re.match(prefix, m.group(2))) else None
            buf = [ln]
            continue
        if cur:
            buf.append(ln)
    if cur:
        out[cur] = "\n".join(buf)
    return out


@pytest.mark.refs
def test_each_lbe_has_one_table_per_announced_kind(md):
    secs = _sections(md)
    lbe = {k: v for k, v in secs.items() if re.search(r"\([A-Z]{3}-[A-Z0-9]{2,6}-(?:BL|CN|\d)\)$", v.split("\n")[0])}
    assert len(lbe) == 106
    for num, text in lbe.items():
        announced = collections.Counter(k for ln in text.split("\n") if not ln.startswith("|")
                                        for _, k in P.announcements(ln))
        tables = collections.Counter(item[0] for item in _md_lbe_items("#### " + num + " x\n" + text))
        assert announced == tables, num
        assert all(v == 1 for v in tables.values()), num


@pytest.mark.refs
def test_rrs_splx_cn_dose(md):
    secs = _sections(md)
    sec = secs["3.9.4.3"]
    assert "(RRS-SPLX-CN)" in sec.split("\n")[0]
    assert "| 8.13E-02 | 2.78E-01 |" in sec and "7.75E+00" not in sec
    assert "| 1.84E-04 |" not in secs["3.7.2.2"] and "| 1.05E-03 | 3.02E-03 | 7.45E-03 |" in secs["3.7.2.2"]


def _table_block(md, caption):
    lines = md.split("\n")
    i = next(k for k, ln in enumerate(lines) if ln.startswith("#") and ln.split(" ", 1)[1].startswith(caption))
    j = next(k for k in range(i + 1, len(lines)) if lines[k].startswith("|"))
    k = j
    while k < len(lines) and lines[k].startswith("|"):
        k += 1
    pre = [ln for ln in lines[i + 1:j] if ln.strip()]
    rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines[j:k]]
    return pre, rows[0], rows[2:]


@pytest.mark.refs
def test_table_3_5_4_summary_of_dbas(md):
    _, hdr, rows = _table_block(md, "Table 3.5-4")
    assert hdr[-1] == "DBA 30-day Low Population Zone Boundary TEDE (rem)" and len(hdr) == 5
    assert len(rows) == 28 and len({r[1] for r in rows}) == 21
    assert all(all(c for c in r) for r in rows)
    by_dbe = {r[0]: r for r in rows}
    assert by_dbe["DHS-ISTL-2"][1:] == ["DHS-ISTL-CN", "Loss of Heat Sink", "No Release", "No Release"]
    assert by_dbe["RFH-FDIV-3"][1] == "RFH-FDIV-CN" and by_dbe["RFH-FDIV-3"][3:] == ["1.74E+00", "3.19E+00"]
    assert by_dbe["RRS-CGR-1"][3:] == ["7.75E+00", "7.77E+00"] and by_dbe["RRS-RWG-2"][3:] == ["9.59E-02", "9.59E-02"]
    assert by_dbe["RFH-ESWR-1"][3:] == ["2.01E-02", "6.09E-01"] and by_dbe["DHS-RNBK-3"][1] == "DHS-RNBK-CN"
    assert by_dbe["IPI-IHEL-BL"][2] == "Intermediate Heat Exchanger Secondary-to-Primary Leak"


@pytest.mark.refs
def test_tables_3_1_2_and_3_1_3_fill_down(md):
    _, hdr, rows = _table_block(md, "Table 3.1-2")
    assert hdr == ["Screening Category", "Hazard"] and len(rows) == 110
    assert collections.Counter(r[0] for r in rows) == {"Individual Hazards - Qualitatively Screened Out": 90,
                                                       "Coexistent Hazards - Qualitatively Screened Out": 10,
                                                       "Individual Hazards - Quantitatively Screened Out": 10}
    _, hdr, rows = _table_block(md, "Table 3.1-3")
    assert hdr == ["Hazard", "Analysis"] and len(rows) == 34 and all(r[1] for r in rows)
    assert dict(rows)["Sodium Fire"].startswith("The internal fire hazards are selected for fire PRA development.")
    assert dict(rows)["Jet Effects"].startswith("The internal flooding hazards")
    _, _, rows = _table_block(md, "Table 3.1-1")
    assert len(rows) == 13 and "(Sheet" not in md


@pytest.mark.refs
def test_source_term_tables_single_header(md):
    for n in range(1, 19):
        pre, hdr, rows = _table_block(md, f"Table 3.2-{n} ")
        assert pre == [P.ST_LABEL], n
        assert hdr[:2] == (["Release", "Isotope"] if n in (4, 5, 6) else ["Isotope", hdr[1]]), n
        assert all(h.endswith("hr") for h in hdr[(2 if n in (4, 5, 6) else 1):]), n
        assert all(VAL.fullmatch(v) for r in rows for v in r[(2 if n in (4, 5, 6) else 1):]), n
    _, _, rows = _table_block(md, "Table 3.2-4 ")
    assert len(rows) == 40 and collections.Counter(r[0] for r in rows) == {"Plenum Release": 16, "Non-Plenum Release": 24}
    _, _, rows = _table_block(md, "Table 3.2-5 ")
    i131 = {r[0]: r[2] for r in rows if r[1] == "I-131"}
    assert i131 == {"Plenum Release": "1.22E+00", "Non-Plenum Release": "4.71E+00"}


@pytest.mark.refs
def test_criticality_block(md):
    sec = md[md.index("### 3.14.2 Methodology"):md.index("#### 3.14.2.1")]
    for s in ["The computed k<sub>eff</sub> for the system plus twice the Monte Carlo uncertainty (σ) must be less than the USL:",
              "\nk<sub>eff</sub> + 2σ < USL (Equation 3.14-1)\n",
              "\nThis ensures that the USL is met at a 95 percent probability and 95 percent confidence level.\n\nThe USL is defined as:\n",
              "\nUSL = 1 + bias – σ<sub>bias</sub> – Δ<sub>SM</sub> – Δ<sub>AOA</sub> (Equation 3.14-2)\n",
              "- σ<sub>bias</sub> is the uncertainty in the bias.",
              "- Δ<sub>SM</sub> is an administrative margin, typically 0.05.",
              "- Δ<sub>AOA</sub> is an additional subcritical margin to account for extensions in the area of applicability if",
              "(Reference 3.14-6). Bias, σ<sub>bias</sub>, and Δ<sub>AOA</sub> are computed",
              "to calculate the bias, σ<sub>bias</sub>, and Δ<sub>AOA</sub> for an input application",
              "the standard Δ<sub>SM</sub> value of 0.05",
              "Limits,” (Reference 3.14-3)."]:
        assert s in sec, s
    assert not re.search(r"^(σ|ΔSM|σbias ΔAOA|- \(Equation 3\.14-\d\))$", sec, re.M)
    assert "keff" not in md and md.count("k<sub>eff</sub>") == 9
    assert "F<sub>ΔH</sub>" in md and "F<sub>Z</sub>" in md and "F<sub>XY</sub>" in md


@pytest.mark.refs
def test_initial_conditions_table_under_3_3_4_2(md):
    sec = md[md.index("#### 3.3.4.2 "):md.index("#### 3.3.4.3 ")]
    assert "used in the LBE analyses:\n\n| Plant Condition | Reactor Power (%) | Core Flow (%) | Core Inlet Temperature (°C) |" in sec
    assert "| Full Power | 100 | 100 | 360.1 |" in sec


@pytest.mark.refs
def test_lbe_internal_order(md):
    for num in ("3.8.1.11", "3.8.2.6"):
        sec = _sections(md)[num]
        a, b = sec.index(f"##### {num}.1 LBE Description"), sec.index(f"##### {num}.2 Radiological Consequences")
        assert a < sec.index("The postulated initiating event") < b < sec.index("The fuel performance acceptance criteria")


@pytest.mark.refs
def test_noise_and_headings(md):
    assert not re.search(r"^\.$", md, re.M)
    assert not re.search(r"^- \(?[A-Z]{3}-[A-Z0-9]{2,6}-(?:BL|CN|\d)\)$|^\([A-Z]{3}-[A-Z0-9]{2,6}-(?:BL|CN|\d)\)$", md, re.M)
    nums = re.findall(r"^#{2,6} (3(?:\.\d+)+) ", md, re.M)
    assert len(nums) == 458 and len(set(nums)) == 458
    for h in ("### 3.12.3 Codes Used in System Evaluation", "#### 3.14.2.2 Ex-Vessel Storage Tank",
              "#### 3.14.2.3 In-Vessel Storage", "### References (3.11)", "### References (3.13)"):
        assert "\n" + h + "\n" in md, h
    assert "\n  - Peak Power\n" in md and "- Heat removal exceeds total heat produced" in md
    assert "Revision 0 (Reference 3.11-1), which also" in md and "is assumed to occur 2.5 days after" in md


@pytest.mark.refs
def test_repeated_content_kept(md):
    fitz = pytest.importorskip("fitz")
    pdf = fitz.open(PDF_PATH)
    txt = " ".join(" ".join(p.get_text().split()) for p in pdf)
    pdf.close()
    for s in ("The fuel performance acceptance criteria are satisfied.", "are listed below.",
              "This is the most limiting DBE that mapped to the", "DL3-RR10 as described in Table 5.2-3"):
        assert md.count(s) == txt.count(s) > 1, s
    assert md.count("| 2.27E-03 | 5.75E-03 | 9.37E-03 |") == 2        # RRS-CGR-BL / RRS-CGR-1
    assert md.count("| 1.00E+01 | 1.40E+01 | 2.10E+01 |") == 3        # RFH-ESWR-3 / RFH-FDBL-2 / RFH-FDPI-1


@pytest.mark.refs
def test_real_no_qa_issues(built):
    doc, aux, text, body, failed = built
    assert failed == []
    assert doc.meta.get("ch03_warnings", []) == []
    assert doc.meta.get("unmatched_headings", []) == [] and doc.meta.get("unmatched_subheads", []) == []
    assert [w for k, v in doc.meta.items() if k.endswith("_warnings") for w in v] == []
    assert len(aux.headings) == 458


@pytest.mark.refs
def test_real_verify_residual_is_pinned(built):
    """The accepted PDF-vs-output residual, 51 of 35,315 tokens (0.14 %) on 2026-09-13.

    Composition: the List-of-Figures page p6 (10 tokens, dropped by D2), `k<sub>eff</sub>` / `F<sub>Z</sub>` style
    markup that the PDF prints as `keff`/`FZ` (14), the `(Sheet n of m)` and `(continued)` sheet labels of the
    merged tables (8), the repeated `Isotope | 2hr | …` header rows of the source-term sheets merged into one table
    (16), and the line-end hyphen splits `Secondary-to-`/`Primary` and `area-of-application` (3). Tolerance +-10
    tokens: a larger change means text left the output somewhere else and must be explained before the pin moves.
    """
    from refclean.verify import verify
    doc, aux, text = built[0], built[1], built[2]
    res = verify(doc, aux, text)
    s = res["summary"]
    assert s["residue"] == {}
    assert s["headings_whitelist"] == s["headings_emitted"] == 458
    assert abs(s["missing_tokens"] - 51) <= 10, s["missing_tokens"]
    assert s["missing_pct"] < 0.2
    assert set(res["pages_missing"]) <= {6, 60, 128}
    missing = collections.Counter(dict(res["top_missing"]))
    assert missing["keff"] == 9 and missing["sheet"] == 4
