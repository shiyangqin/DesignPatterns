# -*- coding: UTF-8 -*-
import logging

from job import Producer

LOG = logging.getLogger(__name__)


class Test(Producer):
    def process(self, request):
        res = {
            "mseeage": "ok"
        }
        pg = self.getPg()
        redis = self.getRedis()
        LOG.debug('this is Test')
        return True, res
 