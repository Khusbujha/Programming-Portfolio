"""This program is a modified version of question_7.py. This program allows the user to enter any number of temperatures. The input process stops when the user
presses Enter without typing a value."""

temperatures = []
while True:
    temp = input("Enter temperature in format '45C' (or press Enter to stop): ")
    if temp == "":
        break
    value = float(temp[:-1])
    temperatures.append(value)
print("Maximum temperature:", max(temperatures))
print("Minimum temperature:", min(temperatures))
print("Mean temperature:", sum(temperatures) / len(temperatures))
