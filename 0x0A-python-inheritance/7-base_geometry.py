#!/usr/bin/python3
"""
Base module
"""


class BaseGeometry:
    """
    my empty class
    """
    def area(self):
        """
        area of geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer method validator
        """
        self.name = name
        self.value = value

        if not isinstance(self.value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
