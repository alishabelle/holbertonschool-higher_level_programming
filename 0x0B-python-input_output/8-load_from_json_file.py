#!/usr/bin/python3
import json
""" documentation module """

def load_from_json_file(filename):
    """ load json """
    with open(filename) as f:
        return json.load(f)
