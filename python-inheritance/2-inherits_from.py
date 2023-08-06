#!/usr/bin/python3
"""This function determines if an object is an instance of a class that inherits from the given class."""


def inherits_from(obj, a_class):
    """Check if the provided object is an instance of a class that is derived (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to be compared against.

    Returns:
        bool: True if the object is an instance of a class that inherits from the specified class,
              otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class

