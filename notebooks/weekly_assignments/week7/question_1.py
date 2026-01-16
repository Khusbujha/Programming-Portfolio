"""This program consists of a function that takes a string as a parameter and returns a sorted list of all unique letters used in the string."""


def sort_letters(s):
    letters = set(s)
    unique_letters = [chr for chr in letters if chr.isalpha()]
    return sorted(unique_letters)


print(sort_letters("Hello, World!"))
print(sort_letters("Python is fun."))
