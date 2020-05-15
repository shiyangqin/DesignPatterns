# -*- coding: utf-8 -*-
"""
可口可乐
"""
from builder_pattern.item.cold_drink import ColdDrink


class Coke(ColdDrink):
    """
    可口可乐
    """
    def name(self):
        """可乐名称"""
        return "Coke"

    def price(self):
        """可乐价格"""
        return 30.0
