#!/usr/bin/python3

"""Defines a class MyInt."""


class MyInt(int):
    """Represents MyInt which is a subclass of int."""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
