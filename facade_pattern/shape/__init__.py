# -*- coding: utf-8 -*-
"""
模型类接口
"""

class Shape(object):
    """
    模型类接口
    """
    def draw(self):
        """画模型"""
        pass


from facade_pattern.shape.circle import Circle
from facade_pattern.shape.rectangle import Rectangle
from facade_pattern.shape.square import Square


class ShapeMaker(object):
    """
    模型外观类
    """
    def __init__(self):
        self.__rectangle = Rectangle()
        self.__square = Square()
        self.__circle = Circle()

    def draw_circle(self):
        """画圆形"""
        self.__circle.draw()

    def draw_rectangle(self):
        """画矩形"""
        self.__rectangle.draw()

    def draw_square(self):
        """画正方形"""
        self.__square.draw()
