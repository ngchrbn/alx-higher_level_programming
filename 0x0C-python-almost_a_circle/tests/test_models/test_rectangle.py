#!/usr/bin/python3

"""Defines test cases for Rectangle class."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_initialization(self):
        """Tests if Rectangle instances are created with correct attributes."""
        rectangle = Rectangle(5, 10, 2, 3)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    def test_width_property(self):
        """Tests the width property."""
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.width, 5)
        rectangle.width = 20
        self.assertEqual(rectangle.width, 20)

    def test_height_property(self):
        """Tests the height property."""
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.height, 10)
        rectangle.height = 40
        self.assertEqual(rectangle.height, 40)

    def test_x_property(self):
        """Tests the x property."""
        rectangle = Rectangle(5, 10, 2)
        self.assertEqual(rectangle.x, 2)
        rectangle.x = 15
        self.assertEqual(rectangle.x, 15)

    def test_y_property(self):
        """Tests the y property."""
        rectangle = Rectangle(5, 10, 0, 4)
        self.assertEqual(rectangle.y, 4)
        rectangle.y = 20
        self.assertEqual(rectangle.y, 20)

    def test_inheritance(self):
        """Test if id from Base can be accessed."""
        rectangle = Rectangle(5, 10, 0, 4, 2)
        self.assertEqual(rectangle.id, 2)
        rectangle = Rectangle(5, 10, 0, 4)
        self.assertEqual(rectangle.id, 7)
