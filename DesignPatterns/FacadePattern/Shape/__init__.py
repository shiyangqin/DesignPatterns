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


from FacadePattern.Shape import Circle,Rectangle,Square


class ShapeMaker(object):
    """
    模型外观类
    """
    def __init__(self):
        self.__Rectangle = Rectangle.Rectangle()
        self.__Square = Square.Square()
        self.__Circle = Circle.Circle()

    def drawCircle(self):
        """画圆形"""
        self.__Circle.draw()

    def drawRectangle(self):
        """画矩形"""
        self.__Rectangle.draw()

    def drawSquare(self):
        """画正方形"""
        self.__Square.draw()
