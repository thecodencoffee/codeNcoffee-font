# Typography usage guide

Codencoffee is currently a **single-weight display face**. The recommended production setup is to pair it with the normal text font supplied by the target platform.

## Recommended roles

| UI role | Font |
| --- | --- |
| Brand wordmark, product name | Codencoffee Bold |
| Large page or screen title | Codencoffee Bold |
| Short section heading or badge | Codencoffee Bold |
| Paragraphs and descriptions | Platform UI sans-serif |
| Form fields, buttons and navigation | Platform UI sans-serif |
| Long documentation or dense data | Platform UI sans-serif |

Do not use Codencoffee Bold for an entire paragraph. Its condensed, cut-out letterforms are visually distinctive but are not designed for sustained reading at small sizes.

## Web

Include the stylesheet:

~~~html
<link rel="stylesheet" href="/path/to/web/codencoffee.css">
~~~

Then assign typography by role:

~~~html
<h1 class="codencoffee-display">Northstar</h1>
<p class="codencoffee-text">
  This paragraph uses the user's platform UI font for comfortable reading.
</p>
~~~

The original `.codencoffee` CSS class remains available as an alias for `.codencoffee-display`.

## Native applications

Use the bundled TTF for short display text, and the platform's default font for paragraphs and interface copy. See the implementation examples:

- [Android](mobile/android/README.md)
- [iOS](mobile/ios/README.md)
- [Flutter](mobile/flutter/README.md)
- [React Native](mobile/react-native/README.md)

## About a future text family

This repository does not currently contain a Regular or Medium Codencoffee style. A genuine text companion would need a separate drawing and spacing pass: less compressed proportions, open counters, distinct letterforms at small sizes, appropriate punctuation, and careful testing across screen sizes and languages. Simply changing the font's weight metadata or applying a CSS filter would not provide those design improvements.
