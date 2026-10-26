"""Document profiles: metadata + ordered cleanup steps per source document.

Internal documents are registered in internal/refclean/docs.json (private repo), never here, so that their keys and
titles stay out of the public repo: {"KEY": {"stem": ..., "profile": ..., "chapter": null, "meta": {...}}}.
"""
import json
import os

DOCS = {
    # key: (stem, profile module, chapter number)
    "PSAR_ch01": ("TP_Natrium_PSAR2025_ch1_General Plant and Site Description", "psar", 1),
    "PSAR_ch03": ("TP_Natrium_PSAR2025_ch3_Licensing Basis Events", "psar", 3),
    "PSAR_ch04": ("TP_Natrium_PSAR2025_ch4_integrated evaluations", "psar", 4),
    "PSAR_ch05": ("TP_Natrium_PSAR2025_ch5_Safety Functions, Design Criteria, and SSC Safety Classification", "psar", 5),
    "PSAR_ch06": ("TP_Natrium_PSAR2025_ch6_Safety-Significant SSC Criteria and Capabilities", "psar", 6),
    "PSAR_ch07": ("TP_Natrium_PSAR2025_ch7_Descriptions for Safety-Significant SSCs", "psar", 7),
    "PSAR_ch11": ("TP_Natrium_PSAR2025_ch11_Conduct of Operations", "psar", 11),
    "RG_1.232": ("RG_1.232_Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors", "rg1232", None),
    "NEI_18-04": ("NEI_18-04_Modernization of Technical Requirements for Licensing of Advanced Non-Light Water Reactors",
                  "nei1804", None),
    "RG_1.233": ("RG_1.233_Guidance for a Technology-Inclusive, Risk-Informed, and Performance-Based Methodology "
                 "for Non-Light-Water Reactors", "generic", None),
    "ACRS_ML25293A458": ("ACRS_ML25293A458_NRC Review of Kemmerer Unit 1 Construction Permit Application, "
                          "Control of Heat Generation", "acrs_slides", None),
    "RG_1.247": ("RG_1.247_Acceptability of Probabilistic Risk Assessment Results for Advanced Non-Light Water "
                 "Reactor Risk-Informed Activities", "rg1247", None),
    "RG_1.253": ("RG_1.253_Guidance for a Technology-Inclusive Content-of-Application Methodology for "
                 "Non-Light-Water Reactors", "generic", None),
    "SER_KU1_CP": ("SER_KU1_CP_Safety Evaluation of the Kemmerer Power Station Unit 1 Construction Permit Application",
                   "ser", None),
    "TP-LIC-RPT-0011": ("TP-LIC-RPT-0011_Core Nuclear and Thermal Hydraulic Design Technical Report", "tp_report", None),
}

INTERNAL_REGISTRY = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))), "internal", "refclean", "docs.json")
INTERNAL_KEYS = set()
INTERNAL_META = {}


def load_internal(path=INTERNAL_REGISTRY):
    """Merge the private registry into DOCS (no-op when internal/ is absent, e.g. in a public clone)."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        reg = json.load(f)
    for key, d in reg.items():
        if key in DOCS and key not in INTERNAL_KEYS:
            raise ValueError(f"internal registry key {key!r} collides with a public document")
        DOCS[key] = (d["stem"], d["profile"], d.get("chapter"))
        INTERNAL_META[key] = d.get("meta", {})
        INTERNAL_KEYS.add(key)


load_internal()
