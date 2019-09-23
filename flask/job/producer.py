# -*- coding: UTF-8 -*-
import json
import logging
from datetime import date
from datetime import datetime
import redis

from flask import current_app
from utils.PostgreSQL import PostgreSQL
from config import REDIS

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


class Producer(object):
    """
    逻辑处理基类：
        job：统一进行异常处理和数据库的连接、提交、异常回滚、关闭等操作，调用process逻辑处理函数
        process：只负责逻辑处理，创建子类重写，数据库通过self.get_pg()和self.get_redis()获取
    """
    __pg = None
    __redis = None

    def do(self, request, process_type='0'):
        """
        request: url请求信息
        msg_type: msg返回类型
             '0': 将process返回的信息装入result_msg['data']，用于返回json，
             '1': 将process返回的信息直接返回，用于返回非json
        """
        result_msg = {}
        try:
            flag, msg = self.process(request)
            if flag:
                if self.__pg:
                    self.__pg.commit()
                if process_type == '0':
                    result_msg['message'] = 'ok'
                    result_msg['data'] = msg
                    result_msg = json.dumps(result_msg, cls=DateEncoder)
                if process_type == '1':
                    result_msg = msg
            else:
                raise Exception(msg)
        except Exception as e:
            if self.__pg:
                self.__pg.rollback()
            LOG.exception(e)
            result_msg['message'] = str(e)
            result_msg = json.dumps(result_msg, cls=DateEncoder)
        if self.__pg:
            del self.__pg
        if self.__redis:
            LOG.debug('>>>>>>redis conn close>>>>>>')
            self.__redis.close()
        return result_msg

    def get_pg(self, conn=None, dict_cursor=True):
        """获取pg数据库对象"""
        if not self.__pg:
            self.__pg = PostgreSQL(conn=conn if conn else current_app.pool.connection(), dict_cursor=dict_cursor)
        return self.__pg

    def get_redis(self,host=REDIS.redis_host, port=REDIS.redis_port, db=REDIS.redis_db, password=REDIS.redis_pwd):
        """获取redis连接"""
        if not self.__redis:
            LOG.debug('>>>>>>redis get conn>>>>>>')
            self.__redis = redis.Redis(host, port, db, password)
        return self.__redis

    def process(self, request):
        """
        在字类中重写process来处理业务
        返回:
            result_flag（标识位：false/true）
            result_msg(返回信息，json/Response)
        """
        result_flag = True
        result_msg = "ok"
        return result_flag, result_msg
