#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()

    if not my_list:
        return new_list
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
            break
    return new_list
