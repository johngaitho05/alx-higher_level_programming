#!/usr/bin /python3

"""Prints 2 new lines after certain special characters"""


def text_indentation(text):
    """
    Print 2 new lines after any of '.?:'
    :param text: the string to print
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    special = ":?."
    for c in special:
        text = text.replace(c, f'{c}<new-line>')
    text = text.split("<new-line>")
    for i, s in enumerate(text):
        s = s.strip()
        if i == len(text)-1:
            print(s, end="")
        else:
            print(s, end="\n\n")
