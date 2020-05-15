# -*- coding: utf-8 -*-
from bridge_pattern.brand.gree import Gree
from bridge_pattern.brand.haier import Haier
from bridge_pattern.brand.midea import Midea
from bridge_pattern.electric_appliance.air_conditioner import AirConditioner
from bridge_pattern.electric_appliance.washing_machine import WashingMachine
from bridge_pattern.electric_appliance.water_heater import WaterHeater


if __name__ == '__main__':
    print("------------------格力------------------")
    gree_air_conditioner = Gree(AirConditioner())
    print(gree_air_conditioner.description())
    gree_washing_machine = Gree(WashingMachine())
    print(gree_washing_machine.description())
    gree_water_heater = Gree(WaterHeater())
    print(gree_water_heater.description())

    print("------------------海尔------------------")
    haier_air_conditioner = Haier(AirConditioner())
    print(haier_air_conditioner.description())
    haier_washing_machine = Haier(WashingMachine())
    print(haier_washing_machine.description())
    haier_water_heater = Haier(WaterHeater())
    print(haier_water_heater.description())

    print("------------------美的------------------")
    midea_air_conditioner = Midea(AirConditioner())
    print(midea_air_conditioner.description())
    midea_washing_machine = Midea(WashingMachine())
    print(midea_washing_machine.description())
    midea_water_heater = Midea(WaterHeater())
    print(midea_water_heater.description())