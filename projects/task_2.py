"""
This is a project for a password system that checks the strength of password through security checks.
This is an interactive password system program that runs on CLI.
The functions in this program are modular and reusable for any password verification systems.
"""

import random


def pw_length(password):
    """
    Checks whether the password length is at least 9 characters.
    Returns True if valid, otherwise False.
    """
    return len(password) >= 9


def letter_verification(password):
    """
    Prompts the user to enter the letter from a random position in the password.
    Returns True if entered correctly, otherwise False.
    """
    pzsn = random.randint(1, len(password))
    print("==================================")
    ltr = input(f"Enter the letter at position {pzsn}:")
    if ltr == password[pzsn - 1]:
        print("-------")
        print("Correct")
        print("-------")
        return True
    else:
        print("**********************")
        print("Security Check Failed.")
        print("**********************")
        return False


def pw_sec_check():
    """
    This is the main function that runs the security check.
    Exits in case even one of the security requirements are not satisfied.
    """
    print("===============================")
    pw = input("Enter your password:")
    print("===============================")
    if not pw_length(pw):
        print("****************************")
        print("THE PASSWORD IS TOO SHORT!!!")
        print("****************************")
        return
    for i in range(3):
        if not letter_verification(pw):
            return
    print("========================")
    print("Security check passed!!!")
    print("========================")


if __name__ == "__main__":
    pw_sec_check()
