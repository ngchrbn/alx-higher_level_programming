#!/usr/bin/python3

"""Defines a base model class."""


class Base:
    """Defines Base class which is a parent for other classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class

        Args:
            id (int): value to be assigned
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
