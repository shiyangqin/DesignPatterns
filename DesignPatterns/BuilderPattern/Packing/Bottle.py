# -*- coding: utf-8 -*-
"""
杯装
"""
from BuilderPattern.Packing import Packing

class Bottle(Packing):
    """
    杯装
    """
    def pack(self):
        """杯装"""
        return "Bottle"
