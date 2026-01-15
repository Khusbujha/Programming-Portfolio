"""This program when run on command line reports how many arguments were provided."""

import sys


def main():
    num_args = len(sys.argv) - 1
    print(f"Number of arguments provided: {num_args}")
