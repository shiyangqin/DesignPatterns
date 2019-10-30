# -*- coding: utf-8 -*-
"""
产品接口
"""

class IPhone (object):
    """
    手机产品接口
    """
    def start(self):
        """开机"""
        pass

    def shutdown(self):
        """关机"""
        pass

    def callUp(self):
        """打电话"""
        pass

    def sendSMS(self):
        """发短信"""
        pass


class IRouter(object):
    """
    路由器产品接口
    """

    def start(self):
        """开机"""
        pass

    def shutdown(self):
        """关机"""
        pass

    def openWiFi(self):
        """打开WiFi"""
        pass

    def setting(self):
        """设置参数"""
        pass
