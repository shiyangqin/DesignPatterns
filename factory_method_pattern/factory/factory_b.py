# -*- coding: utf-8 -*-
from factory_method_pattern.factory import IFactory
from factory_method_pattern.factory.product.product_b import ProductB


class FactoryB(IFactory):
    """工厂B"""

    def create_product(self):
        """生产产品B"""
        return ProductB()
