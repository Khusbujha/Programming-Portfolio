# This program accepts a string and calculates the number of digits and letters.
a = input("Enter a string: ")
digits = 0
letters = 0
for char in a:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
print("Letters:", letters)
print("Digits:", digits)
