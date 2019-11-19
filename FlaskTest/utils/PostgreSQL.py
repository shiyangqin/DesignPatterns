# -*- coding: UTF-8 -*-
import logging

import psycopg2
from DBUtils.PooledDB import PooledDB
from psycopg2.extras import RealDictCursor

from config import PG

LOG = logging.getLogger(__name__)


class PG_Pool(object):
    """pg数据库连接池"""

    def __init__(self, host=PG.pg_host, port=PG.pg_port, database=PG.pg_name, user=PG.pg_user, password=PG.pg_pwd):
        LOG.debug(">>>>>>pg_pool start create>>>>>>")
        self.__pool = PooledDB(
            psycopg2,
            mincached=5,
            blocking=True,
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        LOG.debug(">>>>>>pg_pool create success>>>>>>")

    def get_pool(self):
        return self.__pool


class PostgreSQL(object):
    """pg数据库封装类"""

    def __init__(self, host=PG.pg_host, port=PG.pg_port, database=PG.pg_name, user=PG.pg_user, password=PG.pg_pwd, conn=None, dict_cursor=True):
        """创建连接"""
        self.__commit = False
        if conn:
            LOG.debug(">>>>>>PostgreSQL set conn>>>>>>")
            self.__conn = conn
        else:
            LOG.debug(">>>>>>PostgreSQL get conn>>>>>>")
            self.__conn = psycopg2.connect(
                host=host,
                port=port,
                database=database,
                user=user,
                password=password
            )
        if dict_cursor:
            self.__cursor = self.__conn.cursor(cursor_factory=RealDictCursor)
        else:
            self.__cursor = self.__conn.cursor()

    def __del__(self):
        """关闭数据库连接"""
        if self.__cursor:
            self.__cursor.close()
            self.__cursor = None
        if self.__conn:
            self.__conn.close()
            self.__conn = None
        LOG.debug(">>>>>>PostgreSQL conn close>>>>>>")

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
            LOG.debug(">>>>>>PostgreSQL rollback>>>>>>")
            self.__conn.rollback()
            self.__commit = False

    def commit(self):
        """数据库提交"""
        if self.__commit:
            LOG.debug(">>>>>>PostgreSQL commit>>>>>>")
            self.__conn.commit()
            self.__commit = False

    def set_commit(self, commit=True):
        """设置数据库提交标识"""
        self.__commit = commit

    def get_conn(self):
        """获取conn对象"""
        return self.__conn
