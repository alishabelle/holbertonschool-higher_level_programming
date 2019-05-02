#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 0:
        print("{:d} arguments.".format(argc, end="\n"))
    elif argc == 1:
        print("{:d} argument:".format(argc, end="\n"))
    else:
        print("{:d} arguments:".format(argc, end="\n"))
        for i, v in enumerate(argv):
            if i == 0:
                continue
            else:
                print("{}: {}".format(i, v, end="\n"))
