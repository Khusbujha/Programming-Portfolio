"""This program consists of a function that encrypts the string making it seem like a random text. It radomly generates an interval (between 2 and 20), spaces the
message out accordingly, and fills the gap with random letters. The function also returns the encrypted message and interval used.
"""

import random
import string


def encryption(msg):
    interval = random.randint(2, 20)
    encrypted_lst = []
    for m in msg:
        encrypted_lst.append(m)
        for i in range(interval - 1):
            encrypted_lst.append(random.choice(string.ascii_lowercase))
    encrypted = "".join(encrypted_lst)
    return encrypted, interval


message = input("Enter the message:")
encrypted_msg, interval_used = encryption(message)
print("Encrypted Message:", encrypted_msg)
print("Interval:", interval_used)
