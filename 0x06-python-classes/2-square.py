#!/usr/bin/python3
"""
A module for  the square class
"""


class Square:
    """
    A square class for this task
    """
    def __init__(self, size=0):
        """
        Initializes the class
        Arguments:
            size: The size of the square class
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
