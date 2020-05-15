# -*- coding: utf-8 -*-
"""
亮主题图标
"""
from abstract_factory_pattern.theme.icon import IIcon


class BrightIcon(IIcon):
    """
    亮主题图标
    """
    def show(self):
        """显示图标信息"""
        print('this is BrightIcon')
