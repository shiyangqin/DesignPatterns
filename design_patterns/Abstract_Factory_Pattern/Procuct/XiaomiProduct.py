# -*- coding: utf-8 -*-
"""
小米产品
"""
from Abstract_Factory_Pattern.Procuct import IPhoneProduct,IRouterProduct


class XiaomiPhone(IPhoneProduct):
    """
    小米手机
    """
    def start(self):
        """开机"""
        print('小米手机开机')

    def shutdown(self):
        """关机"""
        print('小米手机关机')

    def callUp(self):
        """打电话"""
        print('小米手机打电话')

    def sendSMS(self):
        """发短信"""
        print('小米手机发短信')


class XiaomiRouter(IRouterProduct):
    """
    小米路由器
    """
    def start(self):
        """开机"""
        print('启动小米路由器')

    def shutdown(self):
        """关机"""
        print('关闭小米路由器')

    def openWiFi(self):
        """打开WiFi"""
        print('打开小米路由器的WiFi功能')

    def setting(self):
        """设置参数"""
        print('设置小米路由器参数')
