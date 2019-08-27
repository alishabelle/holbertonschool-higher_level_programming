#!/usr/bin/python3
""" script takes in a letter and sends a post request """

import sys
import requests

if __name__ == '__main__':

url = 'http://0.0.0.0:5000/search_user'
try:
    aye = requests.post(url, data={'q': sys.argv[1]})
except IndexError:
    aye = requests.post(url, data={'q': ""})
try:
    aye = aye.json()
    if not aye:
        print('No result')
    else:
        print('[{}] {}'.format(aye.get('id'), aye.get('name')))
except ValueError:
    print('Not a valid JSON')
