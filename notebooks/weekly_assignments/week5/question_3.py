"""This program takes a bunch of command-line arguments, and then prints out the shortest. (In case of more than one shortest length it prints any one of them.)"""

import sys


def main():
    args = sys.argv[1:]
    if not args:
        print("No arguments provided.")
        return
    args.sort(key=len)
    print(f"The shortest argument is: {args[0]}")


if __name__ == "__main__":
    main()
