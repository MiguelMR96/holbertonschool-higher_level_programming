#!/usr/bin/python3
""" Is instance the class or subclass
"""


def is_kind_of_class(obj, a_class):
    """ Is instance the class or subclass

    Args:
        obj
        a_class

    Returns:
        True or False
    """
    if isinstance(obj, a_class):
        return True
    return False
