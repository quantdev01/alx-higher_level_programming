#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    """
    class definition witch is extencing TestCase
    """
    def test_max_integer(self):
        """
        actual test with built in methods
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-4, -6, 6, 0]), 6)
        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer, type([2, 3, 6]), True)
        self.assertRaises(TypeError, max_integer, type([1, 3, 6]), False)