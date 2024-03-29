#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """initiatializes the rectangle with height and
        width attributes
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets thewidth attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns printable string rep of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
