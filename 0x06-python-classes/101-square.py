#!/usr/bin/python3
"""Square class definition"""


class Square:
    """A Square class definition"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializer

        Args:
            size (int): size of the square
            position (tuple): position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get and Set size of the square."""
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get and Set position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using #"""

        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        """String representation of a square"""

        if self.__size != 0:
            for i in range(self.__position[1]):
                print()

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")

            for k in range(self.__size):
                print("#", end="")

            if i != self.__size - 1:
                print()
        return ""
