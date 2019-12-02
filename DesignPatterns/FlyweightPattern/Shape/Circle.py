# -*- coding: utf-8 -*-
"""
圆形
"""
from FacadePattern.Shape import Shape


class Circle(Shape):
    """
    圆形
    """
    def __init__(self, color=None, x=None, y=None, radius=None):
        self.__color = color
        self.__x = x
        self.__y = y
        self.__radius = radius

    def setColor(self, color):
        self.__color = color

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setRadius(self, radius):
        self.__radius = radius

    def draw(self):
        """画圆形"""
        print("Circle::draw()[Color: {}, x: {}, y:{}, radius: {}]".format(self.__color, self.__x, self.__y, self.__radius))
