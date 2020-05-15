# -*- coding: utf-8 -*-
import functools


def log(func):
    """无参数装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


def log_with_param(text):
    """有参数装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)

        return wrapper

    return decorator
