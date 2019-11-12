# -*- coding: utf-8 -*-
"""
单例类3
"""
import threading


class SingletonThree(object):
    """
    单例3
    """
    _instance_lock = threading.Lock()

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(SingletonThree, "_instance"):
            with SingletonThree._instance_lock:
                if not hasattr(SingletonThree, "_instance"):
                    SingletonThree._instance = SingletonThree(*args, **kwargs)
        return SingletonThree._instance
