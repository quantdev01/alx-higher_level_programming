#!/usr/bin/python3
"""
New class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    My class inheritance
    """
    def __init__(self, width, height):
        """
        init variable
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
