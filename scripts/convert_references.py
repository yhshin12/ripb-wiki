"""Convert source PDFs in references/raw/ to raw Markdown + JSON with opendataloader-pdf.

The raw Markdown, the JSON element tree and the *_images/ folder are written next to the PDF in references/raw/
and are treated as immutable input for the cleanup step (scripts/clean_references.py reads <stem>.json and the PDF
and writes references/<stem>.md).

Per-document options were selected in the 2026-09-11 review of the opendataloader output:
- content_safety_off="off-page": the default off-page filter drops text right of x = 612 pt on /Rotate 90 pages
  (lost table columns in PSAR ch4-ch7, RG 1.232, ch1, ch11). Disabling it changes nothing else.
- include_header_footer (PSAR only): table captions (Sheet n of m) and underlined subheadings sit in the header band
  and are otherwise deleted. The added boilerplate is removed by the cleanup script.
- detect_strikethrough (RG 1.232): marks the red strike-out words of the Table 1 redline as ~~...~~.
- space_ratio 0.12 (NEI 18-04): restores 89 lost inter-word spaces without false splits.
- markdown_with_html is NOT used: opendataloader-pdf 2.5.7 escapes the opening <td> tags.

Requires JDK 17+ (the Java 8 on PATH fails with UnsupportedClassVersionError).

Usage:
  python scripts/convert_references.py            # convert PDFs whose raw .md does not exist yet
  python scripts/convert_references.py --force    # re-convert all (overwrites raw .md and *_images/)
  python scripts/convert_references.py --only ch4 # restrict to file names containing a substring
"""
import argparse
import datetime
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile

import opendataloader_pdf

RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "references", "raw")
JDK_BIN_DEFAULT = r"C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot\bin"
PAGE_SEP = "<!-- page %page-number% -->"

COMMON = dict(
    format="markdown,json",
    quiet=True,
    markdown_page_separator=PAGE_SEP,
    image_output="external",
    image_format="png",
    content_safety_off="off-page",
)

PROFILES = [
    # (file-name prefix, extra options)
    ("TP_Natrium_PSAR", dict(include_header_footer=True)),
    ("RG_", dict(detect_strikethrough=True)),
    ("NEI_", dict(space_ratio="0.12")),
]

# Auxiliary conversions written as <stem>.<suffix>.json (used by the cleanup profiles).
# NEI 18-04 is a tagged PDF: its structure tree gives correct table cells (headings from it are worse, so the main
# conversion stays untagged and only the tables are taken from this one).
AUX = [
    ("NEI_", "structtree", dict(format="json", quiet=True, use_struct_tree=True, image_output="off",
                                content_safety_off="off-page", space_ratio="0.12")),
]


def options_for(name):
    opts = dict(COMMON)
    for prefix, extra in PROFILES:
        if name.startswith(prefix):
            opts.update(extra)
            break
    return opts


def ensure_java():
    jdk_bin = os.environ.get("JAVA17_BIN", JDK_BIN_DEFAULT)
    if os.path.isdir(jdk_bin):
        os.environ["PATH"] = jdk_bin + os.pathsep + os.environ.get("PATH", "")
    out = subprocess.run(["java", "-version"], capture_output=True, text=True)
    first = (out.stderr or out.stdout).splitlines()[0]
    if '"1.' in first:
        sys.exit(f"JDK 17+ required, found: {first}. Set JAVA17_BIN to a JDK 17 bin directory.")
    return first


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", default="")
    args = ap.parse_args()

    java = ensure_java()
    manifest_path = os.path.join(RAW_DIR, "_conversion.json")
    manifest = json.load(open(manifest_path, encoding="utf-8")) if os.path.exists(manifest_path) else {}

    for pdf in sorted(glob.glob(os.path.join(RAW_DIR, "*.pdf"))):
        name = os.path.basename(pdf)
        if args.only and args.only not in name:
            continue
        md = os.path.splitext(pdf)[0] + ".md"
        if os.path.exists(md) and not args.force:
            print(f"skip (exists): {name}")
            continue
        opts = options_for(name)
        opendataloader_pdf.convert(pdf, output_dir=RAW_DIR, **opts)
        manifest[name] = {
            "output": os.path.basename(md),
            "converter": "opendataloader-pdf " + getattr(opendataloader_pdf, "__version__", "2.5.7"),
            "java": java,
            "options": opts,
            "converted": datetime.datetime.now().isoformat(timespec="seconds"),
        }
        stem = os.path.splitext(name)[0]
        for prefix, suffix, aux_opts in AUX:
            if not name.startswith(prefix):
                continue
            with tempfile.TemporaryDirectory() as tmp:
                opendataloader_pdf.convert(pdf, output_dir=tmp, **aux_opts)
                shutil.move(os.path.join(tmp, stem + ".json"), os.path.join(RAW_DIR, f"{stem}.{suffix}.json"))
            manifest[name].setdefault("aux", {})[suffix] = aux_opts
        print(f"converted: {name}")

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
