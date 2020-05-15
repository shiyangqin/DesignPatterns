# -*- coding: utf-8 -*-
from facade_pattern.shape import Shape


class Circle(Shape):
    """圆形"""

    def __init__(self, color=None, x=None, y=None, radius=None):
        self.__color = color
        self.__x = x
        self.__y = y
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_radius(self, radius):
        self.__radius = radius

    def draw(self):
        """画圆形"""
        print(
            "Circle::draw()[Color: {}, x: {}, y:{}, radius: {}]".format(self.__color, self.__x, self.__y, self.__radius)
        )
