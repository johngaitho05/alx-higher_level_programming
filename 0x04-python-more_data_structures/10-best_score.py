#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    keys = list(a_dictionary.keys())
    largest_val = a_dictionary[keys[0]]
    res = keys[0]
    for k in keys[1:]:
        new_val = a_dictionary[k]
        if new_val > largest_val:
            largest_val = new_val
            res = k
    return res
