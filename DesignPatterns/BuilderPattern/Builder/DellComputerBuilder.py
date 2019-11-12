# -*- coding: utf-8 -*-
from BuilderPattern.Builder import ComputerBuilder


class DellComputerBuilder(ComputerBuilder):
    """
    戴尔电脑生成器
    """
    def buildMaster(self):
        """构建主机"""
        self._computer.setMaster('i7,32g,1TSSD,1060')
        print('i7,32g,1TSSD,1060')

    def buildScreen(self):
        """构建主机"""
        self._computer.setScreen('4k')
        print('4k')

    def buildKeyboard(self):
        """构建主机"""
        self._computer.setKeyboard('cherry 黑轴机械键盘')
        print('cherry 黑轴机械键盘')

    def buildMouse(self):
        """构建主机"""
        self._computer.setMouse('MI 鼠标')
        print('MI 鼠标')

    def buildAudio(self):
        """构建主机"""
        self._computer.setAudio('飞利浦 音响')
        print('飞利浦 音响')