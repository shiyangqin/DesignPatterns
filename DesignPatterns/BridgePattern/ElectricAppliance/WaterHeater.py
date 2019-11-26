# -*- coding: utf-8 -*-
"""
热水器
"""
from BridgePattern.ElectricAppliance import ElectricAppliance


class WaterHeater(ElectricAppliance):
    """
    热水器
    """
    def __init__(self):
        self._name = "热水器"

    def description(self):
        """描述"""
        return self._name
