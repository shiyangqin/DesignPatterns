# -*- coding: utf-8 -*-
"""
模型类接口
"""
from flyweight_pattern.shape.circle import Circle

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
    __circle_dict = {}

    @classmethod
    def get_circle(cls, color):
        circle = None
        if color in cls.__circle_dict:
            circle = cls.__circle_dict[color]

        if not circle:
            circle = Circle(color=color)
            cls.__circle_dict[color] = circle
            print("Creating circle of color : " + color)
        return circle
