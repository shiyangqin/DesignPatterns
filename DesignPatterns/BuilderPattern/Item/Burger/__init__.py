# -*- coding: utf-8 -*-
"""
汉堡接口
"""
from BuilderPattern.Item import Item
from BuilderPattern.Packing.Wrapper import Wrapper


class Burger(Item):
    """
    汉堡接口
    """
    def packing(self):
        return Wrapper()
