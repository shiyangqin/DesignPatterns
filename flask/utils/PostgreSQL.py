# -*- coding: UTF-8 -*-
import psycopg2
import logging

from config import PG

LOG = logging.getLogger(__name__)


class PostgreSQL(object):
    """pg数据库封装类"""
    __conn = None
    __cursor = None
    __commit = False

    def __init__(self):
        """创建连接"""
        LOG.debug(">>>>>>PostgreSQL start connect>>>>>>")
        self.__conn = psycopg2.connect(
            host=PG.pg_host,
            port=PG.pg_port,
            database=PG.pg_name,
            user=PG.pg_user,
            password=PG.pg_pwd
        )
        self.__cursor = self.__conn.cursor()
        LOG.debug(">>>>>>PostgreSQL connect success>>>>>>")

    def __del__(self):
        """关闭数据库连接"""
        if self.__cursor:
            self.__cursor.close()
            self.__cursor = None
        if self.__conn:
            self.__conn.close()
            self.__conn = None
        LOG.debug(">>>>>>db connect shutdown>>>>>>")

    def execute(self, sql, param_dict=(), show_sql=False):
        """执行sql语句，打印日志，设置提交标识，返回数据"""
        self.__cursor.execute(sql, param_dict)
        if show_sql:
            LOG.debug(">>>>>>sql>>>>>>: %s" % (self.__cursor.mogrify(sql, param_dict)))
        if sql.lower().startswith(('update', 'insert', 'delete')):
            self.__commit = True
        if sql.lower().startswith('select') or 'returning' in sql.lower():
            return self.__cursor.fetchall()

    def rollback(self):
        """数据库回滚"""
        if self.__commit:
            self.__conn.rollback()
            self.__commit = False

    def commit(self):
        """数据库提交"""
        if self.__commit:
            self.__conn.commit()
            self.__commit = False

    def set_commit(self, commit=True):
        """设置数据库提交标识"""
        self.__commit = commit

    def get_conn(self):
        """获取conn对象"""
        return self.__conn
