# -*- coding: utf-8 -*-
"""
暗主题图标
"""
from abstract_factory_pattern.theme.icon import IIcon


class DarkIcon(IIcon):
    """
    暗主题图标
    """
    def show(self):
        """显示图标信息"""
        print('this is DarkIcon')
