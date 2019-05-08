#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    new_jawn = []
    for i in my_list:
        if i % 2 == 0:
            new_jawn.append(True)
        else:
            new_jawn.append(False)
    return new_jawn
