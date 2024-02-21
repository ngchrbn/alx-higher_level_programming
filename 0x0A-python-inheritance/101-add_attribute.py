#!/usr/bin/python3

"""Defines a function add_attribute"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if it's possible.

    Args:
        obj (object): object where to set attribute
        attr (str): attribute name
        value (any): value of the attribute.
    Raises:
        TypeError: If the object cannot have new attributes.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute")

    setattr(obj, attr, value)
