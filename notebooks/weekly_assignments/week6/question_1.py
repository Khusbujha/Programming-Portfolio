"""This program has a function that accepts a positive integer as a parameter and then returns representation of that number in binary (base 2)."""


def decimal_to_binary(n):
    if n < 0:
        print("Error: Negative numbers are NOT allowed.")
    else:
        return bin(n)


num = int(input("Enter a positive integer:"))
print(f"Binary representation of {num}: {decimal_to_binary(num)}")
