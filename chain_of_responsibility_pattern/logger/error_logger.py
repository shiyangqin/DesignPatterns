# -*- coding: utf-8 -*-
"""
异常记录器
"""
from chain_of_responsibility_pattern.logger import LoggerLevel,AbstractLogger


class ErrorLogger(AbstractLogger):
    """
    异常记录器
    """
    def __init__(self, level=LoggerLevel.ERROR):
        AbstractLogger.__init__(self)
        self._level = level

    def _write(self, message):
        print("Error Console::Logger: " + message)
