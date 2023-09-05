#!/usr/bin /python3

"""Prints 2 new lines after certain special characters"""


def text_indentation(text):
    """
    Print 2 new lines after any of '.?:'
    :param text: the string to print
    :return: None
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    text = text.strip()
    special = ".?:"
    last_printed = "#"
    for c in text:
        if c == " " and last_printed in special:
            continue
        print(c, end="")
        last_printed = c
        if c in special:
            print('\n')
