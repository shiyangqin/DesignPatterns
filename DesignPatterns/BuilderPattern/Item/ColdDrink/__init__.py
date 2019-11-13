# -*- coding: utf-8 -*-
"""
饮料接口
"""
from BuilderPattern.Item import Item
from BuilderPattern.Packing.Bottle import Bottle


class ColdDrink(Item):
    """
    饮料接口
    """
    def packing(self):
        return Bottle()
