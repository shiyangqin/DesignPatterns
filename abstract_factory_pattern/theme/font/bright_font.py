# -*- coding: utf-8 -*-
"""
亮主题字体
"""
from abstract_factory_pattern.theme.font import IFont


class BrightFont(IFont):
    """
    亮主题字体
    """
    def show(self):
        """显示字体信息"""
        print('this is BrightFont')