# -*- coding: utf-8 -*-
"""
暗主题字体
"""
from Abstract_Factory_Pattern.Theme.Font import IFont


class DarkFont(IFont):
    """
    亮主题字体
    """
    def show(self):
        """显示字体信息"""
        print('this is DarkFont')
