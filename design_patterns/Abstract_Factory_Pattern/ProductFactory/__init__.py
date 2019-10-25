# -*- coding: utf-8 -*-
"""
工厂接口
"""


class IProductFactory(object):
    """
    工厂接口
    """

    def producePhone(self):
        """生产手机"""
        pass

    def produceRouter(self):
        """生产路由器"""
        pass
