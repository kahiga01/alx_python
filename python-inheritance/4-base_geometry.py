#!/usr/bin/python3

"""A foundational class for representing geometric entities."""


class BaseGeometry:
    """
    A foundational class for representing geometric entities.

    This class acts as a base for other classes to inherit from, enabling them to define
    specific geometric entities along with their respective behaviors.

    Attributes:
        None

    Methods:
        area(self):
            This method is not implemented in the base class and should be overridden in subclasses.
            It raises an Exception to indicate that the specific implementation of area() is missing.
    """

    def area(self):
        """
        Calculate the area of the geometric entity.

        Raises:
            Exception: Since the method is not implemented in the base class,
                      this exception is raised to indicate that the specific
                      implementation of area() is missing.

        Returns:
            None: The method does not return any value as it is intended to be overridden.
        """
        raise Exception("area() is not implemented")

