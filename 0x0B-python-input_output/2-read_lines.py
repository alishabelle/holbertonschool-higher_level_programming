#!/usr/bin/python3
""" module documentation - read number of lines """


def read_lines(filename="", nb_lines=0):
    """documentation for reading number of lines"""
    
    with open(filename) as f:
        if nb_lines <= 0 or nb_lines >= len(filename):
            print(f.readlines(nb_lines), end="")
