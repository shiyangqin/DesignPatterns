# -*- coding: utf-8 -*-
from Abstract_Factory_Pattern.ProductFactory.XiaomiProductFactory import XiaomiProductFactory
from Abstract_Factory_Pattern.ProductFactory.HuaweiProductFactory import HuaweiProductFactory


if __name__ == '__main__':
    print('================小米系列产品================')
    xiaomiProductFactory = XiaomiProductFactory()
    # 小米手机
    xiaomiPhone = xiaomiProductFactory.producePhone()
    xiaomiPhone.start()
    xiaomiPhone.shutdown()
    xiaomiPhone.callUp()
    xiaomiPhone.sendSMS()
    # 小米路由器
    xiaomiRouter = xiaomiProductFactory.produceRouter()
    xiaomiRouter.start()
    xiaomiRouter.shutdown()
    xiaomiRouter.openWiFi()
    xiaomiRouter.setting()

    print('================华为系列产品================')
    huaweiProductFactory = HuaweiProductFactory()
    # 小米手机
    huaweiPhone = huaweiProductFactory.producePhone()
    huaweiPhone.start()
    huaweiPhone.shutdown()
    huaweiPhone.callUp()
    huaweiPhone.sendSMS()
    # 小米路由器
    huaweiRouter = huaweiProductFactory.produceRouter()
    huaweiRouter.start()
    huaweiRouter.shutdown()
    huaweiRouter.openWiFi()
    huaweiRouter.setting()