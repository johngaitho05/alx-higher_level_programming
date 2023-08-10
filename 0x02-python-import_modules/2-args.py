#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    count = len(args)
    s = 'argument' if count == 1 else 'arguments'
    symbol = '.' if count == 0 else ':'
    print(f"{count} {s}{symbol}".format(count=count, s=s, symbol=symbol))
    for i, v in enumerate(args):
        print("{i}: {v}".format(i=i + 1, v=v))

