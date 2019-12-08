# -*- coding: utf-8 -*-
"""
暗主题工厂
"""
from abstract_factory_pattern.theme_factory import IThemeFactory
from abstract_factory_pattern.theme.font.dark_font import DarkFont
from abstract_factory_pattern.theme.colour.dark_colour import DarkColour
from abstract_factory_pattern.theme.icon.dark_icon import DarkIcon


class DarkThemeFactory(IThemeFactory):
    """
    暗主题工厂
    """

    def _create_font(self):
        """生产主题字体"""
        return DarkFont()

    def _create_colour(self):
        """生产主题颜色"""
        return DarkColour()

    def _create_icon(self):
        """生产主题字体"""
        return DarkIcon()
