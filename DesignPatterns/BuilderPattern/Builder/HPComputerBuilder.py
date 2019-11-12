# -*- coding: utf-8 -*-
from BuilderPattern.Builder import ComputerBuilder


class HPComputerBuilder(ComputerBuilder):
    """
    惠普电脑生成器
    """
    def buildMaster(self):
        """构建主机"""
        self._computer.setMaster('i7,16g,512SSD,1060')
        print('i7,16g,512SSD,1060')

    def buildScreen(self):
        """构建主机"""
        self._computer.setScreen('1080p')
        print('1080p')

    def buildKeyboard(self):
        """构建主机"""
        self._computer.setKeyboard('cherry 青轴机械键盘')
        print('cherry 青轴机械键盘')

    def buildMouse(self):
        """构建主机"""
        self._computer.setMouse('MI 鼠标')
        print('MI 鼠标')

    def buildAudio(self):
        """构建主机"""
        self._computer.setAudio('飞利浦 音响')
        print('飞利浦 音响')