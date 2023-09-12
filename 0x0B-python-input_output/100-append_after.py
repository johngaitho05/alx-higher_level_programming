#!/usr/bin/python3
"""
Write a function that inserts a line of text to a file,
after each line containing a specific string (see example):

Prototype: def append_after(filename="", search_string="", new_string=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Reads a file and appends a new string after each
    line that matches the search
     """
    with open(filename, 'r', encoding='utf8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
