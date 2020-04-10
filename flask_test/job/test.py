# -*- coding: UTF-8 -*-
import logging

from job import Producer
from utils.auth import Permission

logger = logging.getLogger(__name__)


class Test(Producer):

    @Permission('test')
    def do(self, **kwargs):
        return super().do(**kwargs)

    def process(self, **kwargs):
        logger.debug('this is test')
        res = {
            "msg": "this is test",
            "user": kwargs['user']
        }
        return res
