# -*- coding: UTF-8 -*-

from flask import Blueprint

test_app = Blueprint(__name__ + "_app", __name__, url_prefix='/Test')

from . import app_test
