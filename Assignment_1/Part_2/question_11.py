# This program find the Euclidean distance between two coordinates. Take both the coordinates from the user as input.
import math

print("Euclidean Distance Calculator")
x1 = float(input("Enter x1:"))
x2 = float(input("Enter x2:"))
y1 = float(input("Enter y1:"))
y2 = float(input("Enter y2:"))
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"The Euclidean Distance is: {d:.2f}")
