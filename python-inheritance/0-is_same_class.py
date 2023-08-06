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

