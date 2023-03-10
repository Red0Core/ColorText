# ColorText
This is a one-module Builder that creates colored text.
It works depending on your terminal, which may or may not support certain colors.
It's all based on ANSI escape code.

It's very easy to use!
```
from color_text import ColorBuilder

print(ColorBuilder().red_color().dark_color().italic_mode().green_background().build("some text"))
```

After adjusting, use .build("some text") to generate the resulting multicolored text

RGB colors have an advantage over other colors, that is, if you make yourself RGB text, the other settings will not affect this text.
RGB color has a range from 0 to 255.

The background and the text itself are set separately from each other, but also via Builder
