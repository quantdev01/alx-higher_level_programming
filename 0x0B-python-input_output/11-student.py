#!/usr/bin/python3
"""
Module
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs is None):
            return {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'age': self.age
                    }
        else:
            my_dict = {}

            if 'first_name' in attrs:
                my_dict['first_name'] = self.first_name
            if 'last_name' in attrs:
                my_dict['last_name'] = self.last_name
            if 'age' in attrs:
                my_dict['age'] = self.age
            return my_dict
    def reload_from_json(self, json):
        json['first_name'] = self.first_name
        json['last_name'] = self.last_name
        json['age'] = self.age
        return json 

