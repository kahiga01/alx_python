import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print("Number of argument(s):", num_arguments, end=" ")
    if num_arguments == 0:
        print(".")
    elif num_arguments == 1:
        print("argument:")
    else:
        print("arguments:")

    for i, arg in enumerate(arguments, 1):
        print("{}: {}".format(i, arg))

