# -*- coding: utf-8 -*-
"""
华为产品
"""
from Abstract_Factory.Procuct import IPhoneProduct,IRouterProduct


class HuaweiPhone(IPhoneProduct):
    """
    华为手机
    """
    def start(self):
        """开机"""
        print('华为手机开机')

    def shutdown(self):
        """关机"""
        print('华为手机关机')

    def callUp(self):
        """打电话"""
        print('华为手机打电话')

    def sendSMS(self):
        """发短信"""
        print('华为手机发短信')


class HuaweiRouter(IRouterProduct):
    """
    华为路由器
    """
    def start(self):
        """开机"""
        print('启动华为路由器')

    def shutdown(self):
        """关机"""
        print('关闭华为路由器')

    def openWiFi(self):
        """打开WiFi"""
        print('打开华为路由器的WiFi功能')

    def setting(self):
        """设置参数"""
        print('设置华为路由器参数')
