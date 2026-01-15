"""This program is a re-modified version of greetings program(question_1.py) from week2. This program ensures the first
letter of the name entered is always in uppercase with the rest in lowercase. This should happen even if the user entered
their name differently. So if the user entered arthur, ARTHUR, or even arTHur the name should be displayed as Arthur.
"""

name = input("Enter your name:")
if name == "":
    print("Hello, Stranger!")
else:
    capitalized_name = name.capitalize()
    print("Hello,", capitalized_name)
