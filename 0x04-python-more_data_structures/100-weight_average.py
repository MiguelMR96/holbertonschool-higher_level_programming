#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    summation = 0
    divi = 0
    for k, i in my_list:
        summation += k * i
        divi += i
    return summation / divi
