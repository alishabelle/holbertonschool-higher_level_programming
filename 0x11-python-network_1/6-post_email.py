#!/usr/bin/python3
""" takes in url and email send post request """

import requests
import sys

if __name__ == '__main__':
    email = {'email': sys.argv[2]}
    set = requests.post(sys.argv[1], data=email)
    print(set.text)
