#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
        except:
            pass

        result = result + ((a ** b) / i)

    result = result + (b + a)
    return result
