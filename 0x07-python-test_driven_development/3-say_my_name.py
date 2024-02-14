#!/usr/bin/python3
"""
My module
"""


def say_my_name(first_name, last_name=""):
    """
    printing my name
    """
    if not isinstance(first_name, str) and not isinstance(last_name, str):
        # if type(first_name) != str and type(last_name) != str:
        raise TypeError("first and last name must be string")
    if not isinstance(first_name, str):
        # if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        # if type(last_name) != str:
        raise TypeError("last_name must be a string")
    if first_name is not None and last_name is not None:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))
