#!/usr/bin/python3
"""
Writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj (obj): json object
        filename (str): filename to be written
    """
    with open(filename, 'w') as fd:
        return fd.write(json.dumps(my_obj))
