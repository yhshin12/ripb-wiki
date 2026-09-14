"""Generic profile: the core pipeline only, for plain documents (guides, slide decks) that need no document-specific
steps. Bibliographic fields come from META[key]; add an entry when registering a document with this profile."""
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
    "ACRS_ML25293A458": {
        "doc_id": "ML25293A458", "doc_type": "NRC staff presentation (ACRS subcommittee meeting)",
        "issuer": "U.S. Nuclear Regulatory Commission, NRR/DANU/UTB2 (Reed Anzalone)",
        "revision": "", "date": "2025-10-22/2025-10-23",
        "title": "NRC Review of Kemmerer Unit 1 Construction Permit Application, Control of Heat Generation",
        "tags": ["reference", "nrc", "acrs", "natrium"], "aliases": ["ACRS Control of Heat Generation slides"],
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
