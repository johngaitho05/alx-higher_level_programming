#!/usr/bin/python3
def print_last_digit(number):
    if type(number) != int:
        raise ValueError("Not a valid number")
    res = str(number)[-1]
    print(res, end='')
    return res
