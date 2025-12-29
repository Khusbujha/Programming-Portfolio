# This program takes an input from the user and displays whether the number is positive negative or zero.
n = input("Enter an integer:")
n = int(n)
if n < 0:
    print(n, "is a negative number.")
elif n > 0:
    print(n, "is a positive number.")
else:
    print(n, "is zero.")
