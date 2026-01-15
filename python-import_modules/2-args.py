from sys import argv

if __name__ == "__main__":
    nb_args = len(argv) - 1
    if nb_args == 0:
        print("0 arguments.")
    elif nb_args == - 1:
        print(f"1 arguemnts:")
    else:
        print(f"{nb_args} argumetns:")
    for i in range(1, len(argv)):
        position = i
        print(f"{position}:{argv[i]}")
