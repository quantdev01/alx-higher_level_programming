#!/usr/bin/python3
"""
Module test base
"""
import unittest
from models.base import Base
import json


class BaseTest(unittest.TestCase):
    """
    my class Test
    """
    # Class Test

    def test_base(self):
        a = Base()
        b = Base(20)
        c = Base()
        d = Base(None)
        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, 20)
        self.assertEqual(c.id, 2)
        self.assertEqual(d.id, 3)

    # To json string Test

    def test_to_json(self):
        dictionary = {"name": "Daniel", "age": 22}
        to_json = Base.to_json_string(dictionary)

        self.assertIsInstance(dictionary, dict)
        self.assertIsInstance(to_json, str)

    # Task 17 : json to list

    def test_json_to_list(self):
        my_list = [{'name': 'Daniel'}, {'age': 24}]
        my_json = Base.to_json_string(my_list)
        to_list = Base.from_json_string(my_json)

        self.assertIsInstance(my_json, str)
        self.assertIsInstance(to_list, list)
