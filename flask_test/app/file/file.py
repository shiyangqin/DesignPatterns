# -*- coding: UTF-8 -*-
from job.file.file import *
from . import file_app as app


@app.route('/download', methods=['GET'])
def file_download():
    """下载文件"""
    return FileDownload().do()


@app.route('/upload', methods=['POST'])
def file_upload():
    """上传文件"""
    return FileUpload().do()
