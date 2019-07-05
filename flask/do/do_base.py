# -*- coding: UTF-8 -*-
import json
import logging

from utils.db.db import DB

LOG = logging.getLogger(__name__)


class Do(object):
    """
    逻辑处理基类
    get post 方法：根据不同的请求类型将参数整理成json格式，然后传递给do函数
    do 方法：创建数据库连接，统一负责数据库事务的提交和回滚，将参数传递给process逻辑处理方法
    process 方法：逻辑处理，子类重写此方法来实现业务处理，返回false或者抛出异常会触发数据库回滚
    """
    _db = None  # 数据库对象

    def get(self, request, db=False):
        # 获取参数
        body_dict = request.get_json()
        LOG.debug("body = %s" % body_dict)
        return self.do(body_dict, db)

    def post(self, request, db=False):
        # 获取参数
        body_dict = request.get_json()
        LOG.debug("body = %s" % body_dict)
        return self.do(body_dict, db)

    def do(self, body_dict, db=False):
        result_msg = {}
        try:
            # 创建数据库连接
            if db:
                self._db = DB()
            # 执行逻辑处理函数
            flag, msg = self.process(body_dict)
            # 判断逻辑处理结果
            if flag:
                if self._db:
                    self._db.commit()
                result_msg['message'] = 'ok'
                result_msg['data'] = msg
            else:
                raise Exception(msg)
        except Exception as e:
            # 发生异常时数据库回滚，打印日志，设置返回信息
            if self._db:
                self._db.rollback()
            LOG.exception(e)
            result_msg['message'] = str(e)
        return json.dumps(result_msg)

    def process(self, body_dict):
        """逻辑处理函数"""
        result_flag = True  # 函数返回标识
        result_msg = ''  # 函数返回内容,json格式，不要进行dumps，不需要拼装message和data
        return result_flag, result_msg
