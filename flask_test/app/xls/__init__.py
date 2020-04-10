# -*- coding: UTF-8 -*-
from flask import Blueprint

xls_app = Blueprint(__name__ + "_app", __name__, url_prefix='/xls')

from . import xls
