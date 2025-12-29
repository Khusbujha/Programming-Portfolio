"""This program performs the following tasks on dictionaries in the program:
(a) Merge all dictionaries into a single one.
(b) Add a new pair 'r': 35.
(c) Double all the values in the resulting dictionary.
(d) Delete the key 'y'.
(e) Compute and print the average value of all remaining items.
"""

a = {"x": 5, "y": 10}
b = {"z": 15, "w": 20}
c = {"p": 25, "q": 30}
print("Original dictionaries:")
print("a=", a)
print("b=", b)
print("c=", c)
new_dict = {**a, **b, **c}
print("Merged dictionary:", new_dict)
new_dict["r"] = 35
print("After adding 'r':", new_dict)
new_dict = {k: v * 2 for k, v in new_dict.items()}
print("Dictionary after doubling the values:", new_dict)
new_dict.__delitem__("y")
print("Dictionary after deleting key 'y': ", new_dict)
avg = sum(new_dict.values()) / len(new_dict)
print("The average of all the values in the dictionary:", round(avg, 2))
