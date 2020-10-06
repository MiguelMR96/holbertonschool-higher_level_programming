#!/usr/bin/python3
""" My list subclass
"""


class MyList(list):
    """[summary]

    Args:
        list ([type]): [description]
    """
    def print_sorted(self):
        print(sorted(self))
