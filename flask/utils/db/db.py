# -*- coding: UTF-8 -*-
import psycopg2
import logging

from config import PG

LOG = logging.getLogger(__name__)


class DB(object):
    """数据库封装类"""
    __conn = None
    __cursor = None
    __commit = False

    def __init__(self):
        """创建连接"""
        LOG.debug(">>>>>>开始进行数据库连接>>>>>>")
        self.__conn = psycopg2.connect(
            host=PG.pg_host,
            port=PG.pg_port,
            database=PG.pg_name,
            user=PG.pg_user,
            password=PG.pg_pwd
        )
        if not self.__conn:
            raise Exception('数据库连接失败')
        self.__cursor = self.__conn.cursor()
        LOG.debug(">>>>>>数据库连接成功>>>>>>")

    def __del__(self):
        """关闭连接"""
        if self.__cursor:
            self.__cursor.close()
            self.__cursor = None
        if self.__conn:
            self.__conn.close()
            self.__conn = None
        LOG.debug(">>>>>>关闭数据库连接>>>>>>")

    def execute(self, sql, param_dict=(), show_sql=True):
        """执行sql语句，打印日志，设置提交标识，返回数据"""
        res = self.__cursor.execute(sql, param_dict)
        if show_sql:
            LOG.debug(">>>>>>sql>>>>>>: %s" % (self.__cursor.mogrify(sql, param_dict)))
        if sql.lower().startswith(('update', 'insert', 'delete')):
            self.__commit = True
        if sql.lower().startswith('select'):
            return self.__cursor.fetchall()
        if sql.lower().find('returning'):
            return res

    def rollback(self):
        """数据库回滚"""
        if self.__commit:
            self.__conn.rollback()

    def commit(self):
        """数据库提交"""
        if self.__commit:
            self.__conn.commit()

    def set_commit(self):
        """设置数据库提交标识"""
        self.__commit = True

    def get_conn(self):
        """获取conn对象"""
        return self.__conn

    def get_cursor(self):
        """获取cursor对象"""
        return self.__cursor
