#!/usr/bin/python3
"""Adds 2 integers"""


def add_integer(a, b=98):
    """a function that takes two integers or float and
    returns the sum. The input must be integers or float otherwise
    aTypeError is displayed
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
