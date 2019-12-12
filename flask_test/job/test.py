# -*- coding: UTF-8 -*-
import logging

from job import Producer

logger = logging.getLogger(__name__)


class Test(Producer):
    def process(self, **param):
        logger.debug('this is test')
        return True, "this is test"
