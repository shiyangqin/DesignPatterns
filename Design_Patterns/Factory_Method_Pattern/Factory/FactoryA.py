# -*- coding: utf-8 -*-
"""
工厂A
"""
from Factory_Method_Pattern.Factory import IFactory
from Factory_Method_Pattern.Product.ProductA import ProductA


class FactoryA(IFactory):
    """
    工厂A
    """
    def createProduct(self):
        """生产产品A"""
        return ProductA()
