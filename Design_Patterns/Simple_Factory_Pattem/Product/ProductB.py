# -*- coding: utf-8 -*-
"""
产品B
"""
from Simple_Factory_Pattem.Product import IProduct


class ProductB(IProduct):
    """
    产品B
    """
    def function(self):
        """产品功能"""
        print('这是产品B')