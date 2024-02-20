#!/usr/bin/python3
"""
my module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Mad
    """
    def __init__(self, size):
        """
        initializer
        """
        self.__size = size
        Rectangle.integer_validator(self, "Size", size)
