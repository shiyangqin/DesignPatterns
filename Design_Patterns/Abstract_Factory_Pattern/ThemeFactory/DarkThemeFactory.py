# -*- coding: utf-8 -*-
"""
暗主题工厂
"""
from Abstract_Factory_Pattern.ThemeFactory import IThemeFactory
from Abstract_Factory_Pattern.Theme.Font.DarkFont import DarkFont
from Abstract_Factory_Pattern.Theme.Colour.DarkColour import DarkColour
from Abstract_Factory_Pattern.Theme.Icon.DarkIcon import DarkIcon


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
