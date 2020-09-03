#!/usr/bin/python3
if __name__ == "__main__":
    import sys

counter = len(sys.argv)
sum = 0

for i in range(1, counter):
    num = int(sys.argv[i])
    sum += num
print("{}".format(sum))
