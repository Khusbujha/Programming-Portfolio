"""This program takes the name of a file as a command-line argument, and creates a backup copy of that file with the same contents but a different name."""

import sys
import shutil

if len(sys.argv) < 2:
    print("Error: File name not provided.")
    sys.exit()
file_name = sys.argv[1]
backup = file_name + ".bkp"
try:
    shutil.copy(file_name, backup)
    print("Backup created:", backup)
except FileNotFoundError:
    print("Error: File not found!!!")
