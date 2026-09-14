"""Document profiles: metadata + ordered cleanup steps per source document."""

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
}
