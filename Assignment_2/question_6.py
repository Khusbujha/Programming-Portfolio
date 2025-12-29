"""This program prompts the user for 10 integer inputs and stores only unique values in a list lastly, displays the sorted list of unique numbers at the end."""

n = []
for x in range(10):
    i = int(input("Enter an integer:"))
    if i not in n:
        n.append(i)
print("The final list:", n)
