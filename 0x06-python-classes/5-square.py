#!/usr/bin/python3
"""
A module containing the square class
"""


class Square:
    """
    A square class for this task
    """
    def __init__(self, size=0):
        """
        This function Initializes the class
        Arguments:
            size: The size of  squ
        """
        self.size = size

    @property
    def size(self):
        """
        A function for square size
        Returns:
            The size of square(int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This function sets the square size
        Arguments:
            value: The new size the square gets

        Returns:
            NULL NULL
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This function twil get the area of the square
        Returns:
            The area of squar(int)
        """
        return self.__size ** 2

    def my_print(self):
        """
        This function will be  printing '#' squares
        Returns:
            NULL NULL
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print('#', end="")
                print()
