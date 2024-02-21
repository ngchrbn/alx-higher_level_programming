#!/usr/bin/python3

"""Defines a Square class that inherits from Rectangle."""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a Square class which is subclass of Rectangle."""
    def __init__(self, size):
        """Initializes a Square.

        Args:
            size (int): size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than or equal to 0
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the square's area."""
        return self.__size ** 2

    def __str__(self):
        """Returns a representation of a Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
