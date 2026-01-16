"""This program consists of a function that checks if the given integer is a prime number."""


def prime(n):
    if n < 1:
        return "Enter a positive integer."
    elif n == 1:
        return "Is neither prime nor composite."
    else:
        for i in range(2, n):
            if n % i == 0:
                return "Composite"
        return "Prime"


print("9 = ", prime(9))
print("-8 =", prime(-8))
print("1 =", prime(1))
