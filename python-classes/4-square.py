# -*- coding: utf-8 -*-
"""Square module.

This module defines the Square class, which represents a square with a private size attribute.
"""


class Square:
    """Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initialize the Square instance with an optional size.
        area(self): Calculate the area of the square.
        my_print(self): Print the square with the character '#'.

    Properties:
        size (int): Getter and setter for the size attribute.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
    """

    def __init__(self, size=0):
        """Initialize the Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' characters.

        If the size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)

