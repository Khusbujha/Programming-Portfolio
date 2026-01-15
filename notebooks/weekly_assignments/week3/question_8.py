"""This program is the further modified verison of question_7.py. In this program if a negative number between -1 to -12 it produces the table of the positive number
backwards. That is, if the user enters -7, the program produces the table of 7 starting from 12 ending with 0
"""

num = int(
    input("Enter the number of the table you want (0-12, negative for backwards): ")
)
if abs(num) > 12:
    print("Error: Please enter a number between -12 and 12.")
else:
    if num >= 0:
        for i in range(13):
            result = num * i
            print(f"{num} x {i} = {result}")
    else:
        for i in range(12, -1, -1):
            result = abs(num) * i
            print(f"{abs(num)} x {i} = {result}")
