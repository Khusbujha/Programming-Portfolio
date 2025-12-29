"""This program checks whether a given number is a perfect number or not.
Eg. 6 = 1 + 2 + 3"""

n = int(input("Enter a integer:"))
div = [i for i in range(1, n - 1) if n % i == 0]
s = 0
for i in div:
    s += i
if s == n:
    print("The entered number is a perfect number.")
else:
    print("The entered number is not a perfect number.")
