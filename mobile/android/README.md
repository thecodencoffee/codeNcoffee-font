# Android

Copy `Codencoffee-Bold.ttf` into `app/src/main/res/font/codencoffee_bold.ttf` (use lowercase resource naming).

~~~xml
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:fontFamily="@font/codencoffee_bold"
    android:text="codeNcoffee" />
~~~

For Jetpack Compose, load the file with `Font(R.font.codencoffee_bold, FontWeight.Bold)`.
