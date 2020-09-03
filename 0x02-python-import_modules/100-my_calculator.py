#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    counter = len(sys.argv) - 1
    if counter != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            add = calculator_1.add
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif sys.argv[2] == "-":
            sub = calculator_1.sub
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif sys.argv[2] == "*":
            mul = calculator_1.mul
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif sys.argv[2] == "/":
            div = calculator_1.div
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
