# -*- coding: utf-8 -*-
"""
格力
"""
from bridge_pattern.brand import Brand


class Gree(Brand):
    """
    格力
    """
    def __init__(self, electric_appliance):
        Brand.__init__(self, electric_appliance)
        self._name = "格力"

    def description(self):
        """描述"""
        return self._name + self._electric_appliance.description()
