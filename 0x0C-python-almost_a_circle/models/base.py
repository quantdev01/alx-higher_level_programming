#!/usr/bin/python3
"""
Module python3
"""


class Base:
    """
    My class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        My beautiful init function
        """
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
