# -*- coding: utf-8 -*-
"""
圆形
"""
from facade_pattern.shape import Shape


class Circle(Shape):
    """
    圆形
    """
    def draw(self):
        """画圆形"""
        print("Circle::draw()")
