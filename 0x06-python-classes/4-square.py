#!/usr/bin/python3

"""
Write a class Square that defines a square by: (based on 1-square.py)

Private instance attribute: size
"""


class Square:
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")
