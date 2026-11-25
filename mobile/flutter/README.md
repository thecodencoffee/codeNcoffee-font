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

Use it for short display text:

~~~dart
Text(
  'codeNcoffee',
  style: const TextStyle(
    fontFamily: 'Codencoffee',
    fontWeight: FontWeight.w700,
    fontSize: 32,
  ),
)
~~~

For paragraphs and dense UI text, omit `fontFamily` so Flutter uses the platform's default text family:

~~~dart
const Text(
  'Long descriptions and body copy should use the default platform font.',
  style: TextStyle(fontSize: 16, height: 1.5),
)
~~~
