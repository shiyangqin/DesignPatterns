# -*- coding: utf-8 -*-
from abstract_factory_pattern.theme_factory.theme.icon import IIcon


class DarkIcon(IIcon):
    """暗主题图标"""

    def show(self):
        """显示图标信息"""
        print('this is DarkIcon')
