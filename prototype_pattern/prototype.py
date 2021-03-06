# -*- coding: utf-8 -*-
import copy


class Member(object):
    """成员类"""

    def __init__(self, name):
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Prototype(object):
    """原型"""

    def __init__(self,member):
        self._member = member

    def get_member(self):
        return self._member

    def clone(self):
        return copy.deepcopy(self)
