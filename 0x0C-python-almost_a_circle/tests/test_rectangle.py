#!/usr/bin/python3
"""
This is the test of Task 2
"""
import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """
    This is my rectangle Test class
    """
    def test_rectangle(self):
        """
        My rectangle Test function
        """
        a = Rectangle(2, 5)
        b = Rectangle(3, 34, 0, 0, 15)
        c = Rectangle(4, 5)
        b.x = 4
        b.y = 3

        c.height = 10
        c.width = 7

        # Task 1 tests

        self.assertEqual(a.id, 4)
        self.assertEqual(b.id, 15)
        self.assertEqual(c.id, 5)

        # Task 2 tests

        self.assertEqual(a.height, 5)
        self.assertEqual(a.width, 2)
        self.assertEqual(c.height, 10)
        self.assertEqual(c.width, 7)
        self.assertEqual(b.x, 4)
        self.assertEqual(b.y, 3)

        # Task 3 Tests

        with self.assertRaises(ValueError):
            c.height = -3
        with self.assertRaises(ValueError):
            c.width = -5
        with self.assertRaises(TypeError):
            c.y = ""
        with self.assertRaises(TypeError):
            b.x = None

        # Task 4 Tests calculate area

        a = Rectangle(2, 5)

        self.assertEqual(a.area(), 10)

        # Task 5 Test display function

        # Task 6 Test, implement __str__

        self.assertEqual(a.__str__(), "[Rectangle] \
({}) {}/{} - {}/{}".format(a.id, a.x, a.y, a.width, a.height))

        # task 13 test
        my_dict = a.to_dictionary()

        self.assertIsInstance(my_dict, dict)

    # Task 16 : Test json string to file

    def test_to_json_in_file(self):
        b = Rectangle(4, 3)
        self.assertEqual(Rectangle.save_to_file([b]), None)
