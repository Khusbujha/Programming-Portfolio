"""This program is the modified version of question_2.py where the password must be 8-12 characters (inclusive) long."""

pw = input("Enter new password:")
pw_confirm = input("Re-enter new password:")
if pw != pw_confirm:
    print("Error: Entered passwords do not match.")
elif len(pw) < 8 or len(pw) > 12:
    print("Error: Password must be between 8-12 characters long.")
else:
    print("Password Set.")
