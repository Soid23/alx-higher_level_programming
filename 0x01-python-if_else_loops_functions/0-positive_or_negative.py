#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:e} is positive")
elif number == 0:
    print(f"{number:e} is zero")
else:
    print(f"{number:e} is negative")

