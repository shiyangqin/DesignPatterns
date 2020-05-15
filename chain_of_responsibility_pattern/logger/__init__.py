# -*- coding: utf-8 -*-
"""
抽象记录器
"""


class LoggerLevel(object):

    INFO = 1
    DEBUG = 2
    ERROR = 3


class AbstractLogger(object):
    """
    抽象记录器
    """

    def __init__(self):
        self._level = None
        self._next_logger = None

    def set_next_logger(self, next_logger):
        """设置下一级日志对象"""
        self._next_logger = next_logger

    def log_message(self, level, message):
        """根据级别记录日志"""
        if self._level <= level:
            self._write(message)
        if self._next_logger:
            self._next_logger.log_message(level, message)

    def _write(self, message):
        """写日志"""
        pass


import threading
from chain_of_responsibility_pattern.logger.console_logger import ConsoleLogger
from chain_of_responsibility_pattern.logger.error_logger import ErrorLogger
from chain_of_responsibility_pattern.logger.file_logger import FileLogger


class Logger(object):

    __lock = threading.Lock()
    __logger = None

    @classmethod
    def log_message(cls, level, message):
        if not cls.__logger:
            with Logger.__lock:
                if not cls.__logger:
                    error_logger = ErrorLogger()
                    file_logger = FileLogger()
                    console_logger = ConsoleLogger()

                    error_logger.set_next_logger(file_logger)
                    file_logger.set_next_logger(console_logger)

                    cls.__logger = error_logger

        cls.__logger.log_message(level, message)
