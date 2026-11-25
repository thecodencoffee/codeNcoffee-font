# Android

Copy `Codencoffee-Bold.ttf` into `app/src/main/res/font/codencoffee_bold.ttf` (use lowercase resource naming). Use it for short display text such as a product name or screen heading:

~~~xml
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:fontFamily="@font/codencoffee_bold"
    android:text="codeNcoffee" />
~~~

For Jetpack Compose, load the file with `Font(R.font.codencoffee_bold, FontWeight.Bold)`.

Keep paragraph and dense UI text in Android's normal sans-serif font. For example:

~~~xml
<TextView
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:fontFamily="sans-serif"
    android:text="Long descriptions and body copy should use the platform UI font." />
~~~

In Compose, leave `fontFamily` unset for body text so the platform default is used.
