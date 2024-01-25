#!/usr/bin/python3
"""
A module for the square class
"""


class Square:
    """
    A square class for this task
    """
    def __init__(self, size=0):
        """
        Thia Initializes the class
        Arguments:
            size: The size off squaree
        """
        self.size = size

    @property
    def size(self):
        """
        This function is for the square size
        Returns:
            The size of squar(int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This function sets square size
        Args:
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
        This function gets area of  square
        Returns:
            The area of square(int)
        """
        return self.__size ** 2
