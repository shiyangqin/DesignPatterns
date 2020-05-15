# -*- coding: utf-8 -*-
"""
主函数
"""
from factory_method_pattern.factory.factory_a import FactoryA
from factory_method_pattern.factory.factory_b import FactoryB


if __name__ == '__main__':
    print('================产品A================')
    factory_a = FactoryA()
    product_a = factory_a.create_product()
    product_a.show()
    print('================产品B================')
    factory_b = FactoryB()
    product_b = factory_a.create_product()
    product_b.show()
