# -*- coding: utf-8 -*-
from builder_pattern.meal_builder import MealBuilder


if __name__ == '__main__':
    meal_builder = MealBuilder()

    veg_meal = meal_builder.prepare_veg_meal()
    print("veg Meal")
    veg_meal.show_items()
    print("Total Cost: ", veg_meal.get_cost())

    non_veg_meal = meal_builder.prepare_non_veg_meal()
    print("\nNon-Veg Meal")
    non_veg_meal.show_items()
    print("Total Cost: ", non_veg_meal.get_cost())
