# -*- coding: utf-8 -*-
import threading
from singleton_pattern.singleton_one import singletonOne
from singleton_pattern.singleton_two import SingletonTwo
from singleton_pattern.singleton_three import SingletonThree
from singleton_pattern.singleton_four import SingletonFour


def test_singleton_one():
    obj = singletonOne
    print(obj)


def test_singleton_two():
    obj = SingletonTwo()
    print(obj)


def test_singleton_three():
    # 这种实现方法只能通过SingletonThree.instance()获取的实例才是单例，直接SingletonThree()不是单例
    obj = SingletonThree.instance()
    print(obj)


def test_singleton_four():
    # 推荐使用这种方法
    obj = SingletonFour()
    print(obj)


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=test_singleton_four())
