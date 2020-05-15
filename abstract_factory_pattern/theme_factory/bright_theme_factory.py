# -*- coding: utf-8 -*-
from abstract_factory_pattern.theme_factory import IThemeFactory
from abstract_factory_pattern.theme_factory.theme.font.bright_font import BrightFont
from abstract_factory_pattern.theme_factory.theme.colour.bright_colour import BrightColour
from abstract_factory_pattern.theme_factory.theme.icon.bright_icon import BrightIcon


class BrightThemeFactory(IThemeFactory):
    """亮主题工厂"""

    def _create_font(self):
        """生产主题字体"""
        return BrightFont()

    def _create_colour(self):
        """生产主题颜色"""
        return BrightColour()

    def _create_icon(self):
        """生产主题字体"""
        return BrightIcon()
