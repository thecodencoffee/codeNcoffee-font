# Typography usage guide

Use **Codencoffee Bold as the one typeface throughout the website or application**. The repository intentionally ships one style and does not require a Regular, Medium or separate system-font companion.

## One font for every role

| UI role | Font |
| --- | --- |
| Brand wordmark and product name | Codencoffee Bold |
| Page and screen titles | Codencoffee Bold |
| Section headings and labels | Codencoffee Bold |
| Paragraphs and descriptions | Codencoffee Bold |
| Form fields, buttons and navigation | Codencoffee Bold |
| Menus, tables, lists and dense UI | Codencoffee Bold |
| Documentation and other long-form copy | Codencoffee Bold |

All text uses the same Bold outlines. This is a deliberate single-style setup, not a complete multi-weight family. The typeface will therefore keep its bold visual character in paragraphs and dense UI too.

For longer text, start around 16px with a 1.5–1.65 line height. For compact UI, test at 14px or larger where possible. Avoid shrinking text to fit; adjust layout, wrapping and spacing instead. Check paragraphs, small labels and controls on real device sizes before shipping.

## Web

Include the stylesheet:

~~~html
<link rel="stylesheet" href="/path/to/web/codencoffee.css">
~~~

The stylesheet sets Codencoffee as the default font and applies it to common controls. The two role classes also resolve to the same font:

~~~html
<h1 class="codencoffee-display">Northstar</h1>
<p class="codencoffee-text">
  This paragraph uses Codencoffee Bold too.
</p>
<button>Continue</button>
~~~

The original `.codencoffee` class remains available as an alias for `.codencoffee-display`. Both `.codencoffee-display` and `.codencoffee-text` load the same Codencoffee face.

## Native applications

Register the bundled TTF and apply Codencoffee Bold to every text component, including paragraphs, descriptions, form fields and dense interface copy. See the implementation examples:

- [Android](mobile/android/README.md)
- [iOS](mobile/ios/README.md)
- [Flutter](mobile/flutter/README.md)
- [React Native](mobile/react-native/README.md)

## Character coverage

The current font maps uppercase and lowercase Latin, digits, printable ASCII punctuation, and the additional symbols ₹ × ÷ ¿ ¡. It does not yet include every Unicode character or writing system. When a string contains a character that Codencoffee does not contain, the platform may draw that character with a fallback font. That limitation cannot be fixed through CSS or app configuration; the missing glyph must be designed and added to the font.
