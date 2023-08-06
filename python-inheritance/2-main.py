#!/usr/bin/python3
inherits_from = __import__("2-inherits_from").inherits_from

# Define the object 'a'
a = True

# Check if 'a' is an instance of the specified classes and print the results
if inherits_from(a, int):
    print("{} is an instance of class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} is an instance of class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} is an instance of class {}".format(a, object.__name__))

