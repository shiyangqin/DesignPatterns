# -*- coding: utf-8 -*-
from chain_of_responsibility_pattern.logger import LoggerLevel, AbstractLogger


class ConsoleLogger(AbstractLogger):
    """控制台记录器"""

    def __init__(self, level=LoggerLevel.INFO):
        AbstractLogger.__init__(self)
        self._level = level

    def _write(self, message):
        print("Standard Console::Logger: " + message)
