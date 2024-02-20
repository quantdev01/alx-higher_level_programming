#!/usr/bin/python3
"""
Module python to take an obj from json to string
"""
import json


def from_json_string(my_str):
    """
    from json to string
    """
    return json.loads(my_str)
