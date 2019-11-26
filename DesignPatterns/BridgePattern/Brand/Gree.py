# -*- coding: utf-8 -*-
"""
格力
"""
from BridgePattern.Brand import Brand


class Gree(Brand):
    """
    格力
    """
    def __init__(self, electricAppliance):
        Brand.__init__(self, electricAppliance)
        self._name = "格力"

    def description(self):
        """描述"""
        return self._name + self._electricAppliance.description()
