# -*- coding: UTF-8 -*-
import logging

from flask import Blueprint, request

from job.test import Test

LOG = logging.getLogger(__name__)

app = Blueprint(__name__ + "_app", __name__)


@app.route('/test', methods=['GET'])
def test():
    """测试"""
    LOG.debug("================server test================")
    return Test().do(request)
