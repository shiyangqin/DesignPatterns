# -*- coding: utf-8 -*-
"""
主函数
"""
from Simple_Factory_Pattem.Factory import Factory


if __name__ == '__main__':
    factory = Factory()
    print('================产品A================')
    productA = factory.createProduct('A')
    productA.function()
    print('================产品B================')
    productB = factory.createProduct('B')
    productB.function()
