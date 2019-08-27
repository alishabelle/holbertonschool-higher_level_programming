#!/usr/bin/python3
""" sends post request to url """

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    aye = urllib.request.Request(url, data)
    with urllib.request.urlopen(aye) as response:
        set = response.read()
        print(set.decode('utf-8', 'ignore'))
