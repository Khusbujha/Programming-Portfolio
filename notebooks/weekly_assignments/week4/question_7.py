"""This program accepts six temperature values and displays the maximum, minimum, and mean of the entered
values."""

import statistics

temperatures = []
for i in range(6):
    temp = input(f"Enter temperature number {i+1} in celcius(e.g. 25C): ")
    value = float(temp[:-1])
    temperatures.append(value)

print("Maximum temperature:", max(temperatures))
print("Minimum temperature:", min(temperatures))
print("Mean temperature:", statistics.mean(temperatures))
