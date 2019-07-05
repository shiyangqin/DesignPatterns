# -*- coding: UTF-8 -*-
import logging

from flask import Blueprint, request

from do.do_test import Do_Test

LOG = logging.getLogger(__name__)

app = Blueprint(__name__ + "_app", __name__)


@app.route('/test/get', methods=['GET'])
def test_get():
    """测试"""
    LOG.debug("================server Test get================")
    return Do_Test().get(request, True)


@app.route('/test/post', methods=['POST'])
def test_post():
    """测试"""
    LOG.debug("================server Test post================")
    return Do_Test().post(request, True)
