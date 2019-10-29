# -*- coding: utf-8 -*-
"""
手机产品
"""
from Abstract_Factory_Pattern.Procuct import IPhone


class HuaweiPhone(IPhone):
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


class XiaomiPhone(IPhone):
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
