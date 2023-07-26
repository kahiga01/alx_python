import sys

# Get the number of arguments passed to the script
num_args = len(sys.argv) - 1

# Print the number of arguments and the list of arguments
print(f"Number of argument{'s' if num_args != 1 else ''}: {num_args}{'' if num_args == 0 else ':'}")
for i, arg in enumerate(sys.argv[1:], start=1):
    print(f"{i}: {arg}")

# If no arguments were passed, print a dot
if num_args == 0:
    print(".")
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
