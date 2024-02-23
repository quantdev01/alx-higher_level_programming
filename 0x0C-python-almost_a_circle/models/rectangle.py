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

    @property
    def get_width(self):
        return self.__width

    @get_width.setter
    def set_width(self, width):
        self.__width = width

    @property
    def get_height(self):
        return self_height

    @get_height.setter
    def set_height(self, height):
        self.__height = height

    @property
    def get_x(self):
        return self.__x

    @get_x.setter
    def set_x(self, x):
        self.__x = x

    @property
    def get_y(self):
        return self.__y

    @get_y.setter
    def set_y(self, y):
        self.__y = y
