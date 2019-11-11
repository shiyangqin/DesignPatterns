# -*- coding: utf-8 -*-
"""
产品B
"""
from Simple_Factory_Pattern.Product import IProduct


class ProductB(IProduct):
    """
    产品B
    """
    def show(self):
        """显示产品信息"""
        print('这是产品B')