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
        """ width docu """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        self.__height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        self.__x = x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        self.__y = y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be >= 0")

    # Task 4

    def area(self):
        """ area get """
        return self.__width * self.__height

    # Task 5 and 7 -> manage y and x position

    def display(self):
        """ Display the rectangle """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    # Task 6

    def __str__(self):
        """ return str """
        return "[Rectangle] ({}) {}/{} - {}/{}\
".format(self.id, self.__x, self.__y, self.__width, self.__height)

    # Task 8

    def update(self, *args, **kwargs):
        """ updates the rectangle """
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]

            if len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            if len(args) == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        else:
            # Update class attributes using dictionary kwargs

            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    # Task 13 function to dictionary

    def to_dictionary(self):
        """ rectangle attributes to dictionary """
        my_dict = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
        return my_dict
