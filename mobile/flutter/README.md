# Flutter

Place the TTF in `assets/fonts/Codencoffee-Bold.ttf` and register it in `pubspec.yaml`:

~~~yaml
flutter:
  fonts:
    - family: Codencoffee
      fonts:
        - asset: assets/fonts/Codencoffee-Bold.ttf
          weight: 700
~~~

Set it as the application theme's default font family:

~~~dart
MaterialApp(
  theme: ThemeData(
    fontFamily: 'Codencoffee',
  ),
  home: const YourScreen(),
)
~~~

Use the same family for paragraphs and dense UI:

~~~dart
const Text(
  'Paragraphs and dense interface copy also use Codencoffee Bold.',
  style: TextStyle(
    fontFamily: 'Codencoffee',
    fontWeight: FontWeight.w700,
    fontSize: 16,
    height: 1.6,
  ),
)
~~~

Use `fontFamily: 'Codencoffee'` for custom text styles in buttons, form fields, navigation and other widgets too. This package contains one Bold style, so all text keeps the same bold appearance.
