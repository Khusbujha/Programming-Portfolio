# This code calculate the sum of digits in the number 4729.
n = 4726
s = 0
while n > 0:
    digit = n % 10
    s += digit
    n = n // 10
print("The sum of digits in the number 4726 is", s)
