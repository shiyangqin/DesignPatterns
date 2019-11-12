# -*- coding: utf-8 -*-
import threading
from SingletonPattern.SingletonOne import singletonOne
from SingletonPattern.SingletonTwo import SingletonTwo
from SingletonPattern.SingletonThree import SingletonThree
from SingletonPattern.SingletonFour import SingletonFour


def testSingletonOne():
    obj = singletonOne
    print(obj)


def testSingletonTwo():
    obj = SingletonTwo()
    print(obj)


def testSingletonThree():
    # 这种实现方法只能通过SingletonThree.instance()获取的实例才是单例，直接SingletonThree()不是单例
    obj = SingletonThree.instance()
    print(obj)


def testSingletonFour():
    # 推荐使用这种方法
    obj = SingletonFour()
    print(obj)


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=testSingletonFour())
