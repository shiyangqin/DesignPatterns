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
    def create_product(self, p_type):
        """
        生产产品
        :type 产品类型  A  B  C
        """
        if p_type == 'A':
            return ProductA()
        if p_type == 'B':
            return ProductB()
        if p_type == 'C':
            return ProductC()
        return None
