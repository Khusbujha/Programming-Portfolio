# This program asks the user to enter a number between 1 and 7, and displays the corresponding day of the week (1 for Sunday, 2 for Monday, etc.).
d = int(input("Enter a number between 1 and 7: "))
if d == 1:
    print("Sunday")
elif d == 2:
    print("Monday")
elif d == 3:
    print("Tuesday")
elif d == 4:
    print("Wednesday")
elif d == 5:
    print("Thursday")
elif d == 6:
    print("Friday")
elif d == 7:
    print("Saturday")
else:
    print("Invalid input! Please enter a number between 1 and 7.")
