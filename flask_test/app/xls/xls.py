# -*- coding: UTF-8 -*-
from job.xls.xls import *
from . import xls_app as app


@app.route('/upload', methods=['POST'])
def xls_upload():
    """上传xls文件"""
    return XlsUpload().do()


@app.route('/export', methods=['POST'])
def xls_export():
    """导出xls文件"""
    return XlsExport().do()
