# -*- coding: UTF-8 -*-
import logging

from flask import request

from job.test import Test
from . import test_app as app

logger = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def test():
    """测试"""
    logger.debug("================server test================")
    return Test().do(request=request)
