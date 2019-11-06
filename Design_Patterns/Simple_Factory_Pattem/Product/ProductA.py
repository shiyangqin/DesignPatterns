# -*- coding: utf-8 -*-
"""
产品A
"""
from Simple_Factory_Pattem.Product import IProduct


class ProductA(IProduct):
    """
    产品A
    """
    def function(self):
        """产品功能"""
        print('这是产品A')