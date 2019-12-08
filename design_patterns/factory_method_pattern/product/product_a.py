# -*- coding: utf-8 -*-
"""
产品A
"""
from factory_method_pattern.product import IProduct


class ProductA(IProduct):
    """
    产品A
    """
    def show(self):
        """显示产品信息"""
        print('这是产品A')