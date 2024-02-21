#!/usr/bin/python3
"""
Contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited
    from the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The specified class.
        
    Returns:
        bool: True if obj is an instance of a class that directly or
        indirectly inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class) and obj.__class__ != a_class
