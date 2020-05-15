# -*- coding: utf-8 -*-
import threading


class SingletonFour(object):
    """单例4"""

    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(SingletonFour, "_instance"):
            with SingletonFour._instance_lock:
                if not hasattr(SingletonFour, "_instance"):
                    SingletonFour._instance = object.__new__(cls)
        return SingletonFour._instance
