#!/usr/bin/python3

"""
Module py to transform an object to Json
"""
import json


def to_json_string(my_obj):
    """returning my_obj to json
    Args:
        my_obj - the obj to convert to json
    Return:
        return - json object
    """
    if (my_obj is not type(set)):
        return json.dumps(my_obj)
    else:
        return
    print('created')
