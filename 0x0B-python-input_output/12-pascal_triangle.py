#!/usr/bin/python3
"""Triangle function defination."""


def pascal_triangle(n):
    """Pascal's Triangle of size n rep.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    tr = [[1]]
    while len(tr) != n:
        t = tr[-1]
        tmp = [1]
        for i in range(len(t) - 1):
            tmp.append(t[i] + t[i + 1])
        tmp.append(1)
        tr.append(tmp)
    return tr
