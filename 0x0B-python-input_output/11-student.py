#!/usr/bin/python3
"""Student class module."""


class Student:
    """student class rep."""
    def __init__(self, first_name, last_name, age):
        """attributes defination."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary."""
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        """Loads attributes from json."""
        for key, value in json.items():
            self.__dict__[key] = value
