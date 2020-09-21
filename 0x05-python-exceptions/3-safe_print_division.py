#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if b == 0:
            result = None
            return result
        else:
            result = a / b
            return result
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
