# -*- coding: utf-8 -*-
"""
暗主题颜色
"""
from AbstractFactoryPattern.Theme.Colour import IColour


class DarkColour(IColour):
    """
    暗主题颜色
    """
    def show(self):
        """显示颜色信息"""
        print('this is DarkColour')
