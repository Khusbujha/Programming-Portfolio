"""This program searches a file for lines that contain a particular string.
It is the implementation of Unix 'grep' command."""

import sys

if len(sys.argv) < 3:
    print("ERROR: FILE NAME OR STRING NOT PROVIDED!!!")
    sys.exit()
string = sys.argv[1]
file_name = sys.argv[2]
try:
    with open(file_name, "r") as f:
        for lines in f:
            if string in lines:
                print(lines.rsplit())
except FileNotFoundError:
    print("ERROR: FILE NOT FOUND!!!")
except Exception as e:
    print("UNEXPECTED ERROR:", {e})
