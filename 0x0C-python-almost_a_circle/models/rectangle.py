#!/usr/bin/python3
"""
imports base class module
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle subclass that inherits from the base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the attributes
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """return the area"""
        return self.width * self.height

    def update(self, *args, **kwargs):
        """updates attributes"""
        if args:
            mylist = ['id', 'width', 'height', 'x', 'y']
            i = 0
            for arg in args:
                setattr(self, mylist[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def display(self):
        """print to std out
        """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        """string overide"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def to_dictionary(self):
        """dictionary rep of the rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """method to set width"""
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """method to get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """method to set height"""
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """method to get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """method to set x"""
        self.integer_validator2('x', value)
        self.__x = value

    @property
    def y(self):
        """method get y """
        return self.__y

    @y.setter
    def y(self, value):
        """method to get y"""
        self.integer_validator2('y', value)
        self.__y = value
