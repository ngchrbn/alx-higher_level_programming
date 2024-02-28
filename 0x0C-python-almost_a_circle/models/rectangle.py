#!/usr/bin/python3

"""Defines a Rectangle class inherited from Base class."""

from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle.

        Args:
            width: Rectangle's width
            height: Rectangle's height
            x: Rectangle's x
            y: Rectangle's y
            id: Rectangle's id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """Returns the Rectangle instance's width"""
            return self.__width

        @property
        def height(self):
            """Returns the Rectangle instance's height."""
            return self.__height

        @property
        def x(self):
            """Returns the Rectangle instance's x."""
            return self.__x

        @property
        def y(self):
            """Returns the Rectangle instance's y."""
            return self.__y

        @width.setter
        def width(self, width):
            """Sets a width

            Args:
                width: width to be set
            """
            self.__width = width

        @height.setter
        def height(self, height):
            """Sets a height

            Args:
                height: height to be set
            """
            self.__height = height

        @x.setter
        def x(self, x):
            """Sets an x

            Args:
                x: x to be set
            """
            self.__x = x

        @y.setter
        def y(self, y):
            """Sets a y

            Args:
                y: y to be set
            """
            self.__y = y
