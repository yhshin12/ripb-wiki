"""Generic profile: the core pipeline only, for plain documents (guides) that need no document-specific steps
(the ACRS slide deck has its own profile, acrs_slides). Bibliographic fields come from META[key]; add an entry when registering a document with this profile."""
from .. import structure as S
from ..figures import figures_step
from ..levels import assign_levels

META = {
    "RG_1.233": {
        "doc_id": "RG 1.233", "doc_type": "Regulatory Guide", "issuer": "U.S. Nuclear Regulatory Commission",
        "revision": "0", "date": "2020-06",
        "title": ("Guidance for a Technology-Inclusive, Risk-Informed, and Performance-Based Methodology to Inform "
                  "the Licensing Basis and Content of Applications for Licenses, Certifications, and Approvals for "
                  "Non-Light-Water Reactors"),
        "tags": ["reference", "nrc", "regulatory-guide"], "aliases": ["RG 1.233"],
    },
    "RG_1.247": {
        "doc_id": "RG 1.247", "doc_type": "Regulatory Guide (for trial use)", "issuer": "U.S. Nuclear Regulatory Commission",
        "revision": "Trial", "date": "2022-03",
        "title": ("Acceptability of Probabilistic Risk Assessment Results for Advanced Non-Light Water Reactor "
                  "Risk-Informed Activities"),
        "tags": ["reference", "nrc", "regulatory-guide"], "aliases": ["RG 1.247"],
    },
    "RG_1.253": {
        "doc_id": "RG 1.253", "doc_type": "Regulatory Guide", "issuer": "U.S. Nuclear Regulatory Commission",
        "revision": "0", "date": "2024-03",
        "title": ("Guidance for a Technology-Inclusive Content-of-Application Methodology to Inform the Licensing "
                  "Basis and Content of Applications for Licenses, Certifications, and Approvals for "
                  "Non-Light-Water Reactors"),
        "tags": ["reference", "nrc", "regulatory-guide"], "aliases": ["RG 1.253"],
    },
    "SER_KU1_CP": {
        "doc_id": "ML25329A252", "doc_type": "NRC Safety Evaluation (construction permit)",
        "issuer": "U.S. Nuclear Regulatory Commission", "revision": "", "date": "2025-11",
        "title": ("Safety Evaluation Related to the U.S. SFR Owner, LLC Construction Permit Application for the "
                  "Kemmerer Power Station, Unit 1 (EPID L-2024-CPS-0000)"),
        "tags": ["reference", "nrc", "safety-evaluation", "natrium"], "aliases": ["Kemmerer Unit 1 CP SER"],
    },
    "TP-LIC-RPT-0011": {
        "doc_id": "TP-LIC-RPT-0011", "doc_type": "Technical Report (construction permit application, Enclosure 5)",
        "issuer": "TerraPower, LLC", "revision": "0", "date": "2024-03-27", "adams_accession": "ML24088A085",
        "title": "Core Nuclear and Thermal Hydraulic Design Technical Report",
        "tags": ["reference", "natrium", "technical-report"],
        "aliases": ["TP-LIC-RPT-0011", "Core Design and Thermal Hydraulic Technical Report"],
    },
    "NAT-3049": {
        "doc_id": "NAT-3049", "doc_type": "White Paper (pre-application, transmitted by TP-LIC-LET-0064)",
        "issuer": "TerraPower, LLC", "revision": "0A", "date": "2023-03-15", "adams_accession": "ML23080A013",
        "title": "Nascent Thermal Hydraulic Model White Paper",
        "tags": ["reference", "natrium", "white-paper"], "aliases": ["NAT-3049", "Nascent white paper"],
    },
}


def _rg1233_promote_intro(doc, aux):
    """RG 1.233 only: opendataloader tags the cover-page 'A. INTRODUCTION' line as a plain paragraph (it sits
    directly under the title block, unlike the sibling B/C/D section headings that ODL tags as headings with
    a 'heading level'). Promote it to a heading so it matches its siblings. No effect on any other document."""
    if doc.key != "RG_1.233":
        return
    for e in doc.els:
        if e.kind == "para" and e.text.strip() == "A. INTRODUCTION":
            e.kind = "heading"
            e.level = 2
            e.meta["heading_done"] = True
            break


def steps():
    return [
        S.drop_toc,
        S.withheld_callouts,
        lambda d, a: figures_step(d, a, render=a.meta.get("render_figures", True)),
        _rg1233_promote_intro,
        S.promote_headings,
        S.insert_subheads,
        S.fix_false_items,
        S.join_breaks,
        S.attach_captions_and_merge,
        S.attach_table_notes,
        S.normalise_text,
        S.references_as_items,
        S.normalise_item_levels,
        assign_levels,
    ]


def metadata(doc, aux):
    if doc.key not in META:
        raise KeyError(f"generic profile has no META entry for {doc.key!r}; "
                       "add one to scripts/refclean/profiles/generic.py")
    m = dict(META[doc.key])
    tables = [e.table.caption for e in doc.els if e.kind == "table" and e.table.caption]
    m.update({
        "source_pdf": f"references/raw/{doc.stem}.pdf",
        "raw_json": f"references/raw/{doc.stem}.json",
        "pdf_pages": doc.n_pages,
        "tables": tables,
        "figures": doc.meta.get("figures", []),
        "withheld": doc.meta.get("withheld", []),
    })
    return m
