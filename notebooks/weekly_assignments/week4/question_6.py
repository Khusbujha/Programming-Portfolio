"""This program reads a temperature in Centigrade format (for example, 32C) and displays the equivalent
temperature in Fahrenheit."""

temp = input("Enter temperature in celcius(e.g. 32C): ")
value = float(temp[:-1])
fahrenheit = (value * 9 / 5) + 32
print(f"{fahrenheit}F")
