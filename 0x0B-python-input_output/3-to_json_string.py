#!/usr/bin/python3
import json
"""
Module py to transform an object to Json
"""


def to_json_string(my_obj):
    """returning my_obj to json
    Args:
        my_obj - the obj to convert to json
    Return:
        return - json object
    """
    return json.dumps(my_obj)
