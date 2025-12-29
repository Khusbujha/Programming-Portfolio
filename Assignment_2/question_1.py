"""This program has a function while takes string as an input and returns:
The number of digits,
The number of alphabets,
The number of special characters in that string."""


def str_count(word):
    a = 0
    d = 0
    c = 0
    for i in word:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            d += 1
        else:
            c += 1  # This includes special characters, punctuations and spaces.
    return a, d, c


string = input("Enter a string:")
alpha, digit, char = str_count(string)
print("\nOriginal string:", string)
print("Number of digits:", digit)
print("Number of alphabets:", alpha)
print("Number of special characters:", char)
