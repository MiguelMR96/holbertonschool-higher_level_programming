#!/usr/bin/python3
""" Print square in "#"
"""


def print_square(size):
    """ Print square in "#"

    Args:
        size (int): Square's size

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
