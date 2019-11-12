# -*- coding: utf-8 -*-
"""
主题类
"""


class Theme(object):
    """
    主题类
    """
    __font = None
    __colour = None
    __icon = None

    def getFont(self):
        return self.__font

    def setFont(self, font):
        self.__font = font

    def getColour(self):
        return self.__colour

    def setColour(self, colour):
        self.__colour = colour

    def getIcon(self):
        return self.__icon

    def setIcon(self, icon):
        self.__icon = icon