# -*- coding: utf-8 -*-
from bridge_pattern.brand import Brand


class Midea(Brand):
    """格力"""

    def __init__(self, electric_appliance):
        Brand.__init__(self, electric_appliance)
        self._name = "美的"

    def description(self):
        """描述"""
        return self._name + self._electric_appliance.description()
