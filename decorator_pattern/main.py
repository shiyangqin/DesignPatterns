# -*- coding: utf-8 -*-
from decorator_pattern.decorator import log, log_with_param


@log
def test_log():
    print('test_log')


@log_with_param('test_param')
def test_param():
    print('test_param')


if __name__ == '__main__':
    print('========test_log==========')
    test_log()
    print('========test_param==========')
    test_param()
