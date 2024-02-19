#!/usr/bin/python3
"""
The lookup function module
"""


def lookup(obj):
    """
    The lookup function
        Returns a list of available attributes and
                 methods of an object
    """
    return dir(obj)
