# -*- coding: utf-8 -*-
"""
亮主题图标
"""
from AbstractFactoryPattern.Theme.Icon import IIcon


class BrightIcon(IIcon):
    """
    亮主题图标
    """
    def show(self):
        """显示图标信息"""
        print('this is BrightIcon')
