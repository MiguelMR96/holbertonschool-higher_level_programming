#!/usr/bin/python3
""" Indent text when hit ".", ":", "?"
"""

def text_indentation(text):
    """ Indent text when hit ".", ":", "?"

    Args:
        text (str): No need for description
    """
    if type(text) != str:
        raise TypeError('text must be a string')
    i = 0
    while i < len(text):
        if text[i] in ['.', ':', '?']:
            print("{}".format(text[i]))
            print()
            i += 1
        else:
            print("{}".format(text[i]), end="")
        i += 1
