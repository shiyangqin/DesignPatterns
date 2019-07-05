# -*- coding: UTF-8 -*-
import logging

from do_base import Do

LOG = logging.getLogger(__name__)


class Do_Test(Do):
    def process(self, body_dict):
        db = self._db
        LOG.debug('>>>>>>开始进行逻辑处理>>>>>>')
        error = body_dict['error']
        msg = '测试'
        if error:
            sql = "select * from t_test;"
            msg = db.execute(sql)
            raise Exception('测试抛出异常')
        LOG.debug('>>>>>>逻辑处理完成>>>>>>')
        return True, msg
