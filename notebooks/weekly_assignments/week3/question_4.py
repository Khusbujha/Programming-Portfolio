"""This program is further modified from question_3.py so that the chosen password cannot be one of a list of common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']"""

pw = input("Enter new password:")
pw_confirm = input("Re-enter new password:")
BAD_PASSWORDS = ["password", "letmein", "sesame", "hello", "justinbieber"]
if pw != pw_confirm:
    print("Error: Entered passwords do not match.")
elif pw.lower() in BAD_PASSWORDS:
    print("Error: Please choose a stronger password.")
elif len(pw) < 8 or len(pw) > 12:
    print("Error: Password must be between 8-12 characters long.")
else:
    print("Password Set.")
