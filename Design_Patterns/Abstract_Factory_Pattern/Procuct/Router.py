# -*- coding: utf-8 -*-
"""
路由器产品
"""
from Abstract_Factory_Pattern.Procuct import IRouter


class HuaweiRouter(IRouter):
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



class XiaomiRouter(IRouter):
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
