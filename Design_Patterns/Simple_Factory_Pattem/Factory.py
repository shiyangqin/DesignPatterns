# -*- coding: utf-8 -*-
"""
工厂
"""
from Simple_Factory_Pattem.Product.ProductA import ProductA
from Simple_Factory_Pattem.Product.ProductB import ProductB


class Factory(object):
    """
    工厂
    """
    def createProduct(self, type):
        """
        生产产品
        :type 产品类型  A  B
        """
        if type == 'A':
            return ProductA()
        if type == 'B':
            return ProductB()
        return None
