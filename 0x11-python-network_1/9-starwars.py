#!/usr/bin/python3
""" starwars """

import requests
import sys

if __name__ == '__main__':
    url = 'https://swapi.co/api/people/?search={}'.format(sys.argv[1])
    aye = requests.get(url)
    aye = dict(aye.json())
    print('Number of results: {}'.format(len(aye.get('results'))))
    for aii in aye.get('results'):
        print(aii.get('name'))
