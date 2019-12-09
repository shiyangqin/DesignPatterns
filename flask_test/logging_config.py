# -*- coding: utf-8 -*-

import logging

import logging.handlers

import os

LEVELS = {
    'NOSET': logging.NOTSET,
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}


def configLogging(fileName="log.txt", logLevel="NOSET"):
    """
    @summary: config logging to write logs to local file
    @param fileName: name of log file
    @param logLevel: log level
    """
    logs_dir = os.path.join(os.path.dirname(__file__), "logs")
    if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
        pass
    else:
        os.makedirs(logs_dir)

    logging.getLogger("").handlers = []

    fileName = os.path.join(logs_dir, fileName)
    rotating_file_handler = \
        logging.handlers.RotatingFileHandler(filename=fileName, maxBytes=1024 * 1024 * 50, backupCount=5)
    formatter = logging.Formatter("%(asctime)s %(name)-12s %(process)d %(levelname)-8s %(lineno)-6s %(message)s")
    '''
    format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
     %(levelno)s: 打印日志级别的数值
     %(levelname)s: 打印日志级别名称
     %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
     %(filename)s: 打印当前执行程序名
     %(funcName)s: 打印日志的当前函数
     %(lineno)d: 打印日志的当前行号
     %(asctime)s: 打印日志的时间
     %(thread)d: 打印线程ID
     %(threadName)s: 打印线程名称
     %(process)d: 打印进程ID
     %(message)s: 打印日志信息
    '''
    rotating_file_handler.setFormatter(formatter)
    logging.getLogger("").addHandler(rotating_file_handler)

    console = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(name)-12s %(process)d %(levelname)-8s %(lineno)-6s %(message)s")
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)
    logger = logging.getLogger("")
    level = LEVELS[logLevel.upper()]
    logger.setLevel(level)
