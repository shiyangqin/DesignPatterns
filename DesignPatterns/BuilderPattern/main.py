# -*- coding: utf-8 -*-
from BuilderPattern.MealBuilder import MealBuilder


if __name__ == '__main__':
    mealBuilder = MealBuilder()

    vegMeal = mealBuilder.prepareVegMeal()
    print("veg Meal")
    vegMeal.showItems()
    print("Total Cost: ", vegMeal.getCost())

    nonVegMeal = mealBuilder.prepareNonVegMeal()
    print("\n\nveg Meal")
    vegMeal.showItems()
    print("Total Cost: ", vegMeal.getCost())
