#!/usr/bin/python3
import json
""" documentation module """


def save_to_json_file(my_obj, filename):
    """ write a function that writes """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
