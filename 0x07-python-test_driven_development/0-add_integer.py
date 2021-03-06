#!/usr/bin/python3
""" add two integers
"""


def add_integer(a, b=98):
    """ Add two integers

    Args:
        a (int): number
        b (int, optional): Number. Defaults to 98.

    Raises:
        TypeError: when a is not a number
        TypeError: when b is not a number

    Returns:
        a + b: result af adding two numbers
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
