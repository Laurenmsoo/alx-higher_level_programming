#!/usr/bin/python3
"""
2-is_same_class class module
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a given class
        Args:
            obj:the object to check
            a_class: class to relate the object to
            Returns true if the object is an exact instant
            of the class
    """
    if type(obj) is not a_class:
        return False
    else:
        return True
