#!/usr/bin/python3
""" Reads n lines from a file
"""


def read_lines(filename="", nb_lines=0):
    """ Reads n file and print in stdout

    Args:
        filename (str): file's name. Defaults to "".
        nb_lines (int, optional): Number of lines. Defaults to 0.
    """
    with open(filename, 'r') as fd:
        i = 0
        if nb_lines < 0 or not nb_lines:
            read_data = fd.read()
            print("{}".format(read_data), end='')
        while (i < nb_lines):
            read_data = fd.readline()
            print("{}".format(read_data), end='')
            i += 1
