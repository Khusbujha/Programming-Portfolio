"""This program consists of a function that takes an integer as its parameter and returns the factors of that integer."""


def factors_cal(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


num = int(input("Enter a positive integer:"))
print(f"Factors of {num} = {factors_cal(num)}")
