# -*- coding: utf-8 -*-


class Shape(object):
    """模型类接口"""

    def draw(self):
        """画模型"""
        pass


# 在这里导入的原因是因为这些类实现了上面的抽象类，在文件一开始就导入会报错
from facade_pattern.shape.circle import Circle
from facade_pattern.shape.rectangle import Rectangle
from facade_pattern.shape.square import Square


class ShapeMaker(object):
    """模型外观类"""

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
