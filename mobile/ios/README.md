# iOS

1. Add `Codencoffee-Bold.ttf` to the Xcode project and ensure it is included in the app target.
2. Add the filename to `UIAppFonts` in `Info.plist`.
3. Use the registered PostScript font name in UIKit or SwiftUI for short display text.

~~~swift
Text("codeNcoffee")
    .font(.custom("Codencoffee-Bold", size: 36))
~~~

Use the system font for paragraphs, descriptions and dense UI copy:

~~~swift
Text("Long descriptions and body copy should remain comfortable to read.")
    .font(.system(size: 16))
~~~
