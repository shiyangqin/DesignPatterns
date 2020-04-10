# -*- coding: UTF-8 -*-
import os
import time
import platform
from urllib.parse import quote

from flask import make_response, send_from_directory

from . import FileProducer

try:
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), 'file')
    os.makedirs(file_path)
except:
    pass


class FileDownload(FileProducer):
    def process(self, **kwargs):
        param = kwargs['request'].args
        if "Windows" == platform.system():
            download_path = param['file_path'].rsplit("\\", 1)
        elif "Linux" == platform.system():
            download_path = param['file_path'].rsplit("/", 1)
        else:
            raise Exception('匹配系统类型失败')
        response = make_response(send_from_directory(download_path[0], download_path[1]))
        response.headers["Content-Disposition"] = \
            "attachment; filename={0}; filename*=utf-8''{0}".format(quote(param['file_name']))
        self.set_process_type()
        return response


class FileUpload(FileProducer):
    def process(self, **kwargs):
        f = kwargs['request'].files['file']
        save_path = os.path.join(file_path, str(time.time()))
        f.save(save_path)
        return save_path
