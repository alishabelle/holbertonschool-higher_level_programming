#!/usr/bin/python3
""" documentation module """


def append_write(filename="", text=""):
    """documentation to append file"""
    with open(filename, mode='a') as f:
        f.write(text)
        return(len(text))
