#!/usr/bin/python3

""" BaseGeometry class module """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from basegeometry class"""

    def __init__(self, width, height):
        """
        init function
            Args:
                width: width dimension
                height: length dimension
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string rep of the triangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
