#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Rectangle class
"""


class Rectangle(BaseGeometry):
    """ Rectangle class

    Args:
        BaseGeometry (Parent class): Have some mehotds for validating data
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
