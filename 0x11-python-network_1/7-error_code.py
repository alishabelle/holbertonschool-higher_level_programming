#!/usr/bin/python3
""" takes url sends request displays responese """

import sys
import requests


if __name__ == '__main__':

    
    set = requests.get(sys.argv[1])

    if set.status_code >= 400:
        print("Error code: {}".format(ret.status_code))
    else:
        print(set.text)
