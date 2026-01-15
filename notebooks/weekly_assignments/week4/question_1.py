"""This program consists of a function that accepts a single integer as a parameter and returns True if the integer
is in the range 0 to 100 (inclusive), or False otherwise."""


def is_valid_number(num):
    if 0 <= num <= 100:
        return True
    else:
        return False


value = int(input("Enter an integer: "))
print(is_valid_number(value))
