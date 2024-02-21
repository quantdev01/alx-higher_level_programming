#!/usr/bin/python3
"""
Module py
"""
import json


def load_from_json_file(filename):
    """
    function documentation
    will load a json into a file
    """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
