import sys

def print_arguments():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print("Number of argument(s): {}".format(num_arguments), end="")
    if num_arguments == 0:
        print(".")
    elif num_arguments == 1:
        print(", argument:", end="")
    else:
        print(", arguments:", end="")
    
    print()

    for i, arg in enumerate(arguments, 1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()
