# -*- coding: utf-8 -*-


class Computer(object):
    """
    电脑
    """
    _master = ''
    _screen = ''
    _keyboard = ''
    _mouse = ''
    _audio = ''

    def setMaster(self,master):
        """设置主机"""
        self._master = master

    def setScreen(self,screen):
        """设置显示器"""
        self._screen = screen

    def setKeyboard(self, keyboard):
        """设置键盘"""
        self._keyboard = keyboard

    def setMouse(self,mouse):
        """设置鼠标"""
        self._mouse = mouse

    def setAudio(self,audio):
        """设置音响"""
        self._audio = audio