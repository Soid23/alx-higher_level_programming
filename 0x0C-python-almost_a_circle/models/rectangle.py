#!/usr/bin/python3
"""Defines a rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rep a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a new rectangle
        Args: width - new widht of rect.
        height - new height of rect.
        x(int) x co-ordinate of rect.
        y(int) y co-ordinate of rect.
        id - identity of rect.
        Reaise:
        ValueError - if x or y <= 0/if width or height is less than 0.
        TypeError - if x or y is not an int/ if width/height not int.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)



def area(self):
    """Returns the area value of rect"""
    return self.width * self.height


def display(self):
    """update class rectangle and 
    prints in stdout using # character
    """
