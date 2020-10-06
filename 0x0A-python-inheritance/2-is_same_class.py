#!/usr/bin/python3
""" True or False depending if is instance
"""


def is_same_class(obj, a_class):
    """[summary]

    Args:
        obj ([type]): [description]
        a_class ([type]): [description]

    Returns:
        [type]: [description]
    """
    if type(obj) is a_class:
        return (True)
    return (False)
