#!/usr/bin/python3
"""
Empty class module
"""


class Rectangle:
    """
    class rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        # Exception to raise for WIDTH
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        # Exception for HEIGHT
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if (self.__height < 0):
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        # Exception for HEIGHT
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if (self.__height < 0):
            raise ValueError("height must be >= 0")
