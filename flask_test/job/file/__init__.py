# -*- coding: UTF-8 -*-

from job import Producer
from utils.auth import Permission


class FileProducer(Producer):

    @Permission('file')
    def do(self, **kwargs):
        return super().do(**kwargs)
