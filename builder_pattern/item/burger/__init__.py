# -*- coding: utf-8 -*-
from builder_pattern.item import Item
from builder_pattern.packing.wrapper import Wrapper


class Burger(Item):
    """汉堡接口"""

    def packing(self):
        return Wrapper()
