# -*- coding: utf-8 -*-
"""
工厂
"""
from Simple_Factory_Pattern.Product.ProductA import ProductA
from Simple_Factory_Pattern.Product.ProductB import ProductB
from Simple_Factory_Pattern.Product.ProductC import ProductC


class Factory(object):
    """
    工厂
    """
    def createProduct(self, type):
        """
        生产产品
        :type 产品类型  A  B  C
        """
        if not type:
            return None
        if type == 'A':
            return ProductA()
        if type == 'B':
            return ProductB()
        if type == 'C':
            return ProductC()
        return None
