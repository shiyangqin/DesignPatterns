# -*- coding: utf-8 -*-
"""
套餐建造者
"""
from BuilderPattern.Meal import Meal
from BuilderPattern.Item.ColdDrink.Coke import Coke
from BuilderPattern.Item.ColdDrink.Pepsi import Pepsi
from BuilderPattern.Item.Burger.VegBurger import VegBurger
from BuilderPattern.Item.Burger.ChickenBurger import ChickenBurger


class MealBuilder(object):
    """
    套餐建造者
    """
    def prepareVegMeal(self):
        """构造素食套餐"""
        meal = Meal()
        meal.add(VegBurger())
        meal.add(Coke())
        return meal

    def prepareNonVegMeal(self):
        """构造荤食套餐"""
        meal = Meal()
        meal.add(ChickenBurger())
        meal.add(Pepsi())
        return meal
