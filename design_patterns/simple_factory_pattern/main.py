# -*- coding: utf-8 -*-
"""
主函数
"""
from simple_factory_pattern.factory import Factory


if __name__ == '__main__':
    factory = Factory()
    print('================产品A================')
    product_a = factory.create_product('A')
    product_a.show()
    print('================产品B================')
    product_b = factory.create_product('B')
    product_b.show()
    print('================产品C================')
    product_c = factory.create_product('C')
    product_c.show()
