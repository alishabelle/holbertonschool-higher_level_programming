#!/usr/bin/python3
"""Funtion that adds two integers together"""


def add_integer(a, b=98):
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
