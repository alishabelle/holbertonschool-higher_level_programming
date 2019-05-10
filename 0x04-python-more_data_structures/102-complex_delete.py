#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    newDict = a_dictionary.items()
    emptyList = []

    for empty in newDict:
        if empty[1] is value:
            emptyList.append(empty[0])
    for index in emptyList:
        del a_dictionary[index]
    return a_dictionary
