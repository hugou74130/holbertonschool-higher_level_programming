#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    nb_args = len(argv) - 1

    if nb_args == 0:
        print("0 arguments.")
    elif nb_args == 1:
        print(f"1 argument:")
    else:
        print(f"{nb_args} arguments:")

    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
