# React Native

Place the TTF in your app's font assets and link it using your framework's supported font-asset workflow. Use the font's PostScript family name in styles:

~~~jsx
<Text style={{ fontFamily: "Codencoffee-Bold", fontSize: 32 }}>
  codeNcoffee
</Text>
~~~

On Expo, register the TTF with `expo-font` and use the registered family key.
