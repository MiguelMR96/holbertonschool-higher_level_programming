#!/usr/bin/python3
def remove_char_at(str, n):
    c_str = str
    if n >= 0:
        return (c_str[:n] + c_str[n+1:])
    else:
        return (c_str)
