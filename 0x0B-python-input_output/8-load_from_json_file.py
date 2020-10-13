#!/usr/bin/python3
"""
Creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”

    Args:
        filename (str)
    """
    with open(filename, 'r') as fd:
        return json.load(fd)
