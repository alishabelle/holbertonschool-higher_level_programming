#!/usr/bin/python3
""" documentation module - My list """


class MyList(list):
    """ class that inherits list """

    def print_sorted(self):
        print(sorted(self))
