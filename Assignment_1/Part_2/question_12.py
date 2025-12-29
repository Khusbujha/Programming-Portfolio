# This program finds the simple interest when the value of principle, rate of interest and time period is provided by the user.
p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period in years: "))
s = (p * r * t) / 100
print("The simple interest is:", s)
