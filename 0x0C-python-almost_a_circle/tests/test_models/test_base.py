"""Defines test cases for Base class."""

import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_assignment_with_value(self):
        """Tests if id is assigned correctly when provided."""
        expected_id = 10
        obj = Base(expected_id)
        self.assertEqual(obj.id, expected_id)

    def test_id_assignment_without_value(self):
        """Tests if id is assigned
        correctly with auto-increment when not provided."""
        first_obj = Base()
        second_obj = Base()
        self.assertEqual(first_obj.id, 1)
        self.assertEqual(second_obj.id, 2)

    def test_id_uniqueness(self):
        """Tests if different object instances have unique IDs."""
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_private_attribute_access(self):
        """Tests if accessing private attribute
        raises an AttributeError."""
        with self.assertRaises(AttributeError):
            obj = Base()
            _ = obj.__nb_objects
