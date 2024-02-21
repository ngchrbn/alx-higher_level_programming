#!/usr/bin/python3

"""Defines a BaseGeometry class."""


class BaseGeometry:
    """Represents a BaseGeometry class."""
    def area(self):
        """Raises an exception that the function is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a given value

        Args:
            name (string): name of the value
            value (int): value to be validated

        Raises:
            If value not integer, raises TypeError
            If value <= 0, raises ValueError
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
