#!/usr/bin/python3
"""
My module which print and return a list of available attributes
"""


def lookup(obj):
    """
    Return a list of method in an object or class
    """
    methods = list(dir(obj))
    return methods
