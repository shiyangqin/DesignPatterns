# -*- coding: utf-8 -*-
"""
百事可乐
"""
from BuilderPattern.Item.ColdDrink import ColdDrink


class Pepsi(ColdDrink):
    """
    百事可乐
    """
    def name(self):
        """可乐名称"""
        return "Pepsi"

    def price(self):
        """可乐价格"""
        return 35.0
