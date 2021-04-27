#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(repr(number)[-1])
if (last > 5):
    print("Last digit of " + str(number) + " is " + str(last) + " and is greater than 5\n")
elif (last == 0):
    print("Last digit of " + str(number) + " is " + str(last) + " and is 0\n")
else:
    print("Last digit of " + str(number) + " is " + str(last) + " and is less than six and not 0\n")


