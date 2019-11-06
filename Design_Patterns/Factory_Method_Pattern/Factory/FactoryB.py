# -*- coding: utf-8 -*-
"""
工厂B
"""
from Factory_Method_Pattern.Factory import IFactory
from Factory_Method_Pattern.Product.ProductB import ProductB


class FactoryB(IFactory):
    """
    工厂B
    """
    def createProduct(self):
        """生产产品A"""
        return ProductB()
