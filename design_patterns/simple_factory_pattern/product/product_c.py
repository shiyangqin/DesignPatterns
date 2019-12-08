# -*- coding: utf-8 -*-
"""
产品C
"""
from simple_factory_pattern.product import IProduct


class ProductC(IProduct):
    """
    产品B
    """
    def show(self):
        """显示产品信息"""
        print('这是产品C')
