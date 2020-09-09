#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_value = 0
        for i in my_list:
            if max_value < i:
                max_value = my_list[i]
        return max_value
