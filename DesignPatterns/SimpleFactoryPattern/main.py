# -*- coding: utf-8 -*-
"""
主函数
"""
from SimpleFactoryPattern.Factory import Factory


if __name__ == '__main__':
    factory = Factory()
    print('================产品A================')
    productA = factory.createProduct('A')
    productA.show()
    print('================产品B================')
    productB = factory.createProduct('B')
    productB.show()
    print('================产品C================')
    productC = factory.createProduct('C')
    productC.show()
