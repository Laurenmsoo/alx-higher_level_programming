#!/usr/bin/python3

""" Class that inherits from BaseGeometry class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits from Rectangle """

    def __init__(self, size):
        """Init function
            Args:
                width: width dimension
                height: length dimension
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ Calculates area """
        return super().area()

    def __str__(self):
        """ Print area """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
