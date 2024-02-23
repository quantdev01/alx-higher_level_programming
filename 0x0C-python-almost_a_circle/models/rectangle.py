#!/usr/bin/python3
"""
My module rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle with private attributes
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization function
        """
        Base.__init__(self, id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        # -----------------------
        # -------Task 3----------

        # Exception handling width and height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        # Exception handling for x and y, x and y are position of the rectangle
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    # ---------Task 2----------

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be >= 0")

    def area(self):
        return self.__width * self.__height
