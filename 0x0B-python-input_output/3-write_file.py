#!/usr/bin/python3
""" documentation module - to write file"""


def write_file(filename="", text=""):
    """ write file documentation """
    with open(filename, mode='w') as f:
        f.write(text)
        return(len(text))
