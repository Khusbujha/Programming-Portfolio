"""This program compares two files and reports if there sre differences in their contents (if any). It is implementation of the Unix 'diff' command."""

import sys

if len(sys.argv) < 3:
    print("ERROR: PROVIDE TWO FILE NAMES.")
    sys.exit()
file1, file2 = sys.argv[1], sys.argv[2]
try:
    with open(file1, "r") as a, open(file2, "r") as b:
        if a.read() == b.read():
            print("There are no differences in the two files.")
        else:
            print("There are differences in the contents of the two files.")
except FileNotFoundError:
    print("ERROR: ONE OR MORE FILES NOT FOUND.")
except Exception as e:
    print("UNEXPECTED ERROR:", {e})
