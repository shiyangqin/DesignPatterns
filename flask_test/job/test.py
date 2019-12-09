# -*- coding: UTF-8 -*-
import logging

from job import Producer

logger = logging.getLogger(__name__)


class Test(Producer):
    def process(self, request):
        res = {
            "mseeage": "ok"
        }
        pg = self.get_postgresql()
        redis = self.get_redis()
        logger.debug('this is Test')
        return True, res
 