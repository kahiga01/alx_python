def is_same_class(obj, a_class):
    """
    Check if the given object is exactly an instance of the specified class.

    :param obj: The object to check.
    :type obj: Any
    :param a_class: The class to compare with.
    :type a_class: type
    :return: True if obj is exactly an instance of a_class, otherwise False.
    :rtype: bool
    """
    return type(obj) is a_class

# Test cases
a = 1
print(is_same_class(a, int))  # Output: True

a = True
print(is_same_class(a, int))  # Output: False

a = 3.14
print(is_same_class(a, int))  # Output: False

a = True
print(is_same_class(a, object))  # Output: True

a = None
print(is_same_class(a, object))  # Output: True

a = None
print(is_same_class(a, list))  # Output: False

a = [1, 2, 3]
print(is_same_class(a, list))  # Output: True

a = [1, 2, 3]
print(is_same_class(a, object))  # Output: False

