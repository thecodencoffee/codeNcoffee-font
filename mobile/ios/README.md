# iOS

1. Add `Codencoffee-Bold.ttf` to the Xcode project and ensure it is included in the app target.
2. Add the filename to `UIAppFonts` in `Info.plist`.
3. Use the registered PostScript font name in UIKit or SwiftUI.

~~~swift
Text("codeNcoffee")
    .font(.custom("Codencoffee-Bold", size: 36))
~~~
