# -*- coding: utf-8 -*-
"""
工厂A
"""
from FactoryMethodPattern.Factory import IFactory
from FactoryMethodPattern.Product.ProductA import ProductA


class FactoryA(IFactory):
    """
    工厂A
    """
    def createProduct(self):
        """生产产品A"""
        return ProductA()
