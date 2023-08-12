#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list) - 1 or idx < len(my_list) * -1:
        return
    return my_list[idx]
