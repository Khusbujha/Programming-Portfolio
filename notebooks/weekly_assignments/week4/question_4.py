"""This program consists of a function that takes a string parameter and returns it with the last character removed. (if the string consists of one or fewer characters, it returns it unchanged.)"""


def remove_last_char(string):
    if len(string) <= 1:
        return string
    else:
        return string[:-1]


# Testing the function
print(remove_last_char("Hello, World!"))
print(remove_last_char("A"))
print(remove_last_char(""))
