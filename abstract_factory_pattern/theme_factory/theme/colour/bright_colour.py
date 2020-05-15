# -*- coding: utf-8 -*-
from abstract_factory_pattern.theme_factory.theme.colour import IColour


class BrightColour(IColour):
    """亮主题颜色"""

    def show(self):
        """显示颜色信息"""
        print('this is BrightColour')
