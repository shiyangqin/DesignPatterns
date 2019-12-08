# -*- coding: utf-8 -*-
"""
工厂
"""
from simple_factory_pattern.product.product_a import ProductA
from simple_factory_pattern.product.product_b import ProductB
from simple_factory_pattern.product.product_c import ProductC


class Factory(object):
    """
    工厂
    """
    def create_product(self, type):
        """
        生产产品
        :type 产品类型  A  B  C
        """
        if type == 'A':
            return ProductA()
        if type == 'B':
            return ProductB()
        if type == 'C':
            return ProductC()
        return None
