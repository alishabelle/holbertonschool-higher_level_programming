#!/usr/bin/python3
""" takes url sends request displays responese """

import sys
import requests


if __name__ == '__main__':

    url = sys.argv[1]
    set = requests.get(url)

    if set.status_code >= 400:
        print("Error code: {}".format(set.status_code))
    else:
        print(set.text)
