# -*- coding: utf-8 -*-
"""
亮主题工厂
"""
from AbstractFactoryPattern.ThemeFactory import IThemeFactory
from AbstractFactoryPattern.Theme.Font.BrightFont import BrightFont
from AbstractFactoryPattern.Theme.Colour.BrightColour import BrightColour
from AbstractFactoryPattern.Theme.Icon.BrightIcon import BrightIcon


class BrightThemeFactory(IThemeFactory):
    """
    亮主题工厂
    """

    def _createFont(self):
        """生产主题字体"""
        return BrightFont()

    def _createColour(self):
        """生产主题颜色"""
        return BrightColour()

    def _createIcon(self):
        """生产主题字体"""
        return BrightIcon()
