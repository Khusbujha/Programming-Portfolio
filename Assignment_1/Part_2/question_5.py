# This program accepts three numbers from the user and prints the largest among them.
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
if n1 >= n2 and n1 >= n3:
    print(f"The largest number is: {n1}")
elif n2 >= n1 and n2 >= n3:
    print(f"The largest number is: {n2}")
else:
    print(f"The largest number is: {n3}")
