# -*- coding: utf-8 -*-
"""
品牌抽象类
"""


class Brand(object):
    """
    品牌抽象类
    """
    def __init__(self, electricAppliance):
        self._electricAppliance = electricAppliance

    def description(self):
        """描述"""
        pass
