# -*- coding: utf-8 -*-
"""
员工类
"""


class Employee(object):
    """
    员工类
    """
    def __init__(self, name, dept, salary):
        self.__name = str(name)
        self.__dept = str(dept)
        self.__salary = str(salary)
        self.__subordinates = []

    def add(self, e):
        """添加下级员工"""
        self.__subordinates.append(e)

    def remove(self, e):
        """移除下级员工"""
        self.__subordinates.remove(e)

    def getSubordinates(self):
        """获取下级员工列表"""
        return self.__subordinates

    def __str__(self):
        """对象描述信息"""
        return ("Employee :[ Name : " + self.__name + ", dept : " + self.__dept + ", salary :" + self.__salary+" ]")