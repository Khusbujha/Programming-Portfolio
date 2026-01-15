"""This program simulates the way in which a user might choose a password. The program prompts for a new password and then, prompts again. If the
two passwords entered are the same the program says "Password Set", otherwise it reports an error.
"""

pw = input("Enter new password:")
pw_confirm = input("Re-enter new password:")
if pw == pw_confirm:
    print("Password Set.")
else:
    print("Error: Entered passwords do not match.")
