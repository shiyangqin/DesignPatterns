# -*- coding: utf-8 -*-
"""
海尔
"""
from bridge_pattern.brand import Brand


class Haier(Brand):
    """
    海尔
    """
    def __init__(self, electric_appliance):
        Brand.__init__(self, electric_appliance)
        self._name = "海尔"

    def description(self):
        """描述"""
        return self._name + self._electric_appliance.description()
