# -*- coding: UTF-8 -*-

from job import Producer
from utils.auth import Permission


class XlsProducer(Producer):

    @Permission('xls')
    def do(self, **kwargs):
        return super().do(**kwargs)
