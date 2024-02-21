#!/usr/bin/python3

"""Defines a Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a Rectangle class - subclass of BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        try:
            self.integer_validator("width", width)
            self.integer_validator("height", height)
        except (TypeError, ValueError) as e:
            print(e)
        else:
            self.__width = width
            self.__height = height
