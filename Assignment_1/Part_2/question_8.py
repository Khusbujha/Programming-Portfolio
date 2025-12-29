# This program takes a character input and display whether it is a vowel or consonant.
a = input("Enter a character: ").lower()
vowels = "aeiou"
if a in vowels:
    print(f"{a} is a vowel.")
else:
    print(f"{a} is a consonant.")
