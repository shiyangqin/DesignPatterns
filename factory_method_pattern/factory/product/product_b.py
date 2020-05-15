# -*- coding: utf-8 -*-
from factory_method_pattern.factory.product import IProduct


class ProductB(IProduct):
    """产品B"""
    def show(self):
        """显示产品信息"""
        print('这是产品B')
