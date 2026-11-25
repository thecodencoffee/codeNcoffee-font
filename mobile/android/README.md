# Android

Generate the TTF with the repository build script, then copy `Codencoffee-Bold.ttf` into `app/src/main/res/font/codencoffee_bold.ttf` (use lowercase resource naming). Register this one typeface and use it for every text role, including paragraphs, labels and controls.

For a TextView:

~~~xml
<TextView
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:fontFamily="@font/codencoffee_bold"
    android:text="Paragraphs and dense interface copy also use Codencoffee Bold."
    android:textSize="16sp"
    android:lineSpacingMultiplier="1.15" />
~~~

For Jetpack Compose, create one family and apply it to all text:

~~~kotlin
val Codencoffee = FontFamily(
    Font(R.font.codencoffee_bold, FontWeight.Bold)
)

Text(
    text = "Paragraphs and dense interface copy also use Codencoffee Bold.",
    fontFamily = Codencoffee,
    fontWeight = FontWeight.Bold,
    fontSize = 16.sp,
    lineHeight = 24.sp
)
~~~

Apply the same `fontFamily` and `fontWeight` to text in buttons, navigation, form fields and other components. Configure your app theme's typography to use this family if you want it applied consistently without repeating the style.

This package contains one Bold style. It does not include a Regular or Medium file, so all text will retain the same bold appearance.
