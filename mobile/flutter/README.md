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

Use `TextStyle(fontFamily: 'Codencoffee', fontWeight: FontWeight.w700)`.
