class Square:
    """
    Represents a square with methods to calculate area and print the square pattern.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square's sides (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """
        Get the size of the square's sides.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square's sides.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square pattern using the '#' character.

        If size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

