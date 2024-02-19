#!/usr/bin/python3
"""6-base_geometry.py class module.
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raises exception if value is not an int or is less than 0."""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
