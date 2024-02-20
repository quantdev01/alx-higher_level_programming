#!/usr/bin/python3
"""
Module to write a Json to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function to save to json file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
