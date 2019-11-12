# -*- coding: utf-8 -*-
"""
暗主题工厂
"""
from AbstractFactoryPattern.ThemeFactory import IThemeFactory
from AbstractFactoryPattern.Theme.Font.DarkFont import DarkFont
from AbstractFactoryPattern.Theme.Colour.DarkColour import DarkColour
from AbstractFactoryPattern.Theme.Icon.DarkIcon import DarkIcon


class DarkThemeFactory(IThemeFactory):
    """
    暗主题工厂
    """

    def _createFont(self):
        """生产主题字体"""
        return DarkFont()

    def _createColour(self):
        """生产主题颜色"""
        return DarkColour()

    def _createIcon(self):
        """生产主题字体"""
        return DarkIcon()
