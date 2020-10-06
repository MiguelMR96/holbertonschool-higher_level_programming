#!/usr/bin/python3
"""[summary]
"""


def inherits_from(obj, a_class):
    """[summary]

    Args:
        obj ([type]): [description]
        a_class ([type]): [description]
    """
    if type(obj) != a_class:
        return True
    return False
