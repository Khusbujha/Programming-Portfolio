# This program converts Fahrenheit to Celsius and display the result rounded to two decimal places.
f = input("Enter the temperature in Fahrenheit:")
f = float(f)
c = round(((f - 32) * 5 / 9), 2)
print(f"{f}\u00b0F is equal to {c}\u00b0C.")
