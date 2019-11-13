# -*- coding: utf-8 -*-
"""
素食汉堡
"""
from BuilderPattern.Item.Burger import Burger


class VegBurger(Burger):
    """
    素食汉堡
    """
    def name(self):
        """汉堡名称"""
        return "Veg Burger"

    def price(self):
        """汉堡价格"""
        return 25.0
