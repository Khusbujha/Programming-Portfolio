"""This program decrypts the message encrypted by the method used in question_5.py."""

from question_5 import encryption


def decryption(encrypted, i):
    decrypted = encrypted[::i]
    return decrypted


msg = input("Enter the message:")
encrypted_msg, interval = encryption(msg)
decrypted_msg = decryption(encrypted_msg, interval)
print("Encrypted Message:", encrypted_msg)
print("Interval:", interval)
print("Decrpyted Message:", decrypted_msg)
