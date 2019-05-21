#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    answ = 0

    for index in range(list_length):
        try:
            answ = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new.append(answ)
            answ = 0
    return new
