# React Native

Place the TTF in your app's font assets and link it using your framework's supported font-asset workflow. Use the font's PostScript family name, `Codencoffee-Bold`, for every text role.

Paragraph example:

~~~jsx
<Text
  style={{
    fontFamily: "Codencoffee-Bold",
    fontSize: 16,
    lineHeight: 25,
  }}
>
  Paragraphs and dense interface copy also use Codencoffee Bold.
</Text>
~~~

Use the same `fontFamily: "Codencoffee-Bold"` for headings, buttons, navigation, form fields and compact UI labels. For consistency, create a shared text component that applies the Codencoffee family by default.

On Expo, register the TTF with `expo-font` and use the registered family key in all text styles.

This package contains one Bold style. It does not include a Regular or Medium file, so all text will retain the same bold appearance.
