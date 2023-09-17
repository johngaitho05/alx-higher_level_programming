#!/usr/bin/python3

"""
A rectangle class
"""

from .base import Base


class Rectangle(Base):
    """Rectangle class derived from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(id)
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise TypeError("width must be > 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise TypeError("width must be > 0")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise TypeError("x must be >= 0")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise TypeError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @property
    def height(self):
        """Get height"""
        return self.__height

    @property
    def x(self):
        """Get x"""
        return self.__x

    @property
    def y(self):
        """Get y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise TypeError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise TypeError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes the area of rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle using #"""
        res = ""
        res += "\n" * self.y
        for i in range(self.height):
            res += " " * self.x
            res += '#' * self.width
            if i < self.height - 1:
                res += '\n'
        print(res)

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Update properties based on args and kwargs
        :param args: (id, width, height, x and y) respectively
        :param kwargs: an optional dictionary containing the keys (id,
         width, height, x and y) whose value is used to update the
         attributes of self
        """
        for i in range(min(len(args), 5)):
            arg = args[i]
            if i == 0:
                self.id = arg
            elif i == 1:
                self.width = arg
            elif i == 2:
                self.height = arg
            elif i == 3:
                self.x = arg
            else:
                self.y = arg
        if not args and kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
