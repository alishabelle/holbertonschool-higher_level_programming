#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for index in range(0, x):
            if type(my_list[index]) != int:
                continue
            print("{}".format(my_list[index]), end="")
            count += 1
        print("")
        return (count)

    except (TypeError, ValueError):
        pass
