# -*- coding: utf-8 -*-
from proxy_pattern.image.proxy_image import ProxyImage


if __name__ == '__main__':
    image = ProxyImage("test.jpg")
    image.display()