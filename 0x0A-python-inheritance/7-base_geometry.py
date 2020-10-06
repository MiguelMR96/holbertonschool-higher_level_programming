#!/usr/bin/python3
""" Empty base class
"""


class BaseGeometry():
    """ Empty base class
    """
    def area(self):
        """raise exceptions

        Raises:
            Exception: [description]
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates integers

        Args:
            name ([type]): [description]
            value ([type]): [description]
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
