# -*- coding: utf-8 -*-
"""
模型类接口
"""
from FlyweightPattern.Shape.Circle import Circle

class Shape(object):
    """
    模型类接口
    """
    def draw(self):
        """画模型"""
        pass


class ShapeFactory(object):
    """
    模型工厂
    """
    __circleDict = {}

    @classmethod
    def getCircle(cls, color):
        circle = None
        if color in cls.__circleDict:
            circle = cls.__circleDict[color]

        if not circle:
            circle = Circle(color=color)
            cls.__circleDict[color] = circle
            print("Creating circle of color : " + color)
        return circle
