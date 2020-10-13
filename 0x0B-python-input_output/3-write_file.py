#!/usr/bin/python3
""" Write in a file
"""


def write_file(filename="", text=""):
    """ Write in a file

    Args:
        filename (str): Filename of file text that is going to be written.
        Defaults to "".
        text (str): text to be written in the text file. Defaults to "".
    """
    with open(filename, mode='w') as fd:
        return fd.write(text)
