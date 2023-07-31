class Square:
    """
    The size of the square is a private instance attribute for this class.
    Since the square's dimensions are important for many calculations, they are kept secret.
    """

    def __init__(self, size):
        """
        Constructor to initialize the Square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size


