#!/usr/bin/python3
""" Count the lines
"""


def number_of_lines(filename=""):
    """ Counts number of lines of a file

    Args:
        filename (str): name of the file. Defaults to "".

    Returns:
        [int]: number of lines
    """
    counter = 0

    with open(filename, 'r') as fd:
        for line in fd:
            counter += 1
        return counter
