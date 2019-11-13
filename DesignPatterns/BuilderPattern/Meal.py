# -*- coding: utf-8 -*-
"""
套餐
"""


class Meal(object):
    """
    套餐
    """
    def __init__(self):
        self.items = []

    def add(self, item):
        """添加物品"""
        self.items.append(item)

    def getCost(self):
        """获取总价格"""
        cost = 0.0
        for item in self.items:
            cost += item.price()
        return cost

    def showItems(self):
        """显示物品信息"""
        for item in self.items:
            print("Item: " + item.name() + "; ", end="")
            print("Packing: " + item.packing().pack() + "; ", end="")
            print("Price: " + str(item.price()) + "; ")
