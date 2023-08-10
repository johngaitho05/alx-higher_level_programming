#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    args = argv[1:]
    mapper = {'+': add, '-': sub, '*': mul, '/': div}
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif args[1] not in mapper:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    total = mapper[args[1]](int(args[0]), int(args[2]))
    print("{a} {operator} {b} = {c}".format(a=args[0], operator=args[1], b=args[2], c=total))



