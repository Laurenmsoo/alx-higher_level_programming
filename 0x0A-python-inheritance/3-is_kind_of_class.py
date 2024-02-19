#!/usr/bin/python3
''' is_kind_of_class class module
'''


def is_kind_of_class(obj, a_class):
    '''checks if an object is an instance of a specified class
    Returns true if it is or false if it is not an instance
    '''
    return isinstance(obj, a_class)
