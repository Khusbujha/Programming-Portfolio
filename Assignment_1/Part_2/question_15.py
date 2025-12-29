# This program creates a number guessing game that picks a random number that the user has to guess in 5 attempts.
import random


def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the number guessing game.")
    print("I have selected number from 1 to 100. I bet you can't guess it?")
    print("You have 5 attempts to guess it. Have a fun time guessing!")

    while attempts < 5:
        try:
            player_guess = int(input("Enter your guess: "))
            attempts += 1
            if player_guess < secret_number:
                print("Too low! Try a higher guess.")
            elif player_guess > secret_number:
                print("Too high! Try a lower guess.")
            else:
                print(
                    f"Congratulations! You guessed the number in {attempts} attempts."
                )
        except ValueError:
            print("Invalid input! Please enter an integer!")
        if attempts < 5:
            print(f"{5-attempts} attempts remain.")
        else:
            print("Game Over! You've used all your attempts.")
            print(f"The correct number was {secret_number}.")


guessing_game()
