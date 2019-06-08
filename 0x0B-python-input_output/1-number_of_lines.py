#!/usr/bin/python3
""" module documentation - read file lines """


def number_of_lines(filename=""):
    """documentation for reading file lines"""
    line_number = 0
    with open(filename) as f:
        for line in f:
            line_number += 1
        return(line_number)
