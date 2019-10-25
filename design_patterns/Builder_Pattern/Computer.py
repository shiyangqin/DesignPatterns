# -*- coding: utf-8 -*-


class Computer(object):
    """
    电脑
    """
    master = ''
    screen = ''
    keyboard = ''
    mouse = ''
    audio = ''

    def setMaster(self,master):
        """设置主机"""
        self.master = master

    def setScreen(self,screen):
        """设置显示器"""
        self.screen = screen

    def setKeyboard(self, keyboard):
        """设置键盘"""
        self.keyboard = keyboard

    def setMouse(self,mouse):
        """设置鼠标"""
        self.mouse = mouse

    def setAudio(self,audio):
        """设置音响"""
        self.audio = audio