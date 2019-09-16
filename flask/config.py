# -*- coding: UTF-8 -*-
import configparser
import os


def load_config(path):
    """
    @summary: 加载配置文件
    @param: path,指定配置文件路径
    @return: dict, 详细配置
    """
    cf = configparser.ConfigParser()
    cf.read(path)
    sets = cf.sections()
    config = {}
    for key in sets:
        config[key] = {}
        for val in cf.items(key):
            config[key][val[0]] = val[1]
    return config


# 获取sap.ini所在路径（当前文件所在路径）
filepath = os.path.join(os.path.dirname(__file__), 'sap.ini')
conf = load_config(filepath)


# 日志配置
class Log(object):
    log_name = conf.get('Log').get('log_name')
    log_level = conf.get('Log').get('log_level')


# 数据库配置
class PG(object):
    pg_host = conf.get('PG').get('pg_host')
    pg_port = conf.get('PG').get('pg_port')
    pg_user = conf.get('PG').get('pg_user')
    pg_pwd = conf.get('PG').get('pg_pwd')
    pg_name = conf.get('PG').get('pg_name')
