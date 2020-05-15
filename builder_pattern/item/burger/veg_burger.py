# -*- coding: utf-8 -*-
from builder_pattern.item.burger import Burger


class VegBurger(Burger):
    """素食汉堡"""

    def name(self):
        """汉堡名称"""
        return "Veg burger"

    def price(self):
        """汉堡价格"""
        return 25.0
