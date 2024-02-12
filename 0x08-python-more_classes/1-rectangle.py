#!/usr/bin/python3

"""Module that defines a Rectangle class."""


class Rectangle:
    """Defines a Rectangle."""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Returns width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
