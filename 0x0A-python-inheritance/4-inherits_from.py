#!/usr/bin/python3
"""
Module with function to do something
"""


def inherits_from(obj, a_class):
    """
    My function to return true if instance is a subclass
    """
    return isinstance(obj, a_class) and not isinstance(type(obj), a_class) 
