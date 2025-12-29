# This program takes a temperature in Celsius and prints whether it’s Cold (<10°C), Warm (10–25°C), or Hot (>25°C).
t = float(input("Enter temperature in Celsius: "))
if t < 10:
    print(f"{t}\u00b0C is Cold.")
elif t >= 10 and t <= 25:
    print(f"{t}\u00b0C is Warm.")
else:
    print(f"{t}\u00b0C is Hot.")
