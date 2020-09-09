#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_aux = (0, 0)
    if len(tuple_a) < 2:
        tuple_a += tuple_aux
    if len(tuple_b) < 2:
        tuple_b += tuple_aux
    result = tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
    return result
