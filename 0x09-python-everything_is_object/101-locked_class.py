#!/usr/bin/python3
"""
101-locked_class Module
"""


class LockedClass:
    """ locked class defination. It prevents user from
    dynamically creating new instant.
    """
    __insta__ = ('first_name')
