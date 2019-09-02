# -*- coding: UTF-8 -*-
import logging

from flask import Blueprint, request

from do.test import Test

LOG = logging.getLogger(__name__)

app = Blueprint(__name__ + "_app", __name__)


@app.route('/test/get', methods=['GET'])
def test_get():
    """测试"""
    LOG.debug("================server Test get================")
    return Test().do(request)
