#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = number % 10 if number >= 0 else number % -10
if last_d > 5:
    print("Last digit of {:d}".format(number) + " is " +
          "{:d} and is greater than 5".format(last_d))
elif last_d == 0:
    print("Last digit of {:d}".format(number) + " is " +
          "{:d} and is 0".format(last_d))
elif last_d < 6 and last_d != 0:
    print("Last digit of {:d}".format(number) + " is " +
          "{:d} and is less than 6 and not 0".format(last_d))
