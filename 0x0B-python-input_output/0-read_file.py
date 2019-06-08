#!/usr/bin/python3
""" module documentation - Read file """


def read_file(filename=""):
    """documentation for reading a file"""
    with open(filename) as f:
        print(f.read(), end="")
