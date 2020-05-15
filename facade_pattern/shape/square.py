# -*- coding: utf-8 -*-
from facade_pattern.shape import Shape


class Square(Shape):
    """正方形"""

    def draw(self):
        """画正方形"""
        print("Square::draw()")
