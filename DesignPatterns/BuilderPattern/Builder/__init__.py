# -*- coding: utf-8 -*-
from BuilderPattern.Computer import Computer


class ComputerBuilder(object):
    """
    电脑生成器
    """
    _computer = None

    def getComputer(self):
        """获取电脑实例"""
        return self._computer

    def buildComputer(self):
        """构建电脑"""
        self._computer = Computer()
        print('生产了一台电脑')

    def buildMaster(self):
        """构建主机"""
        pass

    def buildScreen(self):
        """构建显示器"""
        pass

    def buildKeyboard(self):
        """构建键盘"""
        pass

    def buildMouse(self):
        """构建鼠标"""
        pass

    def buildAudio(self):
        """构建音响"""
        pass