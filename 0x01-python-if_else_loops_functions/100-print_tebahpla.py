#!/usr/bin/python3
for idx, a in enumerate(range(122, 96, -1)):
    if idx % 2 != 0:
        a -= 32
    print("{:c}".format(a), end="")
