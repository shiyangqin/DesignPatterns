# -*- coding: utf-8 -*-
"""
品牌抽象类
"""


class Brand(object):
    """
    品牌抽象类
    """
    def __init__(self, electric_appliance):
        self._electric_appliance = electric_appliance

    def description(self):
        """描述"""
        pass
