#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x1 = tuple_a[0] if tuple_a else 0
    x2 = tuple_b[0] if tuple_b else 0
    y1 = tuple_a[1] if (tuple_a and len(tuple_a) > 1) else 0
    y2 = tuple_b[1] if (tuple_b and len(tuple_b) > 1) else 0
    return x1 + x2, y1 + y2
