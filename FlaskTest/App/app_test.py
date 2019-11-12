# -*- coding: UTF-8 -*-
import logging

from job.test import Test
from . import main_app as app

LOG = logging.getLogger(__name__)


@app.route('/test', methods=['GET'])
def test():
    """测试"""
    LOG.debug("================server test================")
    return Test().do()
