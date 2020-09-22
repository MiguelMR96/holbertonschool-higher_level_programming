#!/usr/bin/python3
""" Square with size private attribute
"""


class Square:
    """Square with size private attribute
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif int(size) < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
