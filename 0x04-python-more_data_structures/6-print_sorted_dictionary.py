#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary.items())
    for i in range(len(a)):
        print("{}".format(a[i][0]) + ": " + "{}".format(a[i][1]))
