#!/usr/bin/python3
"""
My rectangle class
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

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = ''
        for _ in range(self.__height):
            lines += '#' * self.__width + '\n'
        return lines.rstrip('\n')

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
