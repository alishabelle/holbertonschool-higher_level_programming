#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if isinstance(last_name, 
