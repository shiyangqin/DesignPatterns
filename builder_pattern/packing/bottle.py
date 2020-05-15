# -*- coding: utf-8 -*-
from builder_pattern.packing import Packing


class Bottle(Packing):
    """杯装"""

    def pack(self):
        """杯装"""
        return "Bottle"
