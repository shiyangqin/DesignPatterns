# -*- coding: utf-8 -*-
"""
正方形
"""
from FacadePattern.Shape import Shape


class Square(Shape):
    """
    正方形
    """
    def draw(self):
        """画正方形"""
        print("Square::draw()")
