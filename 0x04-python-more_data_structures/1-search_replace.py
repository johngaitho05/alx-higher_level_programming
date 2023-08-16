#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not (my_list and search and replace):
        return
    return [replace if v == search else v for v in my_list]
