#!/usr/bin/python3
""" Read a file
"""


def read_file(filename=""):
    """ Read a file and print in stdout

    Args:
        filename (str): Text file's name. Defaults to "".
    """
    with open(filename, 'r') as fd:
        for line in fd:
            print(line, end="")
