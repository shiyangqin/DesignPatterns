# -*- coding: utf-8 -*-
"""
工厂A
"""
from factory_method_pattern.factory import IFactory
from factory_method_pattern.product.product_a import ProductA


class FactoryA(IFactory):
    """
    工厂A
    """
    def create_product(self):
        """生产产品A"""
        return ProductA()
