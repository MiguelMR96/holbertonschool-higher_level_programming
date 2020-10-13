#!/usr/bin/python3
""" Append text in file
"""


def append_write(filename="", text=""):
    """ Append text in a file

    Args:
        filename (str): Filename of file where text is going to be append.
        Defaults to "".
        text (str): Text to append. Defaults to "".
    """
    with open(filename, mode='w') as fd:
        return fd.write(text)
