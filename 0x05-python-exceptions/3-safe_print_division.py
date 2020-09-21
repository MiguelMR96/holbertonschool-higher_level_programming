#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if b == 0:
            result = None
        else:
            result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
