#!/usr/bin/python3

"""
A foundational class for representing geometric entities.
"""


class BaseGeometry:
    """
    A base class for representing geometric entities.

    This class acts as a foundation for other classes to inherit from, enabling them to define
    specific geometric entities along with their respective behaviors.

    Attributes:
        None

    Methods:
        area(self):
            This method is not implemented in the base class and should be overridden in subclasses.
            It raises an Exception to indicate that the specific implementation of area() is missing.

        integer_validator(self, name, value):
            Validate the given value as an integer for a specific attribute.

        Args:
            name (str): The name of the attribute being validated.
            value (int): The value to be validated as an integer.

        Raises:
            TypeError: If the value is not an integer, raises a TypeError with a descriptive message.
            ValueError: If the value is less than or equal to zero, raises a ValueError with a descriptive message.
    """

    def area(self):
        """
        Calculate the area of the geometric entity.

        Raises:
            Exception: This exception is raised to indicate that the specific
                      implementation of area() is missing.

        Returns:
            None: The method does not return any value as it is intended to be overridden.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the given value as an integer for a specific attribute.

        Args:
            name (str): The name of the attribute being validated.
            value (int): The value to be validated as an integer.

        Raises:
            TypeError: If the value is not an integer, raises a TypeError with a descriptive message.
            ValueError: If the value is less than or equal to zero, raises a ValueError with a descriptive message.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

