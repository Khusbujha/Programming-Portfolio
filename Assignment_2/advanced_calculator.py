"""This program performs various calculation with various functions."""


def sq_rt(i):
    import math

    r = math.sqrt(i)
    return r


def abs(i):
    if i < 0:
        r = -i
    else:
        r = i
    return r


def fl_div(i, j):
    return i // j


def per(i, j):
    return (i / 100) * j


def avg(i, j):
    return (i + j) / 2


print("Welcome to the advanced calculator.")
print("***********************************")
print("\n1.Square root")
print("2.Absolute value")
print("3.Floor division")
print("4.Percentage(first number as a  persent of the second)")
print("5.Average of two numbers")
n = int(input("\nEnter corresponding number according to the operation:"))
if n == 1:
    a = int(input("Enter the number:"))
    print("\nThe square root of the entered number is", sq_rt(a))
elif n == 2:
    a = float(input("Enter a number:"))
    print("\nThe absolute value of the number is", abs(a))
elif n == 3:
    a1 = float(input("Enter the divident:"))
    a2 = float(input("Enter the divider:"))
    print("\nThe result is", int(fl_div(a1, a2)))
elif n == 4:
    a1 = float(input("Enter the percentage:"))
    a2 = float(input("Enter the base value:"))
    print("\nThe result is", per(a1, a2))
elif n == 5:
    a1 = float(input("Enter the first number:"))
    a2 = float(input("Enter the second number:"))
    print("\nThe average of the two numbers is", avg(a1, a2))
else:
    print("Invalid Choice!")
