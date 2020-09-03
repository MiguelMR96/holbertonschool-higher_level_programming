#!/usr/bin/python3
if __name__ == "__main__":
    import sys

counter = len(sys.argv)
arguments = sys.argv

if counter == 1:
    print("0 arguments.")
elif counter == 2:
    print("{} argument:".format(counter - 1))
    print("1: {}".format(arguments[1]))
elif counter > 1:
    print("{} arguments:".format(counter - 1))
    for i in range(1, counter):
        print("{}: {}".format(i, arguments[i]))
