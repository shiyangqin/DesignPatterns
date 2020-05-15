# -*- coding: utf-8 -*-
"""
文件记录器
"""
from chain_of_responsibility_pattern.logger import LoggerLevel,AbstractLogger


class FileLogger(AbstractLogger):
    """
    文件记录器
    """
    def __init__(self, level=LoggerLevel.DEBUG):
        AbstractLogger.__init__(self)
        self._level = level

    def _write(self, message):
        print("File Console::Logger: " + message)
