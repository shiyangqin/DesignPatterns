# -*- coding: utf-8 -*-
"""
圆形
"""
from FacadePattern.Shape import Shape


class Circle(Shape):
    """
    圆形
    """
    def draw(self):
        """画圆形"""
        print("Circle::draw()")
