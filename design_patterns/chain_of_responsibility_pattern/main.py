# -*- coding: utf-8 -*-
from chain_of_responsibility_pattern.logger import Logger
from chain_of_responsibility_pattern.logger import LoggerLevel


def main():
    print("=================info=================")
    Logger.log_message(LoggerLevel.INFO, "This is an information.")
    print("=================debug=================")
    Logger.log_message(LoggerLevel.DEBUG, "This is an debug level information.")
    print("=================error=================")
    Logger.log_message(LoggerLevel.ERROR, "This is an error information.")


if __name__ == '__main__':
    main()
