# -*- coding: UTF-8 -*-
import logging

from job import Producer

LOG = logging.getLogger(__name__)


class Test(Producer):
    def process(self, request):
        res = {
            "mseeage": "ok"
        }
        pg = self.get_pg()
        redis = self.get_redis()
        LOG.debug('this is Test')
        return True, res
