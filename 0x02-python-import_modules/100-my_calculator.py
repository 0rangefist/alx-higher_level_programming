#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argc = len(sys.argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    def operation(a, b, op):
        if op == "+":
            return add(a, b)
        elif op == '-':
            return sub(a, b)
        elif op == '*':
            return mul(a, b)
        elif op == '/':
            return div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

    print("{} {} {} = {}".format(a, op, b, operation(a, b, op)))
