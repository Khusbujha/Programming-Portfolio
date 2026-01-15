"""This program consists of two functions one converts a temperature measure in degrees centigrade into the equivalent in fahrenheit, and another does the reverse conversion."""


def celcius_to_fahrenheit(cel):
    return (cel * 9 / 5) + 32


def fahrenheit_to_celcius(fah):
    return (fah - 32) * 5 / 9


print("15\u00b0C =", celcius_to_fahrenheit(15), "\u00b0F")
print("-40\u00b0F =", fahrenheit_to_celcius(-40), "\u00b0C")
