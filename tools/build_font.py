#!/usr/bin/env python3
"""Export TTF and WOFF from the checked-in WOFF2 master and validate coverage.

Requirements: Python 3.10+, fonttools, brotli.
Run from repository root: python tools/build_font.py
"""
from pathlib import Path
import json
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "fonts" / "Codencoffee-Bold.woff2"
font = TTFont(str(MASTER))

# WOFF2 is the canonical checked-in font binary. Export interoperable formats.
font.flavor = None
font.save(str(ROOT / "Codencoffee-Bold.ttf"))
font.flavor = "woff"
font.save(str(ROOT / "Codencoffee-Bold.woff"))

# Re-open every output to ensure the files are valid and preserve cmap coverage.
checks = {}
for path in [MASTER, ROOT / "Codencoffee-Bold.ttf", ROOT / "Codencoffee-Bold.woff"]:
    loaded = TTFont(str(path))
    cmap = loaded.getBestCmap()
    checks[path.name] = {
        "glyphs": len(loaded.getGlyphOrder()),
        "mapped_codepoints": len(cmap),
        "printable_ascii_complete": all(cp in cmap for cp in range(32, 127)),
    }

report = {
    "family": font["name"].getDebugName(1),
    "style": font["name"].getDebugName(2),
    "units_per_em": font["head"].unitsPerEm,
    "master": "fonts/Codencoffee-Bold.woff2",
    "exports": ["Codencoffee-Bold.ttf", "Codencoffee-Bold.woff"],
    "validation": checks,
}
(ROOT / "proof" / "QA-REPORT.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2))
