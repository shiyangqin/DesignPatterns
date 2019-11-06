# -*- coding: utf-8 -*-
"""
主函数
"""
from Factory_Method_Pattern.Factory.FactoryA import FactoryA
from Factory_Method_Pattern.Factory.FactoryB import FactoryB


if __name__ == '__main__':
    print('================产品A================')
    factoryA = FactoryA()
    productA = factoryA.createProduct()
    productA.function()
    print('================产品B================')
    factoryA = FactoryB()
    productB = factoryA.createProduct()
    productB.function()
