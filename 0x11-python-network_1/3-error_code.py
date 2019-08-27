#!/usr/bin/python3
""" takes in url displays body of response decoded """

import sys
import urllib.request

if __name__ == '__main__':
    aye = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(aye) as response:
            set = response.read()
            print(set.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
