# -*- coding: utf-8 -*-
"""
亮主题颜色
"""
from Abstract_Factory_Pattern.Theme.Colour import IColour


class BrightColour(IColour):
    """
    亮主题颜色
    """
    def show(self):
        """显示颜色信息"""
        print('this is BrightColour')
