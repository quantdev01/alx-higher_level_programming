#!/usr/bin/python3
"""
Module python3
"""
import json


class Base:
    """
    My class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        My beautiful init function
        """
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # Task 15 : to json string function

    def to_json_string(list_dictionaries):
        """
        My function
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    # Task 16 : Json string to file

    def save_to_file(list_objs):
        """ Save to file """
        my_obj_list = []

        for obj in list_objs:
            my_obj_list.append(obj.to_dictionary())

        my_json = Base.to_json_string(my_obj_list)

        if list_objs is None:
            with open("Rectangle.json", "w", encoding="utf-8") as file:
                file.write()
        else:
            with open("Rectangle.json", "w", encoding="utf-8") as file:
                file.write(str(my_json))

    # Task 17 : json string to python object:

    def from_json_string(json_string):
        """ from json to string """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    # Task 18 : create an instance from dictionary

    def create(**dictionary):
        """ create a instance from ddictionary """
        from models.rectangle import Rectangle
        dummy = Rectangle(1, 1, 1, 1, 1)
        dummy.update(**dictionary)
        return dummy

    # Task 19 : create instances from file

    def load_from_file():
        """ load instances from file """
        from models.rectangle import Rectangle
        instances_lists = ""

        with open("Rectangle.json", "r") as file:
            instances_lists + file.read()

        my_dict = Rectangle.from_json_string(instances_lists)
        return Rectangle.create(my_dict
