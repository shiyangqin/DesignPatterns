# -*- coding: utf-8 -*-
from Abstract_Factory_Pattern.Factory.XiaomiFactory import XiaomiFactory
from Abstract_Factory_Pattern.Factory.HuaweiFactory import HuaweiFactory


if __name__ == '__main__':
    print('================小米系列产品================')
    xiaomiFactory = XiaomiFactory()
    # 小米手机
    xiaomiPhone = xiaomiFactory.createPhone()
    xiaomiPhone.start()
    xiaomiPhone.callUp()
    xiaomiPhone.sendSMS()
    xiaomiPhone.shutdown()
    # 小米路由器
    xiaomiRouter = xiaomiFactory.createRouter()
    xiaomiRouter.start()
    xiaomiRouter.setting()
    xiaomiRouter.openWiFi()
    xiaomiRouter.shutdown()

    print('================华为系列产品================')
    huaweiFactory = HuaweiFactory()
    # 华为手机
    huaweiPhone = huaweiFactory.createPhone()
    huaweiPhone.start()
    huaweiPhone.callUp()
    huaweiPhone.sendSMS()
    huaweiPhone.shutdown()
    # 华为路由器
    huaweiRouter = huaweiFactory.createRouter()
    huaweiRouter.start()
    huaweiRouter.setting()
    huaweiRouter.openWiFi()
    huaweiRouter.shutdown()
