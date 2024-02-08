#!/usr/bin/python3

"""
Write a class Square that defines a square by: (based on 1-square.py)

Private instance attribute: size
"""


class Square:
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    def my_print(self):
        if self.__size <= 0:
            print()
        else:
            print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if self.__position[0] < 0 and self._position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
