#!/usr/bin/python3
""" Only first_ame attribute allowed in LockedClass
"""


class LockedClass:
    """ Only first_ame attribute allowed in LockedClass
    """
    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        self.first_name = first_name
