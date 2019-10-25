# -*- coding: utf-8 -*-


class ComputerDirector(object):
    """
    电脑导向器
    """
    __computerBuilder = None

    def setComputerBuilder(self,computerBuilder):
        """设置电脑生成器"""
        self.__computerBuilder = computerBuilder

    def getComputer(self):
        """获取电脑"""
        return self.__computerBuilder.getComputer()

    def constructComputer(self):
        """构造电脑"""
        self.__computerBuilder.buildComputer()
        self.__computerBuilder.buildMaster()
        self.__computerBuilder.buildScreen()
        self.__computerBuilder.buildKeyboard()
        self.__computerBuilder.buildMouse()
        self.__computerBuilder.buildAudio()
