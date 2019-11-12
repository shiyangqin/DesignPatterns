# -*- coding: utf-8 -*-
"""
工厂B
"""
from FactoryMethodPattern.Factory import IFactory
from FactoryMethodPattern.Product.ProductB import ProductB


class FactoryB(IFactory):
    """
    工厂B
    """
    def createProduct(self):
        """生产产品A"""
        return ProductB()
