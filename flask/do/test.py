# -*- coding: UTF-8 -*-
import logging

from do.producer import Producer

LOG = logging.getLogger(__name__)


class Test(Producer):
    def process(self, body_dict):
        """
        在字类中重写process来处理业务
        返回result_flag（标识位：false/true）, result_msg(返回信息，json/Response)
        """
        result_flag = True
        result_msg = "ok"
        return result_flag, result_msg
