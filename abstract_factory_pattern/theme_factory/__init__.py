# -*- coding: utf-8 -*-
from abstract_factory_pattern.theme_factory.theme import Theme


class IThemeFactory(object):
    """主题工厂接口"""

    def create_theme(self):
        """生产主题"""
        theme = Theme()
        theme.set_font(self._create_font())
        theme.set_colour(self._create_colour())
        theme.set_icon(self._create_icon())
        return theme

    def _create_font(self):
        """生产主题字体"""
        pass

    def _create_colour(self):
        """生产主题颜色"""
        pass

    def _create_icon(self):
        """生产主题字体"""
        pass
