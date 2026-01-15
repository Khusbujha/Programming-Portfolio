"""This program is modified version of question_7.py from week6 that takes arguments and works on command line."""

import sys
import statistics


def main():
    args = sys.argv[1:]
    if not args:
        print("No temperature readings provided.")
        return
    else:
        temps = [float(arg) for arg in args]
        print(f"Maximum temperature: {max(temps)}\u00b0")
        print(f"Minimum temperature: {min(temps)}\u00b0")
        print(f"Mean temperature: {statistics.mean(temps)}\u00b0")


if __name__ == "__main__":
    main()
