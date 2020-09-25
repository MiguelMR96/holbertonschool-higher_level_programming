#!/usr/bin/python3
""" Print my name
"""


def say_my_name(first_name, last_name=""):
    """ Print my name

    Args:
        first_name (str): Your first name
        last_name (str, optional): Your last name. Defaults to "".

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if type(first_name) != str or first_name == None:
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str) or last_name == None:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
