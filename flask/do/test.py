# -*- coding: UTF-8 -*-
import logging

from do.producer import Producer

LOG = logging.getLogger(__name__)


class Test(Producer):
    def process(self, body_dict):
        """字类重写process实现业务"""
        result_flag = True
        result_msg = "ok"
        return result_flag, result_msg
