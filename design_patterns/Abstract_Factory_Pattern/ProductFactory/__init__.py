# -*- coding: utf-8 -*-
"""
工厂接口
"""


class IFactory(object):
    """
    工厂接口
    """

    def createPhone(self):
        """生产手机"""
        pass

    def createRouter(self):
        """生产路由器"""
        pass
