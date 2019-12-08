# -*- coding: utf-8 -*-
"""
图片代理
"""
from proxy_pattern.image import Image
from proxy_pattern.image.real_image import RealImage


class ProxyImage(Image):
    """图片代理"""
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__real_image = RealImage(file_name)

    def display(self):
        """描述"""
        self.__real_image.display()
