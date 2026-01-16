"""This program contains a function that encrypts the string by obfuscation."""


def obfuscation(s):
    a = s.replace(" ", "")
    encrypt = a[::-1]
    return encrypt


print(obfuscation("Hello World"))
print(obfuscation("Python is fun"))
