#!/usr/bin/python3
for i in range(123, 97, -1):
    if i % 2 == 0:
        i -= 33
    else:
        i -= 1
    print("{:c}".format(i), end="")
