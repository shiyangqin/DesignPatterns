# -*- coding: utf-8 -*-
"""
美的
"""
from BridgePattern.Brand import Brand


class Midea(Brand):
    """
    格力
    """
    def __init__(self, electricAppliance):
        Brand.__init__(self, electricAppliance)
        self._name = "美的"

    def description(self):
        """描述"""
        return self._name + self._electricAppliance.description()
