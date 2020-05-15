# -*- coding: utf-8 -*-
from bridge_pattern.electric_appliance import ElectricAppliance


class WaterHeater(ElectricAppliance):
    """热水器"""

    def __init__(self):
        self._name = "热水器"

    def description(self):
        """描述"""
        return self._name
