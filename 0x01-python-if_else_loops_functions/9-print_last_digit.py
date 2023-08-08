#!/usr/bin/python3
def print_last_digit(number):
    assert type(number) == int
    res = str(number)[-1]
    print(res, end='')
    return res
