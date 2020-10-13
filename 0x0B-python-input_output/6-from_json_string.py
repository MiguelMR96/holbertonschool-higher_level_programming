#!/usr/bin/python3
"""
Returns an object from
json string representation
"""
import json


def from_json_string(my_str):
    """ Returns an object from
        json string representation

    Args:
        my_str (json): json string representation
    """
    return json.loads(my_str)
