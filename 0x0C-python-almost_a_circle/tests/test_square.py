#!/usr/bin/python3
""" My module test """
from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    """ My Class Tester """

    # Task 10 test, square rectangle

    def test_square(self):
        """
        Test square
        """
        a = Square(3)

        self.assertEqual(a.id, 8)
        self.assertEqual(a.__str__(), "[Square] \
({}) {}/{} - {}".format(a.id, a.x, a.y, a.width))
        self.assertEqual(a.area(), 9)

        # Task 11 test

        self.assertEqual(a.size, 3)
        """ a.size = '45'
        with self.assertRaises(TypeError):
            a.size """

        # Task 12 test

        a.update(4)
        self.assertEqual(a.__str__(), "[Square] ({}) \
{}/{} - {}".format(a.id, a.x, a.y, a.size))

        # task 14 test

        my_dict = a.to_dictionary()

        self.assertIsInstance(my_dict, dict)
