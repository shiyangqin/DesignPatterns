# -*- coding: utf-8 -*-
"""
华为工厂接口
"""
from Abstract_Factory_Pattern.ProductFactory import IProductFactory
from Abstract_Factory_Pattern.Procuct.HuaweiProduct import HuaweiPhone,HuaweiRouter


class HuaweiProductFactory(IProductFactory):
    """
    华为产品工厂
    """
    def producePhone(self):
        """生产手机"""
        print('>>>>>>生产华为手机')
        return HuaweiPhone()

    def produceRouter(self):
        """生产路由器"""
        print('>>>>>>生产华为路由器')
        return HuaweiRouter()
