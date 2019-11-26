# -*- coding: utf-8 -*-
"""
海尔
"""
from BridgePattern.Brand import Brand


class Haier(Brand):
    """
    海尔
    """
    def __init__(self, electricAppliance):
        Brand.__init__(self, electricAppliance)
        self._name = "海尔"

    def description(self):
        """描述"""
        return self._name + self._electricAppliance.description()
