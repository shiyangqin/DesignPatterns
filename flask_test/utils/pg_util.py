# -*- coding: UTF-8 -*-
import logging

import psycopg2
from DBUtils.PooledDB import PooledDB
from psycopg2.extras import RealDictCursor

from config import PG

logger = logging.getLogger(__name__)


class PgPool(object):
    """pg数据库连接池"""

    def __init__(self, host=PG.host, port=PG.port, database=PG.name, user=PG.user, password=PG.pwd):
        logger.debug(">>>>>>pg_pool start create>>>>>>")
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
        logger.debug(">>>>>>pg_pool create success>>>>>>")

    def get_pool(self):
        return self.__pool


class PostgreSQL(object):
    """pg数据库封装类"""

    def __init__(self, host=PG.host, port=PG.port, database=PG.name, user=PG.user, password=PG.pwd, conn=None, dict_cursor=True):
        """创建连接"""
        self.__commit = False
        if conn:
            logger.debug(">>>>>>PostgreSQL set conn>>>>>>")
            self.__conn = conn
        else:
            logger.debug(">>>>>>PostgreSQL get conn>>>>>>")
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
        logger.debug(">>>>>>PostgreSQL close>>>>>>")

    def execute(self, sql, sql_dict=(), show_sql=False):
        """执行sql语句，打印日志，设置提交标识，返回数据"""
        self.__cursor.execute(sql, sql_dict)
        if show_sql:
            logger.debug(">>>>>>sql>>>>>>: %s" % (self.__cursor.mogrify(sql, sql_dict)))
        if ('update ' in sql) or ('insert ' in sql) or ('delete ' in sql):
            self.__commit = True
        try:
            return self.__cursor.fetchall()
        except Exception as e:
            pass

    def rollback(self):
        """数据库回滚"""
        if self.__commit:
            logger.exception(">>>>>>PostgreSQL rollback>>>>>>")
            self.__conn.rollback()
            self.__commit = False

    def commit(self):
        """数据库提交"""
        if self.__commit:
            logger.debug(">>>>>>PostgreSQL commit>>>>>>")
            self.__conn.commit()
            self.__commit = False

    def set_commit(self, commit=True):
        """设置数据库提交标识"""
        self.__commit = commit

    def get_conn(self):
        """获取conn对象"""
        return self.__conn
