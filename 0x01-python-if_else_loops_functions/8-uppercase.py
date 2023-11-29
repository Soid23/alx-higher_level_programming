#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        
         if ord(ch) >= 65 and ord(ch) <= 90:
             print("{:s}".format(ch), end='')

print('/n', end="")

