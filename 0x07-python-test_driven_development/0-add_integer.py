#!/usr/bin/python3
""" add two integers
"""


def add_integer(a, b=98):
    """[summary]

    Args:
        a (int): number
        b (int, optional): Number. Defaults to 98.

    Raises:
        TypeError: when a is not a number
        TypeError: when b is not a number

    Returns:
        a + b: result af adding two numbers
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    if type(a) != int:
        raise TypeError('a must be an integer')
    if type(b) != int:
        raise TypeError('b must be an integer')
    return a + b
