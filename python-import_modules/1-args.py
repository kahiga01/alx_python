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
    arguments = sys.argv[1:]
    print_arguments(arguments)

