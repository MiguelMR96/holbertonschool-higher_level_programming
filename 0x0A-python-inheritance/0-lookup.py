#!/usr/bin/python3
""" returns a list of subclass attributes
"""


def lookup(obj):
    """ returns a list of subclass attributes

    Args:
        obj (class): attributtes
    """
    return list(dir(obj))
