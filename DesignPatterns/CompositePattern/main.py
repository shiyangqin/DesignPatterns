# -*- coding: utf-8 -*-
from CompositePattern.Employee import Employee


if __name__ == '__main__':
    # 创建员工信息
    CEO = Employee("John", "CEO", 30000)
    headSales =  Employee("Robert", "Head Sales", 20000)
    headMarketing = Employee("Michel", "Head Marketing", 20000)
    clerk1 = Employee("Laura", "Marketing", 10000)
    clerk2 = Employee("Bob", "Marketing", 10000)
    salesExecutive1 = Employee("Richard", "Sales", 10000)
    salesExecutive2 = Employee("Rob", "Sales", 10000)

    # 设置员工关系
    CEO.add(headSales)
    CEO.add(headMarketing)

    headSales.add(salesExecutive1)
    headSales.add(salesExecutive2)

    headMarketing.add(clerk1)
    headMarketing.add(clerk2)

    # 打印所有员工信息
    print(CEO)
    for headEmployee in CEO.getSubordinates():
        print(headEmployee)
        for employee in headEmployee.getSubordinates():
            print(employee)
