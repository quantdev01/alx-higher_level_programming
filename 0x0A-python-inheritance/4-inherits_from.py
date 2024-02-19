#!/usr/bin/python3
"""
Module with function to do something
"""


def inherits_from(obj, a_class):
    """
    My function to return true if instance is a subclass
    """
    if type(obj) == a_class:
        return True
    else:
        return False
