# -*- coding: utf-8 -*-
from BridgePattern.Brand.Gree import Gree
from BridgePattern.Brand.Haier import Haier
from BridgePattern.Brand.Midea import Midea
from BridgePattern.ElectricAppliance.AirConditioner import AirConditioner
from BridgePattern.ElectricAppliance.WashingMachine import WashingMachine
from BridgePattern.ElectricAppliance.WaterHeater import WaterHeater


if __name__ == '__main__':
    print("------------------格力------------------")
    greeAirConditioner = Gree(AirConditioner())
    print(greeAirConditioner.description())
    greeWashingMachine = Gree(WashingMachine())
    print(greeWashingMachine.description())
    greeWaterHeater = Gree(WaterHeater())
    print(greeWaterHeater.description())

    print("------------------海尔------------------")
    haierAirConditioner = Haier(AirConditioner())
    print(haierAirConditioner.description())
    haierWashingMachine = Haier(WashingMachine())
    print(haierWashingMachine.description())
    haierWaterHeater = Haier(WaterHeater())
    print(haierWaterHeater.description())

    print("------------------美的------------------")
    mideaAirConditioner = Midea(AirConditioner())
    print(mideaAirConditioner.description())
    mideaWashingMachine = Midea(WashingMachine())
    print(mideaWashingMachine.description())
    mideaWaterHeater = Midea(WaterHeater())
    print(mideaWaterHeater.description())