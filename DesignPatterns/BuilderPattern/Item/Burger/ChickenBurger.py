# -*- coding: utf-8 -*-
"""
鸡肉汉堡
"""
from BuilderPattern.Item.Burger import Burger


class ChickenBurger(Burger):
    """
    鸡肉汉堡
    """
    def name(self):
        """汉堡名称"""
        return "Chicken Burger"

    def price(self):
        """汉堡价格"""
        return 50.5
