#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) not in range(97, 123):
            print("{n}".format(n=c), end='')
        else:
            print("{n}".format(n=chr(ord(c) - 32)), end='')
