#!/usr/bin/python3
""" github info """

import requests
import sys

if __name__ == '__main__':
    usr = sys.argv[1]
    pass = sys.argv[2]
    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    aye = requests.get(url, auth=(usr, pass))
    aye = dict(aye.json())
    print(aye.get('id'))
