#!/usr/bin/python3
""" Rectangle class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle

    Args:
        Rectangle (Base subclass): Parent Class
    """
    def __init__(self, size):
        self.__size = self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
