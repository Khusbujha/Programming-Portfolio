"""This program reads a text file given as a command line argument, reads and prints each line of the file prefixed with its line number.
It is an implementation of Unix 'nl' command."""

import sys

if len(sys.argv) < 2:
    print("ERROR: NO FILE NAME PROVIDED!!!")
    sys.exit()
file_name = sys.argv[1]
try:
    with open(file_name, "r") as f:
        for num, line in enumerate(f, start=1):
            print(f"{num}\t{line.rstrip()}")
except FileNotFoundError:
    print("ERROR: FILE NOT FOUND!!!")
except Exception as e:
    print("UNEXPECTED ERROR:", {e})
