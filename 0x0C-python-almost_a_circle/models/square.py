#!/usr/bin/python3
"""
Square class Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initializes attributes
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method overide
        """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x,
                                              self.y, self.width))

    @property
    def size(self):
        """method to get width
        """
        return self.width

    @size.setter
    def size(self, value):
        """method to set width and height
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the square
        """

        if args:
            i = 0
            mylist = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, mylist[i], arg)
                i += 1
            return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary rep of the square
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
