# -*- coding: utf-8 -*-
"""
矩形
"""
from FacadePattern.Shape import Shape


class Rectangle(Shape):
    """
    矩形
    """
    def draw(self):
        """画矩形"""
        print("Rectangle::draw()")
