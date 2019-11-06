# -*- coding: utf-8 -*-
"""
小米工厂接口
"""
from Abstract_Factory_Pattern.Factory import IFactory
from Abstract_Factory_Pattern.Procuct.Phone import XiaomiPhone
from Abstract_Factory_Pattern.Procuct.Router import XiaomiRouter


class XiaomiFactory(IFactory):
    """
    小米产品工厂
    """
    def createPhone(self):
        """生产手机"""
        print('>>>>>>生产小米手机')
        return XiaomiPhone()

    def createRouter(self):
        """生产路由器"""
        print('>>>>>>生产小米路由器')
        return XiaomiRouter()
