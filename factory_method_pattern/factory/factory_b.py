# -*- coding: utf-8 -*-
"""
工厂B
"""
from factory_method_pattern.factory import IFactory
from factory_method_pattern.product.product_b import ProductB


class FactoryB(IFactory):
    """
    工厂B
    """
    def create_product(self):
        """生产产品A"""
        return ProductB()
