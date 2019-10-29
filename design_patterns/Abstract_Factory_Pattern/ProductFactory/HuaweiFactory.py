# -*- coding: utf-8 -*-
"""
华为工厂接口
"""
from Abstract_Factory_Pattern.ProductFactory import IFactory
from Abstract_Factory_Pattern.Procuct.Phone import HuaweiPhone
from Abstract_Factory_Pattern.Procuct.Router import HuaweiRouter


class HuaweiFactory(IFactory):
    """
    华为产品工厂
    """
    def createPhone(self):
        """生产手机"""
        print('>>>>>>生产华为手机')
        return HuaweiPhone()

    def createRouter(self):
        """生产路由器"""
        print('>>>>>>生产华为路由器')
        return HuaweiRouter()
