#!/usr/bin/python3

"""
Module providing a function for adding two integers.
The function takes two parameters a and b (both int or float only).
Raises TypeError if one of the arguments is not int or float
"""

def add_integer(a, b=98):
    """
    Adds two integers. Returns an int.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) if isinstance(a, float) else a) + (int(b) if isinstance(b, float) else b)
