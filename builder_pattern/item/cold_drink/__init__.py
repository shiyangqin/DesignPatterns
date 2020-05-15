# -*- coding: utf-8 -*-
from builder_pattern.item import Item
from builder_pattern.packing.bottle import Bottle


class ColdDrink(Item):
    """饮料接口"""

    def packing(self):
        return Bottle()
