#!/usr/bin/python3
""" Class rectangle
"""


class Rectangle:
    """ Class rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Rectangle's area

        Returns:
            [int]: height * width
        """
        return self.__height * self.__width

    def perimeter(self):
        """ Rectangle's perimeter

        Returns:
            [int]: (2 * height) + (2 * width)
        """
        return (2 * self.__height) + (2 * self.__width)
