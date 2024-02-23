#!/usr/bin/python3
"""
Module test base
"""
import unittest
from models.base import Base

class BaseTest(unittest.TestCase):
    """
    my class Test
    """
    def test_base(self):
        a = Base()
        b = Base(20)
        c = Base()
        d = Base(None)
        self.assertEqual(a.id, 1)  
        self.assertEqual(b.id, 20)
        self.assertEqual(c.id, 2)
        self.assertEqual(d.id, 3)
