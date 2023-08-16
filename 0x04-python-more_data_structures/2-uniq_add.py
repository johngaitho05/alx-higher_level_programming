#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = []
    result = 0
    for num in my_list:
        if num not in seen:
            result += num
            seen.append(num)
    return result
