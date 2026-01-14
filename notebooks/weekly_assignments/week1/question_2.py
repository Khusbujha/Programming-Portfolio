"""This program prompts the user for temperature in Celsius and displays it's corresponding temperature in Fahrenheit."""

c = input("Enter the temperature in Celsius:")
c = int(c)
f = (c * 9 / 5) + 32
print(f"{c}\u00b0C is equivalent to {f}\u00b0F.")
