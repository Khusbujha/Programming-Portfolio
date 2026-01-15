"""This is the final modified version of question_4.py so that it executes until the user successfully chooses a password. That is, if the password chosen fails any of the checks, the
program returns to asking for the password the first time."""

while True:
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
        break
