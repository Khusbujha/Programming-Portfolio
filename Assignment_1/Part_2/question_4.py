# This program prompts the user for an age, and prints whether the person is a child (below 13), teenager (13–19), or adult (20 and above).
a = int(input("Enter your age: "))
if a < 13:
    print("You are a child.")
elif 13 <= a <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")
