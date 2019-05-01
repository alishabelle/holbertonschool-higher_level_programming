#!/usr/bin/python3
def uppercase(str):
    for num in str:
        num = ord(num)
        if num >= 97 and num <= 122:
            num = num - 32
        print("{:c}".format(num), end="")
    print()
