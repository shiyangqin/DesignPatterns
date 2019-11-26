# -*- coding: utf-8 -*-
"""
空调
"""
from BridgePattern.ElectricAppliance import ElectricAppliance


class AirConditioner(ElectricAppliance):
    """
    空调
    """
    def __init__(self):
        self._name = "空调"

    def description(self):
        """描述"""
        return self._name
