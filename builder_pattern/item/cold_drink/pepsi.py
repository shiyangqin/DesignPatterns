# -*- coding: utf-8 -*-
from builder_pattern.item.cold_drink import ColdDrink


class Pepsi(ColdDrink):
    """百事可乐"""

    def name(self):
        """可乐名称"""
        return "Pepsi"

    def price(self):
        """可乐价格"""
        return 35.0
