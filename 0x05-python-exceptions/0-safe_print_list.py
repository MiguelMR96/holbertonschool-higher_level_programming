#!/usr/bin/env python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            counter += 1
        print()
        return counter
    except:
        print()
        return counter
