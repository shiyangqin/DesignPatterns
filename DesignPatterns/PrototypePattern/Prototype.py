# -*- coding: utf-8 -*-
"""
原型类
"""
import copy


class Member(object):
    """
    成员类
    """
    def __init__(self, name):
        self._name = name

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

class Prototype(object):
    """
    原型
    """
    def __init__(self,member):
        self._member = member

    def getMember(self):
        return self._member

    def clone(self):
        return copy.deepcopy(self)
