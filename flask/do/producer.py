# -*- coding: UTF-8 -*-
import json
import logging
from datetime import date
from datetime import datetime

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
        elif isinstance(obj, type(None)):
            return ''
        else:
            return json.JSONEncoder.default(self, obj)


class Producer(object):
    """
    逻辑处理基类：
        do：统一进行异常处理和数据库操作的连接，提交，异常时回滚，关闭，调用process逻辑处理函数
        process：逻辑处理，不需要进行异常处理，创建子类重写，数据库通过self.get_pg()获取
    """
    __pg = None

    def do(self, request, msg_type=False):
        """
        :param request: url请求信息
        :param msg_type: msg返回类型，
             False:将process返回的信息装入result_msg['data']，用于返回json，
             True：将process返回的信息直接返回，用于Response
        :return:json/Response
        """
        result_msg = {}
        try:
            flag, msg = self.process(request)
            if flag:
                if self.__pg:
                    self.__pg.commit()
                if msg_type:
                    result_msg = msg
                else:
                    result_msg['message'] = 'ok'
                    result_msg['data'] = msg
                    result_msg = json.dumps(result_msg, cls=DateEncoder)
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
        return result_msg

    def get_pg(self):
        if not self.__pg:
            self.__pg = PostgreSQL()
        return self.__pg

    def process(self, request):
        db = self.get_pg()
        result_flag = True  # 函数返回标识，返回false时按异常处理，result_msg为异常信息
        result_msg = {  # 函数返回内容,json格式，不要进行dumps，不需要拼装message和data
            "test": "ok"
        }
        return result_flag, result_msg
