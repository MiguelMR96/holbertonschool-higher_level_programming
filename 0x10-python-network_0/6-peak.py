#!/usr/bin/python3
""" Function to find_peak
"""


def find_peak(list_of_integers):
    """ Function to find a peak with binary search
    """
    if len(list_of_integers) == 0:
        return None
    start = 0
    end = len(list_of_integers) - 1

    while start < end:
        mid = start + (end - start) // 2
        if (list_of_integers[mid] > list_of_integers[mid - 1]) and (
                list_of_integers[mid] > list_of_integers[mid + 1]):
            return list_of_integers[mid]
        if list_of_integers[mid - 1] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_of_integers[start]
