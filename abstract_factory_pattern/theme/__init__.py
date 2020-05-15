# -*- coding: utf-8 -*-
"""
主题类
"""


class Theme(object):
    """
    主题类
    """
    def __init__(self):
        self.__font = None
        self.__colour = None
        self.__icon = None

    def get_font(self):
        return self.__font

    def set_font(self, font):
        self.__font = font

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour

    def get_icon(self):
        return self.__icon

    def set_icon(self, icon):
        self.__icon = icon