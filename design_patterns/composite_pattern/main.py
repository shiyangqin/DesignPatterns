# -*- coding: utf-8 -*-
from composite_pattern.employee import Employee


if __name__ == '__main__':
    # 创建员工信息
    CEO = Employee("John", "CEO", 30000)
    head_sales =  Employee("Robert", "Head Sales", 20000)
    head_marketing = Employee("Michel", "Head Marketing", 20000)
    clerk_1 = Employee("Laura", "Marketing", 10000)
    clerk_2 = Employee("Bob", "Marketing", 10000)
    sales_executive_1 = Employee("Richard", "Sales", 10000)
    sales_executive_2 = Employee("Rob", "Sales", 10000)

    # 设置员工关系
    CEO.add(head_sales)
    CEO.add(head_marketing)

    head_sales.add(sales_executive_1)
    head_sales.add(sales_executive_2)

    head_marketing.add(clerk_1)
    head_marketing.add(clerk_2)

    # 打印所有员工信息
    print(CEO)
    for head_employee in CEO.get_subordinates():
        print(head_employee)
        for employee in head_employee.get_subordinates():
            print(employee)
