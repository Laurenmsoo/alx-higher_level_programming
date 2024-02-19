#!/usr/bin/python3
"""
4-inherits_from.py class module
"""


def inherits_from(obj, a_class):
    """
    checks if an object is an instant of a class that inherited from
    specified class
        Args:
            obj: object ti analyse
            a_class: class to check
            Returns: True if the object is an instance of a
                     class that inherited from otherwise False
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
