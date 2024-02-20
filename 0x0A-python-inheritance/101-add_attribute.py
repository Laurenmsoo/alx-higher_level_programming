#!/usr/bin/python3
"""
101-add_attribute class defination
"""


def add_attribute(obj, objname, value):
    """add attribute to object
    args:
        obj: the object
        objname: object name
        value: attribute value
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)
