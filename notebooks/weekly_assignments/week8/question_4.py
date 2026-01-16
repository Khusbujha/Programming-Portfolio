"""This program counts the number of lines and characters in a file. It is implementation of Unix 'wc' command."""

import sys

if len(sys.argv) < 2:
    print("ERROR: NO FILE NAME PROVIDED!!!")
    sys.exit()
file_name = sys.argv[1]
try:
    with open(file_name, "r") as f:
        line_count = len(f.readlines())
        f.seek(0)
        char_count = len(f.read())
    print("File count.")
    print("Lines:", line_count)
    print("Characters:", char_count)
except FileNotFoundError:
    print("ERROR: FILE NOT FOUND.")
except Exception as e:
    print("UNEXPECTED ERROR:", e)
