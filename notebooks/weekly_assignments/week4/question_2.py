"""This program consists of a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string."""


def count_upper_lower(string):
    upper = 0
    lower = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower


sentence = input("Enter a string: ")
u, l = count_upper_lower(sentence)
print("Uppercase letters:", u)
print("Lowercase letters:", l)
