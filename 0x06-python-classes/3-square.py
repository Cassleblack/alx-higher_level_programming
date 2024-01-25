#!/usr/bin/python3
"""
A module for this class task 3
"""


class Square:
    """
    A square class for this task
    """
    def __init__(self, size=0):
        """
        Initializes the class
        Arguments:
            size: The size of square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
            A function to get area of square
            Returns:
                The area of square(int)
        """
        return self.__size ** 2
