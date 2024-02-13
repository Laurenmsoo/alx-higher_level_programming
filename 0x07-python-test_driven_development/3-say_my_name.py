#!/usr/bin/python3
"""
    prints name
"""


def say_my_name(first_name, last_name=""):
    """
        Prints My name is <first_Name> <last_Name>
        It takes the the first and last name as parameters
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
