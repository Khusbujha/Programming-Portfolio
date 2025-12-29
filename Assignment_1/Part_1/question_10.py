# This program prints the Unicode characters corresponding to the codes: 80,121,116,104,111,110.
codes = [80, 121, 116, 104, 111, 110]
result = "".join(chr(code) for code in codes)
print("Unicode Characters:", result)
