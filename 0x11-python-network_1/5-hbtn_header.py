#!/usr/bin/python3
""" takes in url sends request and displays variable to response header """

import requests
import sys

if __name__ == "__main__":
    respo = requests.get(sys.argv[1])
    set = respo.headers.get('X-Request-Id')
    print(set)
