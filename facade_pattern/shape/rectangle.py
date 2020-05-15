# -*- coding: utf-8 -*-
from facade_pattern.shape import Shape


class Rectangle(Shape):
    """矩形"""

    def draw(self):
        """画矩形"""
        print("Rectangle::draw()")
