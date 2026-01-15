"""This program prompts the user to enter their name and if they don't enter anything the program responds "Hello, Stranger!", otherwise prints a greeting with the entered name."""

name = input("Please enter your name: ")
if name == "":
    print("Hello, Stranger!")
else:
    print(f"Hello, {name}!")
