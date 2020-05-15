# -*- coding: utf-8 -*-


def singleton(cls):
    """单例装饰器"""

    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@singleton
class SingletonTwo(object):
    """
    单例2
    """
    def foo(self):
        pass
