# iOS

1. Add `Codencoffee-Bold.ttf` to the Xcode project and ensure it is included in the app target.
2. Add the filename to `UIAppFonts` in `Info.plist`.
3. Use the registered PostScript font name, `Codencoffee-Bold`, for all text roles.

SwiftUI paragraph:

~~~swift
Text("Paragraphs, descriptions and long-form copy use Codencoffee Bold too.")
    .font(.custom("Codencoffee-Bold", size: 16))
    .lineSpacing(5)
~~~

Headings, labels, buttons and form fields should use the same custom font:

~~~swift
Button("Save changes") {
    // Handle the action.
}
.font(.custom("Codencoffee-Bold", size: 16))
~~~

For UIKit, create a UIFont with `UIFont(name: "Codencoffee-Bold", size: 16)` and apply it to labels, text views, text fields and buttons.

This package contains one Bold style. It does not include a Regular or Medium file, so all text will retain the same bold appearance.
