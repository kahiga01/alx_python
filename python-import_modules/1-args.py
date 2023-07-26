# number_and_list_of_args.py

import sys

def print_arguments(arguments):
    num_arguments = len(arguments)
    print(f"Number of argument(s): {num_arguments}", end="")
    
    if num_arguments == 0:
        print(":", end="")
    elif num_arguments == 1:
        print(", followed by:", end="")
    else:
        print("s, followed by:", end="")
    
    print()

    for idx, arg in enumerate(arguments, start=1):
        print(f"{idx}: {arg}")

if __name__ == "__main__":
    print_arguments(sys.argv[1:])

