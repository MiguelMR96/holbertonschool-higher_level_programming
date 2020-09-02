#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:  # exception for negative numbers
        number *= -1
        last_digit = number % 10
        print("{:d}".format(last_digit), end="")
        return(last_digit)
    else:
        print("{:d}".format(number % 10), end="")
        return(number % 10)
