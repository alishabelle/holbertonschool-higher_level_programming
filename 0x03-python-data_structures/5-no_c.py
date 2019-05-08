#!/usr/bin/python3
def no_c(my_string):
    changer = {99:None, 67:None}
    new_string = my_string.translate(changer)
    return (new_string)
