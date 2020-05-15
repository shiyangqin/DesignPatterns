# -*- coding: utf-8 -*-
from proxy_pattern.image import Image


class RealImage(Image):
    """图片类"""

    def __init__(self, file_name):
        self.__file_name = file_name
        self.load_from_disk(file_name)

    def display(self):
        """描述"""
        print("Displaying " + self.__file_name)

    def load_from_disk(self, file_name):
        """加载"""
        print("Loading " + file_name)
