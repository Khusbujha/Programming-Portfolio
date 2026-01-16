"""This program prints out all the words in a text file that are not found in the dictionary.
It is the implementation of the Unix command 'spell'."""

import sys
import string

if len(sys.argv) < 3:
    print("ERROR: ONE OR BOTH FILES NOT PROVIDED.")
    sys.exit()
text_file = sys.argv[1]
dict_file = sys.argv[2]
try:
    with open(dict_file, "r") as dic:
        dictionary = set(word.strip().lower() for word in dic)
    with open(text_file, "r") as txt:
        for line in txt:
            words = (
                line.translate(str.maketrans("", "", string.punctuation))
                .lower()
                .split()
            )
            for i in words:
                if i not in dictionary:
                    print(i)
except FileNotFoundError:
    print("ERROR: FILE NOT FOUND.")
except Exception as e:
    print("UNEXPECTED ERROR:", e)
