import sys

def print_arguments(args):
    num_args = len(args)
    plural_suffix = 's' if num_args != 1 else ''
    argument_str = 'argument' if num_args == 1 else 'arguments'

    print(f"Number of argument{plural_suffix}: {num_args}, followed by:", end="")

    if num_args == 0:
        print(" .")
    else:
        print()
        for idx, arg in enumerate(args, start=1):
            print(f"{idx}: {arg}")

if __name__ == "__main__":
    test_cases = [
        "Hello",
        "Hello Holberton",
        "",
        "98 Battery street",
        "98 Battery street CA"
    ]

    for test_case in test_cases:
        arguments = test_case.split()
        print_arguments(arguments)
        print()

