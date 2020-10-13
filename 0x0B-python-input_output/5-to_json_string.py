#!/usr/bin/python3
""" Returns in a json string representation
"""
import json


def to_json_string(my_obj):
    """ Returns in a json string representation

    Args:
        my_obj (obj): object to be serializated in
        json string representation
    """
    return json.dumps(my_obj)
