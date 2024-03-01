#!/usr/bin/python3
""" Square class inheritate """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square inheritate from  Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializer """
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """ string format """
        return "[Square] ({}) {}/{} \
- {}".format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, size):
        """ size setter """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ update using *args and **kwargs """
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]

            if len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            # Update class attributes using dictionary kwargs

            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    # function to dictionary for square class

    def to_dictionary(self):
        """ to dictionary """
        my_dict = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
        return my_dict

    # Task 18 trynna fix by creating a new function create in the square class


"""
    def create(**dictionary):
        """ create a instance from ddictionary """
        dummy = Square(1)
        dummy = Square.update(**dictionary)
        return dummy
"""
