#!/usr/bin/python3

if __name__ == "__main__":
    try:
        from variable_load_2 import a
        print("Correct output - case: a =", a)
    except ImportError:
        print("Correct output - case: a missing")
