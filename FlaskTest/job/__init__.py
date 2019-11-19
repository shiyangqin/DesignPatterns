# -*- coding: UTF-8 -*-
import json
import logging
from datetime import date
from datetime import datetime

import redis
from flask import current_app, request

from config import REDIS
from utils.PostgreSQL import PostgreSQL

LOG = logging.getLogger(__name__)


class DateEncoder(json.JSONEncoder):
    """
    解决json序列化时时间不能序列化问题
    """
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


class HasRedis(object):
    """redis业务基类"""
    def __init__(self):
        self._redis = None

    def getRedis(self, host=REDIS.redis_host, port=REDIS.redis_port, db=REDIS.redis_db, password=REDIS.redis_pwd):
        """获取redis连接"""
        if not self._redis:
            LOG.debug('>>>>>>redis get conn>>>>>>')
            self._redis = redis.Redis(host=host, port=port, db=db, password=password)
        return self._redis


class HasPostgreSQL(object):
    """PG数据库业务基类"""
    def __init__(self):
        self._pg = None

    def getPostgreSQL(self, dict_cursor=True):
        """获取pg数据库对象"""
        if not self._pg:
            self._pg = PostgreSQL(conn=current_app.pool.connection(), dict_cursor=dict_cursor)
        return self._pg


class Producer(HasRedis, HasPostgreSQL):
    """
    逻辑处理基类：
        do：统一进行异常处理和数据库的连接、提交、异常回滚、关闭等操作，调用process逻辑处理函数
        process：只负责逻辑处理，创建子类重写，数据库通过self.get_pg()和self.get_redis()获取
        __pg：pg对象
        __redis：redis连接
        __process_type：process函数返回值类别
                        0-默认值，将process返回的msg作为json处理，用于大部分业务
                        1-将process返回的msg直接返回给前端，用于下载等业务
    """
    def __init__(self):
        HasRedis.__init__(self)
        HasPostgreSQL.__init__(self)
        self._processType = 0

    def setProcessType(self, type=1):
        """设置返回值类型"""
        self._processType = type

    def do(self):
        """业务代码公共部分"""
        result_msg = {}
        try:
            # 业务处理逻辑
            flag, msg = self.process(request)
            if flag:
                if self._processType == 0:
                    result_msg['message'] = 'ok'
                    result_msg['data'] = msg
                    result_msg = json.dumps(result_msg, cls=DateEncoder)
                if self._processType == 1:
                    result_msg = msg
            else:
                raise Exception(msg)
            if self._pg:
                self._pg.commit()
            return result_msg
        except Exception as e:
            # 异常处理逻辑
            if self._pg:
                self._pg.rollback()
            LOG.exception(e)
            result_msg['message'] = str(e)
            result_msg = json.dumps(result_msg, cls=DateEncoder)
            return result_msg
        finally:
            # 释放资源
            if self._pg:
                del self._pg
                self._pg = None
            if self._redis:
                LOG.debug('>>>>>>redis conn close>>>>>>')
                self._redis.close()
                self._redis = None

    def process(self, request):
        """
        业务代码逻辑部分
        在子类中重写process来处理业务
        返回:
            result_flag（标识位：false/true）
            result_msg(返回信息，json/Response)
        """
        result_flag = True
        result_msg = "ok"
        return result_flag, result_msg
