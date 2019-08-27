#!/usr/bin/python3
""" fetches url """

import requests

if __name__ == '__main__':

    set = requests.request('GET', 'https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".format
          (type(set.text), set.text))
