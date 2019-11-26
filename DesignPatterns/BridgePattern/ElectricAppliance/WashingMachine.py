# -*- coding: utf-8 -*-
"""
洗衣机
"""
from BridgePattern.ElectricAppliance import ElectricAppliance


class WashingMachine(ElectricAppliance):
    """
    洗衣机
    """
    def __init__(self):
        self._name = "洗衣机"

    def description(self):
        """描述"""
        return self._name
