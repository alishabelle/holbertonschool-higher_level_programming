#!/usr/bin/python3
""" takes in url request displays value """

import urllib.request
import sys

if __name__ == "__main__":
    aye = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(aye) as response:
        set = response.headers.get('X-Request-Id')
        print(set)
