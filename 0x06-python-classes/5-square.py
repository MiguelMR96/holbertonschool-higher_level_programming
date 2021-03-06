#!/usr/bin/python3
""" Square with size private attribute
"""


class Square:
    """Square with size private attribute
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif int(value) < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        print('\n'.join(["".join(["#" for j in range(self.__size)])
                        for i in range(self.__size)]))
