# -*- coding: utf-8 -*-
from simple_factory_pattern.product import IProduct


class ProductA(IProduct):
    """产品A"""

    def show(self):
        """显示产品信息"""
        print('这是产品A')
