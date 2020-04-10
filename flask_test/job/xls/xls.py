# -*- coding: UTF-8 -*-
import logging
import os
import time
import platform

import xlrd
import xlwt

from . import XlsProducer

logger = logging.getLogger(__name__)

try:
    if "Windows" == platform.system():
        xls_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
                                , 'file\\xls')
    elif "Linux" == platform.system():
        xls_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
                                , 'file/xls')
    else:
        raise Exception('匹配系统类型失败')
    os.makedirs(xls_path)
except:
    pass


class XlsUpload(XlsProducer):
    def process(self, **kwargs):
        file = kwargs['request'].files['file']

        # 文件名获取方式
        file_name = file.filename

        # 文件内容
        data = xlrd.open_workbook(file_contents=file.read())
        table = data.sheets()[0]
        names = data.sheet_names()  # 返回book中所有工作表的名字
        flag = data.sheet_loaded(names[0])  # 检查sheet1是否导入完毕
        if not flag:
            return {"flag": False, "msg": "excel读取失败！"}

        # table.nrows-获取该sheet中的有效行数
        # table.ncols-获取该sheet中的有效列数
        # table.row_values(0)-获取第1行数据
        # table.col_values(0)-获取第1列数据
        for i in range(table.nrows):
            info = table.row_values(i)
            for j in range(table.ncols):
                logger.debug('第' + str(i+1) + '行' + '第' + str(j+1) + '列：' + str(info[j]))
        return ''


class XlsExport(XlsProducer):
    def process(self, **kwargs):
        export_info = [
            ['1.1', '1.2', '1.3'],
            ['2.1', '2.2', '2.3']
        ]
        work_book = xlwt.Workbook(encoding='utf-8')
        sheet = work_book.add_sheet('测试新建xls')

        for i in range(len(export_info)):
            for j in range(len(export_info[i])):
                sheet.write(i, j, export_info[i][j])

        if "Windows" == platform.system():
            file_path = xls_path + '\\' + str(time.time())
        elif "Linux" == platform.system():
            file_path = xls_path + '/' + str(time.time())
        else:
            raise Exception('匹配系统类型失败')

        work_book.save(file_path)
        return file_path
