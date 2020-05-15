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

    def get_cost(self):
        """获取总价格"""
        cost = 0.0
        for item in self.items:
            cost += item.price()
        return cost

    def show_items(self):
        """显示物品信息"""
        for item in self.items:
            print("item: " + item.name() + "; ", end="")
            print("packing: " + item.packing().pack() + "; ", end="")
            print("Price: " + str(item.price()) + "; ")
