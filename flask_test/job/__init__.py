# -*- coding: UTF-8 -*-
import json
import logging
from datetime import date
from datetime import datetime

from flask import current_app, request

from config import LOG
from utils.pg_util import PostgreSQL

logger = logging.getLogger(__name__)


class DateEncoder(json.JSONEncoder):
    """解决json序列化时时间不能序列化问题"""

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


class HasPostgreSQL(object):
    """PG数据库业务基类"""

    def __init__(self):
        self._pg = None

    def get_pg(self, dict_cursor=True):
        """获取pg数据库对象"""
        if not self._pg:
            self._pg = PostgreSQL(conn=current_app.pool.connection(), dict_cursor=dict_cursor)
        return self._pg


class Producer(HasPostgreSQL):
    """
    逻辑处理基类：
        do：统一进行异常处理和数据库的连接、提交、异常回滚、关闭等操作，调用process逻辑处理函数
        process：只负责逻辑处理，创建子类重写，数据库通过self.get_pg()获取
        _pg：pg对象
        _process_type：process函数返回值类别
                        0-默认值，将process返回的msg作为json处理，用于大部分业务
                        1-将process返回的msg直接返回给前端，用于下载等业务
    """

    def __init__(self):
        HasPostgreSQL.__init__(self)
        self._process_type = 0

    def set_process_type(self, process_type=1):
        """设置返回值类型"""
        self._process_type = process_type

    def do(self, **kwargs):
        """业务代码公共部分"""
        result_msg = {}
        try:
            logger.debug("==================  " + self.__class__.__name__ + "  ==================")
            # 业务处理逻辑
            kwargs['request'] = request
            msg = self.process(**kwargs)

            # 处理返回值
            if self._process_type == 0:
                result_msg['message'] = 'ok'
                result_msg['data'] = msg
                result_msg = json.dumps(result_msg, cls=DateEncoder).replace(': null', ': \"\"')
            if self._process_type == 1:
                result_msg = msg
            if self._pg:
                self._pg.commit()
            return result_msg
        except Exception as e:
            # 异常处理逻辑
            if LOG.level.lower() == "error":
                logger.exception("==================  " + self.__class__.__name__ + "  ==================")
            if self._pg:
                self._pg.rollback()
            logger.exception(e)
            result_msg['message'] = "数据异常！"
            result_msg['error'] = str(e)
            return json.dumps(result_msg)
        finally:
            # 释放资源
            if self._pg:
                del self._pg
                self._pg = None

    def process(self, **kwargs):
        """
        业务代码逻辑部分
        在子类中重写process来处理业务
        """
        return ""
