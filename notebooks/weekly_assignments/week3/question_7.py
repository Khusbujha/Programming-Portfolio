"""This program is a modified version of question_6.py. In this program, user enters the number of the table they want (0-12)."""

num = int(input("Enter the number of the table you want (0-12): "))
if num < 0 or num > 12:
    print("Error: Please enter a number between 0 and 12.")
else:
    print("Times table of ", num)
    print("=================")
    for i in range(13):
        result = num * i
        print(f"{num} x {i} = {result}")
    print("=================")
