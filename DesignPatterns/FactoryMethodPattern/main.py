# -*- coding: utf-8 -*-
"""
主函数
"""
from FactoryMethodPattern.Factory.FactoryA import FactoryA
from FactoryMethodPattern.Factory.FactoryB import FactoryB


if __name__ == '__main__':
    print('================产品A================')
    factoryA = FactoryA()
    productA = factoryA.createProduct()
    productA.show()
    print('================产品B================')
    factoryA = FactoryB()
    productB = factoryA.createProduct()
    productB.show()
