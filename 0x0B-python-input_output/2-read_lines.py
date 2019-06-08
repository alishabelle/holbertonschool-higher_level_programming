#!/usr/bin/python3
""" module documentation - read number of lines """


def read_lines(filename="", nb_lines=0):
    """documentation for reading number of lines"""
    
    if nb_lines is <= 0 or nb_lines 
with open(filename) as f:
        print(f.read(nb_lines), end="")
