# -*- coding: utf-8 -*-
"""
小米工厂接口
"""
from Abstract_Factory_Pattern.ProductFactory import IProductFactory
from Abstract_Factory_Pattern.Procuct.XiaomiProduct import XiaomiPhone,XiaomiRouter


class XiaomiProductFactory(IProductFactory):
    """
    小米产品工厂
    """
    def producePhone(self):
        """生产手机"""
        print('>>>>>>生产小米手机')
        return XiaomiPhone()

    def produceRouter(self):
        """生产路由器"""
        print('>>>>>>生产小米路由器')
        return XiaomiRouter()
