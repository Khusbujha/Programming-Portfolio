"""This program determines whether a given number is a palindrone number or not."""

n = int(input("Enter an integer:"))
m = n
r = 0
while m > 0:
    digit = m % 10
    r = r * 10 + digit
    m //= 10
if n == r:
    print(n, " is a palindrome.")
else:
    print(n, "is not a  palindrome.")
