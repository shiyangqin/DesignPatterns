# -*- coding: utf-8 -*-
"""
主题工厂接口
"""
from Abstract_Factory_Pattern.Theme import Theme


class IThemeFactory(object):
    """
    主题工厂接口
    """

    def createTheme(self):
        """生产主题"""
        theme = Theme()
        theme.setFont(self._createFont())
        theme.setColour(self._createColour())
        theme.setIcon(self._createIcon())
        return theme

    def _createFont(self):
        """生产主题字体"""
        pass

    def _createColour(self):
        """生产主题颜色"""
        pass

    def _createIcon(self):
        """生产主题字体"""
        pass
