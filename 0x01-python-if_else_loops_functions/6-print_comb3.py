#!/usr/bin/python3
for i in range(0, 9):
    for j in range (i +1 , 10):
        if i == 7 and j == 8:
            print('{:d}{:d}'.format(i, j))
        else:
            print('{:d}{:d}'.format(i, j), end=', ')
