# Number Formats

The number format used to display a Parameter is set in the **Format string** box of the [Conversion Properties](conversions/conversion-properties.md) dialog box. If the parameter properties can be edited, the format can be overridden in the **Format override** box on the [Conversion tab](conversion-tab.md) of the Parameter Properties dialog box. Axis formats are overridden on the [Conversion tab](axis-properties/axis-properties-conversion.md) of the Axis Properties dialog box.

The format string is a subset of the print format used in the 'C' programming language:

`%[flag][width][.precision][type]`

| Field | Description |
|---|---|
| **%** | Required. The format string must start with `%`. Text before or after the format is not accepted when you enter a format in System Monitor. |
| *flag* | Optional. Modifies the way the number is displayed: `+` shows the sign of the number; `-` left-justifies the number within the width; `0` shows leading zeros; a space shows a space in front of positive numbers; `#` uses the alternate form (for example a `0x` prefix on hexadecimal numbers). |
| *width* | Optional. The minimum total number of characters, including the decimal point and any digits after it. |
| *.precision* | Optional. For floating-point types, the number of digits after the decimal point. Not allowed with the `c` and `C` types. |
| *type* | The format code, optionally preceded by a size modifier such as `l` (for example `%6.2lf`). |

The main format codes are:

| Code | Format |
|---|---|
| `f` | Floating point |
| `e`, `E` | Floating point in exponent form |
| `g`, `G` | Floating point, in the shorter of `f` or `e` form |
| `d`, `i` | Signed integer |
| `u` | Unsigned integer |
| `x` | Hexadecimal (lower case) |
| `X` | Hexadecimal (upper case) |

Two special formats are also available:

| Format | Displays the value as |
|---|---|
| `%qIP` | An IP address |
| `%qLId` | A lifing ID |

If the format string is not valid, the message *Please enter a valid format string.* is shown.

With the integer and hexadecimal codes, the value is converted to a whole number (the fractional part is dropped) before it is displayed. Leading spaces are removed from the displayed value, so padding to a width is only visible when the `0` flag is used.

**Examples:** `%.2f` displays 3.14159 as `3.14`; `%d` displays 25.7 as `25`; `%04X` displays 255 as `00FF`.

**See also:** [Conversion Properties](conversions/conversion-properties.md); [Parameter Properties – Conversion tab](conversion-tab.md)
