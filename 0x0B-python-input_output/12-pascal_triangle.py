#!/usr/bin/python3
'''12-pascal_triangle.py'''


def pascal_triangle(n):
    '''Function returns the ppascal triangle
        witht the number of rows based on n
    '''
    if n <= 0:
        return []

    res = [[1]]  # Handle first line of pascal triangle
    for i in range(n - 1):  # Minus the initial [[1]]
        temp = [0] + res[-1] + [0]  # Temporary to put zero at start and end
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])  # Whole computation goes on here
        res.append(row)
    return res
