# React Native

Place the TTF in your app's font assets and link it using your framework's supported font-asset workflow. Use the font's PostScript family name for short display text:

~~~jsx
<Text style={{ fontFamily: "Codencoffee-Bold", fontSize: 32 }}>
  codeNcoffee
</Text>
~~~

For paragraphs, descriptions and dense interface copy, leave `fontFamily` unset so React Native uses the platform's default UI font:

~~~jsx
<Text style={{ fontSize: 16, lineHeight: 24 }}>
  Long descriptions and body copy should remain easy to read.
</Text>
~~~

On Expo, register the TTF with `expo-font` and use the registered family key.
