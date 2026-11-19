# codeNcoffee-font

<p align="center"><img src="proof/specimen.svg" alt="Codencoffee Bold vector specimen" width="100%"></p>

<p align="center"><strong>A screenshot-derived geometric display typeface reconstruction.</strong><br>Real vector outlines, distributed as TTF, WOFF and WOFF2.</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Font files

| File | Intended use |
| --- | --- |
| [Codencoffee-Bold.ttf](Codencoffee-Bold.ttf) | Desktop and native applications |
| [Codencoffee-Bold.woff](Codencoffee-Bold.woff) | Web fallback |
| [fonts/Codencoffee-Bold.woff2](fonts/Codencoffee-Bold.woff2) | Recommended web delivery |

## Character coverage

- Uppercase: A–Z
- Lowercase: a–z
- Digits: 0–9
- Printable ASCII punctuation: U+0021–U+007E
- Additional Unicode: ₹ × ÷ ¿ ¡

### Full glyph atlas

Every mapped glyph is shown individually with its character, Unicode code point, and glyph name in the [interactive glyph atlas](proof/glyph-atlas.html). The vector contact sheet is also available below.

<p align="center"><img src="proof/glyph-coverage.svg" alt="All font glyphs with Unicode labels" width="100%"></p>

### Original screenshot references

The uppercase, lowercase, digit and punctuation source crops are stored in [source-references/](source-references/). The glyph-by-glyph provenance notes are in [GLYPH-SOURCES.md](GLYPH-SOURCES.md).

## Web usage

~~~css
@font-face {
  font-family: "Codencoffee";
  src: url("/fonts/Codencoffee-Bold.woff2") format("woff2");
  font-style: normal;
  font-weight: 700;
  font-display: swap;
}

.codencoffee {
  font-family: "Codencoffee", sans-serif;
  font-weight: 700;
  font-synthesis: none;
}
~~~

Open the [web specimen](web/index.html) to preview the typeface in a browser.

## Native applications

- [Android](mobile/android/README.md)
- [iOS](mobile/ios/README.md)
- [Flutter](mobile/flutter/README.md)
- [React Native](mobile/react-native/README.md)

## Rebuild and validate

Requirements: Python 3.10+, fonttools, brotli, and Pillow.

~~~bash
python -m pip install fonttools brotli pillow
python tools/build_font.py
~~~

The script regenerates WOFF/WOFF2, the vector specimen, the labelled glyph atlas, and a QA report from the checked-in TrueType source.

## Project layout

~~~text
.
├── Codencoffee-Bold.ttf
├── Codencoffee-Bold.woff
├── fonts/Codencoffee-Bold.woff2
├── LICENSE
├── GLYPH-SOURCES.md
├── mobile/
├── proof/
│   ├── QA-REPORT.json
│   ├── glyph-atlas.html
│   ├── glyph-coverage.svg
│   └── specimen.svg
├── source-references/
├── tools/build_font.py
└── web/
~~~

## Accuracy and scope

This is an independent reconstruction from supplied raster screenshots, not the original editable source font. Raster images do not preserve the original font's exact control points, spacing data, or hinting, so pixel-identical recovery cannot be guaranteed. Characters not clearly represented in the references were completed to match the observed design language. This is a display face for names, headings, labels and branding, not long-form reading.

## License

Released under the [MIT License](LICENSE).
