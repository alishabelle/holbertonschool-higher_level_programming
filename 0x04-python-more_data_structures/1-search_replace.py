#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if search == item:
            item = replace
            new_list.append(item)
        else:
            new_list.append(item)
    return (new_list)
