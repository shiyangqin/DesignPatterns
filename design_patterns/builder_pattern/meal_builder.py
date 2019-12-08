# -*- coding: utf-8 -*-
"""
套餐建造者
"""
from builder_pattern.meal import Meal
from builder_pattern.item.cold_drink.coke import Coke
from builder_pattern.item.cold_drink.pepsi import Pepsi
from builder_pattern.item.burger.veg_burger import VegBurger
from builder_pattern.item.burger.chicken_burger import ChickenBurger


class MealBuilder(object):
    """
    套餐建造者
    """
    def prepare_veg_meal(self):
        """构造素食套餐"""
        meal = Meal()
        meal.add(VegBurger())
        meal.add(Coke())
        return meal

    def prepare_non_veg_meal(self):
        """构造荤食套餐"""
        meal = Meal()
        meal.add(ChickenBurger())
        meal.add(Pepsi())
        return meal
